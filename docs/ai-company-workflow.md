# AI開発会社ワークフロー

## 役割

- Notion: アイデア、調査、仕様、ロードマップ、意思決定、学習ログ
- Fable5 / Cowork: 全体の進行管理、役割分担、タスク監視
- ChatGPT Work: 企画、調査、Issue設計、Claudeへの指示、仕様レビュー
- GitHub: Issue、コード、PR、CIの正式な保管場所
- Claude Code: `claude` ラベル付きIssueをfeatureブランチで実装
- Codex: PRレビューと、明示的に依頼された修正支援
- Vercel: PR Preview。Productionは人間承認後のみ
- 人間: main merge、Production deploy、課金、重要判断の最終承認

## Claude実装スイッチ

ChatGPT WorkはClaude Codeに実装させるIssueを、`Claude Code 実装依頼`フォームから作成します。このフォームは自動的に `claude` ラベルを付けます。通常の調査・意思決定・人間作業Issueには付けません。

Claude Codeは次の条件がすべて揃ったIssueだけを実装対象にします。

1. Issueがopenである
2. `claude` ラベルがある
3. 実装内容、完了条件、テスト、承認境界が記載されている
4. 人間の判断待ちを示す記載がない

ブランチ名は `claude/feature-<Issue番号>-<内容>` とし、Draft PRを作成します。PR作成によってmainへ自動mergeしてはいけません。

## 標準フロー

1. ChatGPT Workが企画・調査・仕様を作る
2. Notionに背景と意思決定を記録する
3. ChatGPT WorkがGitHub Issueを作り、Claude実装対象なら `claude` ラベルを付ける
4. Claude Codeがfeatureブランチで実装しDraft PRを作る
5. CIとPR Governanceが自動検査する
6. Codexがコード、安全性、テストをレビューする
7. ChatGPT Workが仕様、事業、安全性をレビューする
8. Vercel Previewを人間が確認する
9. 人間承認後だけmainへmergeする
10. 人間承認後だけProductionへ反映する

## 自動化しない操作

- mainへのmerge
- Production deploy
- 課金有効化
- APIキーや秘密情報の作成、表示、保存
- 認証、DB、環境変数、外部サービス設定の変更
- 破壊的DB操作

これらはIssueやPRに必要性を記載し、人間の明示承認を待ちます。
