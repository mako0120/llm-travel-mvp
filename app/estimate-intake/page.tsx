import type { Metadata } from "next";
import Link from "next/link";
import { EstimateIntake } from "./estimate-intake";

export const metadata: Metadata = {
  title: "見積準備度診断 — リフォーム問い合わせ整理",
  description:
    "問い合わせ情報の不足、返信優先度、最初に確認する質問をその場で整理する、リフォーム会社向けの保存なしデモです。",
};

export default function EstimateIntakePage() {
  return (
    <main className="wide-main">
      <p className="breadcrumb"><Link href="/">← サービス紹介に戻る</Link></p>
      <p className="eyebrow">地域密着のリフォーム・修繕会社向け</p>
      <h1>見積もり前の確認を、3分で整理。</h1>
      <p className="lead">
        問い合わせ内容を選ぶだけで、見積準備度・不足情報・最初に聞く質問・対応優先度をまとめます。
        電話やLINEのメモを、現場へ渡せる状態に整えるための検証用デモです。
      </p>
      <EstimateIntake />
    </main>
  );
}
