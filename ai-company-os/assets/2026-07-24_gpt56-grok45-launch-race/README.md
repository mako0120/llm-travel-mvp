# OpenAI「GPT-5.6」 vs xAI「Grok 4.5」(2026-07-24・定期実行26本目)

生成方式A(30枚・エンゲージメント設計ルール・初心者配慮ルール・文字を減らし図解で
伝えるルール)+ AI対話ナレーション・スライド連動モードで制作。

## 選定理由

- 対象ジャンル「AI/エージェント系」枠(70%)
- 2026年7月8日にxAI(SpaceXAI)が「Grok 4.5」、翌7月9日にOpenAIが「GPT-5.6」
  (Sol/Terra/Luna)を発表。1日違いでの競合発表という高い話題性
- どちらも「コーディング・エージェント向け」という共通の切り口で、料金・
  提供チャネル等の具体的な数字が豊富にあり比較しやすい
- これまでの定期実行では単一企業の単一発表を扱うことが多かったため、2社の
  発表を比較するという構成で差別化を図った

## 見送った候補

- Mistral AI「Robostral Navigate」(ロボティクスモデル) — 日本の視聴者にとっての実用性・身近さで劣るため見送り
- Perplexity CometのSamsung統合(Bixby連携) — 既存製品の機能アップデートで新規性が薄いため見送り
- BABYMETAL「Metal Forth」全米Billboard 200トップ10入り — 事実として確認できたが初出は2025年8月であり、新規性の基準を満たさないため見送り
- MrBeastの登録者数記録 — 2024〜2025年の実績の再掲であり、2026年7月時点の新規の節目達成を確認できず、該当なしとして正直に報告

詳細な評価点は`ai-company-os/research/2026-07-24_theme-evaluation-round5.md`を参照。

## ファイル一覧

| ファイル | 内容 |
|---|---|
| `research.md` | 出典付き調査結果(見送った候補の記録を含む) |
| `deck_spec.json` | 30枚のデッキ仕様(同一レイアウト連続なし、bullets比率20.0%) |
| `deck.pptx` | 生成済みの.pptx本体。チャットで直接送付する |
| `narration_script.md` | 単独ナレーション原稿(30スライド、目安約2分) |
| `dialogue_spec.json` | AI対話ナレーション・スライド連動モード仕様(30スライド全カバー、42発言) |
| `dialogue_script.md` | 対話ナレーション原稿(30スライド、目安約5分) |
| `dialogue_audio.wav` | 対話音声(VOICEVOX、GitHub Actions経由で生成済み)。チャットで直接送付 |
| `slide_timings.json` | スライドごとの開始/終了/長さ(秒)。GitHub Actions経由で音声と同時に生成済み |
| `deck_narrated.mp4` | スライド画像+音声を結合したナレーション動画。チャットで直接送付(リポジトリには未コミット、生成バイナリのため) |
| `youtube_assets.md` | YouTube/Shorts向けタイトル案・概要欄・タグ・章立て |
| `canva_brief.md` | Canva移植ブリーフ(レイアウト対応表、`templates/canva_brief_template.md`準拠) |
| `risk-and-quality-review.md` | 著作権・品質自己評価(100点満点中94点、85点以上のため修正不要) |
| `thumbnail.png` | YouTubeサムネイル(1280×720、`build_thumbnail.py`で生成) |
| `thumbnail_spec.json` | サムネイル生成仕様 |
| `thumbnail_brief.md` | サムネイルのフック文言・設計根拠(`templates/thumbnail_brief_template.md`準拠) |

## 適用したルール

- 30枚デッキ、bullets比率20.0%(40%上限クリア)、同一レイアウト連続なし
- 文字中心の説明はtable/diagram/bar_chart/comparisonで図解・グラフ化
  (2社の概要・提供チャネルは`table`、料金比較は`bar_chart`、タイムライン・
  政府審査プロセスは`diagram`、設計思想の違いは`comparison`で表現)
- 初心者向け前提知識スライド + 「これは何を意味するか・どう試すか」の実践セクション
- 進捗バー・カード影・タイトルアクセントの視覚強化(`docs/04_PowerPoint.md`参照)
- 前サイクルとの接続スライドは設けていない
- 両社の他社モデルとの直接比較(優劣主張)は扱わず、「自社発表」と明示した
  数字のみを事実として紹介する方針を徹底(自己言及・自己宣伝リスク回避の
  標準方針に基づく)

## 検品結果

- `verify_pptx.py --min-slides 30 --max-slides 30` → 合格
- `build_deck.py`の同一レイアウト4連続以上チェック・bullets比率40%以下チェック(20.0%) → 合格
- `generate_dialogue_script.py --deck`のスライド数整合性検証(30枚、1〜30連番) → 合格
- 著作権・品質自己評価: 94点/100点(85点以上のため修正不要)

## リスク配慮

- 特定の国・政府・政党を扱う政治的テーマではなく、企業(OpenAI・xAI)の製品発表という事実紹介
- 対立を煽る表現・他社比較の誇張を避け、推測部分は「推測」と明示している
- 実在企業名は事実として扱うが、ロゴ・商標画像は使用しない
- GPT-5.6の政府審査プロセスについて、特定の国・政府への批判・憶測は行っていない

## 生成完了(音声・動画)

- `dialogue_audio.wav`: GitHub Actions(VOICEVOX)で生成済み、コミット済み
- `slide_timings.json`: 音声と同時にGitHub Actionsで生成済み、コミット済み
- `deck_narrated.mp4`: `build_narrated_video.py`で生成済み(30スライド、音声約5:14)。
  チャットで送付済み(リポジトリには未コミット、生成バイナリのため)

## 注意

- 一部のニュース記事本文には直接アクセスできず、検索エンジンの要約経由での
  確認である旨を`research.md`に明記した
- 公開・投稿はまだ行っていない
