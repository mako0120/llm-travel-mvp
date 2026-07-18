export const POLICY_RULES = [
  {
    id: "cancellation",
    title: "キャンセルポリシー",
    category: "予約変更",
    summary: "キャンセル時期に応じた返金可否・手数料を確認してから案内する。",
  },
  {
    id: "late-checkout",
    title: "レイトチェックアウト",
    category: "滞在延長",
    summary: "当日の空室状況と追加料金の有無を確認してから可否を回答する。",
  },
  {
    id: "baby-bed",
    title: "ベビーベッド貸出",
    category: "備品",
    summary: "在庫数と対象部屋タイプを確認してから貸出可否を案内する。",
  },
  {
    id: "noise-response",
    title: "騒音・苦情対応",
    category: "苦情対応",
    summary: "速やかな謝意表明と状況確認を行い、必要に応じ部屋変更や返金を検討する。",
  },
  {
    id: "deposit-refund",
    title: "デポジット返金",
    category: "支払い",
    summary: "預かり金の返金条件と処理日数を確認してから金額を案内する。",
  },
  {
    id: "breakfast-hours",
    title: "朝食提供時間",
    category: "館内サービス",
    summary: "曜日・季節による提供時間の変更有無を確認してから案内する。",
  },
] as const;

export type PolicyRuleId = (typeof POLICY_RULES)[number]["id"];
export type PolicyRule = (typeof POLICY_RULES)[number];

export function getPolicyRulesByIds(ids: readonly PolicyRuleId[]): PolicyRule[] {
  return ids.map((id) => POLICY_RULES.find((rule) => rule.id === id)!);
}
