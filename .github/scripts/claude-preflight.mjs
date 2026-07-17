#!/usr/bin/env node
// Deterministic (no-AI) gate that decides whether the Claude Code Action should
// run for a `claude`-labeled Issue, and with how many turns. Runs before any
// billable/model call so incomplete, duplicate, or unapproved-risk Issues never
// reach the model. See Issue that introduced this file for the full spec.

export const REQUIRED_HEADINGS = [
  "背景",
  "目的",
  "実装内容",
  "完了条件",
  "影響範囲",
  "テスト項目",
  "人間承認が必要なこと",
];

export const DANGEROUS_KEYWORDS = [
  "Production deploy",
  "課金有効化",
  "秘密情報",
  ".env.local",
  "認証",
  "破壊的DB変更",
];

const SCOPE_HEADINGS_FOR_DANGER_CHECK = ["実装内容", "影響範囲"];

const MAX_TURNS_BY_SIZE = {
  small: 12,
  medium: 20,
  large: 30,
};

function escapeRegExp(text) {
  return text.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

// Extracts the text between a `## heading` / `### heading` line and the next
// heading line (or end of body). Returns null if the heading is not present.
function extractSection(body, heading) {
  const lines = body.split(/\r?\n/);
  const headingRe = new RegExp(`^#{2,3}\\s*${escapeRegExp(heading)}\\s*$`);
  const anyHeadingRe = /^#{2,3}\s+/;

  const startIndex = lines.findIndex((line) => headingRe.test(line.trim()));
  if (startIndex === -1) return null;

  const sectionLines = [];
  for (let i = startIndex + 1; i < lines.length; i += 1) {
    if (anyHeadingRe.test(lines[i].trim())) break;
    sectionLines.push(lines[i]);
  }
  return sectionLines.join("\n");
}

export function checkRequiredHeadings(body) {
  const missing = [];
  for (const heading of REQUIRED_HEADINGS) {
    const section = extractSection(body, heading);
    if (section === null || section.trim().length === 0) {
      missing.push(heading);
    }
  }
  return { ok: missing.length === 0, missing };
}

export function parseWorkSize(body) {
  const section = extractSection(body, "作業規模");
  if (section) {
    const match = section.match(/small|medium|large/i);
    if (match) return match[0].toLowerCase();
  }
  return "small";
}

export function maxTurnsForSize(size) {
  return MAX_TURNS_BY_SIZE[size] ?? MAX_TURNS_BY_SIZE.small;
}

// A dangerous keyword only blocks the run when it appears in a scope section
// (実装内容 / 影響範囲) — i.e. the Issue is actually asking for that work —
// and there is no explicit approval record in 人間承認が必要なこと beyond a
// generic "なし / 対象外" disclaimer.
export function checkDangerousOperations(body) {
  const requestedKeywords = new Set();
  for (const heading of SCOPE_HEADINGS_FOR_DANGER_CHECK) {
    const section = extractSection(body, heading) ?? "";
    for (const keyword of DANGEROUS_KEYWORDS) {
      if (section.includes(keyword)) requestedKeywords.add(keyword);
    }
  }

  if (requestedKeywords.size === 0) {
    return { ok: true, requested: [] };
  }

  const approvalSection = (extractSection(body, "人間承認が必要なこと") ?? "").trim();
  const hasApprovalMarker = /承認済み?|approved/i.test(approvalSection);
  const restatesKeyword = DANGEROUS_KEYWORDS.some((keyword) => approvalSection.includes(keyword));

  const ok = hasApprovalMarker && restatesKeyword;
  return { ok, requested: [...requestedKeywords] };
}

export function detectDuplicate({ issueNumber, openPRs = [], branches = [] }) {
  const branchPrefixes = [
    `claude/feature-${issueNumber}-`,
    `claude/fix-${issueNumber}-`,
    `claude/refactor-${issueNumber}-`,
  ];
  const branchHit = branches.find((name) => branchPrefixes.some((prefix) => name.startsWith(prefix)));
  if (branchHit) {
    return { duplicate: true, reason: `既存ブランチ ${branchHit} が既に存在します` };
  }

  const closesRe = new RegExp(`(closes|fixes|resolves)\\s+#${issueNumber}\\b`, "i");
  const prHit = openPRs.find((pr) => closesRe.test(pr.body ?? ""));
  if (prHit) {
    return { duplicate: true, reason: `既存PR #${prHit.number} が Closes #${issueNumber} を含みます` };
  }

  return { duplicate: false, reason: null };
}

// Pure decision function — no network/IO — so it stays unit-testable.
export function evaluatePreflight({ issueNumber, body, openPRs = [], branches = [] }) {
  const headings = checkRequiredHeadings(body);
  if (!headings.ok) {
    return {
      allowed: false,
      reason: `必須見出しが不足しています: ${headings.missing.join(", ")}`,
      size: parseWorkSize(body),
      maxTurns: 0,
    };
  }

  const duplicate = detectDuplicate({ issueNumber, openPRs, branches });
  if (duplicate.duplicate) {
    return {
      allowed: false,
      reason: `重複実行を検知しました: ${duplicate.reason}`,
      size: parseWorkSize(body),
      maxTurns: 0,
    };
  }

  const danger = checkDangerousOperations(body);
  if (!danger.ok) {
    return {
      allowed: false,
      reason: `危険操作(${danger.requested.join(", ")})の要求に対して、人間承認が必要なことセクションに具体的な承認記録がありません`,
      size: parseWorkSize(body),
      maxTurns: 0,
    };
  }

  const size = parseWorkSize(body);
  return {
    allowed: true,
    reason: "preflight passed",
    size,
    maxTurns: maxTurnsForSize(size),
  };
}

async function githubRequest(path, token, repo) {
  const response = await fetch(`https://api.github.com/repos/${repo}${path}`, {
    headers: {
      Authorization: `Bearer ${token}`,
      Accept: "application/vnd.github+json",
      "X-GitHub-Api-Version": "2022-11-28",
    },
  });
  if (!response.ok) {
    throw new Error(`GitHub API ${path} failed: ${response.status} ${response.statusText}`);
  }
  return response.json();
}

async function main() {
  const issueNumber = process.env.ISSUE_NUMBER;
  const body = process.env.ISSUE_BODY ?? "";
  const token = process.env.GITHUB_TOKEN;
  const repo = process.env.GITHUB_REPOSITORY;
  const outputPath = process.env.GITHUB_OUTPUT;

  if (!issueNumber || !token || !repo) {
    throw new Error("ISSUE_NUMBER, GITHUB_TOKEN, and GITHUB_REPOSITORY are required");
  }

  const [openPRs, branchList] = await Promise.all([
    githubRequest(`/pulls?state=open&per_page=100`, token, repo),
    githubRequest(`/branches?per_page=100`, token, repo),
  ]);
  const branches = branchList.map((branch) => branch.name);

  const result = evaluatePreflight({ issueNumber, body, openPRs, branches });

  console.log(`allowed=${result.allowed}`);
  console.log(`size=${result.size}`);
  console.log(`max_turns=${result.maxTurns}`);
  console.log(`reason=${result.reason}`);

  if (outputPath) {
    const fs = await import("node:fs");
    fs.appendFileSync(outputPath, `allowed=${result.allowed}\n`);
    fs.appendFileSync(outputPath, `size=${result.size}\n`);
    fs.appendFileSync(outputPath, `max_turns=${result.maxTurns}\n`);
    // reason may contain characters unsafe for a single GITHUB_OUTPUT line, use a heredoc-style delimiter.
    const delimiter = `ghadelimiter_${Date.now()}`;
    fs.appendFileSync(outputPath, `reason<<${delimiter}\n${result.reason}\n${delimiter}\n`);
  }
}

const isMainModule = process.argv[1] && import.meta.url === `file://${process.argv[1]}`;
if (isMainModule) {
  main().catch((error) => {
    console.error(error);
    process.exit(1);
  });
}
