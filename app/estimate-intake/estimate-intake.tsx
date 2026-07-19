"use client";

import { useState } from "react";
import {
  ESTIMATE_PRESETS,
  calculateEstimateReadiness,
} from "@/lib/estimate-intake/calculate.mjs";

type Values = {
  workType: string;
  buildingType: string;
  desiredTiming: string;
  budget: string;
  location: string;
  hasPhotos: boolean;
  contactMethod: string;
  urgency: "high" | "medium" | "low";
};

const EMPTY_VALUES: Values = {
  workType: "",
  buildingType: "",
  desiredTiming: "",
  budget: "",
  location: "",
  hasPhotos: false,
  contactMethod: "",
  urgency: "low",
};

const SELECTS = [
  {
    id: "buildingType",
    label: "建物種別",
    options: ["戸建て", "マンション", "店舗・事務所", "その他"],
  },
  {
    id: "desiredTiming",
    label: "希望時期",
    options: ["できるだけ早く", "1か月以内", "3か月以内", "半年以内", "未定"],
  },
  {
    id: "contactMethod",
    label: "希望する連絡方法",
    options: ["電話", "メール", "LINE"],
  },
] as const;

export function EstimateIntake() {
  const [values, setValues] = useState<Values>(EMPTY_VALUES);
  const [selectedPreset, setSelectedPreset] = useState("");
  const [interestShown, setInterestShown] = useState(false);
  const result = calculateEstimateReadiness(values);

  function update<K extends keyof Values>(key: K, value: Values[K]) {
    setValues((current) => ({ ...current, [key]: value }));
    setSelectedPreset("");
    setInterestShown(false);
  }

  function choosePreset(preset: (typeof ESTIMATE_PRESETS)[number]) {
    setValues(preset.values as Values);
    setSelectedPreset(preset.id);
    setInterestShown(false);
  }

  return (
    <div className="estimate-intake">
      <p className="demo-disclaimer" role="note">
        入力はブラウザ内だけで計算されます。外部送信・保存・AI接続・課金は行いません。
      </p>

      <section aria-labelledby="estimate-preset-heading">
        <div className="section-heading">
          <div>
            <p className="step-kicker">STEP 1</p>
            <h2 id="estimate-preset-heading">よくある相談から試す</h2>
          </div>
          <span className="time-chip">約30秒</span>
        </div>
        <div className="estimate-preset-grid">
          {ESTIMATE_PRESETS.map((preset) => (
            <button
              type="button"
              className={`estimate-preset${selectedPreset === preset.id ? " selected" : ""}`}
              onClick={() => choosePreset(preset)}
              key={preset.id}
            >
              <strong>{preset.label}</strong>
              <span>{preset.description}</span>
            </button>
          ))}
        </div>
      </section>

      <section aria-labelledby="estimate-input-heading">
        <div className="section-heading">
          <div>
            <p className="step-kicker">STEP 2</p>
            <h2 id="estimate-input-heading">問い合わせ内容を整理</h2>
          </div>
          <button type="button" className="text-button" onClick={() => {
            setValues(EMPTY_VALUES);
            setSelectedPreset("");
          }}>
            入力をリセット
          </button>
        </div>
        <div className="estimate-form">
          <label className="estimate-field estimate-field-wide">
            <span>工事内容</span>
            <input
              value={values.workType}
              onChange={(event) => update("workType", event.target.value)}
              placeholder="例：浴室を全面リフォームしたい"
            />
          </label>
          {SELECTS.map((field) => (
            <label className="estimate-field" key={field.id}>
              <span>{field.label}</span>
              <select
                value={values[field.id]}
                onChange={(event) => update(field.id, event.target.value)}
              >
                <option value="">選択してください</option>
                {field.options.map((option) => <option key={option}>{option}</option>)}
              </select>
            </label>
          ))}
          <label className="estimate-field">
            <span>おおよその予算</span>
            <input
              value={values.budget}
              onChange={(event) => update("budget", event.target.value)}
              placeholder="例：100万円前後"
            />
          </label>
          <label className="estimate-field">
            <span>現場住所（市区町村まで）</span>
            <input
              value={values.location}
              onChange={(event) => update("location", event.target.value)}
              placeholder="例：大阪府吹田市"
            />
          </label>
          <fieldset className="estimate-field">
            <legend>緊急度</legend>
            <div className="segmented-options">
              {[
                ["high", "緊急"],
                ["medium", "早め"],
                ["low", "通常"],
              ].map(([value, label]) => (
                <label key={value}>
                  <input
                    type="radio"
                    name="urgency"
                    checked={values.urgency === value}
                    onChange={() => update("urgency", value as Values["urgency"])}
                  />
                  {label}
                </label>
              ))}
            </div>
          </fieldset>
          <label className="photo-toggle">
            <input
              type="checkbox"
              checked={values.hasPhotos}
              onChange={(event) => update("hasPhotos", event.target.checked)}
            />
            <span>
              <strong>現場写真あり</strong>
              <small>全体・問題箇所・周辺の写真がある</small>
            </span>
          </label>
        </div>
      </section>

      <section className="estimate-results" aria-live="polite" aria-labelledby="estimate-result-heading">
        <div className="section-heading">
          <div>
            <p className="step-kicker">STEP 3</p>
            <h2 id="estimate-result-heading">担当者へ渡す整理結果</h2>
          </div>
          <span className={`priority-badge priority-${values.urgency}`}>{result.priority.label}</span>
        </div>

        <div className="readiness-card">
          <div>
            <span>見積準備度</span>
            <strong>{result.score}<small>%</small></strong>
          </div>
          <div className="readiness-track" aria-label={`見積準備度 ${result.score}%`}>
            <span style={{ width: `${result.score}%` }} />
          </div>
          <p>{result.isReady ? "現地調査の案内へ進める情報量です。" : "不足情報を確認してから、現地調査へつなげましょう。"}</p>
        </div>

        <div className="estimate-result-grid">
          <ResultCard
            title="不足している情報"
            empty="主要情報はそろっています"
            items={result.missing.map((item) => item.label)}
            tone="danger"
          />
          <ResultCard
            title="最初の返信で聞くこと"
            empty="追加質問なし。現地調査の日程を案内できます"
            items={result.questions}
            tone="warn"
          />
        </div>

        <div className="next-action-card">
          <span>次にやること</span>
          <strong>{result.nextAction}</strong>
          <p>{result.priority.reason}</p>
        </div>
      </section>

      <section className="pilot-offer">
        <div>
          <p className="eyebrow">先着3社・有料モニター（仮）</p>
          <h2>初期設定19,800円 + 月額4,980円</h2>
          <p>御社の問い合わせ項目に合わせた初期設定と、30日間の試験運用を想定しています。</p>
        </div>
        <button type="button" className="button button-primary" onClick={() => setInterestShown(true)}>
          導入相談の流れを見る
        </button>
        {interestShown && (
          <p className="pilot-response">
            現在は需要検証中です。このボタンから情報は送信されません。実際の受付開始前に、連絡方法と個人情報の扱いを整備します。
          </p>
        )}
      </section>
    </div>
  );
}

function ResultCard({
  title,
  items,
  empty,
  tone,
}: {
  title: string;
  items: string[];
  empty: string;
  tone: string;
}) {
  return (
    <div className={`estimate-result-card result-${tone}`}>
      <h3>{title}<span>{items.length}件</span></h3>
      {items.length
        ? <ul>{items.map((item) => <li key={item}>{item}</li>)}</ul>
        : <p className="result-empty">✓ {empty}</p>}
    </div>
  );
}
