# Claude Science(ChatGPTプロンプト方式・2026-07-21・定期実行14本目)

## 選定理由

- Anthropic公式発表という一次情報で確認済み(このサイクルで最も確度の高い出典)
- 研究者向けツールというAI Company OS自身のミッション(調査・研究支援)と親和性が高い
- 急成長アカウント枠(YouTube/TikTok)は今回も質の高い候補を見つけられず、AI枠に戻した

## ファイル一覧

| ファイル | 内容 |
|---|---|
| `research.md` | 出典付き調査結果 |
| `chatgpt_prompt.md` | ChatGPTにそのまま貼り付けて使うプロンプト本文 |

## 出典

Anthropic公式(一次情報)、TechRadar、TechTimes、MarkTechPost。詳細は `research.md`。

## 注意

- 公開・投稿はまだ行っていない

## 追記(2026-07-23)

オーナー指示により生成方式Aへ回帰し、実際に `.pptx` を生成した。

| ファイル | 内容 |
|---|---|
| `deck_spec.json` | `build_deck.py` の入力仕様(本README・chatgpt_prompt.mdの内容を反映) |
| `narration_script.md` | `export_script.py` で書き出した発表原稿 |
| `.pptx` | 生成済み。verify_pptx.py 合格。バイナリのためリポジトリには未コミット、ユーザーに送付済み |
