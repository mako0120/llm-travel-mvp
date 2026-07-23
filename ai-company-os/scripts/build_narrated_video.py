#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_narrated_video.py — deck_spec.json + dialogue_audio.wav + slide_timings.json から
   ナレーション動画(.mp4)を組み立てる。

**なぜPowerPointの「自動再生+自動スライド送り」ではなく動画(mp4)にするのか**:
python-pptxのadd_movie()は実験的機能であり、スライド進入時の自動再生・スライドの
自動送りを安定して設定する方法は無い(手動でp:timingを追加するとファイルが破損する
既知の不具合がある: https://github.com/scanny/python-pptx/issues/954 )。そのため、
スライド画像+音声を結合した動画ファイルという、どの環境でも確実に「音声に合わせて
スライドが動く」体験を再現できる形式を採用する。

**なぜpptx→pdf変換ではなくdeck_spec.jsonから直接描画するのか**:
このセッションのLibreOfficeはコア部分のみが入っており、Impress等の実際の文書処理
モジュールが無いため`--convert-to pdf`はどんな文書に対しても失敗する(apt経由の
追加インストールはegressポリシーでブロックされ不可)。そのため、build_deck.pyが
pptxを組み立てるのと同じdeck_spec.jsonを入力に、render_deck_images.pyでスライド画像を
直接描画する。

前提:
  - Pillow(pip install pillow、render_deck_images.py が使用)
  - imageio-ffmpeg(pip install imageio-ffmpeg)が使えること(静的ffmpegバイナリを同梱)

使い方:
  # 事前に synthesize_dialogue_audio.py --slide-timings で slide_timings.json を生成しておく
  python scripts/build_narrated_video.py deck_spec.json dialogue_audio.wav slide_timings.json out.mp4
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from render_deck_images import render_deck  # noqa: E402

MIN_SLIDE_SECONDS = 1.0  # 極端に短いスライドがあった場合の最低表示時間


def find_ffmpeg() -> str:
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def deck_spec_to_images(spec_path: str, out_dir: str) -> list[str]:
    render_deck(spec_path, out_dir)
    n = len(json.loads(Path(spec_path).read_text(encoding="utf-8"))["slides"])
    return [str(Path(out_dir) / f"slide_{i:03d}.png") for i in range(1, n + 1)]


def wav_duration_seconds(wav_path: str) -> float:
    with wave.open(wav_path, "rb") as w:
        return w.getnframes() / w.getframerate()


def build_concat_file(image_paths: list[str], durations: list[float], out_path: str) -> None:
    lines = []
    for img, dur in zip(image_paths, durations):
        lines.append(f"file '{img}'")
        lines.append(f"duration {max(dur, MIN_SLIDE_SECONDS):.3f}")
    # ffmpeg concat demuxerの仕様上、最後のdurationは無視されるため、最後の画像をもう一度書く
    lines.append(f"file '{image_paths[-1]}'")
    Path(out_path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def build(spec_path: str, audio_path: str, timings_path: str, out_path: str) -> int:
    if not Path(spec_path).is_file():
        print(f"ERROR: deck_spec.jsonが見つかりません: {spec_path}")
        return 2
    if not Path(audio_path).is_file():
        print(f"ERROR: 音声ファイルが見つかりません: {audio_path}")
        return 2
    if not Path(timings_path).is_file():
        print(f"ERROR: slide_timings.jsonが見つかりません: {timings_path}")
        return 2

    manifest = json.loads(Path(timings_path).read_text(encoding="utf-8"))
    if not manifest:
        print("ERROR: slide_timings.jsonが空です(スライド連動モードで生成されたものを指定してください)")
        return 1

    with tempfile.TemporaryDirectory() as tmp:
        print("① deck_spec.json → スライド画像 描画中...")
        image_paths = deck_spec_to_images(spec_path, tmp)

        n_slides_deck = len(image_paths)
        n_slides_manifest = len(manifest)
        if n_slides_deck != n_slides_manifest:
            print(f"ERROR: デッキのスライド数({n_slides_deck})とslide_timings.jsonのスライド数"
                  f"({n_slides_manifest})が一致しません")
            return 1

        durations = [entry["duration_sec"] for entry in manifest]

        print("② 音声の長さとタイミング合計の整合性を確認中...")
        audio_dur = wav_duration_seconds(audio_path)
        timings_total = sum(durations)
        if abs(audio_dur - timings_total) > 1.0:
            print(f"WARNING: 音声の長さ({audio_dur:.1f}秒)とタイミング合計"
                  f"({timings_total:.1f}秒)が1秒以上ずれています。同じ生成結果から"
                  "作られたファイルか確認してください。")

        print("③ 動画を組み立て中(ffmpeg)...")
        concat_path = str(Path(tmp) / "concat.txt")
        build_concat_file(image_paths, durations, concat_path)

        ffmpeg = find_ffmpeg()
        cmd = [
            ffmpeg, "-y",
            "-f", "concat", "-safe", "0", "-i", concat_path,
            "-i", audio_path,
            "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-r", "30",
            "-c:a", "aac", "-b:a", "192k",
            "-shortest",
            out_path,
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print("ERROR: ffmpegの実行に失敗しました")
            print(result.stderr[-3000:])
            return 1

    print(f"生成完了: {out_path}({n_slides_deck}スライド、音声{audio_dur:.1f}秒)")
    return 0


def self_test() -> int:
    """外部コマンド(soffice/ffmpeg)を使わずに検証できるロジックのみ確認する。"""
    ok = True

    with tempfile.TemporaryDirectory() as tmp:
        concat_path = str(Path(tmp) / "concat.txt")
        build_concat_file(["a.png", "b.png"], [1.5, 2.25], concat_path)
        content = Path(concat_path).read_text(encoding="utf-8")
        expected = "file 'a.png'\nduration 1.500\nfile 'b.png'\nduration 2.250\nfile 'b.png'\n"
        if content != expected:
            print(f"SELF-TEST FAIL: build_concat_fileの出力が期待と異なります:\n{content!r}\n期待:\n{expected!r}")
            ok = False

    print("SELF-TEST PASSED" if ok else "SELF-TEST FAILED")
    return 0 if ok else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="deck_spec.json + 音声 + slide_timings.json からナレーション動画を作る")
    parser.add_argument("spec", nargs="?", help="deck_spec.json")
    parser.add_argument("audio", nargs="?", help="dialogue_audio.wav")
    parser.add_argument("timings", nargs="?", help="slide_timings.json")
    parser.add_argument("out", nargs="?", help="出力する .mp4 ファイル")
    parser.add_argument("--self-test", action="store_true", help="外部コマンドなしで検証できるロジックのみ確認する")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    if not all([args.spec, args.audio, args.timings, args.out]):
        parser.error("spec, audio, timings, out をすべて指定するか、--self-test を指定してください")

    return build(args.spec, args.audio, args.timings, args.out)


if __name__ == "__main__":
    sys.exit(main())
