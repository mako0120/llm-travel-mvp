export const POLICY_CATEGORIES = [
  { id: "cancellation", label: "キャンセル", guidance: "取消期限、返金条件、無断不泊時の扱い" },
  { id: "checkin", label: "チェックイン・アウト", guidance: "受付時間、遅着、延長料金、鍵の返却方法" },
  { id: "children", label: "子ども・備品", guidance: "子ども料金、添い寝、ベッド・アメニティの条件" },
  { id: "meals", label: "食事", guidance: "提供時間、アレルギー、変更・持ち込みの可否" },
  { id: "payment", label: "支払い", guidance: "利用可能な決済、現地精算、追加料金、領収書" },
  { id: "noise", label: "騒音・苦情", guidance: "静粛時間、禁止事項、苦情時の連絡先と対応手順" },
];

export const STATUS = ["clear", "unclear", "missing"];

export function sanitizeStatus(value) {
  return STATUS.includes(value) ? value : "missing";
}

export const POLICY_PRESETS = [
  {
    id: "starting",
    label: "準備を始めた施設",
    values: {
      cancellation: "missing", checkin: "clear", children: "missing",
      meals: "unclear", payment: "clear", noise: "missing",
    },
  },
  {
    id: "growing",
    label: "運用中の小規模ホテル",
    values: {
      cancellation: "clear", checkin: "clear", children: "unclear",
      meals: "clear", payment: "clear", noise: "unclear",
    },
  },
  {
    id: "ready",
    label: "整備済みの旅館",
    values: Object.fromEntries(POLICY_CATEGORIES.map(({ id }) => [id, "clear"])),
  },
];

export function calculatePolicyAudit(input = {}) {
  const statuses = Object.fromEntries(
    POLICY_CATEGORIES.map(({ id }) => [
      id,
      sanitizeStatus(input[id]),
    ]),
  );
  const answerable = POLICY_CATEGORIES.filter(({ id }) => statuses[id] === "clear");
  const humanReview = POLICY_CATEGORIES.filter(({ id }) => statuses[id] === "unclear");
  const missing = POLICY_CATEGORIES.filter(({ id }) => statuses[id] === "missing");
  const points = answerable.length * 2 + humanReview.length;
  const score = Math.round((points / (POLICY_CATEGORIES.length * 2)) * 100);
  const checklist = [...missing, ...humanReview].map((category) => ({
    id: category.id,
    label: category.label,
    guidance: category.guidance,
    priority: statuses[category.id] === "missing" ? "最優先" : "要明確化",
  }));

  return { score, statuses, answerable, humanReview, missing, checklist };
}
