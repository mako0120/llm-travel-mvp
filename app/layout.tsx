import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "多言語返信AI(検証用デモ) — 宿泊施設向け",
  description:
    "外国語のゲストメッセージを日本語要約・緊急度・規約確認・返信案に変換する、宿泊施設向け多言語返信AIの構想LPと固定サンプルによる検証用デモです。",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="ja">
      <body>
        <div className="demo-banner" role="note">
          このサイトは検証用デモです。固定サンプルのみを扱い、外部AI・外部送信・データ保存は行いません。
        </div>
        {children}
      </body>
    </html>
  );
}
