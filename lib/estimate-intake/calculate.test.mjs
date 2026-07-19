import test from "node:test";
import assert from "node:assert/strict";
import {
  ESTIMATE_PRESETS,
  calculateEstimateReadiness,
} from "./calculate.mjs";

test("complete preset is ready and deterministic", () => {
  const values = ESTIMATE_PRESETS[1].values;
  const first = calculateEstimateReadiness(values);
  const second = calculateEstimateReadiness(values);

  assert.deepEqual(first, second);
  assert.equal(first.score, 100);
  assert.equal(first.isReady, true);
  assert.deepEqual(first.questions, []);
});

test("missing values become concrete questions", () => {
  const result = calculateEstimateReadiness(ESTIMATE_PRESETS[2].values);

  assert.equal(result.score, 14);
  assert.equal(result.missing.length, 5);
  assert.equal(result.questions.length, 6);
  assert.match(result.questions.at(-1), /写真/);
});

test("urgent inquiry gets the highest priority", () => {
  const result = calculateEstimateReadiness(ESTIMATE_PRESETS[0].values);

  assert.equal(result.priority.label, "最優先");
  assert.match(result.nextAction, /安全状況/);
});

test("invalid values are safely normalized", () => {
  const result = calculateEstimateReadiness({
    workType: 123,
    hasPhotos: "yes",
    urgency: "unknown",
  });

  assert.equal(result.score, 0);
  assert.equal(result.priority.label, "通常");
  assert.equal(result.missing.length, 6);
});
