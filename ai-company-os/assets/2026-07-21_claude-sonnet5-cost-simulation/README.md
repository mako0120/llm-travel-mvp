# Claude Sonnet 5 運用費試算デッキ(2026-07-21)

「日本向け最新トレンド・スライド自動生成エージェント」仕様(オーナー提示、フル実行)に基づき、
テーマ発見〜30枚デッキ〜ナレーション原稿〜YouTube/Shorts素材〜Canvaブリーフ〜品質評価まで一気通貫で制作した成果物。

## ファイル一覧

| ファイル | 内容 |
|---|---|
| `deck_spec.json` | 30枚のデッキ仕様(build_deck.py入力) |
| `youtube_assets.md` | 長尺タイトル10件・サムネ文言・概要欄・チャプター・Shorts台本3本 |
| `canva_brief.md` | Canva移植仕様(templates/canva_brief_template.md準拠) |
| `risk-and-quality-review.md` | 著作権・安全性チェック、品質自己評価(85/100点)、既知の制限 |
| `dialogue_spec.json` | AI対話ナレーション形式・スライド連動モード(`docs/13_AI_Dialogue_Script.md`)。30枚全スライドを2AIペルソナが起承転結で解説する仕様(2026-07-23追加) |
| `dialogue_script.md` | 上記から生成した対話ナレーション原稿(30スライド、目安約12分)。`--deck deck_spec.json`で見出し自動取得・スライド数の整合性を検証済み |

テーマ選定の経緯・評価表は `research/2026-07-21_theme-evaluation.md` を参照。

## 再生成方法

```bash
python ai-company-os/scripts/build_deck.py \
  ai-company-os/assets/2026-07-21_claude-sonnet5-cost-simulation/deck_spec.json \
  /tmp/out.pptx

python ai-company-os/scripts/verify_pptx.py /tmp/out.pptx --min-slides 30 --max-slides 30

python ai-company-os/scripts/export_script.py \
  ai-company-os/assets/2026-07-21_claude-sonnet5-cost-simulation/deck_spec.json \
  /tmp/script.md
```

## 検品結果

- `verify_pptx.py --min-slides 30 --max-slides 30` → 合格
- `export_script.py` → 成功(30スライド、目安 約12分)

## 既知の制限

- ナレーション原稿は目標(15〜20分)に対し実際は約12分(詳細は `risk-and-quality-review.md`)
- 公開・投稿はまだ行っていない。仕様書どおり人間承認後に実施すること

生成した `.pptx` / `.md` 本体はリポジトリにコミットしない(`.gitignore` によりバイナリ除外、再生成コマンドで再現可能なため)。
