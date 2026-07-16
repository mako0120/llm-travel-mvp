# Claude Code自動実装の有効化

## 完成している部分

`.github/workflows/claude-implement.yml` は、Issueに `claude` ラベルが付いた瞬間に公式Claude Code GitHub Actionを起動します。

自動処理は次の範囲に限定されています。

1. Issue、`CLAUDE.md`、`AGENTS.md` を読む
2. `claude/feature-<Issue番号>-<内容>` をmainから作る
3. Issue範囲だけを実装する
4. lint、typecheck、build、関連テストを実行する
5. featureブランチをpushする
6. Draft PRを作る
7. mergeせずに停止する

## 安全ゲート

初期状態では自動実装は無効です。次の2つが揃った場合だけClaude Codeを起動します。

- GitHub Actions Secret: `CLAUDE_CODE_OAUTH_TOKEN`
- GitHub Repository variable: `CLAUDE_AUTOMATION_ENABLED` の値が `true`

Secretの値をIssue、PR、コード、Notion、チャットへ貼らないでください。

## 1回だけ必要な設定

1. Claude Codeを利用している本人の端末で `claude setup-token` を実行します。
2. 表示された値をGitHubの `Settings → Secrets and variables → Actions → Secrets` に `CLAUDE_CODE_OAUTH_TOKEN` として保存します。
3. 同じ画面の `Variables` に `CLAUDE_AUTOMATION_ENABLED` を作り、値を `true` にします。
4. テストIssueを作り、`claude` ラベルを付けます。
5. GitHub Actions、featureブランチ、Draft PRを確認します。

OAuth tokenはClaudeの契約を使うCI用認証です。利用条件や割当は契約によって異なるため、有効化前に確認してください。

## 緊急停止

Repository variable `CLAUDE_AUTOMATION_ENABLED` を `false` に変更するか削除します。ワークフローやSecretを削除しなくても、新しい自動実装は開始されません。

実行中のジョブはGitHub Actions画面から停止します。

## 認証情報がない場合

`claude` ラベルを付けても実装は開始されません。Issueには設定不足を示すコメントだけが1回追加されます。
