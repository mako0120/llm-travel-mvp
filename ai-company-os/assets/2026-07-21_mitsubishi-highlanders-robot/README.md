# 三菱自動車×Highlanders 人型ロボット量産(ChatGPTプロンプト方式・2026-07-21)

上位5候補が尽きたため実施した第2ラウンド追加調査からの採用テーマ(評価79点)。

## ファイル一覧

| ファイル | 内容 |
|---|---|
| `research.md` | 出典付き調査結果(日経・ITmedia・TBS NEWS DIG等、複数メディア一致) |
| `chatgpt_prompt.md` | ChatGPTにそのまま貼り付けて使うプロンプト本文 |

## 出典

日本経済新聞、ITmedia AI+、TBS NEWS DIG、ITmediaエグゼクティブ。詳細は `research.md`。

## 注意

- 方針発表段階であり、実際の量産開始前である点をプロンプト内に明記
- ロボットの写真・実在企業ロゴは使用しない設計
- 公開・投稿はまだ行っていない

## 追記(2026-07-23)

オーナー指示により生成方式Aへ回帰し、実際に `.pptx` を生成した。

| ファイル | 内容 |
|---|---|
| `deck_spec.json` | `build_deck.py` の入力仕様(本README・chatgpt_prompt.mdの内容を反映) |
| `narration_script.md` | `export_script.py` で書き出した発表原稿 |
| `.pptx` | 生成済み。verify_pptx.py 合格。バイナリのためリポジトリには未コミット、ユーザーに送付済み |
