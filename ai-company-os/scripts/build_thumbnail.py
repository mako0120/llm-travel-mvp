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
import textwrap
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


def _fit_headline(draw, text, max_width, max_lines=2, start_size=150, min_size=64, stroke_width=6):
    """複数行に折り返しつつ、指定の幅に収まる最大のフォントサイズを探す。"""
    for size in range(start_size, min_size - 1, -4):
        f = font(size)
        avg_char_w = _text_size(draw, "国", f, stroke_width)[0] or 1
        wrap_chars = max(1, int(max_width / avg_char_w))
        lines = textwrap.wrap(text, width=wrap_chars) or [text]
        if len(lines) > max_lines:
            continue
        widths = [_text_size(draw, ln, f, stroke_width)[0] for ln in lines]
        if max(widths) <= max_width:
            return f, lines, size
    f = font(min_size)
    lines = textwrap.wrap(text, width=max(1, len(text) // max_lines + 1)) or [text]
    return f, lines[:max_lines], min_size


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


def build_thumbnail(spec: dict, out_path: str):
    pal = palette(spec.get("palette_preset", "navy_gold"))
    img = Image.new("RGB", (W, H), pal["primary_dark"])
    draw = ImageDraw.Draw(img)

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

    # 抽象アイコン(右上、ロゴではなく「つながり」を示す図形のみ)
    draw_accent_icon(draw, W - 110, 110, 56, pal["base_soft"])

    # 数字バッジ(任意、左上に角丸ボックスで表示)
    stat = spec.get("stat_badge")
    if stat:
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
    stat_offset = 150 if stat else 60
    f, lines, size = _fit_headline(draw, hook, max_w, max_lines=2, stroke_width=8)
    line_h = int(size * 1.18)
    total_h = line_h * len(lines)
    y0 = max(stat_offset, (H - band_h - total_h) // 2 + 20)
    for i, ln in enumerate(lines):
        lw, lh = _text_size(draw, ln, f, stroke_width=8)
        x = (W - lw) // 2
        y = y0 + i * line_h
        draw.text((x, y), ln, font=f, fill=pal["base"],
                   stroke_width=8, stroke_fill=pal["primary_dark"])

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
    print("SELF-TEST PASSED:", out)


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
