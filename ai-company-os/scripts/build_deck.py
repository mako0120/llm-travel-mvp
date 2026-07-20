#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_deck.py — デッキ仕様(JSON)から .pptx を生成する汎用ビルダー

入力: デッキ仕様 JSON(templates/deck_spec_example.json 参照)
出力: docs/04_PowerPoint.md 標準に準拠した 16:9 の .pptx

使い方:
  python scripts/build_deck.py spec.json output.pptx
  python scripts/build_deck.py spec.json output.pptx && python scripts/verify_pptx.py output.pptx

対応レイアウト:
  title     — 表紙(ダーク背景、見出し・サブコピー・脚注)
  bullets   — 見出し+ブレット(最大5、出典行つき)
  cards     — カードグリッド(数字・ラベル・本文、2〜4枚)
  steps     — 番号バッジつき横並びステップ(3〜4個)
  bar_chart — ネイティブ棒グラフ(編集可能、出典行つき)
  cta       — クロージング(ダーク背景、CTA 1つ)

規則(ビルド時に強制):
  - 全スライドに note(スピーカーノート)必須。欠けていればエラー終了
  - bullets は最大5個。超えていればエラー終了
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from pptx import Presentation
    from pptx.chart.data import CategoryChartData
    from pptx.dml.color import RGBColor
    from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION
    from pptx.enum.shapes import MSO_SHAPE
    from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
    from pptx.util import Inches, Pt
except ImportError:
    print("ERROR: python-pptx が見つかりません。`pip install python-pptx` を実行してください。")
    sys.exit(2)

W, H = 13.333, 7.5

DEFAULT_PALETTE = {
    "primary": "1E2761",
    "primary_dark": "141B47",
    "base": "CADCFC",
    "base_soft": "8FA3D0",
    "accent": "D9A441",
    "ink": "1A1A2E",
    "muted": "5B6270",
    "card": "F3F6FC",
}
WHITE = RGBColor(0xFF, 0xFF, 0xFF)


def rgb(hexstr: str) -> RGBColor:
    hexstr = hexstr.lstrip("#")
    return RGBColor(int(hexstr[0:2], 16), int(hexstr[2:4], 16), int(hexstr[4:6], 16))


class DeckBuilder:
    def __init__(self, meta: dict):
        pal = {**DEFAULT_PALETTE, **meta.get("palette", {})}
        self.c = {k: rgb(v) for k, v in pal.items()}
        self.font = meta.get("font", "Yu Gothic")
        self.footer_text = meta.get("footer", "")
        self.prs = Presentation()
        self.prs.slide_width = Inches(W)
        self.prs.slide_height = Inches(H)
        self.blank = self.prs.slide_layouts[6]
        self.page = 0

    # ---- 低レベルヘルパー ----

    def slide(self, dark: bool = False):
        s = self.prs.slides.add_slide(self.blank)
        s.background.fill.solid()
        s.background.fill.fore_color.rgb = self.c["primary_dark"] if dark else WHITE
        self.page += 1
        return s

    def text(self, s, txt, x, y, w, h, size=14, color=None, bold=False,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, spacing=1.0):
        tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = anchor
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        for i, line in enumerate(str(txt).split("\n")):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.alignment = align
            if spacing != 1.0:
                p.line_spacing = spacing
            r = p.add_run()
            r.text = line
            f = r.font
            f.size = Pt(size)
            f.bold = bold
            f.name = self.font
            f.color.rgb = color if color is not None else self.c["ink"]
        return tb

    def card(self, s, x, y, w, h):
        sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
        sh.fill.solid()
        sh.fill.fore_color.rgb = self.c["card"]
        sh.line.fill.background()
        sh.adjustments[0] = 0.06
        return sh

    def badge(self, s, glyph, x, y, d=0.7, size=20):
        c = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y), Inches(d), Inches(d))
        c.fill.solid()
        c.fill.fore_color.rgb = self.c["primary"]
        c.line.fill.background()
        tf = c.text_frame
        tf.word_wrap = False
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        r = p.add_run()
        r.text = str(glyph)
        r.font.size = Pt(size)
        r.font.bold = True
        r.font.name = self.font
        r.font.color.rgb = WHITE
        return c

    def title_bar(self, s, t):
        self.text(s, t, 0.5, 0.45, W - 1.0, 0.8, size=30, bold=True, color=self.c["primary"])

    def footer(self, s):
        if self.footer_text:
            self.text(s, self.footer_text, 0.5, 7.05, 8, 0.35, size=10, color=self.c["muted"])
        self.text(s, str(self.page), W - 1.0, 7.05, 0.5, 0.35, size=10,
                  color=self.c["muted"], align=PP_ALIGN.RIGHT)

    def source_line(self, s, src):
        if src:
            self.text(s, f"出典: {src}", 0.5, 6.6, W - 1.0, 0.35, size=10, color=self.c["muted"])

    def notes(self, s, t):
        s.notes_slide.notes_text_frame.text = t

    # ---- レイアウト ----

    def add_title(self, spec):
        s = self.slide(dark=True)
        self.text(s, spec["heading"], 0.6, 2.2, 12.1, 2.3, size=42, bold=True, color=WHITE, spacing=1.15)
        if spec.get("sub"):
            self.text(s, spec["sub"], 0.6, 4.6, 11.5, 0.6, size=20, color=self.c["base"])
        if spec.get("footnote"):
            self.text(s, spec["footnote"], 0.6, 6.5, 11.5, 0.4, size=12, color=self.c["base_soft"])
        return s

    def add_bullets(self, spec):
        s = self.slide()
        self.title_bar(s, spec["title"])
        y = 1.6
        if spec.get("lead"):
            self.text(s, spec["lead"], 0.5, y, W - 1.0, 0.5, size=16, color=self.c["muted"])
            y += 0.7
        for b in spec["bullets"]:
            self.badge(s, "・", 0.5, y + 0.02, d=0.35, size=12)
            self.text(s, b, 1.05, y, W - 1.6, 0.7, size=18, spacing=1.1)
            y += 0.85
        self.source_line(s, spec.get("source"))
        self.footer(s)
        return s

    def add_cards(self, spec):
        s = self.slide()
        self.title_bar(s, spec["title"])
        cards = spec["cards"]
        n = len(cards)
        gap = 0.35
        cw = (W - 1.0 - gap * (n - 1)) / n
        for i, cd in enumerate(cards):
            x = 0.5 + i * (cw + gap)
            self.card(s, x, 1.7, cw, 4.3)
            y = 2.0
            if cd.get("big"):
                self.text(s, cd["big"], x + 0.3, y, cw - 0.6, 0.9, size=34, bold=True, color=self.c["accent"])
                y += 1.1
            self.text(s, cd["label"], x + 0.3, y, cw - 0.6, 0.6, size=16, bold=True, color=self.c["primary"])
            y += 0.75
            if cd.get("text"):
                self.text(s, cd["text"], x + 0.3, y, cw - 0.6, 2.0, size=13, color=self.c["muted"], spacing=1.15)
        self.source_line(s, spec.get("source"))
        self.footer(s)
        return s

    def add_steps(self, spec):
        s = self.slide()
        self.title_bar(s, spec["title"])
        steps = spec["steps"]
        n = len(steps)
        gap = 0.4
        cw = (W - 1.0 - gap * (n - 1)) / n
        for i, st in enumerate(steps):
            x = 0.5 + i * (cw + gap)
            self.card(s, x, 1.9, cw, 3.6)
            self.badge(s, i + 1, x + 0.3, 2.2, d=0.7, size=20)
            self.text(s, st["label"], x + 0.3, 3.2, cw - 0.6, 0.6, size=16, bold=True, color=self.c["primary"])
            self.text(s, st.get("text", ""), x + 0.3, 3.9, cw - 0.6, 1.4, size=12, color=self.c["muted"], spacing=1.15)
        self.footer(s)
        return s

    def add_bar_chart(self, spec):
        s = self.slide()
        self.title_bar(s, spec["title"])
        data = CategoryChartData()
        data.categories = spec["categories"]
        data.add_series(spec["series"].get("name", ""), spec["series"]["values"])
        gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(0.7), Inches(1.6), Inches(11.9), Inches(4.7), data)
        chart = gf.chart
        chart.has_legend = False
        plot = chart.plots[0]
        plot.has_data_labels = True
        dl = plot.data_labels
        dl.number_format = spec.get("number_format", "#,##0")
        dl.number_format_is_linked = False
        dl.position = XL_LABEL_POSITION.OUTSIDE_END
        dl.font.size = Pt(12)
        dl.font.bold = True
        dl.font.name = self.font
        dl.font.color.rgb = self.c["primary"]
        chart.series[0].format.fill.solid()
        chart.series[0].format.fill.fore_color.rgb = self.c["primary"]
        self.source_line(s, spec.get("source"))
        self.footer(s)
        return s

    def add_cta(self, spec):
        s = self.slide(dark=True)
        self.text(s, spec["heading"], 0.6, 1.8, 12.1, 1.6, size=36, bold=True, color=WHITE, spacing=1.15)
        if spec.get("sub"):
            self.text(s, spec["sub"], 0.6, 3.6, 11.5, 1.0, size=18, color=self.c["base"], spacing=1.2)
        if spec.get("action"):
            self.card(s, 0.6, 5.0, 8.0, 1.1)
            self.text(s, spec["action"], 0.95, 5.28, 7.4, 0.6, size=18, bold=True, color=self.c["primary"])
        return s


LAYOUTS = {
    "title": DeckBuilder.add_title,
    "bullets": DeckBuilder.add_bullets,
    "cards": DeckBuilder.add_cards,
    "steps": DeckBuilder.add_steps,
    "bar_chart": DeckBuilder.add_bar_chart,
    "cta": DeckBuilder.add_cta,
}

MAX_BULLETS = 5


def build(spec_path: str, out_path: str) -> int:
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    errors: list[str] = []
    for i, sl in enumerate(spec.get("slides", []), start=1):
        if sl.get("layout") not in LAYOUTS:
            errors.append(f"スライド {i}: 未知のレイアウト '{sl.get('layout')}'")
        if not str(sl.get("note", "")).strip():
            errors.append(f"スライド {i}: note(スピーカーノート)がありません")
        if sl.get("layout") == "bullets" and len(sl.get("bullets", [])) > MAX_BULLETS:
            errors.append(f"スライド {i}: ブレットが {MAX_BULLETS} 個を超えています")
    if not spec.get("slides"):
        errors.append("slides が空です")
    if errors:
        print(f"仕様エラー ({len(errors)} 件):")
        for e in errors:
            print(f"  - {e}")
        return 1

    builder = DeckBuilder(spec.get("meta", {}))
    for sl in spec["slides"]:
        s = LAYOUTS[sl["layout"]](builder, sl)
        builder.notes(s, sl["note"])
    builder.prs.save(out_path)
    print(f"生成完了: {out_path} ({len(spec['slides'])} スライド)")
    print(f"次に検品を実行してください: python scripts/verify_pptx.py {out_path}")
    return 0


def main() -> int:
    if len(sys.argv) != 3:
        print("使い方: python scripts/build_deck.py <spec.json> <output.pptx>")
        return 2
    if not Path(sys.argv[1]).is_file():
        print(f"ERROR: 仕様ファイルが存在しません: {sys.argv[1]}")
        return 2
    return build(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    sys.exit(main())
