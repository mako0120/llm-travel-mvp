import { strict as assert } from "node:assert";
import { test } from "node:test";
import { calculateRoi, sanitize } from "./calculate.mjs";

// --- sanitize ---

test("sanitize: empty string → 0", () => {
  assert.equal(sanitize("", 100), 0);
});

test("sanitize: non-numeric string → 0", () => {
  assert.equal(sanitize("abc", 100), 0);
});

test("sanitize: NaN → 0", () => {
  assert.equal(sanitize(NaN, 100), 0);
});

test("sanitize: Infinity → 0", () => {
  assert.equal(sanitize(Infinity, 100), 0);
});

test("sanitize: negative → 0", () => {
  assert.equal(sanitize(-1, 100), 0);
});

test("sanitize: over max → max", () => {
  assert.equal(sanitize(200, 100), 100);
});

test("sanitize: valid value passes through", () => {
  assert.equal(sanitize(50, 100), 50);
});

// --- preset cases (手計算で検算済み) ---

test("preset: 飲食店の予約・問い合わせ対応", () => {
  const r = calculateRoi({ count: 400, minutesPerTask: 9, hourlyWage: 1300, reductionRate: 40, monthlyCost: 10000 });
  assert.equal(r.savedHours, 24.0);
  assert.equal(r.savedYen, 31200);
  assert.equal(r.annualYen, 254400);
  assert.ok(r.paybackMonths !== null);
  assert.equal(Number(r.paybackMonths.toFixed(1)), 0.3);
});

test("preset: 不動産仲介の反響対応", () => {
  const r = calculateRoi({ count: 250, minutesPerTask: 24, hourlyWage: 1800, reductionRate: 50, monthlyCost: 30000 });
  assert.equal(r.savedHours, 50.0);
  assert.equal(r.savedYen, 90000);
  assert.equal(r.annualYen, 720000);
  assert.ok(r.paybackMonths !== null);
  assert.equal(Number(r.paybackMonths.toFixed(1)), 0.3);
});

test("preset: ECカスタマーサポート", () => {
  const r = calculateRoi({ count: 1200, minutesPerTask: 6, hourlyWage: 1500, reductionRate: 30, monthlyCost: 20000 });
  assert.equal(r.savedHours, 36.0);
  assert.equal(r.savedYen, 54000);
  assert.equal(r.annualYen, 408000);
  assert.ok(r.paybackMonths !== null);
  assert.equal(Number(r.paybackMonths.toFixed(1)), 0.4);
});

// --- edge cases ---

test("all zero → no NaN/Infinity, paybackMonths null", () => {
  const r = calculateRoi({ count: 0, minutesPerTask: 0, hourlyWage: 0, reductionRate: 0, monthlyCost: 0 });
  assert.equal(r.totalHours, 0);
  assert.equal(r.savedHours, 0);
  assert.equal(r.savedYen, 0);
  assert.equal(r.annualYen, 0);
  assert.equal(r.paybackMonths, null);
});

test("empty string inputs → treat as 0", () => {
  const r = calculateRoi({ count: "", minutesPerTask: "", hourlyWage: "", reductionRate: "", monthlyCost: "" });
  assert.equal(r.savedYen, 0);
  assert.equal(r.paybackMonths, null);
  assert.ok(Number.isFinite(r.annualYen));
});

test("reduction rate 0% → savedYen 0, paybackMonths null, annualYen negative", () => {
  const r = calculateRoi({ count: 1000, minutesPerTask: 10, hourlyWage: 2000, reductionRate: 0, monthlyCost: 5000 });
  assert.equal(r.savedYen, 0);
  assert.equal(r.annualYen, -60000);
  assert.equal(r.paybackMonths, null);
});

test("monthlyCost 0 + savedYen > 0 → paybackMonths 0", () => {
  const r = calculateRoi({ count: 100, minutesPerTask: 60, hourlyWage: 1000, reductionRate: 50, monthlyCost: 0 });
  assert.equal(r.paybackMonths, 0);
});

test("count exceeds max (1e9) → clamped to 100000", () => {
  const r = calculateRoi({ count: 1e9, minutesPerTask: 60, hourlyWage: 1000, reductionRate: 100, monthlyCost: 0 });
  assert.equal(r.savedHours, 100000);
  assert.ok(Number.isFinite(r.savedYen));
  assert.ok(Number.isFinite(r.annualYen));
});

test("negative values → clamped to 0", () => {
  const r = calculateRoi({ count: -100, minutesPerTask: -10, hourlyWage: -500, reductionRate: -50, monthlyCost: -1000 });
  assert.equal(r.savedYen, 0);
  assert.equal(r.paybackMonths, null);
});

test("no NaN or non-finite in result for all presets", () => {
  const presets = [
    { count: 400, minutesPerTask: 9, hourlyWage: 1300, reductionRate: 40, monthlyCost: 10000 },
    { count: 250, minutesPerTask: 24, hourlyWage: 1800, reductionRate: 50, monthlyCost: 30000 },
    { count: 1200, minutesPerTask: 6, hourlyWage: 1500, reductionRate: 30, monthlyCost: 20000 },
  ];
  for (const preset of presets) {
    const r = calculateRoi(preset);
    assert.ok(Number.isFinite(r.totalHours), "totalHours must be finite");
    assert.ok(Number.isFinite(r.savedHours), "savedHours must be finite");
    assert.ok(Number.isFinite(r.savedYen), "savedYen must be finite");
    assert.ok(Number.isFinite(r.annualYen), "annualYen must be finite");
    assert.ok(r.paybackMonths === null || Number.isFinite(r.paybackMonths), "paybackMonths must be finite or null");
  }
});
