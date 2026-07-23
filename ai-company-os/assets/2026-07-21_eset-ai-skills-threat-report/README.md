# ESET AIスキル脅威レポート(ChatGPTプロンプト方式・2026-07-21)

評価表4位のテーマ(76点)。生成方式B(docs/04_PowerPoint.md参照)で制作。

## ファイル一覧

| ファイル | 内容 |
|---|---|
| `research.md` | 出典付き調査結果 |
| `chatgpt_prompt.md` | ChatGPTにそのまま貼り付けて使うプロンプト本文 |

## 出典

GlobeNewswire(ESET公式配信)、ESET公式(日本語)、ITmedia @IT。詳細は `research.md`。

## 注意

- セキュリティベンダー自身の発表であり第三者の独立検証ではない点をプロンプト内に明記
- 悪用方法の詳細手順は紹介しない設計
- 公開・投稿はまだ行っていない

## 追記(2026-07-23)

オーナー指示により生成方式Aへ回帰し、実際に `.pptx` を生成した。

| ファイル | 内容 |
|---|---|
| `deck_spec.json` | `build_deck.py` の入力仕様(本README・chatgpt_prompt.mdの内容を反映) |
| `narration_script.md` | `export_script.py` で書き出した発表原稿 |
| `.pptx` | 生成済み。verify_pptx.py 合格。バイナリのためリポジトリには未コミット、ユーザーに送付済み |
