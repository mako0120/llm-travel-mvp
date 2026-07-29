import test from "node:test";
import assert from "node:assert/strict";
import {
  REPLY_INQUIRIES,
  REPLY_PRESETS,
  calculateReplyScore,
  sanitizeLevel,
} from "./calculate.mjs";

test("sanitizeLevel falls back on unknown or missing values", () => {
  assert.equal(sanitizeLevel("mid", ["low", "mid", "high"], "low"), "mid");
  assert.equal(sanitizeLevel("bogus", ["low", "mid", "high"], "low"), "low");
  assert.equal(sanitizeLevel(undefined, ["low", "mid", "high"], "low"), "low");
});

test("strongest demand case never exceeds a score of 100", () => {
  const input = { elapsed: "over24h", checkin: "0to1day", value: "high", intent: "strong", language: "easy", termsCheckNeeded: false };
  const inputs = Object.fromEntries(REPLY_INQUIRIES.map(({ id }) => [id, input]));
  const result = calculateReplyScore(inputs);
  for (const item of result.items) {
    assert.ok(item.score <= 100);
    assert.equal(item.lane, "reply_now");
  }
  assert.equal(result.summary.urgentCount, REPLY_INQUIRIES.length);
});

test("weakest demand case never drops below a score of 0", () => {
  const input = { elapsed: "under1h", checkin: "over30days", value: "low", intent: "weak", language: "easy", termsCheckNeeded: false };
  const inputs = Object.fromEntries(REPLY_INQUIRIES.map(({ id }) => [id, input]));
  const result = calculateReplyScore(inputs);
  for (const item of result.items) {
    assert.ok(item.score >= 0);
    assert.equal(item.lane, "follow_up");
  }
  assert.equal(result.summary.followUpCount, REPLY_INQUIRIES.length);
});

test("terms confirmation forces human review even at a high score", () => {
  const input = { elapsed: "over24h", checkin: "0to1day", value: "high", intent: "strong", language: "easy", termsCheckNeeded: true };
  const result = calculateReplyScore({ "arrival-time": input });
  const item = result.items.find((i) => i.id === "arrival-time");
  assert.equal(item.score, 100);
  assert.equal(item.lane, "human_review");
});

test("hard language also forces human review even at a high score", () => {
  const input = { elapsed: "over24h", checkin: "0to1day", value: "high", intent: "strong", language: "hard", termsCheckNeeded: false };
  const result = calculateReplyScore({ "arrival-time": input });
  const item = result.items.find((i) => i.id === "arrival-time");
  assert.equal(item.score, 100);
  assert.equal(item.lane, "human_review");
});

test("same input always produces the same classification and summary", () => {
  for (const preset of REPLY_PRESETS) {
    const first = calculateReplyScore(preset.values);
    const second = calculateReplyScore(preset.values);
    assert.deepEqual(first, second);
  }
});

test("invalid or missing values never produce NaN or an exception", () => {
  const result = calculateReplyScore({
    "arrival-time": { elapsed: "bogus", checkin: null, value: 42, intent: undefined, language: "??", termsCheckNeeded: "yes" },
    cancellation: undefined,
  });
  for (const item of result.items) {
    assert.ok(Number.isFinite(item.score));
    assert.ok(item.score >= 0 && item.score <= 100);
    assert.ok(["reply_now", "human_review", "follow_up"].includes(item.lane));
  }
});

test("calculateReplyScore tolerates being called with no argument", () => {
  const result = calculateReplyScore();
  assert.equal(result.items.length, REPLY_INQUIRIES.length);
  assert.equal(result.summary.urgentCount, 0);
  assert.equal(result.summary.followUpCount, REPLY_INQUIRIES.length);
});

test("three fixed facility presets exist with expected lane distribution", () => {
  assert.equal(REPLY_PRESETS.length, 3);

  const [ryokan, minpaku, guesthouse] = REPLY_PRESETS;

  const ryokanResult = calculateReplyScore(ryokan.values);
  assert.deepEqual(
    ryokanResult.items.map((i) => [i.id, i.lane]),
    [
      ["arrival-time", "reply_now"],
      ["cancellation", "human_review"],
      ["amenity-request", "reply_now"],
      ["group-quote", "human_review"],
      ["noise-complaint", "human_review"],
      ["future-availability", "follow_up"],
    ],
  );
  assert.deepEqual(ryokanResult.summary, {
    urgentCount: 2,
    humanReviewCount: 3,
    followUpCount: 1,
    preventedCount: 2,
  });

  const minpakuResult = calculateReplyScore(minpaku.values);
  assert.deepEqual(
    minpakuResult.items.map((i) => [i.id, i.lane]),
    [
      ["arrival-time", "follow_up"],
      ["cancellation", "human_review"],
      ["amenity-request", "reply_now"],
      ["group-quote", "reply_now"],
      ["noise-complaint", "follow_up"],
      ["future-availability", "follow_up"],
    ],
  );
  assert.deepEqual(minpakuResult.summary, {
    urgentCount: 2,
    humanReviewCount: 1,
    followUpCount: 3,
    preventedCount: 1,
  });

  const guesthouseResult = calculateReplyScore(guesthouse.values);
  assert.deepEqual(
    guesthouseResult.items.map((i) => [i.id, i.lane]),
    [
      ["arrival-time", "human_review"],
      ["cancellation", "human_review"],
      ["amenity-request", "human_review"],
      ["group-quote", "reply_now"],
      ["noise-complaint", "follow_up"],
      ["future-availability", "follow_up"],
    ],
  );
  assert.deepEqual(guesthouseResult.summary, {
    urgentCount: 1,
    humanReviewCount: 3,
    followUpCount: 2,
    preventedCount: 2,
  });
});
