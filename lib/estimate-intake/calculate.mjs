export const REQUIRED_FIELDS = [
  { id: "workType", label: "工事内容", question: "どのような工事をご希望ですか？" },
  { id: "buildingType", label: "建物種別", question: "戸建て・マンション・店舗のどれですか？" },
  { id: "desiredTiming", label: "希望時期", question: "工事を希望する時期を教えてください。" },
  { id: "budget", label: "予算", question: "おおよそのご予算は決まっていますか？" },
  { id: "location", label: "現場住所", question: "市区町村までの現場住所を教えてください。" },
  { id: "contactMethod", label: "連絡方法", question: "電話・メール・LINEのうち、ご希望の連絡方法はどれですか？" },
];

export const ESTIMATE_PRESETS = [
  {
    id: "urgent-leak",
    label: "雨漏り・緊急",
    description: "雨漏りが発生し、早急な折り返しが必要",
    values: {
      workType: "雨漏り修繕",
      buildingType: "戸建て",
      desiredTiming: "できるだけ早く",
      budget: "",
      location: "大阪府吹田市",
      hasPhotos: true,
      contactMethod: "電話",
      urgency: "high",
    },
  },
  {
    id: "bathroom",
    label: "浴室リフォーム",
    description: "比較検討中で、現地調査につなげたい",
    values: {
      workType: "浴室の全面リフォーム",
      buildingType: "マンション",
      desiredTiming: "3か月以内",
      budget: "100万円前後",
      location: "大阪市北区",
      hasPhotos: true,
      contactMethod: "メール",
      urgency: "medium",
    },
  },
  {
    id: "vague",
    label: "情報が少ない相談",
    description: "「リフォームしたい」だけの問い合わせ",
    values: {
      workType: "内装をきれいにしたい",
      buildingType: "",
      desiredTiming: "",
      budget: "",
      location: "",
      hasPhotos: false,
      contactMethod: "",
      urgency: "low",
    },
  },
];

const URGENCY = {
  high: { label: "最優先", reason: "緊急性が高いため、30分以内の一次連絡を推奨します。", rank: 3 },
  medium: { label: "優先", reason: "具体的な検討が進んでいるため、本日中の返信を推奨します。", rank: 2 },
  low: { label: "通常", reason: "不足情報を確認し、1営業日以内の返信を推奨します。", rank: 1 },
};

function normalize(value) {
  return typeof value === "string" ? value.trim() : "";
}

export function calculateEstimateReadiness(input = {}) {
  const values = Object.fromEntries(
    REQUIRED_FIELDS.map(({ id }) => [id, normalize(input[id])]),
  );
  const missing = REQUIRED_FIELDS.filter(({ id }) => !values[id]);
  const hasPhotos = input.hasPhotos === true;
  const completedPoints = REQUIRED_FIELDS.length - missing.length;
  const score = Math.round(
    ((completedPoints + (hasPhotos ? 1 : 0)) / (REQUIRED_FIELDS.length + 1)) * 100,
  );
  const urgencyKey = Object.hasOwn(URGENCY, input.urgency) ? input.urgency : "low";
  const priority = URGENCY[urgencyKey];
  const questions = missing.map(({ question }) => question);

  if (!hasPhotos) {
    questions.push("可能であれば、現状が分かる写真を2〜3枚お送りいただけますか？");
  }

  const nextAction =
    priority.rank === 3
      ? "安全状況を電話で確認し、訪問可否を判断する"
      : score >= 70
        ? "内容を確認して現地調査の候補日を案内する"
        : "不足情報をまとめて確認し、見積可能な状態にする";

  return {
    score,
    missing,
    questions,
    priority,
    nextAction,
    isReady: score >= 70,
  };
}
