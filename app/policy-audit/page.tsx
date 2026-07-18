import type { Metadata } from "next";
import Link from "next/link";
import { PolicyAudit } from "./policy-audit";

export const metadata: Metadata = {
  title: "施設FAQ準備度診断(検証用) — 多言語返信AI",
  description: "施設ルールをAIが回答可能・人間確認・情報不足に分類する、保存なしの固定ローカル診断です。",
};

export default function PolicyAuditPage() {
  return (
    <main>
      <p className="breadcrumb"><Link href="/">← LPに戻る</Link></p>
      <p className="eyebrow">5分で確認・固定ローカル診断</p>
      <h1>施設FAQの回答可能範囲を見える化</h1>
      <p className="lead">
        6つの施設ルールがどこまで整っているかを選ぶと、AIに任せられる範囲と、人が確認すべき範囲をその場で整理します。
      </p>
      <PolicyAudit />
    </main>
  );
}
