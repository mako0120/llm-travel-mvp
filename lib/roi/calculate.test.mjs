import { test } from "node:test";
import assert from "node:assert/strict";
import { clampInputs, calculateRoi, formatMonths, PRESETS } from "./calculate.mjs";

test("PRESETS has at least 3 input examples", () => {
  assert.ok(PRESETS.length >= 3);
});

for (const preset of PRESETS) {
  test(`preset "${preset.id}" produces a finite, non-negative result`, () => {
    const { values } = clampInputs(preset.values);
    const result = calculateRoi(values);
    assert.ok(Number.isFinite(result.monthlyTotalHours));
    assert.ok(Number.isFinite(result.monthlySavedHours));
    assert.ok(Number.isFinite(result.monthlySavedCost));
    assert.ok(Number.isFinite(result.annualImpact));
    assert.ok(result.monthlySavedHours >= 0);
    assert.ok(result.monthlySavedCost >= 0);
  });
}

test("restaurant preset matches hand-calculated values", () => {
  const { values } = clampInputs(PRESETS[0].values);
  const result = calculateRoi(values);
  // 300件 * (5分/60) = 25時間、削減率60% -> 15時間
  assert.equal(result.monthlyTotalHours, 25);
  assert.equal(result.monthlySavedHours, 15);
  // 15時間 * 1200円 = 18000円
  assert.equal(result.monthlySavedCost, 18000);
  // (18000 - 15000) * 12 = 36000
  assert.equal(result.annualImpact, 36000);
  // 15000 / 18000 = 0.8333...
  assert.ok(Math.abs(result.paybackMonths - 15000 / 18000) < 1e-9);
});

test("all-zero input never produces NaN or Infinity", () => {
  const { values } = clampInputs({
    monthlyVolume: 0,
    minutesPerItem: 0,
    hourlyLaborCost: 0,
    reductionRate: 0,
    monthlyFee: 0,
  });
  const result = calculateRoi(values);
  assert.equal(result.monthlyTotalHours, 0);
  assert.equal(result.monthlySavedHours, 0);
  assert.equal(result.monthlySavedCost, 0);
  assert.equal(result.annualImpact, 0);
  assert.equal(result.paybackMonths, null);
  assert.equal(formatMonths(result.paybackMonths), "算出不可(削減額が発生しないため)");
});

test("blank/undefined/non-numeric input is treated as 0, never NaN", () => {
  const { values, adjustedFields } = clampInputs({
    monthlyVolume: "",
    minutesPerItem: undefined,
    hourlyLaborCost: "abc",
    reductionRate: null,
    monthlyFee: NaN,
  });
  for (const value of Object.values(values)) {
    assert.ok(Number.isFinite(value));
  }
  const result = calculateRoi(values);
  assert.ok(Number.isFinite(result.monthlySavedCost));
  assert.ok(Number.isFinite(result.annualImpact));
  assert.equal(result.paybackMonths, null);
  assert.ok(adjustedFields.length > 0);
});

test("extreme values are clamped to the documented limits, not left as Infinity", () => {
  const { values, adjustedFields } = clampInputs({
    monthlyVolume: 1e12,
    minutesPerItem: 1e12,
    hourlyLaborCost: 1e12,
    reductionRate: 1e12,
    monthlyFee: 1e12,
  });
  assert.equal(values.monthlyVolume, 100000);
  assert.equal(values.minutesPerItem, 600);
  assert.equal(values.hourlyLaborCost, 100000);
  assert.equal(values.reductionRate, 100);
  assert.equal(values.monthlyFee, 10000000);
  assert.equal(adjustedFields.length, 5);

  const result = calculateRoi(values);
  assert.ok(Number.isFinite(result.monthlyTotalHours));
  assert.ok(Number.isFinite(result.monthlySavedHours));
  assert.ok(Number.isFinite(result.monthlySavedCost));
  assert.ok(Number.isFinite(result.annualImpact));
  assert.ok(result.paybackMonths === null || Number.isFinite(result.paybackMonths));
});

test("negative input is clamped to the minimum (0), not left negative", () => {
  const { values } = clampInputs({
    monthlyVolume: -50,
    minutesPerItem: -10,
    hourlyLaborCost: -100,
    reductionRate: -20,
    monthlyFee: -1000,
  });
  for (const value of Object.values(values)) {
    assert.ok(value >= 0);
  }
});

test("zero monthlyFee still returns a finite payback (0 months)", () => {
  const { values } = clampInputs({
    monthlyVolume: 100,
    minutesPerItem: 30,
    hourlyLaborCost: 2000,
    reductionRate: 50,
    monthlyFee: 0,
  });
  const result = calculateRoi(values);
  assert.equal(result.paybackMonths, 0);
});

test("reductionRate above 100 is clamped to 100", () => {
  const { values } = clampInputs({
    monthlyVolume: 100,
    minutesPerItem: 30,
    hourlyLaborCost: 2000,
    reductionRate: 250,
    monthlyFee: 1000,
  });
  assert.equal(values.reductionRate, 100);
});
