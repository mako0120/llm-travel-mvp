# AI開発会社 運用マニュアル

## 役割分担

| 役割 | 担当 | 責務 | 禁止事項 |
|---|---|---|---|
| 統括 | ChatGPT Work | 進行、接続、権限、承認管理 | 承認なしの外部変更 |
| 企画 | ChatGPT | 市場・競合分析、Issue設計、指示作成 | 実装、main操作、本番操作 |
| 開発・レビュー | Codex | 小さな実装、検証、PR、レビュー | Secrets、破壊的DB変更、本番操作 |
| 記録 | Notion | 企画、意思決定、学習の記録 | 必要範囲外の共有 |
| 開発履歴 | GitHub | Issue、PR、Actions | main直接変更 |
| Preview | Vercel | PRごとの表示確認 | 承認なしの本番反映 |
| 最終決定 | 人間 | 承認、マージ、本番反映 | - |

## 標準フロー

1. ChatGPTがNotion用データとIssue下書きを作る。
2. 人間がIssue化と実装範囲を承認する。
3. Codexが専用ブランチで実装し、品質確認を行う。
4. CodexがPRを作成し、Vercel Previewを確認する。
5. Codexがレビュー観点を提示し、人間が最終レビュー・マージを行う。
6. リリース後の学びをNotionへ記録する。

## 承認が必須の操作

- Notion DBの新規作成・共有範囲変更
- GitHubブランチ保護、Actions、権限、ラベル設定の変更
- Vercelのプロジェクト・環境変数・Production設定の変更
- DB migration、外部API、課金、個人情報を扱う変更
- PRのマージと本番デプロイ

## Notionデータベース

事業アイデア、競合分析、開発ロードマップ、GitHub Issue候補、意思決定ログ、リリース・学習ログの6 DBを使う。各DBのプロパティは、企画担当ルールにある登録項目をそのまま採用する。

## GitHubの推奨保護

`main` はPR必須、CI成功必須、1件以上の承認必須、force push禁止、ブランチ削除禁止とする。管理者例外は設けない。

## Vercel Preview確認

- Preview URLが発行され、トップページが404でない
- 主要画面、ログイン導線、API呼び出しが正常
- Console error、環境変数不足、モバイル崩れがない
