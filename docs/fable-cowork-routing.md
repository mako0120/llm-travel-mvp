# Fable 5をCoworkで一時利用する判断ルール

## 結論

Fable 5は常時使いません。通常の企画はChatGPT Work、通常実装はClaude
Sonnet、レビューとworkflow修正はCodexが担当します。Fable 5は、長時間・
複数段階・難しい判断が必要な一件に限り、Coworkで一回だけ使います。

## 使うタイミング

| 状況 | Fable 5 |
|---|---|
| 複数サービスにまたがる重要アーキテクチャ判断 | 使う候補 |
| 10件以上の資料・競合・要件を統合する長時間調査 | 使う候補 |
| 重大リスクを含む大規模PRの最終設計レビュー | 使う候補 |
| largeかつSonnet/Codexで2回以上失敗 | 使う候補 |
| small/mediumの通常実装・バグ修正・docs・CI | 使わない |
| lint・typecheck・build・定型レビュー | 使わない |

## 流れ

1. GitHubで「Fable 5 一時利用判断」Issueを作る
2. `fable-review` ラベルをイベントとして、AI不使用の判定を行う
3. 合格時だけ `ai:fable-needed` とCowork用プロンプトが作られる
4. 人間がCoworkでFable 5を選び、そのプロンプトを一回だけ実行する
5. 結果をGitHubとNotionへ記録する
6. `ai:fable-used` を付け、`ai:fable-needed` を外して終了する

## 判断パケット方式

Fable 5へリポジトリ全体や大量の資料を直接渡しません。先にSonnet/Codexで
情報を圧縮し、次のパケットだけを渡します。

- 判断したい質問: 最大3件
- 根拠資料: 最大10件
- 既知の事実
- 未確定事項
- 却下済み案
- 制約

一回のFable実行で、仮回答、反対側からの検証、最終推奨、撤退条件、
Sonnet/Codex向けIssue分解まで完了させます。

## Claude Routineを使う場合の最小設定

Claude RoutinesはGitHubイベントとPRラベルで開始できますが、実行ごとに
契約使用量を消費します。作成する場合は次だけを設定します。

- Model: Fable 5
- Repository: `mako0120/llm-travel-mvp` のみ
- GitHub event: Pull request labeled
- Filter: Labels includes `ai:fable-needed`
- Branch push: unrestrictedを無効のまま
- Connectors: GitHub以外をすべて外す
- Environment variables: 追加しない
- Network: Trustedのまま
- Extra usage: 有効化しない

IssueはRoutineのGitHub trigger対象外なので、Issueの場合は生成された
プロンプトをCoworkへ一回だけ貼ります。

## なぜ完全自動起動しないか

Fable 5は使用クレジットを消費する場合があります。GitHub側は無料の機械判定と
プロンプト作成までに止め、実際の開始時だけ人間が使用量表示を確認します。

## 安全境界

Fable 5もmain merge、Production deploy、課金有効化、秘密情報、認証、DB、
環境変数の変更は行いません。これらは別のIssueと明示承認が必要です。
