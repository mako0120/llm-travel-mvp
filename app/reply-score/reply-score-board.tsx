"use client";

import { useState } from "react";
import {
  REPLY_PRESETS,
  calculateReplyScore,
} from "@/lib/reply-score/calculate.mjs";

type Lane = "reply_now" | "human_review" | "follow_up";

type Item = {
  id: string;
  label: string;
  guestMessage: string;
  score: number;
  lane: Lane;
  inputs: {
    elapsed: string;
    checkin: string;
    value: string;
    language: string;
    intent: string;
    termsCheckNeeded: boolean;
  };
};

type Result = {
  items: Item[];
  replyNow: Item[];
  humanReview: Item[];
  followUp: Item[];
  summary: {
    urgentCount: number;
    humanReviewCount: number;
    followUpCount: number;
    preventedCount: number;
  };
};

const LANE_LABEL: Record<Lane, string> = {
  reply_now: "今すぐ返信",
  human_review: "人間確認",
  follow_up: "追客候補",
};

const LANE_PRIORITY_CLASS: Record<Lane, string> = {
  reply_now: "priority-high",
  human_review: "priority-medium",
  follow_up: "priority-low",
};

const ELAPSED_LABEL: Record<string, string> = {
  under1h: "受信から1時間未満",
  "1to6h": "受信から1〜6時間",
  "6to24h": "受信から6〜24時間",
  over24h: "受信から24時間超",
};

const CHECKIN_LABEL: Record<string, string> = {
  "0to1day": "チェックインまで当日〜翌日",
  "2to7days": "チェックインまで2〜7日",
  "8to30days": "チェックインまで8〜30日",
  over30days: "チェックインまで30日超",
};

const VALUE_LABEL: Record<string, string> = {
  low: "想定予約金額: 小",
  mid: "想定予約金額: 中",
  high: "想定予約金額: 大",
};

const LANGUAGE_LABEL: Record<string, string> = {
  easy: "言語難易度: 低",
  medium: "言語難易度: 中",
  hard: "言語難易度: 高",
};

const INTENT_LABEL: Record<string, string> = {
  weak: "予約意欲: 弱",
  medium: "予約意欲: 中",
  strong: "予約意欲: 強",
};

export function ReplyScoreBoard() {
  const [selectedPreset, setSelectedPreset] = useState(REPLY_PRESETS[0].id);

  const preset = REPLY_PRESETS.find((p) => p.id === selectedPreset) ?? REPLY_PRESETS[0];
  const result = calculateReplyScore(preset.values) as Result;

  return (
    <div className="reply-score-board">
      <p className="demo-disclaimer" role="note">
        入力と結果はこの画面内だけで計算します。外部送信、AI接続、保存、課金は行いません。表示される分類は必ず人が確認してください。
      </p>

      <section aria-labelledby="reply-preset-heading">
        <h2 id="reply-preset-heading">施設の状況を選ぶ</h2>
        <div className="roi-preset-grid">
          {REPLY_PRESETS.map((p) => (
            <button
              type="button"
              key={p.id}
              className={`roi-preset-btn${selectedPreset === p.id ? " selected" : ""}`}
              onClick={() => setSelectedPreset(p.id)}
            >
              {p.label}
            </button>
          ))}
        </div>
      </section>

      <section aria-live="polite" aria-labelledby="reply-summary-heading">
        <h2 id="reply-summary-heading">集計</h2>
        <div className="result-grid roi-result-grid">
          <div className="result-block">
            <h3>今すぐ返信が必要</h3>
            <p className="roi-result-value">
              {result.summary.urgentCount}
              <span className="roi-unit">件</span>
            </p>
          </div>
          <div className="result-block">
            <h3>人間確認が必要</h3>
            <p className="roi-result-value">
              {result.summary.humanReviewCount}
              <span className="roi-unit">件</span>
            </p>
          </div>
          <div className="result-block">
            <h3>追客候補</h3>
            <p className="roi-result-value">
              {result.summary.followUpCount}
              <span className="roi-unit">件</span>
            </p>
          </div>
          <div className="result-block">
            <h3>取りこぼし防止見込み(仮)</h3>
            <p className="roi-result-value">
              {result.summary.preventedCount}
              <span className="roi-unit">件</span>
            </p>
          </div>
        </div>
      </section>

      <section aria-labelledby="reply-items-heading">
        <h2 id="reply-items-heading">問い合わせ一覧({result.items.length}件)</h2>
        <div className="reply-item-list">
          {result.items.map((item) => (
            <article className="reply-item-card" key={item.id}>
              <div className="reply-item-head">
                <h3>{item.label}</h3>
                <span className={`priority-badge ${LANE_PRIORITY_CLASS[item.lane]}`}>
                  {LANE_LABEL[item.lane]}
                </span>
              </div>
              <p className="reply-item-message">{item.guestMessage}</p>
              <div className="reply-item-score">
                <span>返信優先度スコア</span>
                <strong>{item.score}</strong>
                <span>/ 100</span>
              </div>
              <ul className="reply-item-inputs">
                <li>{ELAPSED_LABEL[item.inputs.elapsed]}</li>
                <li>{CHECKIN_LABEL[item.inputs.checkin]}</li>
                <li>{VALUE_LABEL[item.inputs.value]}</li>
                <li>{LANGUAGE_LABEL[item.inputs.language]}</li>
                <li>{INTENT_LABEL[item.inputs.intent]}</li>
                <li>{item.inputs.termsCheckNeeded ? "規約確認: 必要" : "規約確認: 不要"}</li>
              </ul>
            </article>
          ))}
        </div>
      </section>

      <section className="roi-formula-section" aria-labelledby="reply-formula-heading">
        <h2 id="reply-formula-heading">計算根拠と前提条件</h2>
        <pre className="roi-formula">{`合計点 = 経過時間(0-3) + 日数(0-3) + 予約金額(0-2) + 予約意欲(0-2)
優先度スコア = (合計点 ÷ 10点) × 100
規約確認が必要 または 言語難易度が高い
  → スコアに関わらず「人間確認」に分類`}</pre>
        <ul className="roi-formula-notes">
          <li>結果は6件の固定サンプル問い合わせと、選択した施設プリセットの固定値だけを使う決定論的な計算です。</li>
          <li>実際に返信する前に、内容と施設ルールを必ず人が確認してください。</li>
          <li>「取りこぼし防止見込み」は、チェックインが近く予約意欲が中〜強で、追客候補に落ちていない件数の仮の目安です。</li>
        </ul>
      </section>
    </div>
  );
}
