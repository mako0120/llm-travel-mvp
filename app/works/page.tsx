import type { Metadata } from "next";
import Link from "next/link";

import { catalog } from "@/lib/ai-company-os/catalog";
import { WorksGallery } from "./works-gallery";

export const metadata: Metadata = {
  title: "制作物一覧 — AI Company OS",
  description:
    "AI Company OS が制作した PowerPoint・ナレーション・AI対話音声の一覧。テーマごとの枚数・尺・品質評価を確認できます。",
};

/**
 * 成果物ファイル(.pptx / .wav)が置かれているブランチ。
 * PR #89 がマージされたら "main" に変更する。
 */
const SOURCE_BRANCH = "claude/feature-65-ai-company-os";

export default function WorksPage() {
  const { totals } = catalog;

  return (
    <main className="works-main">
      <header className="works-header">
        <p className="section-label">AI Company OS</p>
        <h1>制作物一覧</h1>
        <p className="works-lead">
          調査からPowerPoint・ナレーション原稿・AI対話音声までを自動生成した成果物の記録です。
          各テーマの元ファイルは GitHub 上に置いてあります。
        </p>
      </header>

      <section className="works-stats" aria-label="制作実績のサマリー">
        <div>
          <strong>{totals.themes}</strong>
          <span>テーマ</span>
        </div>
        <div>
          <strong>{totals.slides.toLocaleString("ja-JP")}</strong>
          <span>スライド</span>
        </div>
        <div>
          <strong>{totals.withPptx}</strong>
          <span>PowerPoint</span>
        </div>
        <div>
          <strong>{totals.withAudio}</strong>
          <span>音声つき</span>
        </div>
        {totals.averageQualityScore !== null && (
          <div>
            <strong>{totals.averageQualityScore}</strong>
            <span>平均品質スコア</span>
          </div>
        )}
      </section>

      <WorksGallery themes={catalog.themes} branch={SOURCE_BRANCH} />

      <footer className="works-footer">
        <p>
          このページは <code>ai-company-os/scripts/build_catalog.py</code> が生成した
          カタログを表示しています。新しいテーマを制作したら同スクリプトを実行して更新します。
        </p>
        <p>
          <Link href="/">トップへ戻る</Link>
        </p>
      </footer>
    </main>
  );
}
