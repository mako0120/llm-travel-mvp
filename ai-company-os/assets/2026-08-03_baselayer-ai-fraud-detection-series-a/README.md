# Baselayer、AI不正検知でシリーズA2,000万ドルを調達(定期実行123本目)

## 概要

金融機関・政府機関向けにAIで企業の不正リスクを自動検知するBaselayer社が、
2026年8月3日、Koro Capital・M13主導のシリーズAラウンドで2,000万ドルを
調達したと発表した。累計調達額は4,700万ドルに到達している。

## テーマ評価

- `ai-company-os/research/2026-08-04_theme-evaluation-round74.md` にて
  スコア75/100で採用
- 発表は着手日の前日であり、鮮度基準(着手日の前日以内)を満たす

## 成果物一覧

- `research.md` — リサーチ内容・出典
- `deck_spec.json` — 30枚デッキの構造定義(palette_preset: slate_azure)
- `deck.pptx` — PowerPointファイル(verify_pptx.py合格)
- `narration_script.md` — 単独ナレーション原稿
- `dialogue_spec.json` / `dialogue_script.md` — AI対話ナレーション
- `youtube_assets.md` — YouTube/Shorts素材
- `canva_brief.md` — Canvaデザインブリーフ
- `risk-and-quality-review.md` — 品質自己評価87/100

## テスト結果

- `verify_pptx.py --min-slides 30 --max-slides 30` → 合格
- 同一レイアウト4連続以上チェック・bullets比率40%以下チェック(23%) → 合格

## 未解決事項

- 本ラウンドの企業評価額は未確認
- AIモデルの具体的な検知アルゴリズムは未確認
- 具体的な顧客企業名は未確認

## 承認境界

main へのマージ・本番公開・投稿・課金は行っていません(Draft PRまで)。
