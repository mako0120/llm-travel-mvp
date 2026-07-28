#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""export_review_request.py — ChatGPT Work へ渡すレビュー依頼書を書き出す

docs/15_PPT_Handoff.md の二段階品質ゲートで、Claude Code の初稿を
ChatGPT Work(編集長)に渡すための依頼書(Markdown)を deck_spec.json から生成する。

ChatGPT 用の API 接続・MCP サーバーはこのリポジトリに存在しないため、連携は
「人間または Cowork が、この依頼書と全ページ画像を ChatGPT に手渡しする」
手動フローを前提にしている。依頼書を毎回手書きすると指示が揺れて
レビュー品質が安定しないため、仕様から機械的に生成する。

使い方:
  python scripts/export_review_request.py <deck_spec.json> <review_request.md>
  python scripts/export_review_request.py --self-test

依頼書に含まれるもの:
  - ChatGPT Work の役割(編集長)と、やってはいけないこと
  - 確認必須の5分類(story / visibility / speaker_notes / sources / overlap_or_cutoff)
  - スライドごとの本文・ノート・出典の抜粋(画像だけでは読み取りにくい情報を補う)
  - 返してほしい chatgpt_review.json の形式と、記入例

画像そのものは render_deck_images.py で別途書き出して添付する
(このスクリプトはテキストの依頼書のみを生成する)。
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# docs/15_PPT_Handoff.md で定義した確認必須項目。
# verify_chatgpt_review.py の CATEGORIES と一致させること。
CHECK_ITEMS = [
    ("story", "ストーリー・構成", "章立ての流れ、1スライド1メッセージが崩れていないか"),
    ("visibility", "視認性", "文字サイズ・コントラスト・情報量過多がないか"),
    ("speaker_notes", "スピーカーノート", "欠落、内容と食い違う記述、不自然な文体がないか"),
    ("sources", "出典", "数字を伴うスライドに出典が明記されているか"),
    ("overlap_or_cutoff", "重なり・文字切れ", "図形のはみ出し・テキストの見切れがないか"),
]


def _flatten(value) -> str:
    """スライドの各フィールドを、依頼書に載せる1行テキストへ潰す。"""
    if isinstance(value, str):
        return value.replace("\n", " ")
    if isinstance(value, list):
        parts = []
        for item in value:
            if isinstance(item, dict):
                label = item.get("label") or item.get("heading") or ""
                text = item.get("text") or item.get("sublabel") or ""
                parts.append(f"{label}: {text}".strip(": "))
            elif isinstance(item, list):
                parts.append(" | ".join(str(cell) for cell in item))
            else:
                parts.append(str(item))
        return " / ".join(p for p in parts if p)
    if isinstance(value, dict):
        heading = value.get("heading", "")
        items = _flatten(value.get("items", []))
        return f"{heading}: {items}".strip(": ")
    return str(value)


def slide_body(sl: dict) -> str:
    """レイアウトごとに異なる本文キーから、レビュー対象の本文を抜き出す。"""
    keys = (
        "heading", "sub", "title", "bullets", "cards", "items", "steps",
        "nodes", "left", "right", "headers", "rows", "quote", "attribution",
        "stat", "caption", "categories", "action",
    )
    parts = []
    for key in keys:
        if key not in sl:
            continue
        text = _flatten(sl[key]).strip()
        if text:
            parts.append(f"{key}={text}")

    # チャート系はグラフ内の数値そのものが出典チェックの対象になるため、
    # categories と対応させた形で必ず載せる(画像からは読み取りにくいため)。
    series = sl.get("series")
    if isinstance(series, dict):
        name = series.get("name", "")
        values = series.get("values", [])
        parts.append(f"series={name}: {', '.join(str(v) for v in values)}".strip(": "))
    if "values" in sl and not isinstance(series, dict):
        parts.append(f"values={', '.join(str(v) for v in sl['values'])}")

    return " ; ".join(parts) if parts else "(本文なし)"


def build_request(spec_path: str, out_path: str) -> int:
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    slides = spec.get("slides", [])
    if not slides:
        print("ERROR: slides が空です")
        return 1

    meta = spec.get("meta", {})
    deck_title = meta.get("title", Path(spec_path).stem)

    lines: list[str] = []
    lines.append(f"# レビュー依頼: {deck_title}")
    lines.append("")
    lines.append(
        "<!-- このファイルは export_review_request.py により deck_spec.json から"
        "自動生成された。ChatGPT Work への依頼時は、全ページ画像"
        "(render_deck_images.py の出力)と一緒に渡すこと。 -->"
    )
    lines.append("")

    lines.append("## あなたの役割")
    lines.append("")
    lines.append(
        "あなたは AI Company OS の「編集長」(ChatGPT Work)です。"
        "Claude Code が生成した PowerPoint 初稿の全ページを実際に確認し、"
        "内容・構成・視認性・スピーカーノート・出典を評価してください。"
    )
    lines.append("")
    lines.append("**やってはいけないこと**:")
    lines.append("")
    lines.append("- PowerPoint ファイル(.pptx)そのものを編集しない")
    lines.append("- `deck_spec.json` を直接書き換えない")
    lines.append("- 出典のない数字を新たに創作しない(誤りの指摘は歓迎、事実の追加は不可)")
    lines.append("")
    lines.append(
        "修正は Claude Code が `deck_spec.json` に反映して再生成します。"
        "あなたの成果物は下記フォーマットの**レビュー結果 JSON のみ**です。"
    )
    lines.append("")

    lines.append("## 確認してほしい項目(この5分類のいずれかで指摘してください)")
    lines.append("")
    lines.append("| category | 観点 | 見るポイント |")
    lines.append("|---|---|---|")
    for key, label, desc in CHECK_ITEMS:
        lines.append(f"| `{key}` | {label} | {desc} |")
    lines.append("")
    lines.append(
        "`severity` は `critical`(必ず直すべき)または `minor`(直したほうがよい)"
        "の2値で付けてください。"
    )
    lines.append("")

    lines.append("## デッキの基本情報")
    lines.append("")
    lines.append(f"- スライド総数: {len(slides)} 枚")
    lines.append(f"- 配色プリセット: {meta.get('palette_preset', '(未指定)')}")
    lines.append(f"- フッター: {meta.get('footer', '(なし)')}")
    lines.append("")

    lines.append("## スライドごとの内容(画像と突き合わせて確認してください)")
    lines.append("")
    lines.append(
        "画像だけでは読み取りにくいスピーカーノート・出典も含めています。"
        "**画像に写っている見た目**と、**下記のテキスト**の両方を確認してください。"
    )
    lines.append("")

    for i, sl in enumerate(slides, start=1):
        lines.append(f"### スライド {i}(レイアウト: `{sl.get('layout', '不明')}`)")
        lines.append("")
        lines.append(f"- 本文: {slide_body(sl)}")
        note = str(sl.get("note", "")).strip()
        lines.append(f"- スピーカーノート: {note if note else '**(欠落)**'}")
        source = str(sl.get("source", "")).strip()
        footnote = str(sl.get("footnote", "")).strip()
        shown = source or footnote
        lines.append(f"- 出典表記: {shown if shown else '(なし)'}")
        lines.append("")

    lines.append("## 返してほしい形式")
    lines.append("")
    lines.append(
        "下記の JSON だけを返してください(前後に説明文を付けない)。"
        "指摘がないスライドは `slides` に含めなくて構いません。"
    )
    lines.append("")
    lines.append("```json")
    example = {
        "theme_slug": "<テーマのディレクトリ名>",
        "reviewed_pptx": "deck.claude-draft.pptx",
        "reviewer": "ChatGPT Work",
        "review_date": "YYYY-MM-DD",
        "overall_verdict": "approved / needs_revision / rejected のいずれか",
        "slides": [
            {
                "slide_number": 3,
                "issues": [
                    {
                        "category": "visibility",
                        "severity": "critical",
                        "description": "何が問題かを具体的に書く",
                        "suggested_fix": "どう直すべきかを具体的に書く",
                    }
                ],
            }
        ],
        "summary": "全体の講評を1〜2文で",
    }
    lines.append(json.dumps(example, ensure_ascii=False, indent=2))
    lines.append("```")
    lines.append("")
    lines.append(
        "受け取った JSON は `python scripts/verify_chatgpt_review.py` で"
        "機械的に検証します。項目名・値の綴りを上記どおりにしてください。"
    )
    lines.append("")

    Path(out_path).write_text("\n".join(lines), encoding="utf-8")
    print(f"生成完了: {out_path}({len(slides)} スライド分の依頼書)")
    print("次に render_deck_images.py で全ページ画像を書き出し、両方を ChatGPT Work へ渡してください。")
    return 0


def self_test() -> int:
    """最小のデッキ仕様から依頼書を生成し、必須の見出し・項目が含まれるか確認する。"""
    import tempfile

    spec = {
        "meta": {"title": "セルフテスト用デッキ", "palette_preset": "navy_gold"},
        "slides": [
            {"layout": "title", "heading": "見出し", "sub": "サブ", "note": "ノート1"},
            {
                "layout": "cards",
                "title": "カード",
                "cards": [{"label": "A", "text": "本文A"}],
                "note": "ノート2",
                "source": "出典X",
            },
            {"layout": "bullets", "title": "箇条書き", "bullets": ["項目1", "項目2"], "note": ""},
        ],
    }
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        spec_path = Path(tmp) / "spec.json"
        out_path = Path(tmp) / "request.md"
        spec_path.write_text(json.dumps(spec, ensure_ascii=False), encoding="utf-8")

        if build_request(str(spec_path), str(out_path)) != 0:
            print("SELF-TEST FAIL: 依頼書の生成に失敗しました")
            return 1

        text = out_path.read_text(encoding="utf-8")
        required = [
            "## あなたの役割",
            "## 確認してほしい項目",
            "## スライドごとの内容",
            "## 返してほしい形式",
            "スライド 1", "スライド 2", "スライド 3",
            "本文A",
            "出典X",
            "**(欠落)**",  # note が空のスライド3で欠落を明示できているか
        ]
        for token in required:
            if token not in text:
                print(f"SELF-TEST FAIL: 依頼書に '{token}' が含まれていません")
                ok = False
        for key, _, _ in CHECK_ITEMS:
            if f"`{key}`" not in text:
                print(f"SELF-TEST FAIL: 確認項目 '{key}' が依頼書に含まれていません")
                ok = False

    print("SELF-TEST PASSED" if ok else "SELF-TEST FAILED")
    return 0 if ok else 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="deck_spec.json から ChatGPT Work 向けレビュー依頼書を生成する"
    )
    parser.add_argument("spec", nargs="?", help="deck_spec.json")
    parser.add_argument("out", nargs="?", help="出力する依頼書(.md)")
    parser.add_argument("--self-test", action="store_true", help="生成ロジックの健全性のみ確認する")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    if not args.spec or not args.out:
        parser.error("spec と out を指定するか、--self-test を指定してください")
    if not Path(args.spec).is_file():
        print(f"ERROR: 仕様ファイルが存在しません: {args.spec}")
        return 2
    return build_request(args.spec, args.out)


if __name__ == "__main__":
    sys.exit(main())
