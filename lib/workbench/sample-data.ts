import type { PolicyRuleId } from "./policy-links";

export type Urgency = "高" | "中" | "低";

export type Inquiry = {
  id: string;
  languageLabel: string;
  languageCode: string;
  title: string;
  guestMessage: string;
  summary: string;
  urgency: Urgency;
  policyRuleIds: PolicyRuleId[];
  replyDraft: string;
};

// 配列の並び順がそのまま返信優先順(先頭が最優先)。緊急度: 高2件・中2件・低2件。
export const INQUIRIES: Inquiry[] = [
  {
    id: "zh-cancel-urgent",
    languageLabel: "中国語(簡体字)",
    languageCode: "zh",
    title: "直前キャンセルと返金額の緊急相談",
    guestMessage:
      "您好，我们明天的行程突然取消了，今晚的预订可能需要取消。请问现在取消的话，押金能退多少？",
    summary:
      "明日の予定が急遽なくなり、今夜の宿泊を直前キャンセルしたいとの連絡です。デポジットの返金額を至急確認したいとのことです。",
    urgency: "高",
    policyRuleIds: ["cancellation", "deposit-refund"],
    replyDraft:
      "您好，非常理解您的情况。由于是当天取消，可能会产生一定的取消费用，我们会根据规定为您确认押金的可退金额，并尽快回复您。",
  },
  {
    id: "en-noise-complaint",
    languageLabel: "英語",
    languageCode: "en",
    title: "騒音苦情・部屋変更または返金の検討",
    guestMessage:
      "The guests next door have been extremely loud since last night and we couldn't sleep at all. We'd like a room change or at least a partial refund.",
    summary:
      "隣室の騒音により一晩中眠れなかったとの苦情で、部屋変更または一部返金を求めています。",
    urgency: "高",
    policyRuleIds: ["noise-response", "deposit-refund"],
    replyDraft:
      "We are very sorry for the trouble caused by the noise. We will speak with the other guests immediately and check whether another room is available. Regarding a refund, we will confirm what we can offer and follow up with you shortly.",
  },
  {
    id: "en-late-arrival",
    languageLabel: "英語",
    languageCode: "en",
    title: "到着遅延の連絡とレイトチェックアウト相談",
    guestMessage:
      "Our connecting flight was delayed and we'll arrive very late tonight. If we end up missing check-in, will we be charged a no-show fee? Also, could we get a late checkout tomorrow?",
    summary:
      "乗り継ぎ便の遅延で到着が大幅に遅れる可能性があり、無断不泊扱いになった場合の請求と、翌日のレイトチェックアウトの可否を確認しています。",
    urgency: "中",
    policyRuleIds: ["late-checkout", "cancellation"],
    replyDraft:
      "Thank you for letting us know in advance. As long as we hear from you, this will not be treated as a no-show. We will also check tomorrow's room availability and let you know about a late checkout.",
  },
  {
    id: "ko-amenity-breakfast",
    languageLabel: "韓国語",
    languageCode: "ko",
    title: "ベビーベッド貸出と朝食提供時間の確認",
    guestMessage:
      "아기 침대를 빌리고 싶은데 남아있을까요? 그리고 조식은 몇 시부터 몇 시까지 이용할 수 있나요?",
    summary: "ベビーベッドの在庫状況と、朝食の提供時間帯についての問い合わせです。",
    urgency: "中",
    policyRuleIds: ["baby-bed", "breakfast-hours"],
    replyDraft:
      "문의 감사합니다. 아기침대는 재고를 확인한 후 안내드리겠습니다. 조식 제공 시간은 요일에 따라 다를 수 있어 확인 후 다시 연락드리겠습니다.",
  },
  {
    id: "th-deposit-question",
    languageLabel: "タイ語",
    languageCode: "th",
    title: "デポジット返金時期についての一般的な質問",
    guestMessage:
      "สอบถามครับ ถ้าจองแล้วมีเงินมัดจำ จะได้เงินคืนกี่วันหลังเช็คเอาท์ครับ",
    summary: "予約時のデポジットが、チェックアウト後何日程度で返金されるかを事前に知りたいとの一般的な質問です。",
    urgency: "低",
    policyRuleIds: ["deposit-refund", "cancellation"],
    replyDraft:
      "สอบถามข้อมูลนี้ ทางเราจะแจ้งระยะเวลาคืนเงินมัดจำที่ชัดเจนให้ทราบอีกครั้งตามเงื่อนไขการจอง",
  },
  {
    id: "en-breakfast-hours",
    languageLabel: "英語",
    languageCode: "en",
    title: "朝食提供時間とチェックアウト時間の確認",
    guestMessage:
      "Could you tell us the breakfast hours during our stay, and the standard checkout time as well? Just planning our schedule ahead of time.",
    summary: "滞在中の朝食提供時間と、通常のチェックアウト時間を事前に確認したいとの問い合わせです。",
    urgency: "低",
    policyRuleIds: ["breakfast-hours", "late-checkout"],
    replyDraft:
      "Thank you for planning ahead. We will confirm the exact breakfast hours for your stay dates and the standard checkout time, and get back to you shortly.",
  },
];
