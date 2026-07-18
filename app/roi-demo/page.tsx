import type { Metadata } from "next";
import Link from "next/link";
import { RoiCalculator } from "./roi-calculator";

export const metadata: Metadata = {
  title: "ROI計算デモ — 営業担当向けAI導入効果シミュレーター(検証用)",
  description:
    "業種・作業件数・時給・削減率・月額導入費を入力すると、月間削減時間・削減額・年間効果・投資回収月数をブラウザ内で即時計算します。外部AI・通信・データ保存なし。",
};

export default function RoiDemoPage() {
  return (
    <main>
      <p className="breadcrumb">
        <Link href="/">← LPに戻る</Link>
      </p>
      <h1>ROI計算デモ — AI導入効果シミュレーター</h1>
      <p className="lead">
        業種・作業件数・時給・削減率・月額費を入力すると、月間削減時間・削減額・年間効果・投資回収月数をブラウザ内で即時計算します。
      </p>
      <RoiCalculator />
    </main>
  );
}
