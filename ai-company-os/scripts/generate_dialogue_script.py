#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""generate_dialogue_script.py — 起承転結×AIペルソナ2人の対話ナレーション原稿を生成する

`templates/dialogue_script_template.md` の仕様に沿った JSON(dialogue_spec.json)を
入力にして、2人のAIペルソナが時事ニュースを掛け合いで解説する読み上げ原稿(Markdown)を
書き出す。research.md で調査済みの事実を、起(導入)→承(展開)→転(転換)→結(結論)の
4幕構成に割り付けて使うことを想定している。

使い方:
  python scripts/generate_dialogue_script.py spec.json script.md
  python scripts/generate_dialogue_script.py --self-test

検証項目(ビルド時にエラーとして拒否):
  - meta.personas が2人以上定義されている
  - acts が「起」「承」「転」「結」の4幕をこの順序で含む
  - 各 line の speaker が meta.personas に定義された persona id である
  - 各 line の text が空でない
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHARS_PER_MINUTE = 350  # 日本語読み上げ速度の目安(export_script.py と同じ)
REQUIRED_ACTS = ["起", "承", "転", "結"]
ACT_JP_LABEL = {"起": "起(導入)", "承": "承(展開)", "転": "転(転換)", "結": "結(結論)"}


def validate_spec(spec: dict) -> list[str]:
    """仕様を検証し、問題点のリストを返す(空リスト=合格)。"""
    errors: list[str] = []

    meta = spec.get("meta", {})
    personas = meta.get("personas", [])
    if len(personas) < 2:
        errors.append("meta.personas は2人以上のAIペルソナを定義してください")
    persona_ids = {p.get("id") for p in personas if isinstance(p, dict)}

    acts = spec.get("acts", [])
    act_sequence = [a.get("act") for a in acts if isinstance(a, dict)]
    if act_sequence != REQUIRED_ACTS:
        errors.append(
            f"acts は「起・承・転・結」の順で4幕すべて必要です(現在: {act_sequence})"
        )

    for i, act in enumerate(acts, start=1):
        lines = act.get("lines", [])
        if not lines:
            errors.append(f"幕 {i}({act.get('act', '?')}) に lines がありません")
        for j, line in enumerate(lines, start=1):
            speaker = line.get("speaker")
            text = str(line.get("text", "")).strip()
            if speaker not in persona_ids:
                errors.append(
                    f"幕 {i} の {j} 行目: speaker '{speaker}' は meta.personas に未定義です"
                )
            if not text:
                errors.append(f"幕 {i} の {j} 行目: text が空です")

    return errors


def estimate_minutes(text: str) -> float:
    return len(text) / CHARS_PER_MINUTE


def build_script(spec_path: str, out_path: str) -> int:
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))

    errors = validate_spec(spec)
    if errors:
        print(f"ERROR: dialogue_spec の検証に失敗しました ({len(errors)} 件)")
        for e in errors:
            print(f"  - {e}")
        return 1

    meta = spec["meta"]
    personas = {p["id"]: p for p in meta["personas"]}
    title = meta.get("title", Path(spec_path).stem)

    lines_out = [f"# {title} — AI対話ナレーション原稿(起承転結)\n"]
    lines_out.append(
        "<!-- generate_dialogue_script.py により dialogue_spec.json から自動生成 -->\n"
    )

    lines_out.append("## 登場AIペルソナ\n")
    for p in meta["personas"]:
        lines_out.append(f"- **{p['name']}**: {p.get('role', '')}")
    lines_out.append("")

    total_minutes = 0.0
    for act in spec["acts"]:
        act_key = act["act"]
        label = act.get("label", "")
        act_minutes = 0.0
        act_body: list[str] = []
        for line in act["lines"]:
            persona = personas[line["speaker"]]
            text = str(line["text"]).strip()
            act_minutes += estimate_minutes(text)
            source_note = f"(出典: {line['source']})" if line.get("source") else ""
            act_body.append(f"**{persona['name']}**: {text} {source_note}".rstrip())
        total_minutes += act_minutes

        lines_out.append(f"## {ACT_JP_LABEL[act_key]}{f' — {label}' if label else ''}")
        lines_out.append(f"*目安 {act_minutes:.1f}分*\n")
        lines_out.extend(act_body)
        lines_out.append("")

    if meta.get("sources"):
        lines_out.append("## 出典一覧\n")
        for src in meta["sources"]:
            lines_out.append(f"- {src}")
        lines_out.append("")

    lines_out.insert(
        2,
        f"**合計目安時間: 約{total_minutes:.0f}分**"
        f"({len(spec['acts'])}幕、{CHARS_PER_MINUTE}字/分換算)\n",
    )

    Path(out_path).write_text("\n".join(lines_out), encoding="utf-8")
    print(f"生成完了: {out_path} (4幕、目安 約{total_minutes:.0f}分)")
    return 0


def self_test() -> int:
    """合格すべき仕様と不合格すべき仕様を検証し、判定が正しいことを確認する。"""
    good = {
        "meta": {
            "title": "セルフテスト用テーマ",
            "personas": [
                {"id": "host", "name": "ホストAI", "role": "進行役"},
                {"id": "analyst", "name": "アナリストAI", "role": "解説役"},
            ],
            "sources": ["https://example.com"],
        },
        "acts": [
            {"act": "起", "label": "導入", "lines": [{"speaker": "host", "text": "今日はこのテーマです。"}]},
            {"act": "承", "label": "展開", "lines": [{"speaker": "analyst", "text": "詳しく見ると…", "source": "https://example.com"}]},
            {"act": "転", "label": "転換", "lines": [{"speaker": "host", "text": "でも実はこういう見方も。"}]},
            {"act": "結", "label": "結論", "lines": [{"speaker": "analyst", "text": "まとめるとこうです。"}]},
        ],
    }
    bad = {
        "meta": {"title": "不合格ケース", "personas": [{"id": "host", "name": "ホストAI", "role": "進行役"}]},
        "acts": [
            {"act": "起", "label": "導入", "lines": [{"speaker": "unknown", "text": ""}]},
            {"act": "転", "label": "転換", "lines": [{"speaker": "host", "text": "順序がおかしい"}]},
        ],
    }

    ok = True
    good_errors = validate_spec(good)
    if good_errors:
        print(f"SELF-TEST FAIL: 合格すべき仕様でエラー検出: {good_errors}")
        ok = False

    bad_errors = validate_spec(bad)
    expected = ["personas は2人以上", "起・承・転・結", "未定義", "text が空"]
    for key in expected:
        if not any(key in e for e in bad_errors):
            print(f"SELF-TEST FAIL: 不合格仕様で '{key}' が検出されませんでした: {bad_errors}")
            ok = False

    print("SELF-TEST PASSED" if ok else "SELF-TEST FAILED")
    return 0 if ok else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="起承転結×AIペルソナ2人の対話ナレーション原稿を生成する")
    parser.add_argument("spec", nargs="?", help="dialogue_spec.json")
    parser.add_argument("out", nargs="?", help="出力する Markdown ファイル")
    parser.add_argument("--self-test", action="store_true", help="検証ロジック自体を確認する")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    if not args.spec or not args.out:
        parser.error("spec と out を指定するか、--self-test を指定してください")
    if not Path(args.spec).is_file():
        print(f"ERROR: 仕様ファイルが存在しません: {args.spec}")
        return 2

    return build_script(args.spec, args.out)


if __name__ == "__main__":
    sys.exit(main())
