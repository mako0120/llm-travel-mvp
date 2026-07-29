#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""list_pending_audio_themes.py — 音声合成待ちのテーマを列挙する

「新しいテーマを作ったら随時サイトに追加される」自動化のために、CI
(synthesize-dialogue-audio.yml)が push トリガーで自動的に対象テーマを
見つけられるようにする。dialogue_spec.json はあるが dialogue_audio.wav が
無いテーマを「音声合成待ち」として1行1テーマ名で標準出力へ書き出す。

push イベントの before/after 差分に頼らない(git履歴の状態に左右されず、
force-push・squash・CI自身のコミットが混ざっても同じ結果になるため)。
CI自身が作るのは dialogue_audio.wav 等であって dialogue_spec.json では
ないので、この判定方法なら「音声を作った直後にまた自分を呼ぶ」という
無限ループも起きない。

使い方:
  python scripts/list_pending_audio_themes.py              # 1行1テーマ名
  python scripts/list_pending_audio_themes.py --self-test   # ロジックのみ確認
"""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parents[1]
ASSETS_DIR = REPO_ROOT / "ai-company-os" / "assets"

SPEC_NAME = "dialogue_spec.json"
AUDIO_NAME = "dialogue_audio.wav"


def pending_themes(assets_dir: Path) -> list[str]:
    if not assets_dir.is_dir():
        return []
    names = []
    for d in sorted(assets_dir.iterdir()):
        if not d.is_dir():
            continue
        if (d / SPEC_NAME).is_file() and not (d / AUDIO_NAME).is_file():
            names.append(d.name)
    return names


def self_test() -> int:
    import tempfile

    ok = True

    def check(cond: bool, msg: str):
        nonlocal ok
        if not cond:
            print(f"SELF-TEST FAIL: {msg}")
            ok = False

    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)

        ready = base / "2026-01-03_ready"
        ready.mkdir()
        (ready / SPEC_NAME).write_text("{}", encoding="utf-8")
        # dialogue_audio.wav なし → 対象

        done = base / "2026-01-02_done"
        done.mkdir()
        (done / SPEC_NAME).write_text("{}", encoding="utf-8")
        (done / AUDIO_NAME).write_bytes(b"wav")
        # 音声あり → 対象外

        no_spec = base / "2026-01-01_no-dialogue"
        no_spec.mkdir()
        (no_spec / "deck_spec.json").write_text("{}", encoding="utf-8")
        # dialogue_spec.json 自体が無い → 対象外

        result = pending_themes(base)
        check(result == ["2026-01-03_ready"], f"想定と異なる結果: {result}")

        # 空ディレクトリなら空リスト
        empty = base / "empty_root"
        empty.mkdir()
        check(pending_themes(empty) == [], "空ディレクトリで空リストにならない")

        # 存在しないパスでも例外を出さない
        check(pending_themes(base / "does-not-exist") == [], "存在しないパスで例外または誤検出")

    print("SELF-TEST PASSED" if ok else "SELF-TEST FAILED")
    return 0 if ok else 1


def main() -> int:
    if "--self-test" in sys.argv:
        return self_test()

    for name in pending_themes(ASSETS_DIR):
        print(name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
