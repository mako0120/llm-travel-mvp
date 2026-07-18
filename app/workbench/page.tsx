import type { Metadata } from "next";
import Link from "next/link";
import { WorkbenchDemo } from "./workbench-demo";

export const metadata: Metadata = {
  title: "施設ルール根拠付きワークベンチ(検証用) — 多言語返信AI",
  description:
    "固定サンプルの問い合わせキューから、返信優先順・施設ルール根拠・返信案のたたき台を1画面で確認できる、より実運用に近い検証用デモです。",
};

export default function WorkbenchPage() {
  return (
    <main>
      <p className="breadcrumb">
        <Link href="/">← LPに戻る</Link>
      </p>
      <h1>施設ルール根拠付きワークベンチ</h1>
      <p className="lead">
        固定サンプルの問い合わせキューから、どれを先に返すべきか・どの施設ルールが根拠か・どの返信文をたたき台にすべきかを1画面で確認できます。
      </p>
      <WorkbenchDemo />
    </main>
  );
}
