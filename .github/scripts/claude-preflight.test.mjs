import { test } from "node:test";
import assert from "node:assert/strict";
import {
  checkRequiredHeadings,
  checkDangerousOperations,
  detectDuplicate,
  parseWorkSize,
  maxTurnsForSize,
  evaluatePreflight,
} from "./claude-preflight.mjs";

const smallIssueBody = `
## 背景
何かがある。

## 目的
何かをする。

## 実装内容
docs/foo.md を追加する。

## 完了条件
- [ ] docs/foo.md が追加される

## 影響範囲
docs/foo.md のみ。

## テスト項目
- [ ] npm run lint
- [ ] npm run typecheck
- [ ] npm run build

## 人間承認が必要なこと
なし。低リスクな変更。

## 作業規模
small
`;

test("checkRequiredHeadings: passes when all headings are present and non-empty", () => {
  const result = checkRequiredHeadings(smallIssueBody);
  assert.equal(result.ok, true);
  assert.deepEqual(result.missing, []);
});

test("checkRequiredHeadings: reports missing heading", () => {
  const body = smallIssueBody.replace(/## 完了条件[\s\S]*?(?=## 影響範囲)/, "");
  const result = checkRequiredHeadings(body);
  assert.equal(result.ok, false);
  assert.ok(result.missing.includes("完了条件"));
});

test("checkRequiredHeadings: reports heading present but left empty", () => {
  const body = smallIssueBody.replace(
    "## 完了条件\n- [ ] docs/foo.md が追加される",
    "## 完了条件\n"
  );
  const result = checkRequiredHeadings(body);
  assert.equal(result.ok, false);
  assert.ok(result.missing.includes("完了条件"));
});

test("parseWorkSize: reads explicit small/medium/large", () => {
  assert.equal(parseWorkSize(smallIssueBody), "small");
  assert.equal(parseWorkSize(smallIssueBody.replace("small", "medium")), "medium");
  assert.equal(parseWorkSize(smallIssueBody.replace("small", "large")), "large");
});

test("parseWorkSize: defaults to small when heading is absent", () => {
  const body = smallIssueBody.replace(/## 作業規模[\s\S]*$/, "");
  assert.equal(parseWorkSize(body), "small");
});

test("maxTurnsForSize: maps size to the documented turn budget", () => {
  assert.equal(maxTurnsForSize("small"), 12);
  assert.equal(maxTurnsForSize("medium"), 20);
  assert.equal(maxTurnsForSize("large"), 30);
  assert.equal(maxTurnsForSize("unknown"), 12);
});

test("checkDangerousOperations: ok when no dangerous keyword is requested", () => {
  const result = checkDangerousOperations(smallIssueBody);
  assert.equal(result.ok, true);
  assert.deepEqual(result.requested, []);
});

test("checkDangerousOperations: blocks a dangerous request without an approval record", () => {
  const body = smallIssueBody.replace(
    "## 実装内容\ndocs/foo.md を追加する。",
    "## 実装内容\n.env.local に新しいキーを追加する。"
  );
  const result = checkDangerousOperations(body);
  assert.equal(result.ok, false);
  assert.ok(result.requested.includes(".env.local"));
});

test("checkDangerousOperations: allows a dangerous request with an explicit approval record", () => {
  const body = smallIssueBody
    .replace(
      "## 実装内容\ndocs/foo.md を追加する。",
      "## 実装内容\n.env.local に新しいキーを追加する。"
    )
    .replace(
      "## 人間承認が必要なこと\nなし。低リスクな変更。",
      "## 人間承認が必要なこと\n.env.local の変更は2026-07-17に承認済み(承認者: mako0120)。"
    );
  const result = checkDangerousOperations(body);
  assert.equal(result.ok, true);
});

test("detectDuplicate: flags an existing branch for the same issue", () => {
  const result = detectDuplicate({
    issueNumber: "18",
    openPRs: [],
    branches: ["main", "claude/feature-18-usage-guard"],
  });
  assert.equal(result.duplicate, true);
});

test("detectDuplicate: flags an existing open PR that closes the same issue", () => {
  const result = detectDuplicate({
    issueNumber: "18",
    openPRs: [{ number: 42, body: "Closes #18\n\nSummary..." }],
    branches: ["main"],
  });
  assert.equal(result.duplicate, true);
});

test("detectDuplicate: passes when nothing references the issue", () => {
  const result = detectDuplicate({
    issueNumber: "18",
    openPRs: [{ number: 42, body: "Closes #99" }],
    branches: ["main", "claude/feature-99-other"],
  });
  assert.equal(result.duplicate, false);
});

test("evaluatePreflight: allows a normal small Issue with 12 max turns", () => {
  const result = evaluatePreflight({ issueNumber: "18", body: smallIssueBody, openPRs: [], branches: ["main"] });
  assert.equal(result.allowed, true);
  assert.equal(result.size, "small");
  assert.equal(result.maxTurns, 12);
});

test("evaluatePreflight: medium Issue maps to 20 max turns", () => {
  const body = smallIssueBody.replace("small", "medium");
  const result = evaluatePreflight({ issueNumber: "18", body, openPRs: [], branches: ["main"] });
  assert.equal(result.allowed, true);
  assert.equal(result.maxTurns, 20);
});

test("evaluatePreflight: large Issue maps to 30 max turns", () => {
  const body = smallIssueBody.replace("small", "large");
  const result = evaluatePreflight({ issueNumber: "18", body, openPRs: [], branches: ["main"] });
  assert.equal(result.allowed, true);
  assert.equal(result.maxTurns, 30);
});

test("evaluatePreflight: blocks when required headings are missing", () => {
  const body = smallIssueBody.replace(/## 影響範囲[\s\S]*?(?=## テスト項目)/, "");
  const result = evaluatePreflight({ issueNumber: "18", body, openPRs: [], branches: ["main"] });
  assert.equal(result.allowed, false);
  assert.match(result.reason, /必須見出し/);
});

test("evaluatePreflight: blocks a duplicate run even if headings are complete", () => {
  const result = evaluatePreflight({
    issueNumber: "18",
    body: smallIssueBody,
    openPRs: [],
    branches: ["claude/feature-18-already-running"],
  });
  assert.equal(result.allowed, false);
  assert.match(result.reason, /重複実行/);
});

test("evaluatePreflight: blocks unapproved dangerous operations", () => {
  const body = smallIssueBody.replace(
    "## 実装内容\ndocs/foo.md を追加する。",
    "## 実装内容\n認証フローを変更する。"
  );
  const result = evaluatePreflight({ issueNumber: "18", body, openPRs: [], branches: ["main"] });
  assert.equal(result.allowed, false);
  assert.match(result.reason, /危険操作/);
});
