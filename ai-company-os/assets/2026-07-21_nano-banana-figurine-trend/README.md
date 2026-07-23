# Nano Banana「フィギュア化」トレンド(ChatGPTプロンプト方式・2026-07-21)

オーナー指示「再生数がとれている及び取れそうなコンテンツ」により、評価軸を
実証済みバイラル実績優先に切り替えて選定したテーマ。

## 選定理由

- X(旧Twitter)で実際にトレンド入りした実績あり(「Nano Banana祭り」)
- 「#NanoBanana」「#フィギュア化」タグでSNS上に実際の拡散実績
- 無料で誰でも今すぐ試せる実演系コンテンツ(視聴者参加を促しやすい)
- Google公式が続報(Nano Banana 2)を出しており話題が継続中

## ファイル一覧

| ファイル | 内容 |
|---|---|
| `research.md` | 出典付き調査結果 |
| `chatgpt_prompt.md` | ChatGPTにそのまま貼り付けて使うプロンプト本文(実演手順を含む15〜20枚構成) |

## 出典

Google Cloud公式ブログ、TechCrunch、ITreview Labo、WEEL等。詳細は `research.md`。

## 注意

- 実際のフィギュア化画像・他人の写真は著作権・肖像権のため使用しない設計
- SNS投稿数等の正確な統計はX公式データへの直接アクセスがないため「不明」と明記
- 公開・投稿はまだ行っていない

## 追記(2026-07-23)

オーナー指示により生成方式Aへ回帰し、実際に `.pptx` を生成した。

| ファイル | 内容 |
|---|---|
| `deck_spec.json` | `build_deck.py` の入力仕様(本README・chatgpt_prompt.mdの内容を反映) |
| `narration_script.md` | `export_script.py` で書き出した発表原稿 |
| `.pptx` | 生成済み。verify_pptx.py 合格。バイナリのためリポジトリには未コミット、ユーザーに送付済み |
