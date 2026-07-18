"use client";

import { useMemo, useState } from "react";
import {
  LIMITS,
  PRESETS,
  calculateRoi,
  clampInputs,
  formatHours,
  formatMonths,
  formatYen,
} from "@/lib/roi/calculate.mjs";

type InputKey = keyof typeof LIMITS;

type RawInputs = Record<InputKey, string>;

const FIELD_META: Array<{
  key: InputKey;
  label: string;
  suffix: string;
  step?: number;
}> = [
  { key: "monthlyVolume", label: "月間作業件数", suffix: "件" },
  { key: "minutesPerItem", label: "1件あたり作業時間", suffix: "分" },
  { key: "hourlyLaborCost", label: "人件費(時給)", suffix: "円" },
  { key: "reductionRate", label: "想定削減率", suffix: "%" },
  { key: "monthlyFee", label: "月額導入費", suffix: "円" },
];

function toRawInputs(values: Record<InputKey, number>): RawInputs {
  return {
    monthlyVolume: String(values.monthlyVolume),
    minutesPerItem: String(values.minutesPerItem),
    hourlyLaborCost: String(values.hourlyLaborCost),
    reductionRate: String(values.reductionRate),
    monthlyFee: String(values.monthlyFee),
  };
}

export function RoiCalculator() {
  const [raw, setRaw] = useState<RawInputs>(toRawInputs(PRESETS[0].values));
  const [selectedPreset, setSelectedPreset] = useState<string>(PRESETS[0].id);

  const { values, adjustedFields } = useMemo(() => clampInputs(raw), [raw]);
  const result = useMemo(() => calculateRoi(values), [values]);

  const handleChange = (key: InputKey, value: string) => {
    setSelectedPreset("");
    setRaw((prev) => ({ ...prev, [key]: value }));
  };

  const handlePreset = (id: string) => {
    const preset = PRESETS.find((p) => p.id === id);
    if (!preset) return;
    setSelectedPreset(id);
    setRaw(toRawInputs(preset.values));
  };

  return (
    <div className="roi-calculator">
      <p className="demo-disclaimer" role="note">
        これは<strong>簡易シミュレーションのクリックデモ</strong>です。実際の契約条件・効果を保証するものではありません。営業説明時は前提条件を顧客と必ず確認してください。
      </p>

      <fieldset className="sample-picker">
        <legend>入力例(3種類)</legend>
        <div className="preset-list" role="radiogroup" aria-label="入力例プリセット">
          {PRESETS.map((preset) => (
            <button
              key={preset.id}
              type="button"
              className={`preset-button${selectedPreset === preset.id ? " selected" : ""}`}
              aria-pressed={selectedPreset === preset.id}
              onClick={() => handlePreset(preset.id)}
            >
              {preset.label}
            </button>
          ))}
        </div>
      </fieldset>

      <form className="roi-form" aria-label="ROI計算の入力項目" onSubmit={(e) => e.preventDefault()}>
        {FIELD_META.map((field) => {
          const inputId = `roi-${field.key}`;
          const wasAdjusted = adjustedFields.includes(field.label);
          return (
            <div className="roi-field" key={field.key}>
              <label htmlFor={inputId}>
                {field.label}
                <span className="roi-field-suffix">({field.suffix})</span>
              </label>
              <input
                id={inputId}
                type="number"
                inputMode="decimal"
                min={LIMITS[field.key].min}
                max={LIMITS[field.key].max}
                value={raw[field.key]}
                onChange={(e) => handleChange(field.key, e.target.value)}
              />
              {wasAdjusted && (
                <p className="roi-field-note">
                  入力可能な範囲(0〜{LIMITS[field.key].max.toLocaleString("ja-JP")})に調整して計算しています。
                </p>
              )}
            </div>
          );
        })}
      </form>

      <section className="result-panel" aria-live="polite">
        <div className="result-grid">
          <div className="result-block">
            <h3>月間削減時間</h3>
            <p className="roi-headline">{formatHours(result.monthlySavedHours)}</p>
          </div>
          <div className="result-block">
            <h3>月間削減額</h3>
            <p className="roi-headline">{formatYen(result.monthlySavedCost)}</p>
          </div>
          <div className="result-block">
            <h3>年間効果(導入費控除後)</h3>
            <p className="roi-headline">{formatYen(result.annualImpact)}</p>
          </div>
          <div className="result-block">
            <h3>投資回収期間</h3>
            <p className="roi-headline">{formatMonths(result.paybackMonths)}</p>
          </div>
        </div>

        <div className="result-block">
          <h3>計算根拠と前提条件</h3>
          <ul className="notice-list">
            <li>月間総作業時間 = 月間作業件数 × (1件あたり作業時間 ÷ 60)</li>
            <li>月間削減時間 = 月間総作業時間 × (想定削減率 ÷ 100)</li>
            <li>月間削減額 = 月間削減時間 × 人件費(時給)</li>
            <li>年間効果 = (月間削減額 − 月額導入費) × 12</li>
            <li>投資回収期間 = 月額導入費 ÷ 月間削減額(削減額が0円の場合は「算出不可」)</li>
          </ul>
        </div>
      </section>
    </div>
  );
}
