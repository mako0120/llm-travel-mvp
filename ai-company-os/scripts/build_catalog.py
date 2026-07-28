#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_catalog.py — 制作済みテーマ一覧(カタログJSON)を生成する

ai-company-os/assets/<日付>_<slug>/ 配下を走査し、各テーマのメタ情報を
1つのJSONにまとめて lib/ai-company-os/catalog.json へ書き出す。
Webサイト(/works)はこのJSONだけを読むため、実行時にファイルシステムを
走査しない(ビルドの再現性とデプロイの安定性を優先する)。

使い方:
  python scripts/build_catalog.py                 # 既定の出力先へ生成
  python scripts/build_catalog.py <out.json>      # 出力先を指定
  python scripts/build_catalog.py --self-test     # 抽出ロジックのみ確認

抽出する情報(取得できないものは null にし、推測で埋めない):
  - slug / 日付 / タイトル / サブタイトル
  - スライド枚数・レイアウト内訳・bullets比率
  - ナレーション目安分数(ノート文字数から概算)
  - 音声の実尺(slide_timings.json がある場合のみ)
  - 著作権・品質自己評価の点数(risk-and-quality-review.md がある場合のみ)
  - 成果物の有無(pptx / 音声 / 対話原稿 / YouTube素材 / Canvaブリーフ 等)
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

CHARS_PER_MINUTE = 350  # export_script.py と同じ換算

# カタログに載せる成果物とその判定ファイル
ARTIFACT_FILES = {
    "deck_spec": "deck_spec.json",
    "pptx": "deck.pptx",
    "narration": "narration_script.md",
    "dialogue": "dialogue_script.md",
    "audio": "dialogue_audio.wav",
    "timings": "slide_timings.json",
    "youtube": "youtube_assets.md",
    "canva": "canva_brief.md",
    "review": "risk-and-quality-review.md",
    "research": "research.md",
    "thumbnail": "thumbnail.png",
}

DIR_NAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})_(.+)$")
# risk-and-quality-review.md の「| **合計** | **100** | **95** |」から得点を拾う
SCORE_RE = re.compile(r"\|\s*\*\*合計\*\*\s*\|\s*\*\*\d+\*\*\s*\|\s*\*\*(\d+)\*\*")
# README.md の「評価スコア: 82/100」からテーマ評価点を拾う
THEME_SCORE_RE = re.compile(r"評価スコア[:：]\s*(\d+)\s*/\s*100")


def read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def extract_quality_score(theme_dir: Path) -> int | None:
    m = SCORE_RE.search(read_text(theme_dir / "risk-and-quality-review.md"))
    return int(m.group(1)) if m else None


def extract_theme_score(theme_dir: Path) -> int | None:
    m = THEME_SCORE_RE.search(read_text(theme_dir / "README.md"))
    return int(m.group(1)) if m else None


def extract_audio_seconds(theme_dir: Path) -> float | None:
    timings = read_json(theme_dir / "slide_timings.json")
    if not isinstance(timings, list) or not timings:
        return None
    last = timings[-1]
    if isinstance(last, dict) and isinstance(last.get("end_sec"), (int, float)):
        return round(float(last["end_sec"]), 1)
    return None


def summarize_deck(spec: dict) -> dict:
    slides = spec.get("slides", []) or []
    layouts: dict[str, int] = {}
    note_chars = 0
    for sl in slides:
        layout = sl.get("layout", "unknown")
        layouts[layout] = layouts.get(layout, 0) + 1
        note_chars += len(str(sl.get("note", "")))
    total = len(slides)
    bullets_ratio = round(layouts.get("bullets", 0) / total * 100, 1) if total else None
    return {
        "slides": total,
        "layouts": dict(sorted(layouts.items(), key=lambda kv: (-kv[1], kv[0]))),
        "bulletsRatio": bullets_ratio,
        "narrationMinutes": round(note_chars / CHARS_PER_MINUTE, 1) if note_chars else None,
    }


def build_entry(theme_dir: Path) -> dict | None:
    m = DIR_NAME_RE.match(theme_dir.name)
    if not m:
        return None
    date, slug = m.group(1), m.group(2)

    spec = read_json(theme_dir / "deck_spec.json")
    if not isinstance(spec, dict):
        return None

    meta = spec.get("meta", {}) or {}
    deck = summarize_deck(spec)

    artifacts = {
        key: (theme_dir / filename).is_file()
        for key, filename in ARTIFACT_FILES.items()
    }

    return {
        "id": theme_dir.name,
        "date": date,
        "slug": slug,
        "title": meta.get("title") or theme_dir.name,
        "subtitle": meta.get("subtitle"),
        "palette": meta.get("palette_preset"),
        "footer": meta.get("footer"),
        **deck,
        "audioSeconds": extract_audio_seconds(theme_dir),
        "qualityScore": extract_quality_score(theme_dir),
        "themeScore": extract_theme_score(theme_dir),
        "artifacts": artifacts,
    }


def build_catalog(assets_dir: Path) -> dict:
    entries = []
    for theme_dir in sorted(assets_dir.iterdir()):
        if not theme_dir.is_dir():
            continue
        entry = build_entry(theme_dir)
        if entry:
            entries.append(entry)

    # 新しい順に並べる(同日は slug 順で安定させる)
    entries.sort(key=lambda e: (e["date"], e["slug"]), reverse=True)

    # 音声ファイルの有無と、尺を測れるか(slide_timings.json の有無)は別物なので分けて数える
    timed = [e for e in entries if e["audioSeconds"]]
    scores = [e["qualityScore"] for e in entries if e["qualityScore"] is not None]

    return {
        "generatedBy": "ai-company-os/scripts/build_catalog.py",
        "repo": "mako0120/llm-travel-mvp",
        "assetsPath": "ai-company-os/assets",
        "totals": {
            "themes": len(entries),
            "slides": sum(e["slides"] for e in entries),
            "withPptx": sum(1 for e in entries if e["artifacts"]["pptx"]),
            "withAudio": sum(1 for e in entries if e["artifacts"]["audio"]),
            # 尺の合計は、タイミング情報がある分だけの合計であることを名前で示す
            "timedThemes": len(timed),
            "timedAudioSeconds": round(sum(e["audioSeconds"] for e in timed), 1),
            "averageQualityScore": round(sum(scores) / len(scores), 1) if scores else None,
        },
        "themes": entries,
    }


def self_test() -> int:
    """最小のテーマ構成を作り、抽出ロジックが期待どおり動くかを確認する。"""
    import tempfile

    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        assets = Path(tmp) / "assets"
        # 完全なテーマ
        full = assets / "2026-01-02_full-theme"
        full.mkdir(parents=True)
        (full / "deck_spec.json").write_text(json.dumps({
            "meta": {"title": "フルテーマ", "subtitle": "サブ", "palette_preset": "navy_gold"},
            "slides": [
                {"layout": "title", "note": "あ" * 350},
                {"layout": "bullets", "note": "い" * 350},
                {"layout": "cards", "note": ""},
                {"layout": "bullets", "note": ""},
            ],
        }, ensure_ascii=False), encoding="utf-8")
        (full / "deck.pptx").write_bytes(b"x")
        (full / "slide_timings.json").write_text(json.dumps([
            {"slide": 1, "start_sec": 0.0, "end_sec": 10.0},
            {"slide": 2, "start_sec": 10.0, "end_sec": 42.5},
        ]), encoding="utf-8")
        (full / "risk-and-quality-review.md").write_text(
            "| **合計** | **100** | **95** | **85点以上のため修正不要** |", encoding="utf-8")
        (full / "README.md").write_text("評価スコア: 82/100(round27)", encoding="utf-8")

        # 最小構成のテーマ(欠けている情報は null になるべき)
        minimal = assets / "2026-01-01_minimal-theme"
        minimal.mkdir(parents=True)
        (minimal / "deck_spec.json").write_text(json.dumps({
            "meta": {}, "slides": [{"layout": "title", "note": ""}],
        }), encoding="utf-8")

        # テーマではないディレクトリ(無視されるべき)
        (assets / "not-a-theme").mkdir()

        catalog = build_catalog(assets)

        def check(cond: bool, msg: str):
            nonlocal ok
            if not cond:
                print(f"SELF-TEST FAIL: {msg}")
                ok = False

        check(catalog["totals"]["themes"] == 2, f"テーマ数が2でない: {catalog['totals']['themes']}")
        check(catalog["themes"][0]["id"] == "2026-01-02_full-theme", "新しい順に並んでいない")

        f = catalog["themes"][0]
        check(f["title"] == "フルテーマ", "タイトルが取れていない")
        check(f["date"] == "2026-01-02" and f["slug"] == "full-theme", "日付/slugの分解が誤り")
        check(f["slides"] == 4, f"スライド数が誤り: {f['slides']}")
        check(f["bulletsRatio"] == 50.0, f"bullets比率が誤り: {f['bulletsRatio']}")
        check(f["narrationMinutes"] == 2.0, f"ナレーション分数が誤り: {f['narrationMinutes']}")
        check(f["audioSeconds"] == 42.5, f"音声尺が誤り: {f['audioSeconds']}")
        check(f["qualityScore"] == 95, f"品質スコアが誤り: {f['qualityScore']}")
        check(f["themeScore"] == 82, f"テーマ評価点が誤り: {f['themeScore']}")
        check(f["artifacts"]["pptx"] is True, "pptxの有無判定が誤り")
        check(f["artifacts"]["audio"] is False, "存在しない音声をTrueにしている")
        check(f["layouts"].get("bullets") == 2, "レイアウト集計が誤り")

        mn = catalog["themes"][1]
        check(mn["qualityScore"] is None, "無い品質スコアをnullにしていない")
        check(mn["audioSeconds"] is None, "無い音声尺をnullにしていない")
        check(mn["narrationMinutes"] is None, "ノート無しをnullにしていない")
        check(mn["subtitle"] is None, "無いサブタイトルをnullにしていない")

        t = catalog["totals"]
        check(t["slides"] == 5, f"合計スライド数が誤り: {t['slides']}")
        check(t["withPptx"] == 1, f"pptx保有数が誤り: {t['withPptx']}")
        # 音声ファイル(.wav)は無いが、タイミング情報だけはある構成。両者を混同していないか検査する
        check(t["withAudio"] == 0, f"音声ファイル保有数が誤り(wavは無いはず): {t['withAudio']}")
        check(t["timedThemes"] == 1, f"タイミング保有数が誤り: {t['timedThemes']}")
        check(t["timedAudioSeconds"] == 42.5, f"尺合計が誤り: {t['timedAudioSeconds']}")
        check(t["averageQualityScore"] == 95.0, f"平均品質スコアが誤り: {t['averageQualityScore']}")

    print("SELF-TEST PASSED" if ok else "SELF-TEST FAILED")
    return 0 if ok else 1


def main() -> int:
    args = [a for a in sys.argv[1:]]
    if "--self-test" in args:
        return self_test()

    repo_root = Path(__file__).resolve().parents[2]
    assets_dir = repo_root / "ai-company-os" / "assets"
    out_path = Path(args[0]) if args else repo_root / "lib" / "ai-company-os" / "catalog.json"

    if not assets_dir.is_dir():
        print(f"ERROR: assets ディレクトリが見つかりません: {assets_dir}")
        return 2

    catalog = build_catalog(assets_dir)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    t = catalog["totals"]
    print(f"生成完了: {out_path}")
    print(
        f"  テーマ {t['themes']}件 / スライド計 {t['slides']}枚 / "
        f"pptx {t['withPptx']}件 / 音声 {t['withAudio']}件"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
