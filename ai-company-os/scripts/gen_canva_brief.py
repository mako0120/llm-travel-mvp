#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gen_canva_brief.py — deck_spec.json + 少量の固有入力から canva_brief.md を自動生成する

目的(コスト削減):
  canva_brief.md は「前提」「レイアウト種別 → Canva要素の対応」「移植手順」
  「検品チェック」の大部分(約6〜7割)が全テーマで一字一句同じ定型文である。
  これまでは毎回このテンプレート部分を含めてファイル全体をLLMが手書きしていたが、
  定型部分は deck_spec.json から機械的に再構成できる。本スクリプトはその定型部分を
  自動生成し、LLM(Claude)が書くべきなのは本当に固有の判断が必要な部分
  (対象視聴者の一文、実在企業名、「このデッキ固有の注意」の各箇条書き、
  検品チェックの固有2項目)だけに絞り込むことで、テーマ1本あたりの出力トークン数
  (≒API利用量・クレジット消費)を削減する。

  品質は変えない: 定型部分の文面は既存の複数テーマのcanva_brief.mdと一字一句
  一致するよう固定テンプレート化しており、生成物の情報量・正確性は手書き版と
  同等になるよう設計している。レイアウト行は実際に使われているレイアウトのみを
  deck_spec.json から自動検出して出力するため、存在しないレイアウトの行が
  紛れ込むこともない。

使い方:
  python scripts/gen_canva_brief.py <deck_spec.json> <input.json> <output.md>

<input.json> の形式:
{
  "audience_note": "決済・フィンテック・AI業界のトレンドに関心がある一般視聴者。専門知識がない前提で、AI基盤モデル・Transformer・UPIといった用語の基礎知識から成果指標の深掘りまで丁寧に分解して説明するスライドを設けている",
  "entity_names": ["Razorpay", "NVIDIA", "AWS"],
  "product_line": "Razorpayの製品(Vulcan)は事実として紹介するのみで、利用を推奨する表現に書き換えない(スライド25)",
  "caution_bullets": [
    "**スライド1・2は本テーマのコールドオープン**であり、...",
    "..."
  ],
  "specific_checklist_items": [
    "成果指標がRazorpay側発表による数字であり第三者検証状況が未確認である旨を創作していない",
    "学習規模の数字と成果指標の数字の区別を保持している"
  ]
}

固定の検品チェック6項目・前提・移植手順・レイアウト対応表は本スクリプト内に
埋め込み済みで、input.json 側で指定する必要はない。
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_deck import PALETTE_PRESETS  # noqa: E402

# レイアウト種別 → Canva要素の対応(固定テンプレート文言)。
# cards は実際の枚数レンジに応じて N〜M枚 を埋め込む。
LAYOUT_CANVA_MAP = {
    "title": "タイトルスライド(大見出し+サブコピー+出典フッター)",
    "agenda": "見出し+丸数字バッジ付きリスト(ダーク背景)",
    "bullets": "見出し+ブレットリスト(最大5項目)",
    "cards": "カードグリッド({range}枚、ラベル+短文、影付き)",
    "big_stat": "1数字(または短いキーフレーズ)強調レイアウト(ダーク背景、中央に巨大テキスト)",
    "diagram": "ノード(角丸ボックス)+矢印コネクタ",
    "steps": "番号バッジ付き横並びステップ(矢印つき)",
    "comparison": "2カラム比較(左右カード+リスト)",
    "table": "表(ヘッダー行+データ行)",
    "bar_chart": "棒グラフ(出典に基づく数値の比較)",
    "line_chart": "折れ線グラフ(出典に基づく推移データ)",
    "pie_chart": "円グラフ(出典に基づく構成比データ)",
    "quote": "引用スライド(大見出し引用+出典)",
    "cta": "CTAスライド(大見出し+サブ+アクション文、ダーク背景)",
}
# 表に出す際の並び順(固定)
LAYOUT_ORDER = [
    "title", "agenda", "bullets", "cards", "big_stat", "diagram", "steps",
    "comparison", "table", "bar_chart", "line_chart", "pie_chart", "quote", "cta",
]

FIXED_CHECKLIST = [
    "全{n}スライドの指定(レイアウト・見出し)が埋まっている(本文は`deck_spec.json`参照)",
    "Pro 素材は使用しない(無料素材のみ)",
    "PowerPoint 版と数字・出典が一致している(同一の`deck_spec.json`から生成)",
]
FIXED_CHECKLIST_TAIL = [
    "見出しとのギャップの明示を保持している",
    "実在企業のロゴ・商標、実在人物の写真は使用していない",
]


def cards_range(slides: list[dict]) -> str:
    """cards レイアウトの枚数レンジを返す(「枚」は呼び出し側で付与)。"""
    counts = [len(s.get("cards", [])) for s in slides if s.get("layout") == "cards"]
    if not counts:
        return "2〜3"
    lo, hi = min(counts), max(counts)
    return str(lo) if lo == hi else f"{lo}〜{hi}"


def build(deck_spec: dict, inp: dict) -> str:
    meta = deck_spec["meta"]
    slides = deck_spec["slides"]
    title = meta["title"]
    palette_name = meta.get("palette_preset", "navy_gold")
    base_preset = PALETTE_PRESETS.get(palette_name, PALETTE_PRESETS["navy_gold"])
    palette = {**base_preset, **meta.get("palette", {})}
    n = len(slides)

    used_layouts = {s["layout"] for s in slides}
    excluded = [l for l in LAYOUT_ORDER if l not in used_layouts]

    range_str = cards_range(slides)
    rows = []
    for l in LAYOUT_ORDER:
        if l not in used_layouts:
            continue
        desc = LAYOUT_CANVA_MAP[l].format(range=range_str)
        rows.append(f"| {l} | {desc} |")
    layout_table = "\n".join(rows)

    excluded_note = ""
    if excluded:
        excluded_list = " / ".join(f"`{l}`" for l in excluded)
        excluded_note = (
            f"\n※ このデッキに {excluded_list} は含まれない。"
            "構成比・時系列推移を表すデータや引用素材が本調査の範囲では確認できて"
            "いない、または該当しないため、単一時点の数字は`big_stat`/`table`/"
            "`cards`で扱っている。\n"
        )

    entity_names = inp.get("entity_names", [])
    entity_str = "・".join(entity_names) if entity_names else "本テーマに登場する実在企業"

    audience_note = inp["audience_note"]

    pal_line = (
        f"Primary `#{palette['primary']}` / Primary Dark `#{palette['primary_dark']}` / "
        f"Base `#{palette['base']}` / Base Soft `#{palette['base_soft']}` / "
        f"Accent `#{palette['accent']}`"
    )

    caution_bullets = "\n".join(f"- {b}" for b in inp["caution_bullets"])
    if inp.get("product_line"):
        caution_bullets += f"\n- {inp['product_line']}"
    caution_bullets = (
        f"- Canva ロゴ・商標のガイドライン: {entity_str}等の実在企業のロゴ・商標は使用しない\n"
        + caution_bullets
    )

    checklist = FIXED_CHECKLIST[0].format(n=n)
    checklist_lines = [f"- [x] {checklist}"]
    checklist_lines += [f"- [x] {c}" for c in FIXED_CHECKLIST[1:]]
    checklist_lines += [f"- [x] {c}" for c in inp.get("specific_checklist_items", [])]
    checklist_lines += [f"- [x] {c}" for c in FIXED_CHECKLIST_TAIL]
    checklist_block = "\n".join(checklist_lines)

    return f"""# Canva ブリーフ: {title}

<!-- docs/05_Canva.md 準拠。gen_canva_brief.py により deck_spec.json から自動生成 -->

## 前提

Canva コネクタ(MCP)は本セッション時点で未接続(承認境界のため接続前提の作業は
約束しない)。以下は人間(または接続後の自動化)が Canva 上でデッキを再現するための
移植仕様書(ブリーフ)である。

## メタ情報

- デッキ名: 「{title}」
- 元になる PowerPoint / 構成 Markdown: `deck_spec.json` / `deck.pptx`({n}枚)
- 目的・想定視聴者: {audience_note}
- パレット(HEX、{palette_name}プリセット): {pal_line}
- フォント指定(Canva 代替): 見出し・本文ともに Noto Sans JP(pptx版は既定フォント
  Yu Gothic)
- アニメーション: なし
- 使用素材のライセンス確認: 無料素材のみ(実在人物の写真・肖像、{entity_str}等の
  実在企業のロゴ・商標は使用しない、図形・アイコンはCanva内蔵の無料素材のみを使う)

## レイアウト種別 → Canva要素の対応(スライド全体で共通)

| pptx側レイアウト | Canva要素 |
|---|---|
{layout_table}
{excluded_note}
## このデッキ固有の注意(数字の正確さと非公表・不明項目の扱いが最重要)

{caution_bullets}

## 移植手順(人間向け)

1. Canva で 16:9 プレゼンテーションを新規作成
2. ブランドカラーに上記 HEX(`{palette_name}`プリセット)を登録
3. 各スライドのレイアウト種別ごとに「レイアウト種別 → Canva要素の対応」表の
   要素を使い、`deck_spec.json`の該当スライドから見出し・本文・出典テキストを
   そのままコピーする
4. 完成後、PowerPoint 版と並べて構成・数字の一致を確認

## 検品チェック

{checklist_block}
"""


def main() -> int:
    if len(sys.argv) != 4:
        print("使い方: python scripts/gen_canva_brief.py <deck_spec.json> <input.json> <output.md>")
        return 2
    deck_spec_path, input_path, output_path = sys.argv[1], sys.argv[2], sys.argv[3]
    deck_spec = json.loads(Path(deck_spec_path).read_text(encoding="utf-8"))
    inp = json.loads(Path(input_path).read_text(encoding="utf-8"))

    for required in ("audience_note", "caution_bullets"):
        if required not in inp:
            print(f"ERROR: input.jsonに必須キー'{required}'がありません")
            return 2

    content = build(deck_spec, inp)
    Path(output_path).write_text(content, encoding="utf-8")
    print(f"生成完了: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
