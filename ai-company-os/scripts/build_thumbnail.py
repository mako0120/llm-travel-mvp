#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_thumbnail.py — YouTubeサムネイル(1280x720 PNG)をPillowで生成する。

設計方針(出典: `ai-company-os/research/2026-07-24_youtube-thumbnail-best-practices.md`):
- 1メッセージ・1秒で理解できる構成(フック文言は1つ、最大2行)
- 実在人物の写真は使わない(`AGENTS.md`の肖像リスク回避方針)ため、表情ではなく
  太字タイポグラフィ + 高コントラスト配色 + 抽象図形アイコンで注目を引く
- 背景と文字は補色関係に近い高コントラスト配色にし、文字には縁取り(stroke)を
  付けて可読性を確保する(168x94pxに縮小しても判読できることを目安にする)
- `build_deck.py`の PALETTE_PRESETS を共有し、デッキ本体と配色の一貫性を保つ

使い方:
  python scripts/build_thumbnail.py spec.json out.png
  spec.json の形式は self_test() のサンプルを参照。
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

W, H = 1280, 720

FONT_CANDIDATES = [
    "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf",
    "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/noto/NotoSansCJKjp-Regular.otf",
]

FONT_PATH = None
_FONT_CACHE: dict[int, "ImageFont.FreeTypeFont"] = {}


def _find_font_path() -> str:
    for p in FONT_CANDIDATES:
        if Path(p).is_file():
            return p
    raise FileNotFoundError(
        "日本語フォントが見つかりません。候補: " + ", ".join(FONT_CANDIDATES)
    )


def font(size_pt: int):
    global FONT_PATH
    if FONT_PATH is None:
        FONT_PATH = _find_font_path()
    if size_pt not in _FONT_CACHE:
        _FONT_CACHE[size_pt] = ImageFont.truetype(FONT_PATH, size_pt)
    return _FONT_CACHE[size_pt]


def hex_to_rgb(hexstr: str) -> tuple[int, int, int]:
    hexstr = hexstr.lstrip("#")
    return (int(hexstr[0:2], 16), int(hexstr[2:4], 16), int(hexstr[4:6], 16))


def palette(preset_name: str) -> dict:
    preset = PALETTE_PRESETS.get(preset_name, DEFAULT_PALETTE)
    return {k: hex_to_rgb(v) for k, v in preset.items()}


def _text_size(draw, text, f, stroke_width=0):
    bbox = draw.textbbox((0, 0), text, font=f, stroke_width=stroke_width)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def _fit_headline(draw, text, max_width, max_lines=2, start_size=150, min_size=48, stroke_width=6):
    """1行に収まる最大サイズを探し、収まらなければ文字数で均等に2分割する。
    (textwrap.wrap は空白のない日本語を左詰めで機械的に割るため、「発表」のような
    単語がまたがって不格好に割れることがあった。文字数の均等2分割に変更している)"""
    for size in range(start_size, min_size - 1, -4):
        f = font(size)
        w, _h = _text_size(draw, text, f, stroke_width)
        if w <= max_width:
            return f, [text], size

    if max_lines >= 2 and len(text) >= 2:
        split = (len(text) + 1) // 2
        two_lines = [text[:split], text[split:]]
        for size in range(start_size, min_size - 1, -4):
            f = font(size)
            widths = [_text_size(draw, ln, f, stroke_width)[0] for ln in two_lines]
            if max(widths) <= max_width:
                return f, two_lines, size
        f = font(min_size)
        return f, two_lines, min_size

    f = font(min_size)
    return f, [text], min_size


def rounded_rect(draw, xy, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def draw_accent_icon(draw, cx, cy, r, color):
    """ロゴ・実在の意匠を使わない、抽象的な「つながり」アイコン(円+線)を描く。"""
    import math
    pts = []
    for i in range(4):
        ang = math.radians(90 * i - 45)
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            draw.line([pts[i], pts[j]], fill=color, width=3)
    for (px, py) in pts:
        rad = r * 0.16
        draw.ellipse([px - rad, py - rad, px + rad, py + rad], fill=color)


def draw_burst(draw, cx, cy, r_in, r_out, color, n=16):
    """顔の代わりに視線を集める、漫画的な「衝撃線」(放射状バースト)を描く。
    実在の人物・表情の代わりに、抽象図形だけで視覚的なインパクトを出す。"""
    import math
    for i in range(n):
        a0 = math.radians(360 / n * i)
        a1 = math.radians(360 / n * (i + 0.5))
        p0 = (cx + r_in * math.cos(a0), cy + r_in * math.sin(a0))
        p1 = (cx + r_out * math.cos(a1), cy + r_out * math.sin(a1))
        p2 = (cx + r_in * math.cos(a0 + math.radians(360 / n)), cy + r_in * math.sin(a0 + math.radians(360 / n)))
        draw.polygon([p0, p1, p2], fill=color)


def draw_ribbon(draw, text, f, pal, corner="top-left"):
    """参考にした高インパクト系サムネイルの「斜め帯バナー」を再現する。
    誇張・未確認情報ではなく、事実の要約のみを短く載せる想定。"""
    band_img = Image.new("RGBA", (620, 90), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(band_img)
    bdraw.rectangle([0, 15, 620, 75], fill=(*pal["accent"], 255))
    tw, th = _text_size(bdraw, text, f, stroke_width=2)
    bdraw.text(((620 - tw) // 2, 15 + (60 - th) // 2 - 4), text, font=f,
                fill=pal["primary_dark"], stroke_width=2, stroke_fill=pal["accent"])
    rotated = band_img.rotate(-14, expand=True, resample=Image.BICUBIC)
    return rotated


def build_thumbnail(spec: dict, out_path: str):
    style = spec.get("style", "standard")  # "standard" or "impact"
    pal = palette(spec.get("palette_preset", "navy_gold"))
    img = Image.new("RGB", (W, H), pal["primary_dark"])
    draw = ImageDraw.Draw(img)

    if style == "impact":
        # インパクト重視レイアウト(参考: 赤×黄の高コントラスト・放射状バースト・
        # 斜め帯バナー)。出典: ai-company-os/research/2026-07-24_youtube-thumbnail-best-practices.md
        draw_burst(draw, W * 0.5, H * 0.42, 90, 900, pal["primary"], n=20)
        draw.ellipse([W * 0.5 - 260, H * 0.42 - 260, W * 0.5 + 260, H * 0.42 + 260], fill=pal["primary"])
    else:
        # 背景: 斜めの2トーン分割(単色より視覚的な奥行きを出しつつ、要素は増やさない)
        draw.polygon([(0, 0), (W, 0), (W, H * 0.55), (0, H)], fill=pal["primary"])

    # 下部の帯(カテゴリタグ + フッター、細く控えめに)
    band_h = 74
    draw.rectangle([0, H - band_h, W, H], fill=pal["accent"])
    tag = spec.get("tag", "")
    footer = spec.get("footer", "AI Company OS")
    tag_font = font(34)
    draw.text((36, H - band_h + 18), tag, font=tag_font, fill=pal["primary_dark"])
    footer_font = font(24)
    fw, _ = _text_size(draw, footer, footer_font)
    draw.text((W - fw - 36, H - band_h + 24), footer, font=footer_font, fill=pal["primary_dark"])

    if style != "impact":
        # 抽象アイコン(右上、ロゴではなく「つながり」を示す図形のみ)
        draw_accent_icon(draw, W - 110, 110, 56, pal["base_soft"])

    # 斜め帯バナー(任意、事実の短い要約のみ。誇張・未確認の煽り文句は使わない)
    ribbon_text = spec.get("ribbon")
    if ribbon_text:
        ribbon_img = draw_ribbon(draw, ribbon_text, font(30), pal)
        img.paste(ribbon_img, (-40, -10), ribbon_img)

    # 数字バッジ(任意、左上に角丸ボックスで表示。ribbonと併用しない)
    stat = spec.get("stat_badge")
    if stat and not ribbon_text:
        badge_font = font(56)
        bw, bh = _text_size(draw, stat, badge_font, stroke_width=3)
        pad_x, pad_y = 34, 22
        box = [40, 40, 40 + bw + pad_x * 2, 40 + bh + pad_y * 2]
        rounded_rect(draw, box, radius=18, fill=pal["accent"])
        draw.text((box[0] + pad_x, box[1] + pad_y - 6), stat, font=badge_font,
                   fill=pal["primary_dark"], stroke_width=3, stroke_fill=pal["accent"])

    # メインフック(最大2行、太字相当はstroke_widthで表現)
    hook = spec["hook"]
    max_w = W - 100
    top_offset = 230 if ribbon_text else (190 if stat else 60)
    stroke_w = 12 if style == "impact" else 8
    f, lines, size = _fit_headline(draw, hook, max_w, max_lines=2, stroke_width=stroke_w,
                                    start_size=170 if style == "impact" else 150)
    line_h = int(size * 1.18)
    total_h = line_h * len(lines)
    y0 = max(top_offset, (H - band_h - total_h) // 2 + 20)
    text_fill = pal["base"] if style != "impact" else pal["base"]
    for i, ln in enumerate(lines):
        lw, lh = _text_size(draw, ln, f, stroke_width=stroke_w)
        x = (W - lw) // 2
        y = y0 + i * line_h
        if style == "impact":
            # ドロップシャドウ(斜め下にもう一枚描いて奥行きを出す)
            draw.text((x + 6, y + 8), ln, font=f, fill=pal["primary_dark"],
                       stroke_width=stroke_w, stroke_fill=pal["primary_dark"])
        draw.text((x, y), ln, font=f, fill=text_fill,
                   stroke_width=stroke_w, stroke_fill=pal["primary_dark"])

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, "PNG")
    return out_path


def self_test():
    sample = {
        "palette_preset": "navy_gold",
        "hook": "1日違いで発表",
        "stat_badge": "$2→$30",
        "tag": "AI/テック",
        "footer": "AI Company OS",
    }
    out = "/tmp/thumbnail_self_test.png"
    build_thumbnail(sample, out)
    img = Image.open(out)
    assert img.size == (W, H), f"unexpected size: {img.size}"
    # 168x94縮小時にファイルとして開けること(可読性の最終確認は目視だが、破損がないかは検証する)
    img.resize((168, 94)).save("/tmp/thumbnail_self_test_small.png")

    sample_impact = {
        "palette_preset": "impact_red",
        "style": "impact",
        "hook": "1日違いで発表",
        "ribbon": "海外2社が同週発表",
        "tag": "AI/テック",
        "footer": "AI Company OS",
    }
    out2 = "/tmp/thumbnail_self_test_impact.png"
    build_thumbnail(sample_impact, out2)
    img2 = Image.open(out2)
    assert img2.size == (W, H), f"unexpected size: {img2.size}"
    img2.resize((168, 94)).save("/tmp/thumbnail_self_test_impact_small.png")
    print("SELF-TEST PASSED:", out, out2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec", nargs="?", help="サムネイル仕様のJSONファイル")
    ap.add_argument("out", nargs="?", help="出力するPNGファイルパス")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        self_test()
        return

    if not args.spec or not args.out:
        ap.error("spec と out を指定するか、--self-test を使ってください")

    spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    out = build_thumbnail(spec, args.out)
    print("生成完了:", out)


if __name__ == "__main__":
    main()
