// 純粋な計算ロジックのみ。外部通信・保存・DOM依存は一切含まない。

export const LIMITS = {
  monthlyVolume: { min: 0, max: 100000 },
  minutesPerItem: { min: 0, max: 600 },
  hourlyLaborCost: { min: 0, max: 100000 },
  reductionRate: { min: 0, max: 100 },
  monthlyFee: { min: 0, max: 10000000 },
};

const FIELD_LABELS = {
  monthlyVolume: "月間作業件数",
  minutesPerItem: "1件あたり作業時間",
  hourlyLaborCost: "人件費(時給)",
  reductionRate: "想定削減率",
  monthlyFee: "月額導入費",
};

function sanitizeNumber(value, { min, max }) {
  const num = typeof value === "number" ? value : Number(value);
  if (!Number.isFinite(num)) return min;
  if (num < min) return min;
  if (num > max) return max;
  return num;
}

// 生の入力(文字列/未入力/極端値を含む)を、NaN・Infinityを一切生まない
// 安全な数値へクランプする。どのフィールドが調整されたかも返す。
export function clampInputs(raw = {}) {
  const values = {};
  const adjustedFields = [];

  for (const key of Object.keys(LIMITS)) {
    const limit = LIMITS[key];
    const sanitized = sanitizeNumber(raw[key], limit);
    values[key] = sanitized;

    const rawNum = typeof raw[key] === "number" ? raw[key] : Number(raw[key]);
    if (!Number.isFinite(rawNum) || rawNum !== sanitized) {
      adjustedFields.push(FIELD_LABELS[key]);
    }
  }

  return { values, adjustedFields };
}

// values は clampInputs 済みの安全な数値を想定。
export function calculateRoi(values) {
  const { monthlyVolume, minutesPerItem, hourlyLaborCost, reductionRate, monthlyFee } = values;

  const monthlyTotalHours = monthlyVolume * (minutesPerItem / 60);
  const monthlySavedHours = monthlyTotalHours * (reductionRate / 100);
  const monthlySavedCost = monthlySavedHours * hourlyLaborCost;
  const annualImpact = (monthlySavedCost - monthlyFee) * 12;
  // 削減額が発生しない場合はInfinityを返さず null(=算出不可)にする。
  const paybackMonths = monthlySavedCost > 0 ? monthlyFee / monthlySavedCost : null;

  return {
    monthlyTotalHours,
    monthlySavedHours,
    monthlySavedCost,
    annualImpact,
    paybackMonths,
  };
}

export function formatYen(value) {
  const rounded = Math.round(Number.isFinite(value) ? value : 0);
  return `${rounded.toLocaleString("ja-JP")}円`;
}

export function formatHours(value) {
  const rounded = Math.round((Number.isFinite(value) ? value : 0) * 10) / 10;
  return `${rounded.toLocaleString("ja-JP")}時間`;
}

export function formatMonths(value) {
  if (value === null || !Number.isFinite(value)) return "算出不可(削減額が発生しないため)";
  const rounded = Math.round(value * 10) / 10;
  return `${rounded.toLocaleString("ja-JP")}か月`;
}

export const PRESETS = [
  {
    id: "restaurant",
    label: "飲食店(予約・問い合わせ対応)",
    values: {
      monthlyVolume: 300,
      minutesPerItem: 5,
      hourlyLaborCost: 1200,
      reductionRate: 60,
      monthlyFee: 15000,
    },
  },
  {
    id: "realestate",
    label: "不動産仲介(反響対応)",
    values: {
      monthlyVolume: 150,
      minutesPerItem: 10,
      hourlyLaborCost: 1800,
      reductionRate: 50,
      monthlyFee: 30000,
    },
  },
  {
    id: "ecommerce",
    label: "ECカスタマーサポート",
    values: {
      monthlyVolume: 800,
      minutesPerItem: 4,
      hourlyLaborCost: 1500,
      reductionRate: 40,
      monthlyFee: 25000,
    },
  },
];
