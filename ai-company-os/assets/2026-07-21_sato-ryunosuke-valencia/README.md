# 佐藤龍之介 バレンシア移籍デッキ(2026-07-21)

「日本向け最新トレンド・スライド自動生成エージェント」仕様(オーナー提示)に基づく第2弾。
評価表2位テーマ(78点)を採用し、「海外・国内で活躍する日本人」枠での実行例。

## ファイル一覧

| ファイル | 内容 |
|---|---|
| `deck_spec.json` | 28枚のデッキ仕様(build_deck.py入力。仕様書の30枚から、水増しを避けて内容量に応じ調整) |
| `youtube_assets.md` | 長尺タイトル10件・サムネ文言・Shorts台本3本 |
| `canva_brief.md` | Canva移植仕様 |
| `risk-and-quality-review.md` | 著作権・安全性チェック(全項目クリア)、品質自己評価(**79/100点、85点基準未達を正直に報告**) |

テーマ選定の経緯は `research/2026-07-21_theme-evaluation.md`(評価表2位)を参照。

## 再生成方法

```bash
python ai-company-os/scripts/build_deck.py \
  ai-company-os/assets/2026-07-21_sato-ryunosuke-valencia/deck_spec.json \
  /tmp/out.pptx

python ai-company-os/scripts/verify_pptx.py /tmp/out.pptx --min-slides 28 --max-slides 28

python ai-company-os/scripts/export_script.py \
  ai-company-os/assets/2026-07-21_sato-ryunosuke-valencia/deck_spec.json \
  /tmp/script.md
```

## 検品結果

- `verify_pptx.py --min-slides 28 --max-slides 28` → 合格
- `export_script.py` → 成功(28スライド、目安 約10分)

## 重要な制限(正直な報告)

- **品質自己評価79/100点**(採用基準85点未満)。日本需要の統計不足・他選手比較データ不足が原因。数字を創作して基準を満たすことはしていない
- デビュー戦(7/18予定)の結果は本デッキ作成時点で未確認
- 実在の19歳選手を扱うため、本人写真・試合映像・合成音声は一切使用していない
- 公開・投稿はまだ行っていない。人間承認後に実施すること

生成した `.pptx` / `.md` 本体はリポジトリにコミットしない。
