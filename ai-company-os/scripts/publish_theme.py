#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""publish_theme.py — 制作済みテーマをWebサイト(/works)に公開できる状態にする

新しいテーマを作るたびに手作業で「動画を組み立てて、public/へ置いて、カタログを
作り直す」のを繰り返さないための1コマンド。CI(synthesize-dialogue-audio.yml)から
音声合成の直後に呼ばれ、新テーマが自動でサイトへ載るようにする。

やること:
  ① ナレーション動画(deck_narrated.mp4)が無ければ組み立てる
  ② public/videos/<テーマID>.mp4 へ配置する(Webから配信するのはこの1本)
  ③ lib/ai-company-os/catalog.json を作り直す

使い方:
  python scripts/publish_theme.py <テーマディレクトリ名>   # 1テーマを公開
  python scripts/publish_theme.py --all                    # 公開できる全テーマを処理
  python scripts/publish_theme.py --self-test              # ロジックのみ確認

音声(dialogue_audio.wav)と slide_timings.json が揃っていないテーマは動画を作れない。
その場合はスキップし、理由を出力する(勝手に空の動画を作ったりはしない)。
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parents[1]
ASSETS_DIR = REPO_ROOT / "ai-company-os" / "assets"
PUBLIC_VIDEO_DIR = REPO_ROOT / "public" / "videos"
CATALOG_PATH = REPO_ROOT / "lib" / "ai-company-os" / "catalog.json"

VIDEO_NAME = "deck_narrated.mp4"
REQUIRED_FOR_VIDEO = ("deck_spec.json", "dialogue_audio.wav", "slide_timings.json")


def missing_inputs(theme_dir: Path) -> list[str]:
    return [name for name in REQUIRED_FOR_VIDEO if not (theme_dir / name).is_file()]


def build_video(theme_dir: Path) -> bool:
    """動画が無ければ組み立てる。作成した/既にあるなら True、作れないなら False。"""
    out = theme_dir / VIDEO_NAME
    if out.is_file():
        return True

    lacking = missing_inputs(theme_dir)
    if lacking:
        print(f"  スキップ(動画を作れない): {', '.join(lacking)} が無い")
        return False

    print("  動画を組み立て中...")
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPTS_DIR / "build_narrated_video.py"),
            str(theme_dir / "deck_spec.json"),
            str(theme_dir / "dialogue_audio.wav"),
            str(theme_dir / "slide_timings.json"),
            str(out),
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"  動画の組み立てに失敗しました:\n{result.stdout[-800:]}{result.stderr[-800:]}")
        return False
    return out.is_file()


def publish_video(theme_dir: Path) -> bool:
    """assets 側の動画を public/videos へ複製する。内容が同じならコピーしない。"""
    src = theme_dir / VIDEO_NAME
    if not src.is_file():
        return False
    PUBLIC_VIDEO_DIR.mkdir(parents=True, exist_ok=True)
    dst = PUBLIC_VIDEO_DIR / f"{theme_dir.name}.mp4"
    if dst.is_file() and dst.stat().st_size == src.stat().st_size:
        return True
    shutil.copy2(src, dst)
    try:  # 実際に書いた場所を出す(self-test では一時ディレクトリになる)
        shown = dst.relative_to(REPO_ROOT)
    except ValueError:
        shown = dst
    print(f"  公開: {shown}({dst.stat().st_size / 1024 / 1024:.1f}MB)")
    return True


def rebuild_catalog() -> bool:
    builder = SCRIPTS_DIR / "build_catalog.py"
    if not builder.is_file():
        print("build_catalog.py が無いためカタログ更新をスキップしました")
        return False
    result = subprocess.run(
        [sys.executable, str(builder)], capture_output=True, text=True
    )
    print(result.stdout.strip() or result.stderr.strip())
    return result.returncode == 0


def publish(theme_names: list[str], strict: bool = False) -> int:
    """strict=True なら、名指ししたテーマを公開できなかった時に異常終了する。

    CIから1テーマを指定して呼ぶ場合、公開に失敗しているのにジョブが緑になると
    「動画が無いまま成功した」ことに気付けない。--all の一括処理では音声待ちの
    テーマが混ざるのが正常なので、そちらは失敗扱いにしない。
    """
    if not ASSETS_DIR.is_dir():
        print(f"ERROR: assets ディレクトリが見つかりません: {ASSETS_DIR}")
        return 2

    published = 0
    for name in theme_names:
        theme_dir = ASSETS_DIR / name
        if not theme_dir.is_dir():
            print(f"{name}: ディレクトリが存在しません")
            continue
        print(f"{name}:")
        if build_video(theme_dir) and publish_video(theme_dir):
            published += 1

    rebuild_catalog()
    print(f"公開できたテーマ: {published} / {len(theme_names)}")
    if strict and published < len(theme_names):
        print("ERROR: 指定したテーマを公開できませんでした")
        return 1
    return 0


def self_test() -> int:
    """入力の過不足判定と、公開処理の冪等性を確認する。"""
    import tempfile

    ok = True

    def check(cond: bool, msg: str):
        nonlocal ok
        if not cond:
            print(f"SELF-TEST FAIL: {msg}")
            ok = False

    with tempfile.TemporaryDirectory() as tmp:
        # 揃っているテーマ / 音声だけ足りないテーマ
        full = Path(tmp) / "2026-01-02_full"
        full.mkdir()
        for n in REQUIRED_FOR_VIDEO:
            (full / n).write_text("{}", encoding="utf-8")
        check(missing_inputs(full) == [], f"揃っているのに不足と判定: {missing_inputs(full)}")

        partial = Path(tmp) / "2026-01-01_partial"
        partial.mkdir()
        (partial / "deck_spec.json").write_text("{}", encoding="utf-8")
        lacking = missing_inputs(partial)
        check("dialogue_audio.wav" in lacking, "不足している音声を検出できていない")
        check("slide_timings.json" in lacking, "不足しているタイミングを検出できていない")
        check("deck_spec.json" not in lacking, "存在するファイルを不足と誤判定")

        # 動画が既にあるテーマは組み立てをスキップする(再エンコードしない)
        (full / VIDEO_NAME).write_bytes(b"video")
        check(build_video(full) is True, "既存動画があるのに False を返した")

        # publish_video が公開先へコピーし、2回目はコピーし直さないこと
        global PUBLIC_VIDEO_DIR
        original = PUBLIC_VIDEO_DIR
        try:
            PUBLIC_VIDEO_DIR = Path(tmp) / "public_videos"
            check(publish_video(full) is True, "公開に失敗した")
            dst = PUBLIC_VIDEO_DIR / "2026-01-02_full.mp4"
            check(dst.is_file(), "公開先に動画が置かれていない")
            first = dst.stat().st_mtime_ns
            check(publish_video(full) is True, "2回目の公開に失敗した")
            check(dst.stat().st_mtime_ns == first, "同じ動画を毎回コピーし直している(冪等でない)")
            # 動画が無いテーマは公開されない
            check(publish_video(partial) is False, "動画が無いのに公開したと報告した")
        finally:
            PUBLIC_VIDEO_DIR = original

        # 公開できなかった時に終了コードで分かること(CIが緑のまま素通りしないこと)
        global ASSETS_DIR, rebuild_catalog
        orig_assets, orig_rebuild = ASSETS_DIR, rebuild_catalog
        try:
            ASSETS_DIR = Path(tmp)
            rebuild_catalog = lambda: True  # noqa: E731  カタログ生成は別スクリプトで検証済み
            check(publish(["2026-01-01_partial"], strict=True) == 1,
                  "名指ししたテーマを公開できないのに正常終了した")
            check(publish(["2026-01-01_partial"], strict=False) == 0,
                  "--all 相当の一括処理で音声待ちテーマを失敗扱いにしている")
            check(publish(["存在しないテーマ"], strict=True) == 1,
                  "存在しないテーマ名を指定したのに正常終了した")
        finally:
            ASSETS_DIR, rebuild_catalog = orig_assets, orig_rebuild

    print("SELF-TEST PASSED" if ok else "SELF-TEST FAILED")
    return 0 if ok else 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="制作済みテーマをWebサイト(/works)へ公開できる状態にする"
    )
    parser.add_argument("theme", nargs="?", help="assets/ 配下のテーマディレクトリ名")
    parser.add_argument("--all", action="store_true", help="公開できる全テーマを処理する")
    parser.add_argument("--self-test", action="store_true", help="ロジックのみ確認する")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    if args.all:
        names = sorted(d.name for d in ASSETS_DIR.iterdir() if d.is_dir())
    elif args.theme:
        names = [args.theme]
    else:
        parser.error("テーマ名を指定するか、--all / --self-test を指定してください")

    return publish(names, strict=bool(args.theme) and not args.all)


if __name__ == "__main__":
    sys.exit(main())
