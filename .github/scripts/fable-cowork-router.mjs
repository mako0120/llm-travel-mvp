import { readFile } from "node:fs/promises";
import { pathToFileURL } from "node:url";

export const FABLE_LABELS = [
  {
    name: "fable-review",
    color: "D4A72C",
    description: "CoworkのFable 5利用候補を判定する",
  },
  {
    name: "ai:fable-needed",
    color: "B60205",
    description: "CoworkのFable 5へ一回だけ渡す",
  },
  {
    name: "ai:fable-used",
    color: "5319E7",
    description: "Fable 5利用済み・再実行禁止",
  },
];

const REQUIRED_SECTIONS = [
  "目的",
  "期待する成果",
  "Fableが必要な理由",
  "これまでの試行",
  "Fable利用回数",
  "人間承認",
];

export function parseSections(body = "") {
  const sections = new Map();
  const matches = [...body.matchAll(/^#{2,3}\s+(.+?)\s*$/gm)];
  for (let index = 0; index < matches.length; index += 1) {
    const current = matches[index];
    const next = matches[index + 1];
    sections.set(
      current[1].trim(),
      body
        .slice(current.index + current[0].length, next?.index ?? body.length)
        .trim(),
    );
  }
  return sections;
}

function isEmpty(value = "") {
  return !value.replace(/[-[\]\s]/g, "");
}

export function evaluateFableRequest({ body, labels = [] }) {
  const names = labels.map((label) =>
    typeof label === "string" ? label : label.name,
  );
  if (names.includes("ai:fable-used")) {
    return { allowed: false, reason: "Fable 5は利用済みです。再実行しません。" };
  }

  const sections = parseSections(body);
  const missing = REQUIRED_SECTIONS.filter((name) =>
    isEmpty(sections.get(name)),
  );
  if (missing.length > 0) {
    return {
      allowed: false,
      reason: `必須項目が不足または空です: ${missing.join("、")}`,
    };
  }

  if (!/^\s*1回\s*$/m.test(sections.get("Fable利用回数"))) {
    return {
      allowed: false,
      reason: "Fable利用回数は「1回」に限定してください。",
    };
  }

  const reason = sections.get("Fableが必要な理由");
  const architecture =
    /アーキテクチャ|複数サービス|重要判断|設計判断|全体設計/i.test(reason);
  const research =
    /(?:10件以上|多数).*(?:資料|競合|要件)|長時間調査|統合調査/i.test(reason);
  const migration =
    /大規模移行|複雑な実装|複数段階|長時間|large/i.test(reason);
  const finalReview = /重大リスク|大規模PR|最終設計レビュー/i.test(reason);
  const failedTwice =
    /(?:Sonnet|Codex).*(?:2回|二回).*(?:失敗|行き詰まり)|(?:2回|二回).*(?:失敗|行き詰まり).*(?:Sonnet|Codex)/i.test(
      sections.get("これまでの試行"),
    );

  if (!(architecture || research || finalReview || (migration && failedTwice))) {
    return {
      allowed: false,
      reason:
        "通常作業はSonnet/Codexを使います。Fable条件（重要設計、10件以上の統合調査、重大PRレビュー、またはlargeかつ2回失敗）を満たしていません。",
    };
  }

  const fullText = [...sections.values()].join("\n");
  if (
    /(?:秘密情報|APIキー|token|トークン|\.env\.local).{0,20}(?:表示|保存|取得)|(?:Production|本番).{0,20}(?:deploy|デプロイ)|課金.{0,20}有効|DB.{0,20}(?:破壊|削除|drop)/i.test(
      fullText,
    )
  ) {
    return {
      allowed: false,
      reason: "秘密情報・本番・課金・破壊的DB操作はFableへ渡せません。",
    };
  }

  return {
    allowed: true,
    reason: "Fable 5を一回だけ使う条件を満たしています。",
    goal: sections.get("目的"),
    deliverable: sections.get("期待する成果"),
  };
}

export function buildCoworkPrompt({ url, title, goal, deliverable }) {
  return `あなたはClaude Cowork上のFable 5です。

次の1件だけを、長時間・多段階の難しい判断担当として処理してください。

対象: ${title}
URL: ${url}

目的:
${goal}

期待する成果:
${deliverable}

必須ルール:
- 最初にGitHubの対象IssueまたはPRと関連資料を読む
- 実装の定型作業はSonnet/Codexへ戻し、Fable自身は難しい設計・統合・最終判断に集中する
- 結論、根拠、選択肢、推奨案、リスク、次のIssue案を出す
- APIキー、秘密情報、.env.localを読まない・表示しない・保存しない
- mainへmergeしない
- Production deploy、課金有効化、認証・DB・環境変数の変更を行わない
- 作業完了後、対象に \`ai:fable-used\` を付け、\`ai:fable-needed\` を外して停止する
- Fableを連続して再実行しない`;
}

async function request(path, token, options = {}) {
  const response = await fetch(`https://api.github.com${path}`, {
    ...options,
    headers: {
      Accept: "application/vnd.github+json",
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
      "X-GitHub-Api-Version": "2022-11-28",
      ...options.headers,
    },
  });
  if (!response.ok) throw new Error(`GitHub API ${response.status}: ${path}`);
  return response.status === 204 ? null : response.json();
}

async function ensureLabels(owner, repo, token) {
  const existing = await request(`/repos/${owner}/${repo}/labels?per_page=100`, token);
  const names = new Set(existing.map((label) => label.name));
  for (const label of FABLE_LABELS) {
    if (!names.has(label.name)) {
      await request(`/repos/${owner}/${repo}/labels`, token, {
        method: "POST",
        body: JSON.stringify(label),
      });
    }
  }
}

async function run() {
  const token = process.env.GITHUB_TOKEN;
  const [owner, repo] = process.env.GITHUB_REPOSITORY.split("/");
  await ensureLabels(owner, repo, token);
  if (process.argv.includes("--bootstrap")) return;

  const event = JSON.parse(await readFile(process.env.GITHUB_EVENT_PATH, "utf8"));
  const subject = event.issue ?? event.pull_request;
  const number = subject.number;
  const result = evaluateFableRequest({
    body: subject.body ?? "",
    labels: subject.labels ?? [],
  });
  const marker = "<!-- ai-handoff:fable-cowork -->";
  const comments = await request(
    `/repos/${owner}/${repo}/issues/${number}/comments?per_page=100`,
    token,
  );
  const existing = comments.find((comment) => comment.body?.includes(marker));
  const prompt = result.allowed
    ? buildCoworkPrompt({
        url: subject.html_url,
        title: subject.title,
        goal: result.goal,
        deliverable: result.deliverable,
      })
    : null;
  const body = result.allowed
    ? `${marker}\n## Fable 5 一時利用の準備完了\n\n${result.reason}\n\nCoworkでモデルを **Fable 5** にし、次のプロンプトを一回だけ実行してください。\n\n\`\`\`text\n${prompt}\n\`\`\``
    : `${marker}\n## Fable 5は使用しません\n\n${result.reason}\n\n通常のChatGPT Work / Codex / Claude Sonnetルートを使用してください。`;

  if (result.allowed) {
    await request(`/repos/${owner}/${repo}/issues/${number}/labels`, token, {
      method: "POST",
      body: JSON.stringify({ labels: ["ai:fable-needed"] }),
    });
  }
  if (existing) {
    await request(`/repos/${owner}/${repo}/issues/comments/${existing.id}`, token, {
      method: "PATCH",
      body: JSON.stringify({ body }),
    });
  } else {
    await request(`/repos/${owner}/${repo}/issues/${number}/comments`, token, {
      method: "POST",
      body: JSON.stringify({ body }),
    });
  }
}

if (import.meta.url === pathToFileURL(process.argv[1]).href) {
  run().catch((error) => {
    console.error(error instanceof Error ? error.message : error);
    process.exitCode = 1;
  });
}
