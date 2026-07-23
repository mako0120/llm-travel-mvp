# 08. GitHub Operations(GitHub 運用)

## 基本フロー

1. 作業は open な GitHub Issue から始める(`claude` ラベル付きが Claude Code の担当)。
2. Issue には必須セクションを書く: 目的 / 完了条件 / 変更予定ファイル / 非対象 / テスト計画。
3. ブランチ: `claude/feature-<issue番号>-<slug>`(最新 main から作成)。
4. PR は Draft で作成し、`Closes #<issue番号>` を本文に含める。
5. CI green + レビュー完了後、merge は人間(または人間が明示的に承認した自動化)が行う。

## ラベル運用

| ラベル | 意味 |
|---|---|
| `claude` | Claude Code が実装担当 |
| `in-progress` | 実装中(重複着手防止) |
| `ai:claude-ready` | Issue が実装可能な状態 |
| `ai:codex-review` | PR がレビュー可能な状態 |

## 重複防止

- 着手前に既存ブランチ・open PR を確認し、同じ Issue の作業が進行中なら着手しない。
- 競合に気づいたら自分の PR を閉じ、理由をコメントに残す(再オープンしない)。

## 認証と実行コスト

- GitHub Actions での Claude 実行は `anthropics/claude-code-action` + サブスクリプションの
  OAuth トークン(`claude setup-token` で発行、Secret 名 `CLAUDE_CODE_OAUTH_TOKEN`)を使う。
  追加の API 課金は発生しないが、**サブスクのレート制限は消費する**。無制限ではない。
- トークン節約: トリガーは最小限のイベントに絞り、`--max-turns` で上限を設ける。
- 料金制限の回避・複数アカウント・非公式の「無制限化」ツールは使わない(`docs/01_Core_Rules.md`)。

## 禁止事項

- `main` への直接 push。
- Secret・トークンのログ出力・コミット。
- 他エージェントのブランチ(`chatgpt/`, `codex/`)への push。
