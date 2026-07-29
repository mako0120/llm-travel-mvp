export const ELAPSED_LEVELS = ["under1h", "1to6h", "6to24h", "over24h"];
export const CHECKIN_LEVELS = ["0to1day", "2to7days", "8to30days", "over30days"];
export const VALUE_BANDS = ["low", "mid", "high"];
export const LANGUAGE_DIFFICULTIES = ["easy", "medium", "hard"];
export const INTENT_LEVELS = ["weak", "medium", "strong"];

const ELAPSED_POINTS = { under1h: 0, "1to6h": 1, "6to24h": 2, over24h: 3 };
const CHECKIN_POINTS = { "0to1day": 3, "2to7days": 2, "8to30days": 1, over30days: 0 };
const VALUE_POINTS = { low: 0, mid: 1, high: 2 };
const INTENT_POINTS = { weak: 0, medium: 1, strong: 2 };

const MAX_POINTS =
  Math.max(...Object.values(ELAPSED_POINTS)) +
  Math.max(...Object.values(CHECKIN_POINTS)) +
  Math.max(...Object.values(VALUE_POINTS)) +
  Math.max(...Object.values(INTENT_POINTS));

const REPLY_NOW_THRESHOLD = 50;
const SOON_CHECKIN_LEVELS = ["0to1day", "2to7days"];
const STRONG_INTENT_LEVELS = ["medium", "strong"];

export const REPLY_INQUIRIES = [
  {
    id: "arrival-time",
    label: "到着時間・レイトチェックインの確認",
    guestMessage: "本日の到着が少し遅れそうです。何時までにチェックインすればよいですか。",
  },
  {
    id: "cancellation",
    label: "予約キャンセル・返金の相談",
    guestMessage: "予定が変わり、キャンセルを検討しています。返金はどのくらい戻りますか。",
  },
  {
    id: "amenity-request",
    label: "備品・アレルギー対応の相談",
    guestMessage: "子ども用ベッドをお願いしたいのと、食物アレルギーの対応可否を知りたいです。",
  },
  {
    id: "group-quote",
    label: "団体・法人利用の見積もり相談",
    guestMessage: "10名程度の団体で利用したいのですが、空室状況と料金の目安を教えてください。",
  },
  {
    id: "noise-complaint",
    label: "騒音に関する苦情",
    guestMessage: "隣室の音が気になり眠れませんでした。対応をお願いできますか。",
  },
  {
    id: "future-availability",
    label: "来月以降の空室に関する軽い問い合わせ",
    guestMessage: "来月以降でまだ検討中ですが、空室状況だけ大まかに知りたいです。",
  },
];

export function sanitizeLevel(value, levels, fallback) {
  return levels.includes(value) ? value : fallback;
}

function sanitizeInputs(raw = {}) {
  return {
    elapsed: sanitizeLevel(raw.elapsed, ELAPSED_LEVELS, "under1h"),
    checkin: sanitizeLevel(raw.checkin, CHECKIN_LEVELS, "over30days"),
    value: sanitizeLevel(raw.value, VALUE_BANDS, "low"),
    language: sanitizeLevel(raw.language, LANGUAGE_DIFFICULTIES, "easy"),
    intent: sanitizeLevel(raw.intent, INTENT_LEVELS, "weak"),
    termsCheckNeeded: raw.termsCheckNeeded === true,
  };
}

export const REPLY_PRESETS = [
  {
    id: "ryokan-weekend",
    label: "週末前で埋まりかけの旅館",
    values: {
      "arrival-time": { elapsed: "6to24h", checkin: "0to1day", value: "high", intent: "strong", language: "easy", termsCheckNeeded: false },
      cancellation: { elapsed: "1to6h", checkin: "2to7days", value: "high", intent: "weak", language: "easy", termsCheckNeeded: true },
      "amenity-request": { elapsed: "under1h", checkin: "0to1day", value: "mid", intent: "medium", language: "medium", termsCheckNeeded: false },
      "group-quote": { elapsed: "6to24h", checkin: "8to30days", value: "high", intent: "strong", language: "hard", termsCheckNeeded: false },
      "noise-complaint": { elapsed: "under1h", checkin: "0to1day", value: "mid", intent: "weak", language: "easy", termsCheckNeeded: true },
      "future-availability": { elapsed: "over24h", checkin: "over30days", value: "low", intent: "weak", language: "easy", termsCheckNeeded: false },
    },
  },
  {
    id: "minpaku-weekday",
    label: "平日集客に悩む民泊",
    values: {
      "arrival-time": { elapsed: "1to6h", checkin: "8to30days", value: "mid", intent: "medium", language: "easy", termsCheckNeeded: false },
      cancellation: { elapsed: "under1h", checkin: "over30days", value: "low", intent: "weak", language: "easy", termsCheckNeeded: true },
      "amenity-request": { elapsed: "6to24h", checkin: "2to7days", value: "mid", intent: "medium", language: "medium", termsCheckNeeded: false },
      "group-quote": { elapsed: "over24h", checkin: "8to30days", value: "high", intent: "strong", language: "easy", termsCheckNeeded: false },
      "noise-complaint": { elapsed: "1to6h", checkin: "over30days", value: "low", intent: "weak", language: "easy", termsCheckNeeded: false },
      "future-availability": { elapsed: "over24h", checkin: "over30days", value: "low", intent: "weak", language: "easy", termsCheckNeeded: false },
    },
  },
  {
    id: "guesthouse-inbound",
    label: "インバウンド比率が高いゲストハウス",
    values: {
      "arrival-time": { elapsed: "6to24h", checkin: "0to1day", value: "mid", intent: "strong", language: "hard", termsCheckNeeded: false },
      cancellation: { elapsed: "1to6h", checkin: "2to7days", value: "mid", intent: "weak", language: "medium", termsCheckNeeded: true },
      "amenity-request": { elapsed: "under1h", checkin: "2to7days", value: "low", intent: "medium", language: "hard", termsCheckNeeded: false },
      "group-quote": { elapsed: "over24h", checkin: "8to30days", value: "high", intent: "strong", language: "easy", termsCheckNeeded: false },
      "noise-complaint": { elapsed: "under1h", checkin: "0to1day", value: "low", intent: "weak", language: "medium", termsCheckNeeded: false },
      "future-availability": { elapsed: "6to24h", checkin: "over30days", value: "low", intent: "medium", language: "easy", termsCheckNeeded: false },
    },
  },
];

export function calculateReplyScore(inputsByInquiryId = {}) {
  const items = REPLY_INQUIRIES.map((inquiry) => {
    const inputs = sanitizeInputs((inputsByInquiryId ?? {})[inquiry.id]);
    const points =
      ELAPSED_POINTS[inputs.elapsed] +
      CHECKIN_POINTS[inputs.checkin] +
      VALUE_POINTS[inputs.value] +
      INTENT_POINTS[inputs.intent];
    const score = Math.round((points / MAX_POINTS) * 100);

    const needsHumanReview = inputs.termsCheckNeeded || inputs.language === "hard";
    const lane = needsHumanReview
      ? "human_review"
      : score >= REPLY_NOW_THRESHOLD
        ? "reply_now"
        : "follow_up";

    return {
      id: inquiry.id,
      label: inquiry.label,
      guestMessage: inquiry.guestMessage,
      score,
      lane,
      inputs,
    };
  });

  const replyNow = items.filter((item) => item.lane === "reply_now");
  const humanReview = items.filter((item) => item.lane === "human_review");
  const followUp = items.filter((item) => item.lane === "follow_up");

  const preventedCount = items.filter(
    (item) =>
      SOON_CHECKIN_LEVELS.includes(item.inputs.checkin) &&
      STRONG_INTENT_LEVELS.includes(item.inputs.intent) &&
      item.lane !== "follow_up",
  ).length;

  return {
    items,
    replyNow,
    humanReview,
    followUp,
    summary: {
      urgentCount: replyNow.length,
      humanReviewCount: humanReview.length,
      followUpCount: followUp.length,
      preventedCount,
    },
  };
}
