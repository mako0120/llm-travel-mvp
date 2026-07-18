import test from "node:test";
import assert from "node:assert/strict";
import {
  evaluatePreflight,
  hasDuplicate,
  parseSections,
} from "./claude-preflight.mjs";

const validBody = `
## 背景
重複実行を防ぎたい。
## 目的
AI使用量を減らす。
## 実装内容
決定的なpreflightを追加する。
## 完了条件
- [ ] テストが通る
## 影響範囲
.githubのみ。
## テスト項目
- [ ] node --test
## 人間承認が必要なこと
なし。危険な変更は対象外。
## 変更予定ファイル/ディレクトリ
src/
`;

test("small is the safe default", () => {
  const result = evaluatePreflight({ body: validBody, issueNumber: 18 });
  assert.equal(result.allowed, true);
  assert.equal(result.size, "small");
  assert.equal(result.maxTurns, 12);
});

test("medium and large select bounded turns", () => {
  const medium = evaluatePreflight({
    body: `${validBody}\n## 作業規模\nmedium`,
    issueNumber: 18,
  });
  const large = evaluatePreflight({
    body: `${validBody}\n## 作業規模\nlarge`,
    issueNumber: 18,
  });
  assert.equal(medium.maxTurns, 20);
  assert.equal(large.maxTurns, 30);
});

test("missing required section is rejected", () => {
  const sections = parseSections(validBody);
  sections.delete("テスト項目");
  const body = [...sections]
    .map(([heading, content]) => `## ${heading}\n${content}`)
    .join("\n");
  const result = evaluatePreflight({ body, issueNumber: 18 });
  assert.equal(result.allowed, false);
  assert.match(result.reason, /テスト項目/);
});

test("safe heading aliases are accepted", () => {
  const body = validBody
    .replace("## 目的", "## 実装目的")
    .replace("## 影響範囲", "## 変更範囲")
    .replace(
      "## 変更予定ファイル/ディレクトリ",
      "## 変更予定ファイル",
    );
  const result = evaluatePreflight({ body, issueNumber: 18 });
  assert.equal(result.allowed, true);
});

test("an empty alias does not satisfy a required section", () => {
  const body = validBody.replace(
    "## 目的\nAI使用量を減らす。",
    "## 実装目的\n- [ ]",
  );
  const result = evaluatePreflight({ body, issueNumber: 18 });
  assert.equal(result.allowed, false);
  assert.match(result.reason, /目的/);
});

test("unapproved dangerous implementation is rejected", () => {
  const body = validBody.replace(
    "決定的なpreflightを追加する。",
    "Production deployを有効化する。",
  );
  const result = evaluatePreflight({ body, issueNumber: 18 });
  assert.equal(result.allowed, false);
  assert.match(result.reason, /人間承認/);
});

test("existing PR or Claude branch prevents duplicate work", () => {
  assert.equal(
    hasDuplicate(
      18,
      [{ state: "open", body: "Closes #18", head: { ref: "other" } }],
      [],
    ),
    true,
  );
  assert.equal(
    hasDuplicate(18, [], [{ name: "claude/feature-18-usage-guard" }]),
    true,
  );
});

test("workflow changes are routed away from Claude", () => {
  const body = validBody.replace("src/", ".github/workflows/");
  const result = evaluatePreflight({ body, issueNumber: 18 });
  assert.equal(result.allowed, false);
  assert.match(result.reason, /Codex/);
});
