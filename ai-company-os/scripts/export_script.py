#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""export_script.py — デッキ仕様(JSON)から発表原稿(Markdown)を書き出す

build_deck.py と同じ deck_spec.json を入力にして、スピーカーノートを
「読み上げ原稿」として整形した Markdown を出力する。PowerPoint のノート欄を
開かなくても、原稿だけを読んで練習・推敲できるようにするためのツール。

使い方:
  python scripts/export_script.py spec.json script.md

出力に含まれるもの:
  - スライドごとの見出し(レイアウトに応じて title/heading/quote から抽出)
  - ノート全文(そのまま読み上げ原稿として使える文章)
  - 各スライドの目安発表時間(日本語 350字/分で概算)
  - 合計の目安発表時間

目安発表時間はあくまで概算(一般的な日本語プレゼン速度の目安)であり、
実際の発表時間を保証するものではない。
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

CHARS_PER_MINUTE = 350  # 日本語プレゼン読み上げ速度の目安


def slide_heading(sl: dict) -> str:
    """レイアウトごとに異なる見出しキーから、原稿用の見出しを取り出す。"""
    if sl["layout"] == "title":
        return sl["heading"].replace("\n", " ")
    if sl["layout"] == "cta":
        return sl["heading"].replace("\n", " ")
    if sl["layout"] == "quote":
        return f"引用: {sl['quote'][:24]}{'…' if len(sl['quote']) > 24 else ''}"
    return sl.get("title", "(無題)")


def estimate_minutes(text: str) -> float:
    return len(text) / CHARS_PER_MINUTE


def build_script(spec_path: str, out_path: str) -> int:
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    slides = spec.get("slides", [])
    if not slides:
        print("ERROR: slides が空です")
        return 1

    deck_title = spec.get("meta", {}).get("title", Path(spec_path).stem)
    lines = [f"# {deck_title} — 発表原稿\n"]
    lines.append(f"<!-- {export_notice()} -->\n")

    total_minutes = 0.0
    for i, sl in enumerate(slides, start=1):
        note = str(sl.get("note", "")).strip()
        if not note:
            print(f"ERROR: スライド {i} に note がありません(build_deck.py と同じ仕様を使ってください)")
            return 1
        minutes = estimate_minutes(note)
        total_minutes += minutes
        heading = slide_heading(sl)
        lines.append(f"## スライド {i}: {heading}")
        lines.append(f"*レイアウト: {sl['layout']} / 目安 {minutes:.1f}分*\n")
        lines.append(note)
        lines.append("")

    lines.insert(2, f"**合計目安時間: 約{total_minutes:.0f}分**({len(slides)}スライド、{CHARS_PER_MINUTE}字/分換算)\n")

    Path(out_path).write_text("\n".join(lines), encoding="utf-8")
    print(f"生成完了: {out_path} ({len(slides)} スライド、目安 約{total_minutes:.0f}分)")
    return 0


def export_notice() -> str:
    return "このファイルは export_script.py により deck_spec.json から自動生成された。手編集した場合は元のJSONにも反映すること。"


def main() -> int:
    if len(sys.argv) != 3:
        print("使い方: python scripts/export_script.py <spec.json> <script.md>")
        return 2
    if not Path(sys.argv[1]).is_file():
        print(f"ERROR: 仕様ファイルが存在しません: {sys.argv[1]}")
        return 2
    return build_script(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    sys.exit(main())
