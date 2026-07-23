#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""synthesize_dialogue_audio.py — dialogue_spec.json をVOICEVOX Engineで音声化する

**オーナー自身のマシンで、VOICEVOX Engine(https://voicevox.hiroshiba.jp/ )を
起動した状態で実行することを前提とする。** Claude Codeのリモートセッションは
Docker Hub/GitHub releasesへのアクセスがegressポリシーでブロックされており、
VOICEVOX Engine自体をこのセッション内でセルフホストすることはできない
(詳細: research/2026-07-23_tts-options.md)。

前提:
  1. https://voicevox.hiroshiba.jp/ からVOICEVOXをインストールして起動するか、
     VOICEVOX ENGINE単体(https://github.com/VOICEVOX/voicevox_engine )を起動する
  2. デフォルトで http://127.0.0.1:50021 でエンジンが待ち受ける

使い方:
  # まずどんな話者(speaker id)が使えるか確認する
  python scripts/synthesize_dialogue_audio.py --list-speakers

  # dialogue_spec.json を音声化する(host=ずんだもん, analyst=四国めたん が既定)
  python scripts/synthesize_dialogue_audio.py dialogue_spec.json output.wav

  # 話者を指定する場合
  python scripts/synthesize_dialogue_audio.py dialogue_spec.json output.wav \\
    --voice-map host=3,analyst=2

  # エンジンが別ホスト/ポートの場合
  python scripts/synthesize_dialogue_audio.py dialogue_spec.json output.wav \\
    --engine-url http://127.0.0.1:50021

既定の話者ID(VOICEVOXの一般的な配布物での代表的なノーマルスタイル。環境により
IDが異なる場合があるため、必ず --list-speakers で確認すること):
  host    = 3 (ずんだもん・ノーマル)
  analyst = 2 (四国めたん・ノーマル)
"""

from __future__ import annotations

import argparse
import json
import sys
import wave
from pathlib import Path
from urllib import error, request

DEFAULT_ENGINE_URL = "http://127.0.0.1:50021"
DEFAULT_VOICE_MAP = {"host": 3, "analyst": 2}
SILENCE_MS_BETWEEN_LINES = 300


def _post(url: str, params: dict | None = None, json_body: dict | None = None, timeout: int = 30) -> bytes:
    if params:
        qs = "&".join(f"{k}={v}" for k, v in params.items())
        url = f"{url}?{qs}"
    data = json.dumps(json_body).encode("utf-8") if json_body is not None else b""
    req = request.Request(url, data=data, method="POST",
                           headers={"Content-Type": "application/json"})
    with request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _get(url: str, timeout: int = 10) -> bytes:
    with request.urlopen(url, timeout=timeout) as resp:
        return resp.read()


def check_engine(engine_url: str) -> bool:
    try:
        _get(f"{engine_url}/version", timeout=5)
        return True
    except (error.URLError, TimeoutError, ConnectionError):
        return False


def list_speakers(engine_url: str) -> int:
    if not check_engine(engine_url):
        print(f"ERROR: VOICEVOX Engineに接続できません({engine_url})。")
        print("VOICEVOX(https://voicevox.hiroshiba.jp/)を起動してから再実行してください。")
        return 2
    speakers = json.loads(_get(f"{engine_url}/speakers"))
    for sp in speakers:
        print(f"# {sp['name']}")
        for style in sp.get("styles", []):
            print(f"  id={style['id']:<4} style={style['name']}")
    return 0


def synth_line(engine_url: str, text: str, speaker_id: int) -> bytes:
    query = json.loads(_post(f"{engine_url}/audio_query", params={"text": text, "speaker": speaker_id}))
    return _post(f"{engine_url}/synthesis", params={"speaker": speaker_id}, json_body=query)


def iter_lines(spec: dict):
    """dialogue_spec.json からspeaker/textの順序付きリストを取り出す(フラット/スライド連動 両対応)。"""
    for act in spec["acts"]:
        if "slides" in act:
            for seg in act["slides"]:
                for line in seg["lines"]:
                    yield line["speaker"], str(line["text"])
        else:
            for line in act["lines"]:
                yield line["speaker"], str(line["text"])


def concat_wavs(wav_bytes_list: list[bytes], out_path: str, silence_ms: int) -> None:
    import io

    frames = []
    params = None
    for wb in wav_bytes_list:
        with wave.open(io.BytesIO(wb), "rb") as wf:
            if params is None:
                params = wf.getparams()
            frames.append(wf.readframes(wf.getnframes()))
            if silence_ms > 0:
                n_silence_frames = int(params.framerate * silence_ms / 1000)
                frames.append(b"\x00" * n_silence_frames * params.sampwidth * params.nchannels)

    with wave.open(out_path, "wb") as out:
        out.setparams(params)
        for f in frames:
            out.writeframes(f)


def parse_voice_map(s: str | None) -> dict:
    if not s:
        return dict(DEFAULT_VOICE_MAP)
    mapping = dict(DEFAULT_VOICE_MAP)
    for pair in s.split(","):
        k, v = pair.split("=")
        mapping[k.strip()] = int(v.strip())
    return mapping


def build(spec_path: str, out_path: str, engine_url: str, voice_map: dict) -> int:
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))

    if not check_engine(engine_url):
        print(f"ERROR: VOICEVOX Engineに接続できません({engine_url})。")
        print("VOICEVOX(https://voicevox.hiroshiba.jp/)を起動してから再実行してください。")
        print("詳細: ai-company-os/research/2026-07-23_tts-options.md")
        return 2

    lines = list(iter_lines(spec))
    if not lines:
        print("ERROR: dialogue_spec.json に発言がありません")
        return 1

    unknown_speakers = {speaker for speaker, _ in lines if speaker not in voice_map}
    if unknown_speakers:
        print(f"ERROR: --voice-map に定義されていない speaker があります: {unknown_speakers}")
        print("例: --voice-map host=3,analyst=2")
        return 1

    wav_chunks: list[bytes] = []
    for i, (speaker, text) in enumerate(lines, start=1):
        print(f"  [{i}/{len(lines)}] {speaker}: {text[:30]}{'…' if len(text) > 30 else ''}")
        wav_chunks.append(synth_line(engine_url, text, voice_map[speaker]))

    concat_wavs(wav_chunks, out_path, SILENCE_MS_BETWEEN_LINES)
    print(f"生成完了: {out_path}({len(lines)}発言)")
    return 0


def self_test() -> int:
    """VOICEVOX Engineを使わずに検証できるロジック(WAV結合・仕様パース)を確認する。"""
    import io
    import struct
    import tempfile

    ok = True

    # parse_voice_map
    if parse_voice_map(None) != DEFAULT_VOICE_MAP:
        print("SELF-TEST FAIL: 既定のvoice-mapが期待と異なります")
        ok = False
    if parse_voice_map("host=5,analyst=7") != {"host": 5, "analyst": 7}:
        print("SELF-TEST FAIL: --voice-map の解析が正しくありません")
        ok = False

    # iter_lines(フラットモード・スライド連動モード両方)
    flat_spec = {"acts": [
        {"act": "起", "lines": [{"speaker": "host", "text": "a"}]},
        {"act": "結", "lines": [{"speaker": "analyst", "text": "b"}]},
    ]}
    if list(iter_lines(flat_spec)) != [("host", "a"), ("analyst", "b")]:
        print("SELF-TEST FAIL: iter_lines(フラットモード)が正しくありません")
        ok = False

    linked_spec = {"acts": [
        {"act": "起", "slides": [{"slide": 1, "lines": [{"speaker": "host", "text": "c"}]}]},
        {"act": "結", "slides": [{"slide": 2, "lines": [{"speaker": "analyst", "text": "d"}]}]},
    ]}
    if list(iter_lines(linked_spec)) != [("host", "c"), ("analyst", "d")]:
        print("SELF-TEST FAIL: iter_lines(スライド連動モード)が正しくありません")
        ok = False

    # concat_wavs: 3つの無音チャンクを結合し、長さが期待通りか確認
    def make_silence_wav(seconds: float, rate: int = 24000) -> bytes:
        n = int(rate * seconds)
        buf = io.BytesIO()
        with wave.open(buf, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(rate)
            w.writeframes(struct.pack(f"<{n}h", *([0] * n)))
        return buf.getvalue()

    with tempfile.TemporaryDirectory() as tmp:
        out_path = str(Path(tmp) / "out.wav")
        chunks = [make_silence_wav(0.1), make_silence_wav(0.1), make_silence_wav(0.1)]
        concat_wavs(chunks, out_path, silence_ms=100)
        with wave.open(out_path, "rb") as w:
            duration = w.getnframes() / w.getframerate()
        expected = 0.1 * 3 + 0.1 * 3  # 音声3つ + 各行の後の無音3つ
        if abs(duration - expected) > 0.01:
            print(f"SELF-TEST FAIL: concat_wavsの出力長が期待と異なります(期待 {expected}秒, 実際 {duration}秒)")
            ok = False

    print("SELF-TEST PASSED" if ok else "SELF-TEST FAILED")
    return 0 if ok else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="dialogue_spec.json をVOICEVOX Engineで音声化する")
    parser.add_argument("spec", nargs="?", help="dialogue_spec.json")
    parser.add_argument("out", nargs="?", help="出力する .wav ファイル")
    parser.add_argument("--engine-url", default=DEFAULT_ENGINE_URL, help=f"VOICEVOX EngineのURL(既定: {DEFAULT_ENGINE_URL})")
    parser.add_argument("--voice-map", help="例: host=3,analyst=2 (省略時は既定値を使用)")
    parser.add_argument("--list-speakers", action="store_true", help="利用可能な話者一覧を表示する")
    parser.add_argument("--self-test", action="store_true", help="VOICEVOX Engineなしで検証できるロジックのみ確認する")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    if args.list_speakers:
        return list_speakers(args.engine_url)

    if not args.spec or not args.out:
        parser.error("spec と out を指定するか、--list-speakers を指定してください")
    if not Path(args.spec).is_file():
        print(f"ERROR: 仕様ファイルが存在しません: {args.spec}")
        return 2

    return build(args.spec, args.out, args.engine_url, parse_voice_map(args.voice_map))


if __name__ == "__main__":
    sys.exit(main())
