# ソフトバンク×Sierra事例(ChatGPTプロンプト方式・2026-07-21)

オーナー指示により、build_deck.py による直接生成ではなく、**調査結果を反映したChatGPT投入用プロンプト**を成果物とする回。

## ファイル一覧

| ファイル | 内容 |
|---|---|
| `research.md` | 出典付き調査結果(検証済み事実/推測/不明点を区別) |
| `chatgpt_prompt.md` | ChatGPTにそのまま貼り付けて使うプロンプト本文 |

## 使い方

1. `chatgpt_prompt.md` 内のコードブロックをコピー
2. ChatGPT(Code Interpreter/Advanced Data Analysisが使えるプランを推奨)に貼り付け
3. Code Interpreterが使える場合、実際に .pptx ファイルが生成されダウンロードできる
4. 使えない場合は、スライドごとのテキスト出力をPowerPoint/Canvaへ手動転記する

## 出典

`research.md` に記載(ソフトバンク公式・Sierra公式・AI Watch・マイナビ・Hawk Insight)。

## 注意

- プロンプト内で「必ず使う事実」の範囲を明示し、数字の創作を防ぐ設計にしている
- 公開・投稿はまだ行っていない

## 追記(2026-07-23)

オーナー指示により生成方式Aへ回帰し、実際に `.pptx` を生成した。

| ファイル | 内容 |
|---|---|
| `deck_spec.json` | `build_deck.py` の入力仕様(本README・chatgpt_prompt.mdの内容を反映) |
| `narration_script.md` | `export_script.py` で書き出した発表原稿 |
| `.pptx` | 生成済み。verify_pptx.py 合格。バイナリのためリポジトリには未コミット、ユーザーに送付済み |
