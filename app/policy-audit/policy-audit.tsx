"use client";

import { useState } from "react";
import {
  POLICY_CATEGORIES,
  POLICY_PRESETS,
  calculatePolicyAudit,
} from "@/lib/policy-audit/calculate.mjs";

type Status = "clear" | "unclear" | "missing";
type Values = Record<string, Status>;

const STATUS_OPTIONS: { value: Status; label: string }[] = [
  { value: "clear", label: "記載あり" },
  { value: "unclear", label: "曖昧" },
  { value: "missing", label: "未記載" },
];

const initialValues = Object.fromEntries(
  POLICY_CATEGORIES.map(({ id }) => [id, "missing"]),
) as Values;

export function PolicyAudit() {
  const [values, setValues] = useState<Values>(initialValues);
  const [selectedPreset, setSelectedPreset] = useState("");
  const [interestShown, setInterestShown] = useState(false);
  const result = calculatePolicyAudit(values);

  function choosePreset(preset: (typeof POLICY_PRESETS)[number]) {
    setValues(preset.values as Values);
    setSelectedPreset(preset.id);
    setInterestShown(false);
  }

  function updateCategory(id: string, status: Status) {
    setValues((current) => ({ ...current, [id]: status }));
    setSelectedPreset("");
  }

  return (
    <div className="policy-audit">
      <p className="demo-disclaimer" role="note">
        入力と結果はこの画面内だけで計算します。外部送信、AI接続、保存、課金は行いません。
      </p>

      <section aria-labelledby="preset-heading">
        <h2 id="preset-heading">施設の例を選ぶ</h2>
        <div className="audit-preset-grid">
          {POLICY_PRESETS.map((preset) => (
            <button
              type="button"
              className={`roi-preset-btn${selectedPreset === preset.id ? " selected" : ""}`}
              onClick={() => choosePreset(preset)}
              key={preset.id}
            >
              {preset.label}
            </button>
          ))}
        </div>
      </section>

      <section aria-labelledby="categories-heading">
        <h2 id="categories-heading">6つの施設ルールを確認</h2>
        <div className="audit-category-list">
          {POLICY_CATEGORIES.map((category) => (
            <fieldset className="audit-category" key={category.id}>
              <legend>{category.label}</legend>
              <p>{category.guidance}</p>
              <div className="audit-status-options">
                {STATUS_OPTIONS.map((option) => (
                  <label key={option.value}>
                    <input
                      type="radio"
                      name={category.id}
                      value={option.value}
                      checked={values[category.id] === option.value}
                      onChange={() => updateCategory(category.id, option.value)}
                    />
                    {option.label}
                  </label>
                ))}
              </div>
            </fieldset>
          ))}
        </div>
      </section>

      <section className="audit-results" aria-live="polite" aria-labelledby="result-heading">
        <div className="audit-score">
          <span>FAQ準備度</span>
          <strong>{result.score}</strong>
          <span>/ 100</span>
        </div>
        <progress className="audit-progress" max="100" value={result.score}>
          {result.score}%
        </progress>
        <h2 id="result-heading">診断結果</h2>
        <div className="audit-result-grid">
          <ResultList title="AI回答可能" tone="ok" items={result.answerable.map((item) => item.label)} />
          <ResultList title="人間確認" tone="warn" items={result.humanReview.map((item) => item.label)} />
          <ResultList title="情報不足" tone="danger" items={result.missing.map((item) => item.label)} />
        </div>
        <div className="result-block">
          <h3>優先整備チェックリスト</h3>
          {result.checklist.length ? (
            <ol className="audit-checklist">
              {result.checklist.map((item) => (
                <li key={item.id}>
                  <strong>{item.priority}: {item.label}</strong>
                  <span>{item.guidance}</span>
                </li>
              ))}
            </ol>
          ) : <p>全カテゴリが明確です。実際の回答内容は必ず人が確認してください。</p>}
        </div>
      </section>

      <section className="roi-formula-section" aria-labelledby="audit-formula-heading">
        <h2 id="audit-formula-heading">計算根拠と前提条件</h2>
        <pre className="roi-formula">準備度 = (合計点 ÷ 12点) × 100{"\n"}記載あり: 2点 / 曖昧: 1点 / 未記載: 0点</pre>
        <ul className="roi-formula-notes">
          <li>結果は入力した6カテゴリだけを使う固定計算です。</li>
          <li>実際にAIへ任せる前に、回答内容と施設ルールを人が確認してください。</li>
        </ul>
      </section>

      <section className="audit-offer">
        <p className="eyebrow">想定プラン(仮)</p>
        <h2>月額4,980円</h2>
        <p>正式な販売・契約・決済ではありません。需要を確認するための仮表示です。</p>
        <button type="button" className="button button-primary" onClick={() => setInterestShown(true)}>
          導入相談に興味がある
        </button>
        {interestShown && <p className="audit-interest">ありがとうございます。この操作は保存・送信されません。</p>}
      </section>
    </div>
  );
}

function ResultList({ title, tone, items }: { title: string; tone: string; items: string[] }) {
  return (
    <div className={`result-block audit-result audit-result-${tone}`}>
      <h3>{title} <span>{items.length}件</span></h3>
      {items.length ? <ul>{items.map((item) => <li key={item}>{item}</li>)}</ul> : <p>該当なし</p>}
    </div>
  );
}
