"use client";

import { useId, useState } from "react";
import { INQUIRIES } from "@/lib/workbench/sample-data";
import { POLICY_RULES, getPolicyRulesByIds, type PolicyRuleId } from "@/lib/workbench/policy-links";

const URGENCY_LABEL: Record<string, string> = {
  高: "緊急度: 高 — 早めの対応を推奨",
  中: "緊急度: 中 — 通常対応でよいが早めに返信",
  低: "緊急度: 低 — 通常の対応で問題なし",
};

export function WorkbenchDemo() {
  const [selectedId, setSelectedId] = useState(INQUIRIES[0].id);
  const groupName = useId();
  const selected = INQUIRIES.find((inquiry) => inquiry.id === selectedId) ?? INQUIRIES[0];
  const selectedRules = getPolicyRulesByIds(selected.policyRuleIds);
  const selectedRuleIdSet = new Set<PolicyRuleId>(selected.policyRuleIds);

  return (
    <div className="workbench">
      <p className="demo-disclaimer" role="note">
        これは<strong>固定サンプルによる検証用ワークベンチ</strong>です。外部AI・外部通信・データ保存は行いません。
        表示される返信案は必ず<strong>人間が確認したうえで、ご自身で送信してください(自動送信はしません)</strong>。
      </p>

      <fieldset className="sample-picker queue-picker">
        <legend>問い合わせキュー(返信優先順・{INQUIRIES.length}件)</legend>
        <div className="sample-list queue-list" role="radiogroup" aria-label="問い合わせキュー">
          {INQUIRIES.map((inquiry, index) => {
            const inputId = `${groupName}-${inquiry.id}`;
            return (
              <label
                key={inquiry.id}
                htmlFor={inputId}
                className={`sample-card queue-item${inquiry.id === selectedId ? " selected" : ""}`}
              >
                <input
                  type="radio"
                  id={inputId}
                  name={groupName}
                  value={inquiry.id}
                  checked={inquiry.id === selectedId}
                  onChange={() => setSelectedId(inquiry.id)}
                />
                <span className="queue-rank" aria-hidden="true">
                  {index + 1}
                </span>
                <span className="sample-language">{inquiry.languageLabel}</span>
                <span className="sample-title">{inquiry.title}</span>
                <span className={`urgency-badge urgency-${inquiry.urgency}`}>{inquiry.urgency}</span>
              </label>
            );
          })}
        </div>
      </fieldset>

      <section className="result-panel" aria-live="polite">
        <div className="result-block guest-message">
          <h3>受信メッセージ({selected.languageLabel})</h3>
          <p lang={selected.languageCode}>{selected.guestMessage}</p>
        </div>

        <div className="result-grid">
          <div className="result-block">
            <h3>日本語要約</h3>
            <p>{selected.summary}</p>
          </div>

          <div className="result-block">
            <h3>優先度・緊急度</h3>
            <p>
              優先度 {INQUIRIES.findIndex((inquiry) => inquiry.id === selected.id) + 1}/{INQUIRIES.length}
            </p>
            <p className={`urgency-badge urgency-${selected.urgency}`}>{URGENCY_LABEL[selected.urgency]}</p>
          </div>

          <div className="result-block">
            <h3>返信案(たたき台・{selected.languageLabel})</h3>
            <p lang={selected.languageCode}>{selected.replyDraft}</p>
            <p className="workbench-human-note">
              この返信案は必ず人が確認してから送信してください。自動送信はしません。
            </p>
          </div>
        </div>

        <div className="result-block">
          <h3>根拠として参照した施設ルール</h3>
          <div className="rule-chip-list">
            {selectedRules.map((rule) => (
              <span className="rule-chip" key={rule.id}>
                {rule.title}
              </span>
            ))}
          </div>
        </div>
      </section>

      <section aria-labelledby="policy-rules-heading">
        <h3 id="policy-rules-heading">施設ルール一覧</h3>
        <div className="card-grid">
          {POLICY_RULES.map((rule) => {
            const isActive = selectedRuleIdSet.has(rule.id);
            return (
              <div className={`card policy-card${isActive ? " active" : ""}`} key={rule.id}>
                {isActive && <span className="policy-card-badge">参照中</span>}
                <h3>{rule.title}</h3>
                <p className="muted">{rule.category}</p>
                <p className="policy-card-detail">{rule.summary}</p>
              </div>
            );
          })}
        </div>
      </section>
    </div>
  );
}
