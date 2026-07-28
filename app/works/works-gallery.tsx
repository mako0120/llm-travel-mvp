"use client";

import { useMemo, useState } from "react";

import {
  ARTIFACT_LABELS,
  BADGE_ORDER,
  formatDuration,
  themeSourceUrl,
  type ArtifactKey,
  type Theme,
} from "@/lib/ai-company-os/catalog";

type Filter = "all" | "video" | "pptx" | "audio" | "youtube";

const FILTERS: { key: Filter; label: string }[] = [
  { key: "all", label: "すべて" },
  { key: "video", label: "動画あり" },
  { key: "pptx", label: "PowerPointあり" },
  { key: "audio", label: "音声あり" },
  { key: "youtube", label: "YouTube素材あり" },
];

export function WorksGallery({ themes, branch }: { themes: Theme[]; branch: string }) {
  const [query, setQuery] = useState("");
  const [filter, setFilter] = useState<Filter>("all");

  const visible = useMemo(() => {
    const needle = query.trim().toLowerCase();
    return themes.filter((theme) => {
      if (filter === "video" && !theme.videoUrl) return false;
      if (filter !== "all" && filter !== "video" && !theme.artifacts[filter as ArtifactKey]) {
        return false;
      }
      if (!needle) return true;
      return (
        theme.title.toLowerCase().includes(needle) ||
        theme.slug.toLowerCase().includes(needle) ||
        theme.date.includes(needle)
      );
    });
  }, [themes, query, filter]);

  return (
    <section className="works-gallery" aria-label="制作物の一覧">
      <div className="works-controls">
        <label className="works-search">
          <span className="visually-hidden">テーマを検索</span>
          <input
            type="search"
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="テーマ名・日付で検索(例: NVIDIA、2026-07-28)"
          />
        </label>
        <div className="works-filters" role="group" aria-label="成果物で絞り込む">
          {FILTERS.map((item) => (
            <button
              key={item.key}
              type="button"
              className={filter === item.key ? "is-active" : undefined}
              aria-pressed={filter === item.key}
              onClick={() => setFilter(item.key)}
            >
              {item.label}
            </button>
          ))}
        </div>
      </div>

      <p className="works-count" role="status">
        {visible.length === themes.length
          ? `${themes.length}件を表示中`
          : `${themes.length}件中 ${visible.length}件を表示中`}
      </p>

      {visible.length === 0 ? (
        <p className="works-empty">条件に一致するテーマがありませんでした。</p>
      ) : (
        <ul className="works-list">
          {visible.map((theme) => (
            <li key={theme.id}>
              <article className="works-card">
                <div className="works-card-head">
                  <time dateTime={theme.date}>{theme.date}</time>
                  {theme.qualityScore !== null && (
                    <span className="works-score" title="著作権・品質自己評価">
                      品質 {theme.qualityScore}
                    </span>
                  )}
                </div>

                <h2>
                  <a href={themeSourceUrl(theme, branch)} target="_blank" rel="noreferrer">
                    {theme.title}
                  </a>
                </h2>

                {theme.videoUrl && (
                  <video
                    className="works-video"
                    src={theme.videoUrl}
                    controls
                    preload="none"
                    playsInline
                  >
                    お使いのブラウザは動画再生に対応していません。
                  </video>
                )}

                <dl className="works-meta">
                  <div>
                    <dt>スライド</dt>
                    <dd>{theme.slides}枚</dd>
                  </div>
                  {theme.audioSeconds !== null && (
                    <div>
                      <dt>音声</dt>
                      <dd>{formatDuration(theme.audioSeconds)}</dd>
                    </div>
                  )}
                  {theme.narrationMinutes !== null && (
                    <div>
                      <dt>原稿</dt>
                      <dd>約{theme.narrationMinutes}分</dd>
                    </div>
                  )}
                  {theme.themeScore !== null && (
                    <div>
                      <dt>テーマ評価</dt>
                      <dd>{theme.themeScore}点</dd>
                    </div>
                  )}
                </dl>

                <ul className="works-badges">
                  {BADGE_ORDER.filter((key) => theme.artifacts[key]).map((key) => (
                    <li key={key}>{ARTIFACT_LABELS[key] ?? key}</li>
                  ))}
                </ul>
              </article>
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}
