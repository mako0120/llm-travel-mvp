"use client";

import { useState } from "react";
import { calculateRoi } from "@/lib/roi/calculate.mjs";

type Fields = {
  industry: string;
  count: string;
  minutesPerTask: string;
  hourlyWage: string;
  reductionRate: string;
  monthlyCost: string;
};

const EMPTY: Fields = {
  industry: "",
  count: "",
  minutesPerTask: "",
  hourlyWage: "",
  reductionRate: "",
  monthlyCost: "",
};

const PRESETS = [
  {
    label: "飲食店の予約・問い合わせ対応",
    count: 400,
    minutesPerTask: 9,
    hourlyWage: 1300,
    reductionRate: 40,
    monthlyCost: 10000,
  },
  {
    label: "不動産仲介の反響対応",
    count: 250,
    minutesPerTask: 24,
    hourlyWage: 1800,
    reductionRate: 50,
    monthlyCost: 30000,
  },
  {
    label: "ECカスタマーサポート",
    count: 1200,
    minutesPerTask: 6,
    hourlyWage: 1500,
    reductionRate: 30,
    monthlyCost: 20000,
  },
] as const;

const LIMITS = {
  count: 100_000,
  minutesPerTask: 600,
  hourlyWage: 100_000,
  reductionRate: 100,
  monthlyCost: 10_000_000,
};

function isClamped(raw: string, max: number): boolean {
  const n = Number(raw);
  if (!Number.isFinite(n)) return false;
  return n < 0 || n > max;
}

export function RoiCalculator() {
  const [fields, setFields] = useState<Fields>(EMPTY);
  const [selectedPreset, setSelectedPreset] = useState<number | null>(null);

  function applyPreset(index: number) {
    const p = PRESETS[index];
    setFields({
      industry: p.label,
      count: String(p.count),
      minutesPerTask: String(p.minutesPerTask),
      hourlyWage: String(p.hourlyWage),
      reductionRate: String(p.reductionRate),
      monthlyCost: String(p.monthlyCost),
    });
    setSelectedPreset(index);
  }

  function handleChange(key: keyof Fields) {
    return (e: React.ChangeEvent<HTMLInputElement>) => {
      setFields((prev) => ({ ...prev, [key]: e.target.value }));
      if (key !== "industry") setSelectedPreset(null);
    };
  }

  const result = calculateRoi({
    count: fields.count,
    minutesPerTask: fields.minutesPerTask,
    hourlyWage: fields.hourlyWage,
    reductionRate: fields.reductionRate,
    monthlyCost: fields.monthlyCost,
  });

  const clamped =
    isClamped(fields.count, LIMITS.count) ||
    isClamped(fields.minutesPerTask, LIMITS.minutesPerTask) ||
    isClamped(fields.hourlyWage, LIMITS.hourlyWage) ||
    isClamped(fields.reductionRate, LIMITS.reductionRate) ||
    isClamped(fields.monthlyCost, LIMITS.monthlyCost);

  const paybackText =
    result.paybackMonths === null
      ? "算出不可(削減額が発生しないため)"
      : result.paybackMonths === 0
        ? "0.0ヶ月(初月から効果)"
        : `${result.paybackMonths.toFixed(1)}ヶ月`;

  return (
    <div className="roi-calculator">
      <p className="demo-disclaimer" role="note">
        これは<strong>シミュレーションです</strong>。実際の契約や効果を保証するものではありません。
        外部AI・外部通信・データ保存は行いません。
      </p>

      <section>
        <h2>入力例を選ぶ</h2>
        <div className="roi-preset-grid">
          {PRESETS.map((p, i) => (
            <button
              key={p.label}
              type="button"
              className={`roi-preset-btn${selectedPreset === i ? " selected" : ""}`}
              onClick={() => applyPreset(i)}
            >
              {p.label}
            </button>
          ))}
        </div>
      </section>

      <section>
        <h2>数値を入力する</h2>
        {clamped && (
          <p className="roi-clamp-note" role="note">
            ⚠ 一部の入力値が上限を超えているため、上限値で計算しています。
          </p>
        )}
        <div className="roi-form">
          <label className="roi-label">
            <span>業種(任意・計算に影響しません)</span>
            <input
              type="text"
              value={fields.industry}
              onChange={handleChange("industry")}
              placeholder="例: 飲食店"
              className="roi-input"
            />
          </label>
          <label className="roi-label">
            <span>月間作業件数</span>
            <input
              type="number"
              value={fields.count}
              onChange={handleChange("count")}
              min={0}
              max={LIMITS.count}
              placeholder="例: 400"
              className="roi-input"
            />
          </label>
          <label className="roi-label">
            <span>1件あたり作業時間(分)</span>
            <input
              type="number"
              value={fields.minutesPerTask}
              onChange={handleChange("minutesPerTask")}
              min={0}
              max={LIMITS.minutesPerTask}
              placeholder="例: 9"
              className="roi-input"
            />
          </label>
          <label className="roi-label">
            <span>人件費(時給・円)</span>
            <input
              type="number"
              value={fields.hourlyWage}
              onChange={handleChange("hourlyWage")}
              min={0}
              max={LIMITS.hourlyWage}
              placeholder="例: 1300"
              className="roi-input"
            />
          </label>
          <label className="roi-label">
            <span>想定削減率(%)</span>
            <input
              type="number"
              value={fields.reductionRate}
              onChange={handleChange("reductionRate")}
              min={0}
              max={LIMITS.reductionRate}
              placeholder="例: 40"
              className="roi-input"
            />
          </label>
          <label className="roi-label">
            <span>月額導入費(円)</span>
            <input
              type="number"
              value={fields.monthlyCost}
              onChange={handleChange("monthlyCost")}
              min={0}
              max={LIMITS.monthlyCost}
              placeholder="例: 10000"
              className="roi-input"
            />
          </label>
        </div>
      </section>

      <section aria-live="polite">
        <h2>計算結果</h2>
        <div className="result-grid roi-result-grid">
          <div className="result-block">
            <h3>月間削減時間</h3>
            <p className="roi-result-value">
              {result.savedHours.toFixed(1)}
              <span className="roi-unit">時間</span>
            </p>
          </div>
          <div className="result-block">
            <h3>月間削減額</h3>
            <p className="roi-result-value">¥{result.savedYen.toLocaleString("ja-JP")}</p>
          </div>
          <div className="result-block">
            <h3>年間効果</h3>
            <p className="roi-result-value">¥{result.annualYen.toLocaleString("ja-JP")}</p>
            {result.annualYen < 0 && (
              <p className="roi-note">現在の入力では投資対効果が出ません</p>
            )}
          </div>
          <div className="result-block">
            <h3>投資回収月数</h3>
            <p className="roi-result-value roi-payback">{paybackText}</p>
          </div>
        </div>
        <p className="demo-disclaimer roi-disclaimer-bottom" role="note">
          これはシミュレーションです。実際の契約・効果を保証するものではありません。
        </p>
      </section>

      <section className="roi-formula-section">
        <h2>計算根拠と前提条件</h2>
        <pre className="roi-formula">{`月間総作業時間(時) = 月間作業件数 × (1件あたり作業時間(分) ÷ 60)
月間削減時間(時)   = 月間総作業時間 × (想定削減率 ÷ 100)
月間削減額(円)     = 月間削減時間 × 人件費(時給)
年間効果(円)       = (月間削減額 − 月額導入費) × 12
投資回収月数        = 月間削減額 > 0 ? 月額導入費 ÷ 月間削減額 : 算出不可`}</pre>
        <ul className="roi-formula-notes">
          <li>削減率は想定値であり、実際の削減効果を保証するものではありません。</li>
          <li>年間効果 = (月間削減額 − 月額導入費) × 12ヶ月で算出しています。</li>
          <li>各入力値の上限: 件数 100,000件 / 作業時間 600分 / 時給 100,000円 / 削減率 100% / 月額費 10,000,000円</li>
          <li>入力が未入力・0・上限超過の場合は 0 または上限値として計算します。</li>
        </ul>
      </section>
    </div>
  );
}
