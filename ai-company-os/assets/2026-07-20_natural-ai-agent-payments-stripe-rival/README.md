# Natural、AIエージェント決済でシリーズA3,000万ドルを調達(定期実行125本目)

## 概要

AIエージェント同士が自律的に支払い・請求を行える決済基盤の構築を目指す
Natural社が、2026年7月20日、Forerunner Ventures主導のシリーズAで
3,000万ドルを調達したと発表した。創業からわずか193日での調達。
Logan Paul氏・Jake Paul氏のAntifundを含む著名投資家が参加している。

## テーマ評価

- `ai-company-os/research/2026-08-04_theme-evaluation-round75.md` にて
  スコア74/100で採用
- 発表は着手日の15日前であり、鮮度基準(着手日の前日以内)を満たして
  いない点を正直に開示している(round72の約40日前と比べると改善)

## 成果物一覧

- `research.md` — リサーチ内容・出典
- `deck_spec.json` — 30枚デッキの構造定義(palette_preset: navy_gold)
- `deck.pptx` — PowerPointファイル(verify_pptx.py合格)
- `narration_script.md` — 単独ナレーション原稿
- `dialogue_spec.json` / `dialogue_script.md` — AI対話ナレーション
- `youtube_assets.md` — YouTube/Shorts素材
- `canva_brief.md` — Canvaデザインブリーフ
- `risk-and-quality-review.md` — 品質自己評価86/100(鮮度項目を減点)

## テスト結果

- `verify_pptx.py --min-slides 30 --max-slides 30` → 合格
- 同一レイアウト4連続以上チェック・bullets比率40%以下チェック(23%) → 合格

## 未解決事項

- 具体的な決済処理件数・取引額の実績は未確認
- 導入済みの顧客企業名は未確認
- 本ラウンドの企業評価額は未確認
- 発表日が着手日の15日前であり、鮮度基準を満たしていない

## 承認境界

main へのマージ・本番公開・投稿・課金は行っていません(Draft PRまで)。
