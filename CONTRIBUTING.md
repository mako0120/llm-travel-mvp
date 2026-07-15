# 開発・AI運用ルール

## 原則

- `main` へ直接pushしない。作業は `feature/issue-番号-内容` または `codex/` 接頭辞のブランチで行う。
- Pull Requestは人間が最終承認し、マージと本番反映も人間が行う。
- Secrets、`.env*`、外部APIキー、個人情報を表示・変更・投稿しない。
- 破壊的なDB変更、課金設定、外部サービス設定、本番デプロイは実行しない。必要なら提案として記録する。

## 実装前後の確認

1. Issueの背景、目的、受け入れ条件を確認する。
2. 関連ファイルを読み、小さく限定した変更にする。
3. `npm run lint`、`npm run typecheck`、利用可能なテスト、`npm run build` を実行する。
4. PRには変更内容、検証結果、リスク、Preview URL、人間の確認事項を記載する。

詳細な役割とレビュー基準は [運用マニュアル](docs/ai-company-operating-manual.md) を参照してください。
