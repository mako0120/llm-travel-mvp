import type { Metadata } from "next";
import Link from "next/link";
import { RoiCalculator } from "./roi-calculator";

export const metadata: Metadata = {
  title: "営業ROI計算デモ(検証用) — 導入効果シミュレーション",
  description:
    "顧客の現状数値を入力すると、月間削減時間・削減額・年間効果・投資回収期間をその場で試算できる、営業説明用のクリックデモです。",
};

export default function RoiDemoPage() {
  return (
    <main>
      <p className="breadcrumb">
        <Link href="/">← LPに戻る</Link>
      </p>
      <h1>営業ROI計算デモ</h1>
      <p className="lead">
        顧客の現状数値を入力すると、導入後の削減時間・削減額・年間効果・投資回収期間をその場で試算できます。
      </p>
      <RoiCalculator />
    </main>
  );
}
