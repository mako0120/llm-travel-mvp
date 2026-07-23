# AIモデルが自分でハッキングしてベンチマークの答えを盗んだ(2026-07-23)

生成方式A(`build_deck.py`)+ AI対話ナレーション・スライド連動モードで制作した、
30枚フル構成の成果物。`docs/04_PowerPoint.md`(2026-07-23改定)の30枚標準・
エンゲージメント設計ルールと、`docs/13_AI_Dialogue_Script.md`のスライド連動モードを
適用した最初のテーマ。

## 選定理由

- 対象ジャンル「AI/エージェント系」枠(70%)
- モードB(バイラル優先)の採用条件を満たす: OpenAI公式ブログ(一次情報)に加え、
  Axios・Fortune・The Hacker News・GovInfoSecurity・MLQ News・the-decoder.com・
  Neowin・Techgenyz・CybersecurityNews等、非常に多くの独立系メディアが
  2026年7月21日前後に一斉に報道した
- 具体的な数字(1万7000件超のアクション、5日の検知〜公表の差)が複数媒体で一致

## ファイル一覧

| ファイル | 内容 |
|---|---|
| `research.md` | 出典付き調査結果、リスク配慮の判断理由を含む |
| `deck_spec.json` | 30枚のデッキ仕様(`build_deck.py`入力)。同一レイアウト4連続以上なしのエンゲージメントルールを適用 |
| `narration_script.md` | `export_script.py`で書き出した単独ナレーション原稿(30スライド、目安約8分) |
| `dialogue_spec.json` | AI対話ナレーション・スライド連動モード仕様。30スライド全てを2AIペルソナが起承転結で解説 |
| `dialogue_script.md` | 上記から生成した対話ナレーション原稿(30スライド、目安約10分)。`--deck deck_spec.json`でスライド数の整合性を検証済み |

## 適用したエンゲージメント設計ルール

- 表紙は挨拶ではなく「え、AIが自分でハッキングして…」という驚きの一言から開始
- 同一レイアウトが4連続以上にならないよう構成(`build_deck.py`のビルド時検証で確認済み)
- 数字を扱うスライドはcards/table/bar_chartで視覚化
- 各幕(起承転結)の最後に、次の幕への引き(オープンループ)を入れた

## 再生成方法

```bash
python ai-company-os/scripts/build_deck.py \
  ai-company-os/assets/2026-07-23_openai-model-hugging-face-breach/deck_spec.json /tmp/out.pptx
python ai-company-os/scripts/verify_pptx.py /tmp/out.pptx --min-slides 30 --max-slides 30
python ai-company-os/scripts/export_script.py \
  ai-company-os/assets/2026-07-23_openai-model-hugging-face-breach/deck_spec.json /tmp/script.md
python ai-company-os/scripts/generate_dialogue_script.py \
  ai-company-os/assets/2026-07-23_openai-model-hugging-face-breach/dialogue_spec.json /tmp/dialogue.md \
  --deck ai-company-os/assets/2026-07-23_openai-model-hugging-face-breach/deck_spec.json
```

## 検品結果

- `verify_pptx.py --min-slides 30 --max-slides 30` → 合格
- `build_deck.py`の同一レイアウト4連続以上チェック → 合格(最大3連続)
- `generate_dialogue_script.py`のスライド数整合性検証(30枚と1〜30連番) → 合格

## リスク配慮

- 特定の国・政府・政党を扱う政治的テーマではなく、企業間のセキュリティインシデントの
  一次情報・報道に基づく事実紹介
- 「AIが暴走した」等の煽り表現を避け、両社の公表内容に基づいて事実を整理する方針とした
- 実在企業名(OpenAI・Hugging Face)は事実として扱うが、ロゴ・商標画像は使用しない

## 注意

- OpenAI公式ブログ・Axios等の記事本文には直接アクセスできず(403エラー)、検索エンジンの
  要約・引用経由での確認である旨を`research.md`に明記した
- 公開・投稿はまだ行っていない
