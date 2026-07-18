/**
 * @param {number | string} value
 * @param {number} max
 * @returns {number}
 */
export function sanitize(value, max) {
  const n = Number(value);
  if (!Number.isFinite(n)) return 0;
  if (n < 0) return 0;
  if (n > max) return max;
  return n;
}

/**
 * @typedef {{ totalHours: number; savedHours: number; savedYen: number; annualYen: number; paybackMonths: number | null }} RoiResult
 */

/**
 * @param {{ count: number | string; minutesPerTask: number | string; hourlyWage: number | string; reductionRate: number | string; monthlyCost: number | string }} input
 * @returns {RoiResult}
 */
export function calculateRoi({ count, minutesPerTask, hourlyWage, reductionRate, monthlyCost }) {
  const safeCount = sanitize(count, 100_000);
  const safeMinutes = sanitize(minutesPerTask, 600);
  const safeWage = sanitize(hourlyWage, 100_000);
  const safeRate = sanitize(reductionRate, 100);
  const safeCost = sanitize(monthlyCost, 10_000_000);

  const totalHours = safeCount * (safeMinutes / 60);
  const savedHours = totalHours * (safeRate / 100);
  const savedYen = Math.round(savedHours * safeWage);
  const annualYen = Math.round((savedYen - safeCost) * 12);
  const paybackMonths = savedYen > 0 ? safeCost / savedYen : null;

  return { totalHours, savedHours, savedYen, annualYen, paybackMonths };
}
