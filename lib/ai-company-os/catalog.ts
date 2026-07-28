import catalogJson from "./catalog.json";

/**
 * 制作物カタログの型定義。
 * 実体は ai-company-os/scripts/build_catalog.py が生成する catalog.json。
 * 値を追加・変更したときは、生成スクリプト側と両方を更新すること。
 */

export type ArtifactKey =
  | "deck_spec"
  | "pptx"
  | "narration"
  | "dialogue"
  | "audio"
  | "timings"
  | "youtube"
  | "canva"
  | "review"
  | "research"
  | "thumbnail";

export type Theme = {
  id: string;
  date: string;
  slug: string;
  title: string;
  subtitle: string | null;
  palette: string | null;
  footer: string | null;
  slides: number;
  layouts: Record<string, number>;
  bulletsRatio: number | null;
  narrationMinutes: number | null;
  audioSeconds: number | null;
  qualityScore: number | null;
  themeScore: number | null;
  artifacts: Record<ArtifactKey, boolean>;
};

export type Catalog = {
  generatedBy: string;
  repo: string;
  assetsPath: string;
  totals: {
    themes: number;
    slides: number;
    withPptx: number;
    withAudio: number;
    timedThemes: number;
    timedAudioSeconds: number;
    averageQualityScore: number | null;
  };
  themes: Theme[];
};

export const catalog = catalogJson as Catalog;

/** 成果物の表示名。カードのバッジに使う。 */
export const ARTIFACT_LABELS: Partial<Record<ArtifactKey, string>> = {
  pptx: "PowerPoint",
  audio: "音声",
  dialogue: "対話原稿",
  narration: "ナレーション原稿",
  youtube: "YouTube素材",
  canva: "Canvaブリーフ",
  research: "調査レポート",
};

/** カードに出す成果物バッジの表示順。 */
export const BADGE_ORDER: ArtifactKey[] = [
  "pptx",
  "audio",
  "dialogue",
  "narration",
  "youtube",
  "canva",
  "research",
];

/** 秒を「5分54秒」形式にする。null はそのまま null を返す。 */
export function formatDuration(seconds: number | null): string | null {
  if (seconds === null || Number.isNaN(seconds)) return null;
  const total = Math.round(seconds);
  const m = Math.floor(total / 60);
  const s = total % 60;
  return m > 0 ? `${m}分${s}秒` : `${s}秒`;
}

/** 秒の合計を「2時間13分」形式にする(サマリー用)。 */
export function formatTotalDuration(seconds: number): string {
  const total = Math.round(seconds);
  const h = Math.floor(total / 3600);
  const m = Math.round((total % 3600) / 60);
  return h > 0 ? `${h}時間${m}分` : `${m}分`;
}

/** そのテーマのGitHub上のディレクトリURL。ファイル本体はここから辿る。 */
export function themeSourceUrl(theme: Theme, branch: string): string {
  return `https://github.com/${catalog.repo}/tree/${branch}/${catalog.assetsPath}/${theme.id}`;
}
