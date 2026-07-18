import test from "node:test";
import assert from "node:assert/strict";
import {
  POLICY_CATEGORIES,
  POLICY_PRESETS,
  calculatePolicyAudit,
  sanitizeStatus,
} from "./calculate.mjs";

test("sanitizeStatus converts unknown and empty values to missing", () => {
  assert.equal(sanitizeStatus("clear"), "clear");
  assert.equal(sanitizeStatus("unclear"), "unclear");
  assert.equal(sanitizeStatus("missing"), "missing");
  assert.equal(sanitizeStatus("foo"), "missing");
  assert.equal(sanitizeStatus(undefined), "missing");
  assert.equal(sanitizeStatus(null), "missing");
});

test("all clear produces 100 and every category is answerable", () => {
  const input = Object.fromEntries(POLICY_CATEGORIES.map(({ id }) => [id, "clear"]));
  const result = calculatePolicyAudit(input);
  assert.equal(result.score, 100);
  assert.equal(result.answerable.length, 6);
  assert.equal(result.checklist.length, 0);
});

test("all missing produces 0 and every category is missing", () => {
  const result = calculatePolicyAudit({});
  assert.equal(result.score, 0);
  assert.equal(result.missing.length, 6);
  assert.equal(result.checklist.length, 6);
});

test("unclear categories require human review", () => {
  const result = calculatePolicyAudit({ cancellation: "unclear" });
  assert.equal(result.humanReview[0].id, "cancellation");
  assert.equal(result.checklist[0].priority, "最優先");
  assert.equal(result.checklist.at(-1).priority, "要明確化");
});

test("all unclear produces 50 and every category needs human review", () => {
  const input = Object.fromEntries(POLICY_CATEGORIES.map(({ id }) => [id, "unclear"]));
  const result = calculatePolicyAudit(input);
  assert.equal(result.score, 50);
  assert.equal(result.humanReview.length, 6);
});

test("invalid values never produce a non-finite score", () => {
  const result = calculatePolicyAudit({ cancellation: "foo", checkin: null });
  assert.ok(Number.isFinite(result.score));
  assert.ok(Number.isInteger(result.score));
  assert.ok(result.score >= 0 && result.score <= 100);
});

test("calculation is deterministic and bounded", () => {
  for (const preset of POLICY_PRESETS) {
    const first = calculatePolicyAudit(preset.values);
    assert.deepEqual(first, calculatePolicyAudit(preset.values));
    assert.ok(first.score >= 0 && first.score <= 100);
  }
  assert.equal(POLICY_PRESETS.length, 3);
});
