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
| `deck_spec.json` | Claude Code | ただ。1つの正本(source of truth)。初稿・改善版とも常にこのファイルから生成する |
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
2. 人間または Cowork が `deck_review_images/` の画像一式と下記チェック項目を
   ChatGPT Work に渡す。
3. ChatGPT Work がページごとに確認し、`chatgpt_review.json` の内容(または
   それに相当する指摘一覧)を返す。
4. Claude Code が指摘を精査し、対応する変更を `deck_spec.json` に加え、
   何を・なぜ変えたかを `improvement_patch.md` に記録し、
   `build_deck.py` で `deck.chatgpt-reviewed.pptx` を再生成する。
5. `python scripts/verify_pptx.py deck.chatgpt-reviewed.pptx` で機械検品を通す。
6. Codex が `deck.chatgpt-reviewed.pptx` と `chatgpt_review.json` を確認する。

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
- `python scripts/verify_pptx.py deck.chatgpt-reviewed.pptx` が PASS している。
- `deck.chatgpt-reviewed.pptx` が `deck_spec.json`(最新版)から再生成された
  ものであり、ChatGPT 側で直接編集されたバイナリではない。
- `improvement_patch.md` に記載の変更点と `deck_spec.json` の実際の差分が一致する。

## 承認境界

この工程はドキュメント・テンプレート整備および既存パイプライン(`build_deck.py` /
`render_deck_images.py` / `verify_pptx.py`)の再利用のみで完結する。
`docs/01_Core_Rules.md` の承認境界(main 直接 push・本番公開・課金・外部連携の
新規導入など)に変更はない。
