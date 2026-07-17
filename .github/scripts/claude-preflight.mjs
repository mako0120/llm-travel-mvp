import { appendFile, readFile } from "node:fs/promises";
import { pathToFileURL } from "node:url";

export const REQUIRED_SECTIONS = [
  "背景",
  "目的",
  "実装内容",
  "完了条件",
  "影響範囲",
  "テスト項目",
  "人間承認が必要なこと",
  "変更予定ファイル/ディレクトリ",
];

export const TURN_LIMITS = {
  small: 12,
  medium: 20,
  large: 30,
};

export function parseSections(body = "") {
  const sections = new Map();
  const matches = [...body.matchAll(/^#{2,3}\s+(.+?)\s*$/gm)];

  for (let index = 0; index < matches.length; index += 1) {
    const current = matches[index];
    const next = matches[index + 1];
    const name = current[1].trim();
    const content = body
      .slice(current.index + current[0].length, next?.index ?? body.length)
      .trim();
    sections.set(name, content);
  }

  return sections;
}

export function getSize(sections) {
  const raw = sections.get("作業規模")?.toLowerCase() ?? "small";
  const size = raw.match(/\b(small|medium|large)\b/)?.[1] ?? "small";
  return { size, maxTurns: TURN_LIMITS[size] };
}

export function findMissingSections(sections) {
  return REQUIRED_SECTIONS.filter((name) => {
    const content = sections.get(name);
    return !content || !content.replace(/[-[\]\s]/g, "");
  });
}

export function requestsUnapprovedRisk(sections) {
  const implementation = sections.get("実装内容") ?? "";
  const approval = sections.get("人間承認が必要なこと") ?? "";
  const explicitlyApproved =
    /承認済み|人間承認[:：]\s*(済|あり)|approved/i.test(approval);

  if (explicitlyApproved) return false;

  const riskyAction =
    /(?:Production|本番).{0,20}(?:deploy|デプロイ|変更|有効)|課金.{0,20}(?:有効|変更)|(?:秘密情報|APIキー|token|トークン|\.env\.local).{0,20}(?:表示|保存|変更|コミット)|認証.{0,20}(?:変更|追加|削除)|DB.{0,20}(?:破壊|削除|drop|変更)/i;
  const negative =
    /(?:しない|禁止|対象外|維持|読み取らない|表示しない|保存しない|変更しない)/;

  return implementation
    .split(/\r?\n/)
    .some((line) => riskyAction.test(line) && !negative.test(line));
}

export function requestsClaudeProtectedPath(sections) {
  const paths = sections.get("変更予定ファイル/ディレクトリ") ?? "";
  return /(?:^|[\s`])\.github\/workflows(?:\/|[\s`,]|$)/m.test(paths);
}

export function hasDuplicate(issueNumber, pullRequests = [], branches = []) {
  const issuePattern = new RegExp(
    `(?:closes|fixes|resolves)\\s+#${issueNumber}\\b`,
    "i",
  );
  const branchPattern = new RegExp(
    `^claude\\/(?:feature-|issue-)${issueNumber}(?:-|$)`,
  );

  return (
    pullRequests.some(
      (pull) =>
        pull.state === "open" &&
        (issuePattern.test(pull.body ?? "") ||
          branchPattern.test(pull.head?.ref ?? pull.headRefName ?? "")),
    ) || branches.some((branch) => branchPattern.test(branch.name ?? branch))
  );
}

export function evaluatePreflight({
  body,
  issueNumber,
  pullRequests = [],
  branches = [],
}) {
  const sections = parseSections(body);
  const missing = findMissingSections(sections);
  const { size, maxTurns } = getSize(sections);

  if (missing.length > 0) {
    return {
      allowed: false,
      reason: `必須項目が不足または空です: ${missing.join("、")}`,
      size,
      maxTurns,
    };
  }

  if (requestsUnapprovedRisk(sections)) {
    return {
      allowed: false,
      reason:
        "危険な変更が実装内容に含まれています。具体的な人間承認記録を追加してください。",
      size,
      maxTurns,
    };
  }

  if (requestsClaudeProtectedPath(sections)) {
    return {
      allowed: false,
      reason:
        "Claude GitHub Appは.github/workflowsを変更できません。このIssueはCodexへ割り当ててください。",
      size,
      maxTurns,
    };
  }

  if (hasDuplicate(issueNumber, pullRequests, branches)) {
    return {
      allowed: false,
      reason: "同じIssueのopen PRまたはClaudeブランチが既に存在します。",
      size,
      maxTurns,
    };
  }

  return {
    allowed: true,
    reason: "preflightを通過しました。",
    size,
    maxTurns,
  };
}

async function githubRequest(path, token) {
  const response = await fetch(`https://api.github.com${path}`, {
    headers: {
      Accept: "application/vnd.github+json",
      Authorization: `Bearer ${token}`,
      "X-GitHub-Api-Version": "2022-11-28",
    },
  });
  if (!response.ok) {
    throw new Error(`GitHub API ${response.status}: ${path}`);
  }
  return response.json();
}

async function run() {
  const event = JSON.parse(
    await readFile(process.env.GITHUB_EVENT_PATH, "utf8"),
  );
  const [owner, repo] = process.env.GITHUB_REPOSITORY.split("/");
  const token = process.env.GITHUB_TOKEN;
  const issueNumber = event.issue.number;
  const pulls = await githubRequest(
    `/repos/${owner}/${repo}/pulls?state=open&per_page=100`,
    token,
  );
  const branches = await githubRequest(
    `/repos/${owner}/${repo}/branches?per_page=100`,
    token,
  );
  const result = evaluatePreflight({
    body: event.issue.body ?? "",
    issueNumber,
    pullRequests: pulls,
    branches,
  });

  const output = [
    `allowed=${result.allowed}`,
    `size=${result.size}`,
    `max_turns=${result.maxTurns}`,
    `reason=${result.reason.replace(/\r?\n/g, " ")}`,
  ].join("\n");
  await appendFile(process.env.GITHUB_OUTPUT, `${output}\n`);
  console.log(JSON.stringify(result));
}

if (import.meta.url === pathToFileURL(process.argv[1]).href) {
  run().catch((error) => {
    console.error(error instanceof Error ? error.message : error);
    process.exitCode = 1;
  });
}
