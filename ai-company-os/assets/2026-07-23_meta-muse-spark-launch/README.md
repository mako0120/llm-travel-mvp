# Meta、agentic AIモデル「Muse Spark 1.1」を発表(2026-07-23・定期実行24本目)

生成方式A(30枚・エンゲージメント設計ルール・初心者配慮ルール・文字を減らし図解で
伝えるルール)+ AI対話ナレーション・スライド連動モードで制作。

## 選定理由

- 対象ジャンル「AI/エージェント系」枠(70%)
- 2026年7月9日発表、SiliconANGLE・Dataconomy・Campus Technology・Tech Startups・
  Inc.com等、複数の独立系メディアが継続して報道
- Zuckerberg氏が3年ぶりにX(旧Twitter)に投稿してこのモデルを発表したという、
  それ自体が独立して報道されるほどの強いバイラル性のあるフックがある

## 見送った候補

- Kimi K3の蒸留疑惑(米政府高官による批判) — 国家間の対立構造が強く高リスクのため見送り
- Claude Fable 5の復帰 — 本シリーズを制作しているAI(Claude)自身の関連製品であり、
  自己言及・自己宣伝と見なされるリスクがあるため見送り
- Grok 4.5 — 前サイクルで既に検討・不採用と判断済みのため再見送り
- Korea IP OfficeのAIエージェント3種 — 一機関の内部利用にとどまり話題性で劣るため見送り
- Frigade Skills / MarketBlazer AI Chat Bot Machine — 独立系メディアでの報道の広がりが
  限定的なため見送り

詳細な評価点は`ai-company-os/research/2026-07-23_theme-evaluation-round3.md`を参照。

## ファイル一覧

| ファイル | 内容 |
|---|---|
| `research.md` | 出典付き調査結果(見送った候補の記録を含む) |
| `deck_spec.json` | 30枚のデッキ仕様(同一レイアウト連続なし、bullets比率23.3%) |
| `deck.pptx` | 生成済みの.pptx本体。チャットで直接送付する |
| `narration_script.md` | 単独ナレーション原稿(30スライド、目安約2分) |
| `dialogue_spec.json` | AI対話ナレーション・スライド連動モード仕様(30スライド全カバー、45発言) |
| `dialogue_script.md` | 対話ナレーション原稿(30スライド、目安約6分) |
| `dialogue_audio.wav` | 対話音声(VOICEVOX、GitHub Actions経由で生成済み、約5分42秒)。チャットで直接送付済み |
| `slide_timings.json` | スライドごとの開始/終了/長さ(秒)。GitHub Actions経由で音声と同時に生成済み |
| `deck_narrated.mp4` | スライド画像+音声を結合したナレーション動画(約5分42秒)。チャットで直接送付済み(リポジトリには未コミット、生成バイナリのため) |
| `youtube_assets.md` | YouTube/Shorts向けタイトル案・概要欄・タグ・章立て |
| `canva_brief.md` | Canva移植ブリーフ(レイアウト対応表、`templates/canva_brief_template.md`準拠) |
| `risk-and-quality-review.md` | 著作権・品質自己評価(100点満点中95点、85点以上のため修正不要) |
| `thumbnail.png` | YouTubeサムネイル(1280×720、`build_thumbnail.py`で生成) |
| `thumbnail_spec.json` | サムネイル生成仕様 |
| `thumbnail_brief.md` | サムネイルのフック文言・設計根拠(`templates/thumbnail_brief_template.md`準拠) |

## 適用したルール

- 30枚デッキ、bullets比率23.3%(40%上限クリア)、同一レイアウト連続なし
- 文字中心の説明はtable/diagram/bar_chart/comparisonで図解・グラフ化
  (ベンチマーク3種は`bar_chart`、料金・強化点は`table`、サブエージェントの仕組みは
  `diagram`で表現)
- 初心者向け前提知識スライド + 「これは何を意味するか・どう試すか」の実践セクション
- 進捗バー・カード影・タイトルアクセントの視覚強化(`docs/04_PowerPoint.md`参照)
- 前サイクルとの接続スライドは設けていない

## 検品結果

- `verify_pptx.py --min-slides 30 --max-slides 30` → 合格
- `build_deck.py`の同一レイアウト4連続以上チェック・bullets比率40%以下チェック(23.3%) → 合格
- `generate_dialogue_script.py --deck`のスライド数整合性検証(30枚、1〜30連番) → 合格
- 著作権・品質自己評価: 95点/100点(85点以上のため修正不要)

## リスク配慮

- 特定の国・政府・政党を扱う政治的テーマではなく、企業(Meta)の製品発表という事実紹介
- 対立を煽る表現・他社比較の誇張を避け、推測部分は「推測」と明示している
- 実在企業名・実在人物名(Mark Zuckerberg氏)は事実として扱うが、ロゴ・商標画像・
  写真・肖像は使用しない
- 本シリーズを制作しているAI(Claude)自身に関連する製品は自己言及リスクを避けるため
  意図的に見送った

## 注意

- SiliconANGLE・Tech Startups等の記事本文には直接アクセスできず(403エラー)、
  検索エンジンの要約経由での確認である旨を`research.md`に明記した
- ベンチマーク数値はMeta社発表の自社測定値であり、第三者検証済みとは書いていない
- 公開・投稿はまだ行っていない
