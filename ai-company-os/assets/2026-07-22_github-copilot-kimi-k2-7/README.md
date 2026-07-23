# GitHub Copilotに初のオープンウェイトモデル「Kimi K2.7 Code」(ChatGPTプロンプト方式・2026-07-22・定期実行18本目)

## 選定理由

- 対象ジャンル「AI/エージェント系」枠(70%)。開発者向けAIツールの選定という、
  AI Company OS自身のミッションとも直結するテーマ
- モードB(バイラル優先)の採用条件を満たす: GitHub公式Changelog(一次情報)に加え、
  Windows Forum・Enterprise DNA・TechTimes・AlphaSignal・ChatForest等、複数の
  独立系メディアが2026年7月1〜2日の短期間に一斉に報道
- 数字(1兆パラメータ、320億活性化、256Kコンテキスト、0.95ドル/100万トークン、
  19日というスピード)が複数媒体で一致

## 前回テーマとの違い

定期実行9本目(`2026-07-21_qwen-kimi-model-race/`)のQwen 3.8 vs Kimi K3の
ベンチマーク競争とは別の出来事(Kimi K2.7 CodeのGitHub Copilot統合)であり、
内容の重複はない。`research.md`に区別を明記した。

## ファイル一覧

| ファイル | 内容 |
|---|---|
| `research.md` | 出典付き調査結果(前回テーマとの違いの説明を含む) |
| `chatgpt_prompt.md` | ChatGPTにそのまま貼り付けて使うプロンプト本文 |

## 出典

GitHub公式Changelog(一次情報)、Windows Forum、Enterprise DNA、TechTimes、
ChatForest、AlphaSignal。詳細は `research.md`。

## 注意

- GitHub公式Changelog本文には直接アクセスできず(403エラー)、検索エンジンの
  要約・引用経由での確認である旨を明記した
- 公開・投稿はまだ行っていない

## 追記(2026-07-23)

オーナー指示により生成方式Aへ回帰し、実際に `.pptx` を生成した。

| ファイル | 内容 |
|---|---|
| `deck_spec.json` | `build_deck.py` の入力仕様(本README・chatgpt_prompt.mdの内容を反映) |
| `narration_script.md` | `export_script.py` で書き出した発表原稿 |
| `.pptx` | 生成済み。verify_pptx.py 合格。バイナリのためリポジトリには未コミット、ユーザーに送付済み |
