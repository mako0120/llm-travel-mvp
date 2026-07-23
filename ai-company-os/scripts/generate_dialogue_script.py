#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""generate_dialogue_script.py — 起承転結×AIペルソナ2人の対話ナレーション原稿を生成する

`templates/dialogue_script_template.md` の仕様に沿った JSON(dialogue_spec.json)を
入力にして、2人のAIペルソナが時事ニュースを掛け合いで解説する読み上げ原稿(Markdown)を
書き出す。research.md で調査済みの事実を、起(導入)→承(展開)→転(転換)→結(結論)の
4幕構成に割り付けて使うことを想定している。

## 2つのモード

- **フラットモード**(従来): 各幕に `lines`(発言のリスト)を直接書く。短いハイライト向け。
- **スライド連動モード**(2026-07-23〜): 各幕に `slides`(スライド単位のセグメント)を書き、
  各セグメントが `deck_spec.json` の特定のスライド番号に対応する。これにより、
  PowerPoint(.pptx)の全スライドを漏れなく解説する対話原稿を作れる。
  `--deck deck_spec.json` を指定すると、スライド数の一致・見出しの自動取得・
  スライド番号の連番検証(1件も抜け漏れなく1..Nを解説しているか)まで行う。
  1幕でも `slides` を使う場合、仕様全体がスライド連動モードとして扱われ、
  全幕が `slides` 形式である必要がある。

使い方:
  python scripts/generate_dialogue_script.py spec.json script.md
  python scripts/generate_dialogue_script.py spec.json script.md --deck deck_spec.json
  python scripts/generate_dialogue_script.py --self-test

検証項目(ビルド時にエラーとして拒否):
  - meta.personas が2人以上定義されている
  - acts が「起」「承」「転」「結」の4幕をこの順序で含む
  - 各 line の speaker が meta.personas に定義された persona id である
  - 各 line の text が空でない
  - (スライド連動モード) 全幕を通じたスライド番号が 1..N の連番で、抜け・重複・逆順がない
  - (スライド連動モード、--deck指定時) N が deck_spec.json のスライド数と一致する
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHARS_PER_MINUTE = 350  # 日本語読み上げ速度の目安(export_script.py と同じ)
REQUIRED_ACTS = ["起", "承", "転", "結"]
ACT_JP_LABEL = {"起": "起(導入)", "承": "承(展開)", "転": "転(転換)", "結": "結(結論)"}


def slide_heading(sl: dict) -> str:
    """deck_spec.json の1スライド分の仕様から、表示用の見出しを取り出す(export_script.py と同じ規則)。"""
    if sl.get("layout") in ("title", "cta"):
        return str(sl.get("heading", "")).replace("\n", " ")
    if sl.get("layout") == "quote":
        q = sl.get("quote", "")
        return f"引用: {q[:24]}{'…' if len(q) > 24 else ''}"
    return sl.get("title", "(無題)")


def is_slide_linked(spec: dict) -> bool:
    acts = spec.get("acts", [])
    return any(isinstance(a, dict) and "slides" in a for a in acts)


def _validate_line(line, where: str, persona_ids: set, errors: list[str]) -> None:
    speaker = line.get("speaker") if isinstance(line, dict) else None
    text = str(line.get("text", "")).strip() if isinstance(line, dict) else ""
    if speaker not in persona_ids:
        errors.append(f"{where}: speaker '{speaker}' は meta.personas に未定義です")
    if not text:
        errors.append(f"{where}: text が空です")


def validate_spec(spec: dict, deck: dict | None = None) -> list[str]:
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

    slide_linked = is_slide_linked(spec)

    if slide_linked:
        seen_slides: list[int] = []
        for i, act in enumerate(acts, start=1):
            segments = act.get("slides")
            if not segments:
                errors.append(
                    f"幕 {i}({act.get('act', '?')}): スライド連動モードでは全幕に slides が必要です"
                )
                continue
            for seg in segments:
                slide_no = seg.get("slide")
                if not isinstance(slide_no, int):
                    errors.append(f"幕 {i}: slides 内の slide 番号が整数ではありません({slide_no})")
                else:
                    seen_slides.append(slide_no)
                lines = seg.get("lines", [])
                if not lines:
                    errors.append(f"幕 {i} スライド{slide_no}: lines がありません")
                for j, line in enumerate(lines, start=1):
                    _validate_line(line, f"幕 {i} スライド{slide_no} の {j} 行目", persona_ids, errors)

        if seen_slides:
            expected = list(range(1, len(seen_slides) + 1))
            if seen_slides != expected:
                errors.append(
                    "スライド番号が1から始まる連番になっていません"
                    f"(抜け・重複・逆順の可能性): 検出順={seen_slides}"
                )
            if deck is not None:
                n_deck = len(deck.get("slides", []))
                if len(seen_slides) != n_deck:
                    errors.append(
                        f"対話原稿がカバーするスライド数({len(seen_slides)})と "
                        f"deck_spec.json のスライド数({n_deck})が一致しません"
                    )
    else:
        for i, act in enumerate(acts, start=1):
            lines = act.get("lines", [])
            if not lines:
                errors.append(f"幕 {i}({act.get('act', '?')}) に lines がありません")
            for j, line in enumerate(lines, start=1):
                _validate_line(line, f"幕 {i} の {j} 行目", persona_ids, errors)

    return errors


def estimate_minutes(text: str) -> float:
    return len(text) / CHARS_PER_MINUTE


def _render_line(personas: dict, line: dict) -> str:
    persona = personas[line["speaker"]]
    text = str(line["text"]).strip()
    source_note = f"(出典: {line['source']})" if line.get("source") else ""
    return f"**{persona['name']}**: {text} {source_note}".rstrip()


def build_script(spec_path: str, out_path: str, deck_path: str | None = None) -> int:
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    deck = json.loads(Path(deck_path).read_text(encoding="utf-8")) if deck_path else None

    errors = validate_spec(spec, deck=deck)
    if errors:
        print(f"ERROR: dialogue_spec の検証に失敗しました ({len(errors)} 件)")
        for e in errors:
            print(f"  - {e}")
        return 1

    meta = spec["meta"]
    personas = {p["id"]: p for p in meta["personas"]}
    title = meta.get("title", Path(spec_path).stem)
    slide_linked = is_slide_linked(spec)
    deck_slides = deck.get("slides", []) if deck else []

    lines_out = [f"# {title} — AI対話ナレーション原稿(起承転結)\n"]
    tag = "スライド連動モード" if slide_linked else "フラットモード"
    lines_out.append(
        f"<!-- generate_dialogue_script.py により dialogue_spec.json から自動生成({tag}) -->\n"
    )

    lines_out.append("## 登場AIペルソナ\n")
    for p in meta["personas"]:
        lines_out.append(f"- **{p['name']}**: {p.get('role', '')}")
    lines_out.append("")

    total_minutes = 0.0
    total_units = 0
    for act in spec["acts"]:
        act_key = act["act"]
        label = act.get("label", "")
        act_minutes = 0.0
        act_body: list[str] = []

        if slide_linked:
            for seg in act["slides"]:
                slide_no = seg["slide"]
                if deck_slides and 1 <= slide_no <= len(deck_slides):
                    heading = slide_heading(deck_slides[slide_no - 1])
                else:
                    heading = seg.get("slide_title", "")
                act_body.append(f"### ▶ スライド{slide_no}{f': {heading}' if heading else ''}")
                for line in seg["lines"]:
                    act_body.append(_render_line(personas, line))
                    act_minutes += estimate_minutes(str(line["text"]))
                act_body.append("")
                total_units += 1
        else:
            for line in act["lines"]:
                act_body.append(_render_line(personas, line))
                act_minutes += estimate_minutes(str(line["text"]))
            total_units += 1

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

    unit_label = f"{total_units}スライド" if slide_linked else f"{len(spec['acts'])}幕"
    lines_out.insert(
        2,
        f"**合計目安時間: 約{total_minutes:.0f}分**"
        f"({unit_label}、{CHARS_PER_MINUTE}字/分換算)\n",
    )

    Path(out_path).write_text("\n".join(lines_out), encoding="utf-8")
    print(f"生成完了: {out_path} ({tag}、{unit_label}、目安 約{total_minutes:.0f}分)")
    return 0


def self_test() -> int:
    """合格すべき仕様と不合格すべき仕様を検証し、判定が正しいことを確認する。"""
    personas = [
        {"id": "host", "name": "ホストAI", "role": "進行役"},
        {"id": "analyst", "name": "アナリストAI", "role": "解説役"},
    ]

    # フラットモード
    good_flat = {
        "meta": {"title": "セルフテスト用テーマ(フラット)", "personas": personas, "sources": ["https://example.com"]},
        "acts": [
            {"act": "起", "label": "導入", "lines": [{"speaker": "host", "text": "今日はこのテーマです。"}]},
            {"act": "承", "label": "展開", "lines": [{"speaker": "analyst", "text": "詳しく見ると…", "source": "https://example.com"}]},
            {"act": "転", "label": "転換", "lines": [{"speaker": "host", "text": "でも実はこういう見方も。"}]},
            {"act": "結", "label": "結論", "lines": [{"speaker": "analyst", "text": "まとめるとこうです。"}]},
        ],
    }
    bad_flat = {
        "meta": {"title": "不合格ケース", "personas": [personas[0]]},
        "acts": [
            {"act": "起", "label": "導入", "lines": [{"speaker": "unknown", "text": ""}]},
            {"act": "転", "label": "転換", "lines": [{"speaker": "host", "text": "順序がおかしい"}]},
        ],
    }

    # スライド連動モード
    good_linked = {
        "meta": {"title": "セルフテスト用テーマ(スライド連動)", "personas": personas, "sources": ["https://example.com"]},
        "acts": [
            {"act": "起", "label": "導入", "slides": [
                {"slide": 1, "lines": [{"speaker": "host", "text": "表紙です。"}]},
            ]},
            {"act": "承", "label": "展開", "slides": [
                {"slide": 2, "lines": [{"speaker": "analyst", "text": "詳細1", "source": "https://example.com"}]},
                {"slide": 3, "lines": [{"speaker": "analyst", "text": "詳細2"}]},
            ]},
            {"act": "転", "label": "転換", "slides": [
                {"slide": 4, "lines": [{"speaker": "host", "text": "別の見方も。"}]},
            ]},
            {"act": "結", "label": "結論", "slides": [
                {"slide": 5, "lines": [{"speaker": "analyst", "text": "まとめ。"}]},
            ]},
        ],
    }
    bad_linked_gap = {
        "meta": {"title": "不合格ケース(欠番)", "personas": personas},
        "acts": [
            {"act": "起", "label": "導入", "slides": [{"slide": 1, "lines": [{"speaker": "host", "text": "a"}]}]},
            {"act": "承", "label": "展開", "slides": [{"slide": 3, "lines": [{"speaker": "host", "text": "b"}]}]},
            {"act": "転", "label": "転換", "slides": [{"slide": 4, "lines": [{"speaker": "host", "text": "c"}]}]},
            {"act": "結", "label": "結論", "slides": []},
        ],
    }

    ok = True

    if validate_spec(good_flat):
        print(f"SELF-TEST FAIL: 合格すべき仕様(フラット)でエラー検出: {validate_spec(good_flat)}")
        ok = False
    bad_flat_errors = validate_spec(bad_flat)
    for key in ["personas は2人以上", "起・承・転・結", "未定義", "text が空"]:
        if not any(key in e for e in bad_flat_errors):
            print(f"SELF-TEST FAIL: 不合格仕様(フラット)で '{key}' が検出されませんでした: {bad_flat_errors}")
            ok = False

    if validate_spec(good_linked):
        print(f"SELF-TEST FAIL: 合格すべき仕様(スライド連動)でエラー検出: {validate_spec(good_linked)}")
        ok = False
    # deck との整合性チェック(5スライド想定 vs 実際4スライドのdeckでずれを検出できるか)
    fake_deck = {"slides": [{"layout": "bullets", "title": f"s{i}"} for i in range(1, 5)]}
    mismatch_errors = validate_spec(good_linked, deck=fake_deck)
    if not any("スライド数" in e for e in mismatch_errors):
        print(f"SELF-TEST FAIL: deckとのスライド数不一致が検出されませんでした: {mismatch_errors}")
        ok = False

    bad_linked_errors = validate_spec(bad_linked_gap)
    if not any("連番になっていません" in e for e in bad_linked_errors):
        print(f"SELF-TEST FAIL: スライド欠番が検出されませんでした: {bad_linked_errors}")
        ok = False

    print("SELF-TEST PASSED" if ok else "SELF-TEST FAILED")
    return 0 if ok else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="起承転結×AIペルソナ2人の対話ナレーション原稿を生成する")
    parser.add_argument("spec", nargs="?", help="dialogue_spec.json")
    parser.add_argument("out", nargs="?", help="出力する Markdown ファイル")
    parser.add_argument("--deck", help="deck_spec.json(スライド連動モードの整合性検証・見出し自動取得に使用)")
    parser.add_argument("--self-test", action="store_true", help="検証ロジック自体を確認する")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    if not args.spec or not args.out:
        parser.error("spec と out を指定するか、--self-test を指定してください")
    if not Path(args.spec).is_file():
        print(f"ERROR: 仕様ファイルが存在しません: {args.spec}")
        return 2
    if args.deck and not Path(args.deck).is_file():
        print(f"ERROR: deck_spec.json が存在しません: {args.deck}")
        return 2

    return build_script(args.spec, args.out, deck_path=args.deck)


if __name__ == "__main__":
    sys.exit(main())
