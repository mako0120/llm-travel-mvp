#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""render_deck_images.py — deck_spec.json から各スライドのPNG画像を直接描画する。

**なぜLibreOffice経由のpptx→画像変換ではなくPillowで直接描画するのか**:
このリポジトリが動くClaude Codeのリモートセッションには、LibreOffice本体は入っている
ものの実際に文書を開くためのフィルタ・アプリケーションモジュール(Impress/Writer/Calc
本体)が入っておらず、`--convert-to pdf`はどんな文書に対しても
`Error: source file could not be loaded`で失敗する(apt経由の追加インストールは
egressポリシーでブロックされ不可)。そのため、build_deck.py がpptxを組み立てるのと
同じ deck_spec.json を入力に、Pillowで直接スライド画像を描画するアプローチを取る。
build_deck.py とレイアウト・配色(PALETTE_PRESETS)を共有し、見た目の一貫性を保つ。

前提: pip install pillow(インストール済みが多い)。日本語フォントは
`/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf`(IPAゴシック)を使う。

使い方:
  python scripts/render_deck_images.py deck_spec.json out_dir/
  → out_dir/slide_001.png ... slide_0NN.png を生成する
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("ERROR: Pillow が見つかりません。`pip install pillow` を実行してください。")
    sys.exit(2)

sys.path.insert(0, str(Path(__file__).parent))
from build_deck import PALETTE_PRESETS, DEFAULT_PALETTE  # noqa: E402

W_IN, H_IN = 13.333, 7.5
SCALE = 144  # px/inch (1920x1080相当)
W, H = round(W_IN * SCALE), round(H_IN * SCALE)

FONT_CANDIDATES = [
    "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf",
    "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/noto/NotoSansCJKjp-Regular.otf",
]


def _find_font_path() -> str:
    for p in FONT_CANDIDATES:
        if Path(p).is_file():
            return p
    raise FileNotFoundError(
        "日本語フォントが見つかりません。候補: " + ", ".join(FONT_CANDIDATES) +
        " のいずれかをインストールしてください(例: apt-get install fonts-ipafont-gothic)。"
    )


FONT_PATH = None  # 初回のfont()呼び出し時に_find_font_path()で解決する(import時エラーを避ける)
_FONT_CACHE: dict[int, "ImageFont.FreeTypeFont"] = {}


def px(inches: float) -> int:
    return round(inches * SCALE)


def font(size_pt: int, bold: bool = False) -> "ImageFont.FreeTypeFont":
    # ボールドは同じ日本語フォントを流用(専用ボールド書体が無いため太字表現はできないが、
    # サイズ・色・レイアウトで代替する)
    global FONT_PATH
    if FONT_PATH is None:
        FONT_PATH = _find_font_path()
    size_px = round(size_pt * SCALE / 72)
    key = size_px
    if key not in _FONT_CACHE:
        _FONT_CACHE[key] = ImageFont.truetype(FONT_PATH, size_px)
    return _FONT_CACHE[key]


def hex_to_rgb(hexstr: str) -> tuple[int, int, int]:
    hexstr = hexstr.lstrip("#")
    return (int(hexstr[0:2], 16), int(hexstr[2:4], 16), int(hexstr[4:6], 16))


def wrap_text(draw: "ImageDraw.ImageDraw", text: str, f: "ImageFont.FreeTypeFont", max_width: int) -> list[str]:
    """CJK混じりのテキストを1文字ずつ幅を測って折り返す(単語区切りに依存しない)。"""
    lines = []
    for raw_line in str(text).split("\n"):
        if not raw_line:
            lines.append("")
            continue
        cur = ""
        for ch in raw_line:
            trial = cur + ch
            w = draw.textlength(trial, font=f)
            if w > max_width and cur:
                lines.append(cur)
                cur = ch
            else:
                cur = trial
        lines.append(cur)
    return lines


def draw_text(draw, text, x, y, w, size, color, bold=False, align="left", spacing=1.15, max_lines=None):
    f = font(size, bold)
    lines = wrap_text(draw, text, f, px(w))
    if max_lines:
        lines = lines[:max_lines]
    line_h = size * SCALE / 72 * spacing
    cy = y
    for line in lines:
        lw = draw.textlength(line, font=f)
        lx = x
        if align == "center":
            lx = x + (px(w) - lw) / 2
        elif align == "right":
            lx = x + px(w) - lw
        draw.text((lx, cy), line, font=f, fill=color)
        cy += line_h
    return cy  # 描画後のy座標(次の要素の開始位置の目安)


def rounded_card(draw, x, y, w, h, fill):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=px(0.08), fill=fill)


class Renderer:
    def __init__(self, meta: dict):
        preset = PALETTE_PRESETS.get(meta.get("palette_preset", "navy_gold"), DEFAULT_PALETTE)
        pal = {**preset, **meta.get("palette", {})}
        self.c = {k: hex_to_rgb(v) for k, v in pal.items()}
        self.white = (255, 255, 255)
        self.footer_text = meta.get("footer", "")

    def canvas(self, dark=False):
        bg = self.c["primary_dark"] if dark else self.white
        img = Image.new("RGB", (W, H), bg)
        return img, ImageDraw.Draw(img)

    def title_bar(self, draw, text):
        draw_text(draw, text, px(0.5), px(0.45), W_IN - 1.0, 26, self.c["primary"], bold=True)

    def footer(self, draw, page):
        if self.footer_text:
            draw_text(draw, self.footer_text, px(0.5), px(7.05), 8, 9, self.c["muted"])
        f = font(9)
        t = str(page)
        tw = draw.textlength(t, font=f)
        draw.text((W - px(1.0) + px(0.5) - tw, px(7.05)), t, font=f, fill=self.c["muted"])

    def source_line(self, draw, src):
        if src:
            draw_text(draw, f"出典: {src}", px(0.5), px(6.6), W_IN - 1.0, 9, self.c["muted"])

    # ---- レイアウトごとの描画 ----

    def render(self, spec: dict, page: int) -> "Image.Image":
        layout = spec["layout"]
        method = getattr(self, f"r_{layout}", None)
        if method is None:
            raise ValueError(f"未対応のレイアウトです: {layout}")
        return method(spec, page)

    def r_title(self, spec, page):
        img, d = self.canvas(dark=True)
        draw_text(d, spec["heading"], px(0.6), px(2.2), 12.1, 34, self.white, bold=True)
        if spec.get("sub"):
            draw_text(d, spec["sub"], px(0.6), px(4.6), 11.5, 16, self.c["base"])
        if spec.get("footnote"):
            draw_text(d, spec["footnote"], px(0.6), px(6.5), 11.5, 10, self.c["base_soft"])
        return img

    def r_agenda(self, spec, page):
        img, d = self.canvas(dark=True)
        draw_text(d, spec["title"], px(0.6), px(0.7), 12.1, 26, self.white, bold=True)
        y = px(2.1)
        for i, item in enumerate(spec["items"], start=1):
            r = px(0.3)
            cx, cy = px(0.6) + r, y + r
            d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=self.c["primary"])
            f = font(14, bold=True)
            t = str(i)
            tw, th = d.textbbox((0, 0), t, font=f)[2:]
            d.text((cx - tw / 2, cy - th / 2 - px(0.03)), t, font=f, fill=self.white)
            draw_text(d, item, px(1.45), y + px(0.05), 10.5, 16, self.c["base"])
            y += px(0.85)
        return img

    def r_bullets(self, spec, page):
        img, d = self.canvas()
        self.title_bar(d, spec["title"])
        y = px(1.7)
        if spec.get("lead"):
            draw_text(d, spec["lead"], px(0.5), y, W_IN - 1.0, 13, self.c["muted"])
            y += px(0.55)
        for b in spec["bullets"]:
            r = px(0.05)
            d.ellipse([px(0.55) - r, y + px(0.12) - r, px(0.55) + r, y + px(0.12) + r], fill=self.c["accent"])
            end_y = draw_text(d, b, px(0.8), y, W_IN - 1.3, 15, self.c["ink"], spacing=1.2)
            y = max(end_y, y + px(0.5)) + px(0.12)
        self.source_line(d, spec.get("source"))
        self.footer(d, page)
        return img

    def r_cards(self, spec, page):
        img, d = self.canvas()
        self.title_bar(d, spec["title"])
        cards = spec["cards"]
        n = len(cards)
        gap = 0.35
        cw = (W_IN - 1.0 - gap * (n - 1)) / n
        for i, cd in enumerate(cards):
            x = 0.5 + i * (cw + gap)
            rounded_card(d, px(x), px(1.7), px(cw), px(4.3), self.c["card"])
            y = px(2.0)
            if cd.get("big"):
                draw_text(d, cd["big"], px(x + 0.3), y, cw - 0.6, 24, self.c["accent"], bold=True)
                y += px(1.1)
            draw_text(d, cd["label"], px(x + 0.3), y, cw - 0.6, 15, self.c["primary"], bold=True)
            y += px(0.75)
            if cd.get("text"):
                draw_text(d, cd["text"], px(x + 0.3), y, cw - 0.6, 12, self.c["muted"], spacing=1.15)
        self.source_line(d, spec.get("source"))
        self.footer(d, page)
        return img

    def r_steps(self, spec, page):
        img, d = self.canvas()
        self.title_bar(d, spec["title"])
        steps = spec["steps"]
        n = len(steps)
        gap = 0.4
        cw = (W_IN - 1.0 - gap * (n - 1)) / n
        for i, st in enumerate(steps):
            x = 0.5 + i * (cw + gap)
            rounded_card(d, px(x), px(1.9), px(cw), px(3.6), self.c["card"])
            r = px(0.35)
            cx, cy = px(x + 0.3) + r, px(2.2) + r
            d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=self.c["primary"])
            f = font(13, bold=True)
            t = str(i + 1)
            tw, th = d.textbbox((0, 0), t, font=f)[2:]
            d.text((cx - tw / 2, cy - th / 2), t, font=f, fill=self.white)
            draw_text(d, st["label"], px(x + 0.3), px(3.2), cw - 0.6, 14, self.c["primary"], bold=True)
            draw_text(d, st.get("text", ""), px(x + 0.3), px(3.9), cw - 0.6, 11, self.c["muted"], spacing=1.15)
            if i < n - 1:
                ax = px(x + cw + gap * 0.18)
                ay = px(3.5) + px(0.2)
                d.polygon([(ax, ay - px(0.15)), (ax + px(gap * 0.5), ay), (ax, ay + px(0.15))],
                          fill=self.c["accent"])
        self.footer(d, page)
        return img

    def r_comparison(self, spec, page):
        img, d = self.canvas()
        self.title_bar(d, spec["title"])
        cols = [spec["left"], spec["right"]]
        gap = 0.4
        cw = (W_IN - 1.0 - gap) / 2
        for i, col in enumerate(cols):
            x = 0.5 + i * (cw + gap)
            rounded_card(d, px(x), px(1.7), px(cw), px(4.6), self.c["card"])
            draw_text(d, col["heading"], px(x + 0.35), px(2.0), cw - 0.7, 16, self.c["primary"], bold=True)
            y = px(2.75)
            for item in col.get("items", []):
                r = px(0.045)
                d.ellipse([px(x + 0.35) - r, y + px(0.1) - r, px(x + 0.35) + r, y + px(0.1) + r],
                          fill=self.c["muted"])
                draw_text(d, item, px(x + 0.8), y, cw - 1.15, 12, self.c["ink"], spacing=1.1)
                y += px(0.6)
        self.footer(d, page)
        return img

    def r_table(self, spec, page):
        img, d = self.canvas()
        self.title_bar(d, spec["title"])
        headers = spec["headers"]
        rows = spec["rows"]
        ncols = len(headers)
        x0, y0 = px(0.5), px(1.7)
        table_w = W_IN - 1.0
        col_w = table_w / ncols
        row_h = 0.55
        d.rectangle([x0, y0, x0 + px(table_w), y0 + px(row_h)], fill=self.c["primary"])
        for j, h in enumerate(headers):
            draw_text(d, h, x0 + px(col_w * j) + px(0.1), y0 + px(0.12), col_w - 0.2, 13, self.white, bold=True)
        for i, row in enumerate(rows):
            ry = y0 + px(row_h) * (i + 1)
            fill = self.c["card"] if i % 2 == 0 else self.white
            d.rectangle([x0, ry, x0 + px(table_w), ry + px(row_h)], fill=fill)
            for j, cell in enumerate(row):
                draw_text(d, str(cell), x0 + px(col_w * j) + px(0.1), ry + px(0.12), col_w - 0.2, 12, self.c["ink"])
        self.source_line(d, spec.get("source"))
        self.footer(d, page)
        return img

    def r_quote(self, spec, page):
        img, d = self.canvas(dark=True)
        draw_text(d, f"“{spec['quote']}”", px(1.2), px(2.0), 10.9, 22, self.white, bold=True, spacing=1.3)
        if spec.get("attribution"):
            draw_text(d, f"— {spec['attribution']}", px(1.2), px(5.0), 10.9, 13, self.c["base"])
        return img

    def r_cta(self, spec, page):
        img, d = self.canvas(dark=True)
        draw_text(d, spec["heading"], px(0.6), px(1.8), 12.1, 28, self.white, bold=True, spacing=1.15)
        if spec.get("sub"):
            draw_text(d, spec["sub"], px(0.6), px(3.6), 11.5, 15, self.c["base"], spacing=1.2)
        if spec.get("action"):
            draw_text(d, spec["action"], px(0.95), px(5.28), 7.4, 15, self.c["primary"], bold=True)
        return img

    def r_big_stat(self, spec, page):
        img, d = self.canvas(dark=True)
        draw_text(d, spec["title"], px(0.6), px(0.6), 12.1, 17, self.c["base"], bold=True)
        f = font(66, bold=True)
        stat = spec["stat"]
        tw = d.textlength(stat, font=f)
        d.text(((W - tw) / 2, px(2.6)), stat, font=f, fill=self.c["accent"])
        if spec.get("caption"):
            draw_text(d, spec["caption"], px(1.2), px(4.4), 10.9, 15, self.white, align="center", spacing=1.2)
        if spec.get("source"):
            draw_text(d, f"出典: {spec['source']}", px(0.6), px(6.6), 12.1, 9, self.c["base_soft"], align="center")
        return img

    def r_diagram(self, spec, page):
        img, d = self.canvas()
        self.title_bar(d, spec["title"])
        nodes = spec["nodes"]
        n = len(nodes)
        gap, nw, nh = 0.9, 2.6, 1.6
        total_w = nw * n + gap * (n - 1)
        start_x = (W_IN - total_w) / 2
        y = 2.8
        for i, node in enumerate(nodes):
            x = start_x + i * (nw + gap)
            rounded_card(d, px(x), px(y), px(nw), px(nh), self.c["card"])
            draw_text(d, node["label"], px(x + 0.2), px(y + 0.35), nw - 0.4, 14, self.c["primary"],
                      bold=True, align="center")
            if node.get("sublabel"):
                draw_text(d, node["sublabel"], px(x + 0.2), px(y + 0.95), nw - 0.4, 10, self.c["muted"],
                          align="center", spacing=1.1)
            if i < n - 1:
                ax = px(x + nw + 0.08)
                ay = px(y + nh / 2)
                aw = px(gap - 0.16)
                d.polygon([(ax, ay - px(0.14)), (ax + aw * 0.7, ay - px(0.14)), (ax + aw * 0.7, ay - px(0.25)),
                           (ax + aw, ay), (ax + aw * 0.7, ay + px(0.25)), (ax + aw * 0.7, ay + px(0.14)),
                           (ax, ay + px(0.14))], fill=self.c["accent"])
        if spec.get("caption"):
            draw_text(d, spec["caption"], px(0.6), px(y + nh + 0.5), W_IN - 1.2, 12, self.c["muted"])
        self.footer(d, page)
        return img

    def _bar_like_chart(self, spec, page, kind):
        img, d = self.canvas()
        self.title_bar(d, spec["title"])
        cats = spec["categories"]
        values = spec["series"]["values"] if "series" in spec else spec["values"]
        max_v = max(values) if values else 1
        max_v = max_v or 1
        x0, y0, y1 = px(1.0), px(1.9), px(6.2)
        area_w = W_IN - 2.0
        n = len(cats)
        if kind == "bar":
            gap = 0.3
            bw = (area_w - gap * (n - 1)) / n
            for i, (cat, v) in enumerate(zip(cats, values)):
                bh = (y1 - y0) * (v / max_v)
                x = x0 + px(i * (bw + gap))
                d.rectangle([x, y1 - bh, x + px(bw), y1], fill=self.c["primary"])
                draw_text(d, str(v), x, y1 - bh - px(0.35), bw, 12, self.c["ink"], align="center")
                draw_text(d, str(cat), x, y1 + px(0.1), bw, 11, self.c["muted"], align="center")
        else:  # line
            step = area_w / max(n - 1, 1)
            points = []
            for i, v in enumerate(values):
                x = x0 + px(i * step)
                yv = y1 - (y1 - y0) * (v / max_v)
                points.append((x, yv))
            if len(points) > 1:
                d.line(points, fill=self.c["primary"], width=4)
            for (x, yv), cat in zip(points, cats):
                r = px(0.07)
                d.ellipse([x - r, yv - r, x + r, yv + r], fill=self.c["accent"])
                draw_text(d, str(cat), x - px(0.5), y1 + px(0.1), 1.0, 11, self.c["muted"], align="center")
        self.source_line(d, spec.get("source"))
        self.footer(d, page)
        return img

    def r_bar_chart(self, spec, page):
        return self._bar_like_chart(spec, page, "bar")

    def r_line_chart(self, spec, page):
        return self._bar_like_chart(spec, page, "line")

    def r_pie_chart(self, spec, page):
        img, d = self.canvas()
        self.title_bar(d, spec["title"])
        cats = spec["categories"]
        values = spec["values"]
        total = sum(values) or 1
        cx, cy, r = px(W_IN / 2), px(4.2), px(2.0)
        colors = [self.c["primary"], self.c["accent"], self.c["muted"], self.c["base_soft"], self.c["primary_dark"]]
        start = -90.0
        for i, v in enumerate(values):
            sweep = 360.0 * v / total
            d.pieslice([cx - r, cy - r, cx + r, cy + r], start, start + sweep, fill=colors[i % len(colors)])
            start += sweep
        legend_y = px(6.6)
        lx = px(1.0)
        for i, (cat, v) in enumerate(zip(cats, values)):
            box = px(0.15)
            d.rectangle([lx, legend_y, lx + box, legend_y + box], fill=colors[i % len(colors)])
            label = f"{cat}({v})"
            draw_text(d, label, lx + box + px(0.1), legend_y - px(0.03), 2.0, 11, self.c["ink"])
            lx += px(2.4)
        self.source_line(d, spec.get("source"))
        self.footer(d, page)
        return img


def render_deck(spec_path: str, out_dir: str) -> int:
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    meta = spec.get("meta", {})
    slides = spec["slides"]
    renderer = Renderer(meta)
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    for i, sl in enumerate(slides, start=1):
        img = renderer.render(sl, i)
        img.save(str(Path(out_dir) / f"slide_{i:03d}.png"))
    print(f"生成完了: {out_dir}({len(slides)}枚)")
    return 0


def self_test() -> int:
    """フォント・パレット読み込みと、代表的なレイアウト数種の描画がエラーなく行えるかを確認する。"""
    ok = True
    meta = {"palette_preset": "navy_gold", "footer": "test"}
    renderer = Renderer(meta)
    samples = [
        {"layout": "title", "heading": "テスト見出し", "sub": "サブ", "note": ""},
        {"layout": "bullets", "title": "テスト", "bullets": ["項目1", "項目2"], "note": ""},
        {"layout": "cards", "title": "テスト", "cards": [{"label": "A", "text": "本文"}], "note": ""},
        {"layout": "big_stat", "title": "テスト", "stat": "123", "note": ""},
        {"layout": "diagram", "title": "テスト", "nodes": [{"label": "A"}, {"label": "B"}], "note": ""},
    ]
    for i, sample in enumerate(samples, start=1):
        try:
            img = renderer.render(sample, i)
            if img.size != (W, H):
                print(f"SELF-TEST FAIL: 画像サイズが期待と異なります({img.size})")
                ok = False
        except Exception as e:  # noqa: BLE001
            print(f"SELF-TEST FAIL: レイアウト{sample['layout']}の描画で例外: {e}")
            ok = False
    print("SELF-TEST PASSED" if ok else "SELF-TEST FAILED")
    return 0 if ok else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="deck_spec.json から各スライドのPNG画像を描画する")
    parser.add_argument("spec", nargs="?", help="deck_spec.json")
    parser.add_argument("out_dir", nargs="?", help="出力ディレクトリ")
    parser.add_argument("--self-test", action="store_true", help="代表的なレイアウトの描画のみ確認する")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    if not args.spec or not args.out_dir:
        parser.error("spec と out_dir を指定するか、--self-test を指定してください")

    return render_deck(args.spec, args.out_dir)


if __name__ == "__main__":
    sys.exit(main())
