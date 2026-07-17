import test from "node:test";
import assert from "node:assert/strict";
import {
  buildCoworkPrompt,
  evaluateFableRequest,
} from "./fable-cowork-router.mjs";

function requestBody(reason, attempts = "Sonnetを1回試した。") {
  return `
## 目的
AI開発会社の全体方針を決める。
## 期待する成果
選択肢、推奨案、リスク、次のIssue案。
## Fableが必要な理由
${reason}
## これまでの試行
${attempts}
## Fable利用回数
1回
## 人間承認
Cowork上で一回だけ開始する。
`;
}

test("normal work stays on Sonnet or Codex", () => {
  const result = evaluateFableRequest({
    body: requestBody("smallの通常実装。"),
  });
  assert.equal(result.allowed, false);
});

test("important cross-service architecture is eligible", () => {
  const result = evaluateFableRequest({
    body: requestBody("複数サービスにまたがる重要アーキテクチャ判断。"),
  });
  assert.equal(result.allowed, true);
});

test("large task requires two failed attempts", () => {
  const rejected = evaluateFableRequest({
    body: requestBody("largeの複雑な実装。"),
  });
  const allowed = evaluateFableRequest({
    body: requestBody(
      "largeの複雑な実装。",
      "SonnetとCodexで合計2回失敗し、行き詰まり。",
    ),
  });
  assert.equal(rejected.allowed, false);
  assert.equal(allowed.allowed, true);
});

test("used label prevents a second Fable run", () => {
  const result = evaluateFableRequest({
    body: requestBody("複数サービスの全体設計。"),
    labels: ["ai:fable-used"],
  });
  assert.equal(result.allowed, false);
});

test("usage count must be exactly once", () => {
  const result = evaluateFableRequest({
    body: requestBody("複数サービスの全体設計。").replace(
      "## Fable利用回数\n1回",
      "## Fable利用回数\n3回",
    ),
  });
  assert.equal(result.allowed, false);
});

test("Cowork prompt preserves safety boundaries", () => {
  const prompt = buildCoworkPrompt({
    url: "https://github.com/example/repo/issues/1",
    title: "Architecture",
    goal: "方針を決める",
    deliverable: "設計書",
  });
  assert.match(prompt, /Fable 5/);
  assert.match(prompt, /mainへmergeしない/);
  assert.match(prompt, /ai:fable-used/);
});
