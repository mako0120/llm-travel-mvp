# OpenAI、企業向けAIエージェント基盤「Presence」を発表(2026-07-23・定期実行23本目)

生成方式A(30枚標準・エンゲージメント設計ルール・初心者配慮ルール)+ AI対話ナレーション・
スライド連動モードで制作。

## 選定理由

- 対象ジャンル「AI/エージェント系」枠(70%)
- 2026年7月22日発表、調査時点の前日という新しさ
- OpenAI公式に加え、VentureBeat・SiliconANGLE・Help Net Security・MLQ News・
  Techgenyz・ITBrief Asia等、複数の独立系メディアが一斉報道
- 早期導入企業にSoftBank Corp(日本語エージェント)が含まれ、日本の読者にも身近

## 見送った候補

- Kimi K3の蒸留疑惑(米政府高官による批判) — 国家間の対立構造が強く高リスクのため見送り
- Project Camellia(OpenAIのデータセンター投資) — AIエージェントという主眼から外れるため見送り
- Google Threat Intelligence agentic AI一般提供 — 発表時期がやや曖昧で報道の広がりも限定的
- ISPS HANDAスコットランド女子オープン(日本人ゴルファー10人出場) — 大会がこれからで確定した成果ではないため見送り
- 急成長SNSアカウント枠 — 独立系メディアの裏付け報道がある候補を発見できず、該当なしとして正直に報告

詳細な評価点は`ai-company-os/research/2026-07-23_theme-evaluation-round2.md`を参照。

## ファイル一覧

| ファイル | 内容 |
|---|---|
| `research.md` | 出典付き調査結果(見送った候補の記録を含む) |
| `deck_spec.json` | 30枚のデッキ仕様(同一レイアウト連続なし、bullets比率33.3%) |
| `deck.pptx` | 生成済みの.pptx本体。チャットで直接送付する |
| `narration_script.md` | 単独ナレーション原稿(30スライド、目安約3分) |
| `dialogue_spec.json` | AI対話ナレーション・スライド連動モード仕様(30スライド全カバー、63発言) |
| `dialogue_script.md` | 対話ナレーション原稿(30スライド、目安約9分) |
| `dialogue_audio.wav` | 対話音声(VOICEVOX、GitHub Actions経由で生成済み、約9分)。チャットで直接送付済み |
| `slide_timings.json` | スライドごとの開始/終了/長さ(秒)。GitHub Actions経由で音声と同時に生成 |
| `deck_narrated.mp4` | スライド画像+音声を結合したナレーション動画(約9分)。チャットで直接送付済み(リポジトリには未コミット、生成バイナリのため) |
| `youtube_assets.md` | YouTube/Shorts向けタイトル案・概要欄・タグ・章立て |
| `canva_brief.md` | Canva移植ブリーフ(レイアウト対応表、`templates/canva_brief_template.md`準拠) |
| `risk-and-quality-review.md` | 著作権・品質自己評価(100点満点中95点、85点以上のため修正不要) |

## 今回の設計上の変更点(オーナー指示)

- **初心者配慮**: 専門用語(AIエージェント/エージェント基盤/ガードレール)の前提知識スライドと、
  「これは何を意味するのか・どう使えるのか」という実践セクションを新設(`docs/04_PowerPoint.md`参照)
- **前サイクルとの接続なし**: 以前のテーマのように「前回テーマとの共通点」スライドは
  今回から設けていない(オーナー指示により廃止)

## 検品結果

- `verify_pptx.py --min-slides 30 --max-slides 30` → 合格
- `build_deck.py`の同一レイアウト4連続以上チェック・bullets比率40%以下チェック(33.3%) → 合格
- `generate_dialogue_script.py --deck`のスライド数整合性検証(30枚、1〜30連番) → 合格
- 著作権・品質自己評価: 95点/100点(85点以上のため修正不要)

## リスク配慮

- 特定の国・政府・政党を扱う政治的テーマではなく、企業(OpenAI)の製品発表という事実紹介
- 対立を煽る表現・他社比較の誇張を避け、推測部分は「推測」と明示している
- 実在企業名は事実として扱うが、ロゴ・商標画像・実在人物の写真は使用しない

## 注意

- VentureBeat・SiliconANGLE・Help Net Security等の記事本文には直接アクセスできず(403エラー)、
  検索エンジンの要約経由での確認である旨を`research.md`に明記した
- 公開・投稿はまだ行っていない
