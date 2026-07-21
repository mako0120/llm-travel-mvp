# AIプレゼン自動化デッキ(2026-07-21)

PowerPoint自動化パイプライン(調査→構成→JSON→生成→検品→原稿)の実動作確認を兼ねた、実データによる調査デッキ。

## 内容

生成AIによるプレゼン資料自動化の市場動向と、精度面のリスクをWeb検索で調査し、8枚のデッキにまとめたもの。
数字はすべて出典付き(`deck_spec.json` の各スライドに記載)。

## 再生成方法

```bash
python ai-company-os/scripts/build_deck.py \
  ai-company-os/assets/2026-07-21_ai-presentation-automation/deck_spec.json \
  /tmp/out.pptx

python ai-company-os/scripts/verify_pptx.py /tmp/out.pptx --min-slides 8 --max-slides 8

python ai-company-os/scripts/export_script.py \
  ai-company-os/assets/2026-07-21_ai-presentation-automation/deck_spec.json \
  /tmp/script.md
```

## 出典

- 2Slides Blog『State of AI Presentations in 2026』(2026): https://2slides.com/blog/state-of-ai-presentations-2026-trends-stats-predictions
- Medium『We Fact-Checked 6 AI Presentation Makers』(2026年2月): https://medium.com/@neel2108/we-fact-checked-6-ai-presentation-makers-heres-how-often-they-hallucinate-90e6093e42fc
- FINRA 2026 Annual Regulatory Oversight Report(生成AIに関する言及、間接引用)

いずれも業界ブログ・調査記事であり、公的統計そのものではない。判断材料として利用する際は一次情報の追加確認を推奨する。

## 検品結果

- `verify_pptx.py --min-slides 8 --max-slides 8` → 合格
- `export_script.py` による原稿出力 → 成功(8スライド、目安 約3分)

生成した `.pptx` / `.md` 本体はリポジトリにコミットしない(`.gitignore` によりバイナリ除外、Markdown原稿もこのREADMEに再生成コマンドを残すことで再現可能なため)。
