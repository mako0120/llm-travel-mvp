import type { Metadata } from "next";
import Link from "next/link";
import { ReplyScoreBoard } from "./reply-score-board";

export const metadata: Metadata = {
  title: "問い合わせ返信優先度ボード(検証用) — 多言語返信AI",
  description:
    "固定サンプルの問い合わせを、返信優先度スコアで今すぐ返信・人間確認・追客候補の3レーンに分類する、保存なしの固定ローカルデモです。",
};

export default function ReplyScorePage() {
  return (
    <main>
      <p className="breadcrumb"><Link href="/">← LPに戻る</Link></p>
      <p className="eyebrow">5分で確認・固定ローカルデモ</p>
      <h1>問い合わせ返信優先度ボード</h1>
      <p className="lead">
        固定サンプルの問い合わせを、経過時間・チェックインまでの日数・想定予約金額・言語難易度・規約確認の要否・予約意欲から算出した
        返信優先度スコアで、今すぐ返信・人間確認・追客候補の3レーンに分類します。
      </p>
      <p>
        施設ルールの整備状況を先に確認したい場合は、<Link href="/policy-audit">施設FAQ準備度診断</Link>をお試しください。
      </p>
      <ReplyScoreBoard />
    </main>
  );
}
