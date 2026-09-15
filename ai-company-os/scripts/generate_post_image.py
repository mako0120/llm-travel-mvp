#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""generate_post_image.py — SNS投稿用画像(1080x1920px)をオリジナルデザインで生成する

実写画像を一切使わず、テーマカラーのグラデーション+見出しテキスト+⚡ハイライトチップ
+要約テキストだけで構成する完全オリジナルの投稿画像を、Pillowで直接描画する。
`docs/01_Core_Rules.md`の著作権ルール(実写画像は許可された出典に限る)に一切触れない
(実写画像そのものを使わない)ため、このスクリプトで作る画像は常に問題なく使える。

デザインはfeed.html(見出しフィード)の drawCardToCanvas() と同じレイアウト比率
(上余白22%:グラデーション帯36%:要約欄42%)を踏襲しているが、あちらは「ユーザーが
自分の写真をアップロードした場合」の代替として使うのに対し、本スクリプトは最初から
写真を使わない前提で、常にこのグラデーション版を生成する。

使い方:
  python scripts/generate_post_image.py <テーマディレクトリ名または任意のslug> \
      --heading "見出しテキスト" --chip "⚡ハイライト" --sub "出典情報" \
      --summary "要約テキスト" --primary "#RRGGBB" --dark "#RRGGBB" --accent "#RRGGBB" \
      --out output.png
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
MARGIN_H = round(H * 0.22)
PHOTO_AREA_H = round(H * 0.36)
PHOTO_TOP = MARGIN_H
PHOTO_BOTTOM = MARGIN_H + PHOTO_AREA_H

FONT_PATH = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"


def _font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_PATH, size)


def _hex(c: str) -> tuple[int, int, int]:
    c = c.lstrip("#")
    return tuple(int(c[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def _wrap(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_width: int, max_lines: int = 0) -> list[str]:
    text = (text or "").replace("\n", " ")
    lines: list[str] = []
    line = ""
    for ch in text:
        test = line + ch
        if line and draw.textlength(test, font=font) > max_width:
            lines.append(line)
            line = ch
        else:
            line = test
    if line:
        lines.append(line)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
        last = lines[-1]
        while len(last) > 1 and draw.textlength(last + "…", font=font) > max_width:
            last = last[:-1]
        lines[-1] = last + "…"
    return lines


def _vertical_gradient(size: tuple[int, int], top: tuple[int, int, int], bottom: tuple[int, int, int]) -> Image.Image:
    w, h = size
    base = Image.new("RGB", (1, h), 0)
    for y in range(h):
        t = y / max(1, h - 1)
        rgb = tuple(round(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        base.putpixel((0, y), rgb)
    return base.resize((w, h))


def render_post_image(
    heading: str,
    chip_big: str,
    chip_label: str,
    sub: str,
    summary: str,
    primary: str,
    dark: str,
    accent: str,
    out_path: str,
) -> None:
    img = Image.new("RGB", (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # 写真エリア(グラデーション、実写画像は使わない)
    grad = _vertical_gradient((W, PHOTO_AREA_H), _hex(primary), _hex(dark))
    img.paste(grad, (0, PHOTO_TOP))

    # 下端スクリム(見出しテキストの可読性確保、写真エリア下45%のみ暗くする)
    scrim = Image.new("RGBA", (W, PHOTO_AREA_H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(scrim)
    scrim_start = round(PHOTO_AREA_H * 0.55)
    for y in range(scrim_start, PHOTO_AREA_H):
        t = (y - scrim_start) / max(1, PHOTO_AREA_H - scrim_start)
        sd.line([(0, y), (W, y)], fill=(0, 0, 0, round(140 * t)))
    img.paste(scrim, (0, PHOTO_TOP), scrim)

    draw = ImageDraw.Draw(img)

    # ハイライトチップ(上余白の下端、写真エリアのすぐ上)。絵文字フォント非依存のため
    # 「⚡」文字は使わず、小さな稲妻ポリゴンを自前で描画する
    chip_font = _font(28)
    chip_text = f"{chip_big}  {chip_label}"
    chip_lines = _wrap(draw, chip_text, chip_font, W - 160, 1)
    chip_str = chip_lines[0] if chip_lines else chip_text
    cw = draw.textlength(chip_str, font=chip_font)
    chip_h = 60
    chip_y = PHOTO_TOP - chip_h - 24
    chip_w = cw + 84
    draw.rounded_rectangle([40, chip_y, 40 + chip_w, chip_y + chip_h], radius=chip_h // 2, fill=_hex("#f1e4cd"))
    bolt_cx, bolt_cy = 40 + 30, chip_y + chip_h // 2
    draw.polygon(
        [
            (bolt_cx + 4, bolt_cy - 16), (bolt_cx - 6, bolt_cy + 2), (bolt_cx + 1, bolt_cy + 2),
            (bolt_cx - 4, bolt_cy + 16), (bolt_cx + 7, bolt_cy - 3), (bolt_cx, bolt_cy - 3),
        ],
        fill=_hex(accent),
    )
    draw.text((78, chip_y + 15), chip_str, font=chip_font, fill=(26, 26, 26))

    # 見出しテキスト(写真エリア左下、白抜き太字)
    heading_font = _font(58)
    heading_lines = _wrap(draw, heading, heading_font, W - 80, 2)
    line_h = 68
    heading_bottom_y = PHOTO_BOTTOM - 32
    for i, line in enumerate(heading_lines):
        y = heading_bottom_y - (len(heading_lines) - 1 - i) * line_h - line_h
        draw.text((40, y), line, font=heading_font, fill=(255, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0))

    # 下部(白背景): 出典 + 要約
    cy = PHOTO_BOTTOM + 50
    sub_font = _font(30)
    sub_lines = _wrap(draw, sub, sub_font, W - 80, 2)
    for i, line in enumerate(sub_lines):
        draw.text((40, cy + i * 42), line, font=sub_font, fill=_hex(accent))
    cy += len(sub_lines) * 42 + 22

    summary_font = _font(30)
    right_gap = round(W / 8)
    summary_lines = _wrap(draw, summary, summary_font, W - 40 - right_gap, 0)
    for i, line in enumerate(summary_lines):
        draw.text((40, cy + i * 44), line, font=summary_font, fill=(20, 20, 19))
    cy += len(summary_lines) * 44 + 48

    # 下端: 要約の直後からキャンバス最下端まで、アクセントカラーの帯で埋める
    # (要約が短くても余白を持て余さないよう、帯の開始位置を可変にする)
    footer_top = min(cy, H - 220)
    draw.rectangle([0, footer_top, W, H], fill=_hex(primary))
    tagline_font = _font(28)
    tagline = "有益なAI活用法だけを、出典付きでお届けします"
    tw = draw.textlength(tagline, font=tagline_font)
    draw.text(((W - tw) / 2, footer_top + 56), tagline, font=tagline_font, fill=(255, 255, 255))
    credit_font = _font(34)
    credit_text = "AI研究家ミライ  ｜  AI Company OS"
    cwid = draw.textlength(credit_text, font=credit_font)
    draw.text(((W - cwid) / 2, H - 96), credit_text, font=credit_font, fill=(255, 255, 255))

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, "PNG")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("theme", help="出力ファイル名のベース(テーマslug)")
    p.add_argument("--heading", required=True)
    p.add_argument("--chip", required=True, help="⚡チップの太字部分")
    p.add_argument("--chip-label", default="")
    p.add_argument("--sub", default="")
    p.add_argument("--summary", default="")
    p.add_argument("--primary", default="#1E2761")
    p.add_argument("--dark", default="#141B47")
    p.add_argument("--accent", default="#D9A441")
    p.add_argument("--out", required=True)
    args = p.parse_args()

    render_post_image(
        heading=args.heading,
        chip_big=args.chip,
        chip_label=args.chip_label,
        sub=args.sub,
        summary=args.summary,
        primary=args.primary,
        dark=args.dark,
        accent=args.accent,
        out_path=args.out,
    )
    print(f"生成完了: {args.out} ({W}x{H}px)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
