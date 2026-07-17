import type { Metadata } from "next";
import Link from "next/link";
import { ReplyDemo } from "./reply-demo";

export const metadata: Metadata = {
  title: "固定サンプルデモ — 多言語返信AI(検証用)",
  description:
    "外国語のゲストメッセージのサンプルを選び、日本語要約・緊急度・規約確認・返信案の見え方を確認できる検証用デモです。",
};

export default function DemoPage() {
  return (
    <main>
      <p className="breadcrumb">
        <Link href="/">← LPに戻る</Link>
      </p>
      <h1>多言語返信AI 固定サンプルデモ</h1>
      <p className="lead">
        外国語のゲストメッセージのサンプルを選ぶと、日本語要約・緊急度・規約確認・外国語の返信案が表示されます。
      </p>
      <ReplyDemo />
    </main>
  );
}
