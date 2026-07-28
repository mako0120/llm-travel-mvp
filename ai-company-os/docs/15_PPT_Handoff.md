# 15. PPT Handoff(Claude → ChatGPT Work → Codex 品質ゲート)

## 背景

これまで Claude Code が生成した PowerPoint(`deck.pptx`)は、検品スクリプト
(`verify_pptx.py`)による機械的なチェックのみを経て Codex レビューに渡っていた。
「ストーリーの流れ」「実際に画像として見たときの視認性」「スピーカーノートの
自然さ」といった、スクリプトでは検出できない観点は未整備だった。

本ドキュメントは、`docs/02_Architecture.md` の役割分担にある ChatGPT Work を
「全ページを実際に画像として確認し、内容・構成・視認性・ノート・出典を改善する
編集長」と位置付け、Claude Code の初稿とCodexの最終レビューの間に配置する
二段階品質ゲートを標準化する。

## 役割分担(この工程限定)

| 工程 | 担当 | 責務 | 成果物 |
|---|---|---|---|
| 初稿生成 | Claude Code | `deck_spec.json` から初稿を生成し、全ページを画像化する | `deck_spec.json`, `deck.claude-draft.pptx`, `deck_review_images/` |
| 全ページレビュー・改善指示 | ChatGPT Work(編集長) | 画像を1枚ずつ確認し、内容・構成・視認性・ノート・出典を評価する | `chatgpt_review.json` |
| 仕様反映・再生成 | Claude Code | レビュー内容を `deck_spec.json` に反映し、差分を記録して再生成する | `improvement_patch.md`, 更新後 `deck_spec.json`, `deck.chatgpt-reviewed.pptx` |
| 最終レビュー | Codex | 改善版と記録を確認し、スコープ・安全・品質を検査する | レビューコメント |

**PowerPoint の実体ファイル(`.pptx`)を編集できるのは常に Claude Code だけである。**
ChatGPT Work は画像とレビュー記録を通じてのみ改善を指示し、`deck_spec.json`
(テキストの仕様)を直接書き換えない。これにより、同じバイナリファイルを
Claude と ChatGPT が同時に編集する状態を作らない。

## ファイル配置(`assets/<日付>_<slug>/` 配下)

| ファイル | 生成者 | 内容 |
|---|---|---|
| `deck_spec.json` | Claude Code | 単一の正本(source of truth)。初稿・改善版とも常にこのファイルから生成する |
| `deck.claude-draft.pptx` | Claude Code | `build_deck.py` による初稿。ChatGPT Work のレビュー対象 |
| `deck_review_images/slide_NNN.png` | Claude Code | `render_deck_images.py` による全ページ画像(3桁連番)。ChatGPT Work に渡す実体 |
| `chatgpt_review.json` | ChatGPT Work | ページごとのレビュー結果。`templates/chatgpt_review_example.json` 準拠 |
| `improvement_patch.md` | Claude Code | `chatgpt_review.json` を受けて `deck_spec.json` のどこをどう変えたかの差分記録。`templates/improvement_patch_template.md` 準拠 |
| `deck.chatgpt-reviewed.pptx` | Claude Code | 改善反映後に `build_deck.py` で再生成した最終版。Codex のレビュー対象 |

## 手順(現状: 手動連携)

ChatGPT 用の API 接続・MCP サーバーは未整備のため、次の手動フローを前提とする。

1. Claude Code が `deck_spec.json` から `deck.claude-draft.pptx` を生成し、
   `python scripts/render_deck_images.py deck_spec.json deck_review_images/` で
   全ページを画像化する。
2. Claude Code が渡す依頼書を生成する:

   ```text
   python scripts/export_review_request.py deck_spec.json review_request.md
   ```

   依頼書には、ChatGPT Work の役割・禁止事項・確認必須の5分類・スライドごとの
   本文/ノート/出典/グラフ数値・返してほしい JSON 形式が入る。毎回手書きすると
   指示が揺れてレビュー品質が安定しないため、仕様から機械的に生成する。
3. 人間または Cowork が `review_request.md` と `deck_review_images/` の画像一式を
   ChatGPT Work に渡す。
4. ChatGPT Work がページごとに確認し、`chatgpt_review.json` を返す。
5. Claude Code が受け取った記録を機械検証する:

   ```text
   python scripts/verify_chatgpt_review.py chatgpt_review.json --deck deck_spec.json
   ```

   ChatGPT の出力は自由記述のため、項目名の揺れ・未定義の分類・存在しない
   スライド番号が混入しうる。**検証を通す前に `deck_spec.json` を書き換えない。**
6. Claude Code が指摘を精査し、対応する変更を `deck_spec.json` に加え、
   何を・なぜ変えたかを `improvement_patch.md` に記録し、
   `build_deck.py` で `deck.chatgpt-reviewed.pptx` を再生成する。
7. `python scripts/verify_pptx.py deck.chatgpt-reviewed.pptx` で機械検品を通す。
8. Codex が `deck.chatgpt-reviewed.pptx` と `chatgpt_review.json` を確認する。

### 連携ツール

| スクリプト | 役割 | 実行するタイミング |
|---|---|---|
| `export_review_request.py` | ChatGPT Work へ渡す依頼書を `deck_spec.json` から生成する | 初稿生成の直後(手順2) |
| `verify_chatgpt_review.py` | 返ってきた `chatgpt_review.json` の構造・分類・スライド番号を検証する | 仕様反映の直前(手順5) |

いずれも `--self-test` で、テーマの成果物なしにロジックの健全性を確認できる。

## ChatGPT Work が確認する必須項目

`chatgpt_review.json` の各ページ指摘は、次のいずれかの分類に属する。

- `story`(ストーリー・構成): 章立ての流れ、1スライド1メッセージが崩れていないか
- `visibility`(視認性): 文字サイズ・コントラスト・情報量過多がないか
- `speaker_notes`(スピーカーノート): 欠落、内容と食い違う記述、不自然な文体がないか
- `sources`(出典): 数字を伴うスライドに出典が明記されているか
- `overlap_or_cutoff`(重なり・文字切れ): 図形のはみ出し・テキストの見切れがないか

## Codex が確認する最終対象と合格条件

**対象**: `deck.chatgpt-reviewed.pptx` / `chatgpt_review.json` / `improvement_patch.md`

**合格条件**:

- `chatgpt_review.json` で `severity: "critical"` の指摘が、すべて
  `improvement_patch.md` 上で対応(反映済み)として記録されている。
- `python scripts/verify_chatgpt_review.py chatgpt_review.json --deck deck_spec.json`
  が PASS している(レビュー記録そのものが仕様どおりであること)。
- `python scripts/verify_pptx.py deck.chatgpt-reviewed.pptx` が PASS している。
- `deck.chatgpt-reviewed.pptx` が `deck_spec.json`(最新版)から再生成された
  ものであり、ChatGPT 側で直接編集されたバイナリではない。
- `improvement_patch.md` に記載の変更点と `deck_spec.json` の実際の差分が一致する。

## 前提と制約(正直な記録)

- **ChatGPT は API/MCP で接続されていない。** この環境で利用可能なコネクタは
  Canva / Notion / Slack / Vercel のみで、OpenAI 系コネクタは存在しない
  (2026-07-28 時点、`ListConnectors` で確認済み)。したがって「ChatGPT Work」は
  自動起動するエージェントではなく、**組織上の役割名**である。
- 本ドキュメントの連携は、人間または Cowork が依頼書と画像を ChatGPT に手渡しし、
  返答を `chatgpt_review.json` として保存する**完全な手動フロー**を前提とする。
  `export_review_request.py` / `verify_chatgpt_review.py` は、その手渡しの
  入口と出口を機械化して品質を安定させるためのもので、ChatGPT を呼び出さない。
- `render_deck_images.py`(手順1で使う画像化スクリプト)は別ブランチで開発中で
  あり、`main` にはまだ存在しない。`main` 単体で完結するのは手順2以降である。

将来 API/コネクタ経由の自動連携に切り替える場合、それは**新規外部連携の導入**に
あたり、`docs/01_Core_Rules.md` の承認境界により人間承認が必要になる。

## 承認境界

この工程はドキュメント・テンプレート整備と、リポジトリ内で完結する検証スクリプト
(`export_review_request.py` / `verify_chatgpt_review.py`)の追加のみで完結する。
外部への通信・認証・課金は一切発生しない。
`docs/01_Core_Rules.md` の承認境界(main 直接 push・本番公開・課金・外部連携の
新規導入など)に変更はない。
