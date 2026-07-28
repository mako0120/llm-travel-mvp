#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_chatgpt_review.py — ChatGPT Work のレビュー記録(JSON)を検証する

docs/15_PPT_Handoff.md の二段階品質ゲートで、ChatGPT Work が返した
chatgpt_review.json が仕様どおりかを機械的に検査する。

ChatGPT の出力は自由記述のため、項目名の揺れ・未定義の分類・存在しない
スライド番号が混入しうる。それを Claude Code が読み込む前に検出し、
壊れたレビュー記録のまま deck_spec.json を書き換えてしまう事故を防ぐ。

使い方:
  python scripts/verify_chatgpt_review.py <chatgpt_review.json>
  python scripts/verify_chatgpt_review.py <chatgpt_review.json> --deck <deck_spec.json>
  python scripts/verify_chatgpt_review.py --self-test

--deck を指定すると、slide_number が実際のデッキのスライド数の範囲内かも検査する。

検査項目:
  1. JSON として解釈できる
  2. 必須の最上位キーが揃っている
  3. overall_verdict が approved / needs_revision / rejected のいずれか
  4. 各 slides 要素に slide_number(1以上の整数)と issues がある
  5. slide_number が重複していない
  6. (--deck 指定時)slide_number がデッキのスライド数を超えていない
  7. 各 issue の category が定義された5分類のいずれか
  8. 各 issue の severity が critical / minor のいずれか
  9. description と suggested_fix が空でない

エラーは1件目で止めず、全件をまとめて報告する(修正の往復を減らすため)。
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# docs/15_PPT_Handoff.md で定義した確認必須項目。
# export_review_request.py の CHECK_ITEMS と一致させること。
CATEGORIES = {"story", "visibility", "speaker_notes", "sources", "overlap_or_cutoff"}
SEVERITIES = {"critical", "minor"}
VERDICTS = {"approved", "needs_revision", "rejected"}
REQUIRED_TOP_KEYS = ["theme_slug", "reviewed_pptx", "reviewer", "review_date", "overall_verdict", "slides"]


def validate(review: dict, deck_slide_count: int | None = None) -> list[str]:
    """レビュー記録を検証し、エラーメッセージの一覧を返す(空なら合格)。"""
    errors: list[str] = []

    if not isinstance(review, dict):
        return ["最上位が JSON オブジェクトではありません"]

    for key in REQUIRED_TOP_KEYS:
        if key not in review:
            errors.append(f"必須キー '{key}' がありません")

    verdict = review.get("overall_verdict")
    if verdict is not None and verdict not in VERDICTS:
        errors.append(
            f"overall_verdict が不正です: '{verdict}'(許可されるのは {sorted(VERDICTS)})"
        )

    slides = review.get("slides")
    if slides is None:
        return errors
    if not isinstance(slides, list):
        errors.append("slides が配列ではありません")
        return errors

    seen_numbers: set[int] = set()
    for idx, entry in enumerate(slides):
        where = f"slides[{idx}]"
        if not isinstance(entry, dict):
            errors.append(f"{where} がオブジェクトではありません")
            continue

        number = entry.get("slide_number")
        if number is None:
            errors.append(f"{where}: slide_number がありません")
        elif not isinstance(number, int) or isinstance(number, bool):
            errors.append(f"{where}: slide_number が整数ではありません: {number!r}")
        elif number < 1:
            errors.append(f"{where}: slide_number が1未満です: {number}")
        else:
            if number in seen_numbers:
                errors.append(f"{where}: slide_number {number} が重複しています")
            seen_numbers.add(number)
            if deck_slide_count is not None and number > deck_slide_count:
                errors.append(
                    f"{where}: slide_number {number} はデッキのスライド数({deck_slide_count})を超えています"
                )

        issues = entry.get("issues")
        if issues is None:
            errors.append(f"{where}: issues がありません")
            continue
        if not isinstance(issues, list):
            errors.append(f"{where}: issues が配列ではありません")
            continue
        if not issues:
            errors.append(f"{where}: issues が空です(指摘のないスライドは含めないでください)")
            continue

        for j, issue in enumerate(issues):
            iwhere = f"{where}.issues[{j}]"
            if not isinstance(issue, dict):
                errors.append(f"{iwhere} がオブジェクトではありません")
                continue

            category = issue.get("category")
            if category not in CATEGORIES:
                errors.append(
                    f"{iwhere}: category が不正です: {category!r}(許可されるのは {sorted(CATEGORIES)})"
                )

            severity = issue.get("severity")
            if severity not in SEVERITIES:
                errors.append(
                    f"{iwhere}: severity が不正です: {severity!r}(許可されるのは {sorted(SEVERITIES)})"
                )

            for field in ("description", "suggested_fix"):
                value = issue.get(field)
                if not isinstance(value, str) or not value.strip():
                    errors.append(f"{iwhere}: {field} が空です")

    return errors


def summarize(review: dict) -> tuple[int, int]:
    """critical / minor の件数を数える。"""
    critical = minor = 0
    for entry in review.get("slides", []) or []:
        if not isinstance(entry, dict):
            continue
        for issue in entry.get("issues", []) or []:
            if not isinstance(issue, dict):
                continue
            if issue.get("severity") == "critical":
                critical += 1
            elif issue.get("severity") == "minor":
                minor += 1
    return critical, minor


def verify_file(review_path: str, deck_path: str | None) -> int:
    try:
        review = json.loads(Path(review_path).read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"検証対象: {review_path}")
        print(f"不合格 (1 件):\n  - JSON として解釈できません: {e}")
        return 1

    deck_slide_count = None
    if deck_path:
        try:
            deck = json.loads(Path(deck_path).read_text(encoding="utf-8"))
            deck_slide_count = len(deck.get("slides", []))
        except (json.JSONDecodeError, OSError) as e:
            print(f"ERROR: デッキ仕様を読めません: {deck_path}: {e}")
            return 2

    print(f"検証対象: {review_path}")
    if deck_slide_count is not None:
        print(f"デッキ照合: {deck_path}({deck_slide_count} スライド)")

    errors = validate(review, deck_slide_count)
    if errors:
        print(f"不合格 ({len(errors)} 件):")
        for e in errors:
            print(f"  - {e}")
        return 1

    critical, minor = summarize(review)
    print("合格: 問題は検出されませんでした")
    print(f"指摘の内訳: critical {critical} 件 / minor {minor} 件")
    print(f"総合判定: {review.get('overall_verdict')}")
    if critical:
        print(
            "critical の指摘は、improvement_patch.md に「反映済み」または"
            "理由付きの見送りとして必ず記録してください(docs/15_PPT_Handoff.md)。"
        )
    return 0


def self_test() -> int:
    """検証ロジック自体が、正常な記録を通し・異常な記録を弾けるかを確認する。"""
    ok = True

    def check(label: str, review: dict, deck_count, should_pass: bool, expect: str | None = None):
        nonlocal ok
        errors = validate(review, deck_count)
        passed = not errors
        if passed != should_pass:
            print(f"SELF-TEST FAIL: {label} — 期待 {'合格' if should_pass else '不合格'} / 実際 {'合格' if passed else '不合格'}")
            if errors:
                print(f"  検出: {errors}")
            ok = False
            return
        if expect and not any(expect in e for e in errors):
            print(f"SELF-TEST FAIL: {label} — '{expect}' を含むエラーが出ませんでした: {errors}")
            ok = False

    valid = {
        "theme_slug": "2026-07-20_example",
        "reviewed_pptx": "deck.claude-draft.pptx",
        "reviewer": "ChatGPT Work",
        "review_date": "2026-07-20",
        "overall_verdict": "needs_revision",
        "slides": [
            {
                "slide_number": 3,
                "issues": [
                    {
                        "category": "visibility",
                        "severity": "critical",
                        "description": "カードが見切れている",
                        "suggested_fix": "2段組に分解する",
                    }
                ],
            }
        ],
        "summary": "おおむね良好",
    }
    check("正常な記録", valid, None, True)
    check("正常な記録(デッキ照合あり)", valid, 30, True)

    missing_key = json.loads(json.dumps(valid))
    del missing_key["reviewer"]
    check("必須キー欠落", missing_key, None, False, "reviewer")

    bad_verdict = json.loads(json.dumps(valid))
    bad_verdict["overall_verdict"] = "looks_good"
    check("不正な overall_verdict", bad_verdict, None, False, "overall_verdict")

    bad_category = json.loads(json.dumps(valid))
    bad_category["slides"][0]["issues"][0]["category"] = "typo"
    check("未定義の category", bad_category, None, False, "category")

    bad_severity = json.loads(json.dumps(valid))
    bad_severity["slides"][0]["issues"][0]["severity"] = "blocker"
    check("未定義の severity", bad_severity, None, False, "severity")

    empty_desc = json.loads(json.dumps(valid))
    empty_desc["slides"][0]["issues"][0]["description"] = "   "
    check("空の description", empty_desc, None, False, "description")

    out_of_range = json.loads(json.dumps(valid))
    out_of_range["slides"][0]["slide_number"] = 31
    check("デッキ範囲外の slide_number", out_of_range, 30, False, "超えています")

    duplicated = json.loads(json.dumps(valid))
    duplicated["slides"].append(json.loads(json.dumps(valid["slides"][0])))
    check("slide_number の重複", duplicated, None, False, "重複")

    not_int = json.loads(json.dumps(valid))
    not_int["slides"][0]["slide_number"] = "3"
    check("整数でない slide_number", not_int, None, False, "整数ではありません")

    empty_issues = json.loads(json.dumps(valid))
    empty_issues["slides"][0]["issues"] = []
    check("空の issues", empty_issues, None, False, "issues が空です")

    # 集計ロジックの確認
    critical, minor = summarize(valid)
    if (critical, minor) != (1, 0):
        print(f"SELF-TEST FAIL: 集計が期待と異なります: critical={critical}, minor={minor}")
        ok = False

    print("SELF-TEST PASSED" if ok else "SELF-TEST FAILED")
    return 0 if ok else 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="ChatGPT Work のレビュー記録(chatgpt_review.json)を検証する"
    )
    parser.add_argument("review", nargs="?", help="chatgpt_review.json")
    parser.add_argument("--deck", help="照合する deck_spec.json(slide_number の範囲を検査する)")
    parser.add_argument("--self-test", action="store_true", help="検証ロジック自体の健全性を確認する")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    if not args.review:
        parser.error("review を指定するか、--self-test を指定してください")
    if not Path(args.review).is_file():
        print(f"ERROR: レビュー記録が存在しません: {args.review}")
        return 2
    if args.deck and not Path(args.deck).is_file():
        print(f"ERROR: デッキ仕様が存在しません: {args.deck}")
        return 2
    return verify_file(args.review, args.deck)


if __name__ == "__main__":
    sys.exit(main())
