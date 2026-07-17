"use client";

import { useId, useState } from "react";

type Urgency = "高" | "中" | "低";

type Sample = {
  id: string;
  languageLabel: string;
  languageCode: string;
  title: string;
  guestMessage: string;
  summary: string;
  urgency: Urgency;
  policyCheck: string;
  replyDraft: string;
};

const SAMPLES: Sample[] = [
  {
    id: "en-late-checkin",
    languageLabel: "英語",
    languageCode: "en",
    title: "到着遅延・レイトチェックアウトの相談",
    guestMessage:
      "Hi, our flight is delayed and we will arrive around 11pm. Is that okay? Also, could we get a late checkout tomorrow?",
    summary:
      "フライト遅延のため到着が23時頃になる旨の連絡と、翌日のレイトチェックアウトが可能か尋ねています。",
    urgency: "中",
    policyCheck:
      "到着時間の変更自体は通常の対応範囲内です。レイトチェックアウトは施設の追加料金・可否ルールを確認してください。",
    replyDraft:
      "Thank you for letting us know. Arriving around 11pm is no problem — our front desk will be ready for you. Regarding late checkout, we will check availability and get back to you shortly.",
  },
  {
    id: "zh-cancel",
    languageLabel: "中国語(簡体字)",
    languageCode: "zh",
    title: "予約キャンセル・返金の問い合わせ",
    guestMessage:
      "您好，我们的行程有变，可能需要取消预订。请问取消政策是怎样的？会退款吗？",
    summary:
      "予定変更により予約のキャンセルを検討しており、キャンセルポリシーと返金の可否を尋ねています。",
    urgency: "高",
    policyCheck:
      "キャンセルポリシーの案内が必要です。返金可否・金額は予約プランと時期によって異なるため、必ず施設の規約と照合してください。",
    replyDraft:
      "您好，感谢您的联系。请问您预订时选择的是哪种价格方案？我们会根据规定为您确认可退款金额，并尽快回复您。",
  },
  {
    id: "ko-amenity",
    languageLabel: "韓国語",
    languageCode: "ko",
    title: "備品リクエスト・朝食時間の確認",
    guestMessage:
      "안녕하세요! 방에 어린이용 침대(아기침대)를 추가할 수 있을까요? 그리고 조식 시간이 궁금합니다.",
    summary: "部屋へのベビーベッド追加が可能か、また朝食の提供時間についての問い合わせです。",
    urgency: "低",
    policyCheck:
      "備品の貸出可否・在庫、朝食の提供時間帯は施設ごとに異なるため、最新の状況を確認してから回答してください。",
    replyDraft:
      "안녕하세요, 문의 감사합니다. 아기침대는 재고를 확인한 후 다시 안내드리겠습니다. 조식은 오전 7시부터 10시까지 제공됩니다.",
  },
  {
    id: "en-noise-complaint",
    languageLabel: "英語",
    languageCode: "en",
    title: "騒音に関する苦情対応",
    guestMessage:
      "The room next door is very noisy and we couldn't sleep well last night. Can something be done about this?",
    summary: "隣室の騒音により十分に眠れなかったという苦情で、対応を求めています。",
    urgency: "高",
    policyCheck:
      "苦情対応が必要な事案です。速やかな謝意の表明と状況確認、必要に応じた部屋変更や返金対応の検討を行ってください。",
    replyDraft:
      "We are very sorry for the inconvenience caused by the noise last night. We will speak with the other guests right away, and please let us know if you would like us to check whether another room is available.",
  },
];

const URGENCY_LABEL: Record<Urgency, string> = {
  高: "緊急度: 高 — 早めの対応を推奨",
  中: "緊急度: 中 — 通常対応でよいが早めに返信",
  低: "緊急度: 低 — 通常の対応で問題なし",
};

export function ReplyDemo() {
  const [selectedId, setSelectedId] = useState(SAMPLES[0].id);
  const groupName = useId();
  const selected = SAMPLES.find((sample) => sample.id === selectedId) ?? SAMPLES[0];

  return (
    <div className="reply-demo">
      <p className="demo-disclaimer" role="note">
        これは<strong>固定サンプルによる検証用デモ</strong>です。外部AI・外部通信・データ保存は行いません。
        表示される返信案は必ず<strong>人間が確認したうえで、ご自身で送信してください(自動送信はしません)</strong>。
      </p>

      <fieldset className="sample-picker">
        <legend>サンプルを選ぶ(4種類)</legend>
        <div className="sample-list" role="radiogroup" aria-label="固定サンプル一覧">
          {SAMPLES.map((sample) => {
            const inputId = `${groupName}-${sample.id}`;
            return (
              <label
                key={sample.id}
                htmlFor={inputId}
                className={`sample-card${sample.id === selectedId ? " selected" : ""}`}
              >
                <input
                  type="radio"
                  id={inputId}
                  name={groupName}
                  value={sample.id}
                  checked={sample.id === selectedId}
                  onChange={() => setSelectedId(sample.id)}
                />
                <span className="sample-language">{sample.languageLabel}</span>
                <span className="sample-title">{sample.title}</span>
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
            <h3>緊急度</h3>
            <p className={`urgency-badge urgency-${selected.urgency}`}>
              {URGENCY_LABEL[selected.urgency]}
            </p>
          </div>

          <div className="result-block">
            <h3>規約確認</h3>
            <p>{selected.policyCheck}</p>
          </div>

          <div className="result-block">
            <h3>外国語返信案({selected.languageLabel})</h3>
            <p lang={selected.languageCode}>{selected.replyDraft}</p>
          </div>
        </div>
      </section>
    </div>
  );
}
