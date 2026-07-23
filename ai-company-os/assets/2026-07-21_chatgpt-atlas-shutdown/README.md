# ChatGPT Atlas終了(ChatGPTプロンプト方式・2026-07-21・定期実行10本目)

## 選定理由

- OpenAI公式ヘルプセンターという一次情報で確認済み
- 「公開から1年足らずで終了」という意外性のあるストーリー
- 8月9日という具体的な締切があり、視聴者への行動喚起(データ移行)がしやすい
- ITmedia NEWS・ケータイWatch・INTERNET Watch等の複数メディアが一致して報道

## ファイル一覧

| ファイル | 内容 |
|---|---|
| `research.md` | 出典付き調査結果 |
| `chatgpt_prompt.md` | ChatGPTにそのまま貼り付けて使うプロンプト本文 |

## 出典

OpenAI公式ヘルプセンター、ITmedia NEWS、ケータイWatch、INTERNET Watch。詳細は `research.md`。

## 注意

- 公開・投稿はまだ行っていない

## 追記(2026-07-23)

オーナー指示により生成方式Aへ回帰し、実際に `.pptx` を生成した。

| ファイル | 内容 |
|---|---|
| `deck_spec.json` | `build_deck.py` の入力仕様(本README・chatgpt_prompt.mdの内容を反映) |
| `narration_script.md` | `export_script.py` で書き出した発表原稿 |
| `.pptx` | 生成済み。verify_pptx.py 合格。バイナリのためリポジトリには未コミット、ユーザーに送付済み |
