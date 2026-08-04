# Dili、Khosla Ventures主導で2,170万ドルを調達(定期実行124本目)

## 概要

建設・インフラ・エネルギー業界向けにAIでコンプライアンス監査を自動化する
Dili社が、2026年7月30日、Khosla Ventures主導のシリーズA(1,500万ドル)を
含む累計2,170万ドルの調達を発表した。Y CombinatorのGarry Tan氏らも
出資に参加している。

## テーマ評価

- `ai-company-os/research/2026-08-04_theme-evaluation-round74.md` にて
  スコア72/100で採用
- 発表は着手日の5日前であり、鮮度基準(着手日の前日以内)をわずかに
  外れる点を正直に開示している(同ラウンドのBaselayer[123本目]は
  着手日前日で基準を満たす)

## 成果物一覧

- `research.md` — リサーチ内容・出典
- `deck_spec.json` — 30枚デッキの構造定義(palette_preset: forest_sand)
- `deck.pptx` — PowerPointファイル(verify_pptx.py合格)
- `narration_script.md` — 単独ナレーション原稿
- `dialogue_spec.json` / `dialogue_script.md` — AI対話ナレーション
- `youtube_assets.md` — YouTube/Shorts素材
- `canva_brief.md` — Canvaデザインブリーフ
- `risk-and-quality-review.md` — 品質自己評価85/100(鮮度項目を減点)

## テスト結果

- `verify_pptx.py --min-slides 30 --max-slides 30` → 合格
- 同一レイアウト4連続以上チェック・bullets比率40%以下チェック(27%) → 合格

## 未解決事項

- 本ラウンドの企業評価額は未確認
- 具体的な導入プロジェクト数・顧客企業名は未確認
- 発表日が着手日の5日前であり、鮮度基準をわずかに外れる

## 承認境界

main へのマージ・本番公開・投稿・課金は行っていません(Draft PRまで)。
