# 09. Notion Operations(Notion 運用)

## 前提

- Notion コネクタは環境により接続状態が異なる。使用前に必ず検証する(未接続なら記録は Markdown で `docs/` 配下に残し、接続後に転記する)。

## 記録のタイミング

- 結果が**確定してから**記録する(PR merge 後、レビュー完了後)。見込みで書かない。
- 1作業1レコード。後から検索できるよう Issue/PR の URL を必ず入れる。

## 記録する内容

| 項目 | 内容 |
|---|---|
| タイトル | 成果物または Issue の名前 |
| ステータス | Backlog / Ready / In Progress / PR Open / Reviewing / Released |
| リンク | GitHub Issue / PR / 成果物 |
| 結果 | 完了・中断・失敗と、その一行理由 |
| 学び | 次に活かす教訓(失敗時は必須) |

## ChatGPTプロンプトのNotion書き込み(2026-07-21〜、オーナー指示によりデフォルト運用)

生成方式B(docs/04_PowerPoint.md参照)で `chatgpt_prompt.md` を作成したら、必ずNotionにも
プロンプト本文を書き込む。目的は、オーナーがファイルを開かずにNotion上でコピーして
ChatGPTに貼り付けられるようにするため。

- 親ページ: `AI Company OS 運用基盤の導入` ページ(collection://328a5d80-7f18-40ec-b24d-fd7d6cf91788
  配下、開発ロードマップDB)の子ページとして作成する
- タイトル: `ChatGPTプロンプト: <テーマ名>(<評価点>点)`
- 内容: 出典付き調査結果の要約(research.mdの要点) + プロンプト本文全文(コードブロックのまま)
- 末尾に関連するGitHub Issue/PRへのリンクを付ける
- ファイル送付(SendUserFile)と併用する。Notion書き込みはファイル送付の代替ではなく追加

## 見やすさの改善(2026-07-23〜、オーナー指示)

「Notionをもっと見やすく」という指示を受けた運用変更。

- **索引テーブル**: 親ページ(`AI Company OS 運用基盤の導入`)の冒頭に、全テーマを
  一覧できる表(定期実行番号・テーマ名・確信度・ジャンル・子ページへのリンク)を置く。
  子ページを増やすたびにこの表も更新する
- **子ページの構成統一**: 見出し(`##`)・コールアウト風の要約ブロック・出典リストで
  構造化し、書きっぱなしの段落だけにしない

## pptx / 音声のNotion添付は廃止(2026-07-23、オーナー指示により撤回)

一時期、`.pptx`と音声(TTS)ファイルをNotionの`notion-create-attachment`(source_url方式)で
埋め込む運用を試みたが、オーナーから「Notionで送らなくていい、代わりにどこで見れるか
分かりやすくして」と撤回指示があったため**この運用は行わない**。

- pptx・音声ファイルはNotionに添付せず、**SendUserFileでチャットに直接送付**し、
  加えてGitHub上のパス(`ai-company-os/assets/<テーマ>/deck.pptx` /
  `dialogue_audio.wav`)を明記して「どこにあるか」が分かるようにする
- Notionの子ページには、ファイル本体を埋め込まず、GitHubのファイルパス(または
  raw URL)をテキストリンクとして記載するだけにとどめる
- 音声(TTS)は、VOICEVOXがClaude Codeのリモートセッションから起動できない
  (Docker Hubへのegressブロック)ため、`.github/workflows/synthesize-dialogue-audio.yml`
  (workflow_dispatch、mainマージ済み)でGitHub Actionsランナー上に限定して生成する。
  生成物はActions Artifact(blob.core.windows.net、これも当セッションからは
  ダウンロード不可)ではなく、ワークフロー自身がリポジトリへ直接コミットする形で
  取り出し、そこからSendUserFileでオーナーに送付する

## 学習ログ

失敗・手戻り・環境の罠(例: LibreOffice フィルタ破損、npm install 不可)は
「リリース・学習ログ」に記録し、`docs/03_Development.md` の既知事実にも反映する。
記録先が二重になる場合はリポジトリ側(`docs/`)を一次情報とする。
