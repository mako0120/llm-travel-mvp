# AI開発ワークフロー運用規約

`mako0120/llm-travel-mvp` をAI開発会社方式で開発するための運用規約です。
すべての機能開発は **Issue起点** で行い、**人間の最終承認** を経てmainへmergeします。

## 役割分担

| 担当 | 役割 | GitHub上の動き |
|---|---|---|
| 人間(最終承認者) | main merge、Production deploy、課金有効化、破壊的変更の承認 | PR承認・merge |
| ChatGPT Work | 企画・調査・仕様設計・Issue設計・PRレビュー・Notion記録 | Issue作成、`claude` ラベル付与、PRレビューコメント |
| Claude Code | Issueに基づく実装、PR作成、レビュー対応 | `claude/` ブランチで実装、draft PR作成 |
| Codex | PRレビュー・修正支援 | `codex/` ブランチ、レビューコメント |
| Fable5 / Cowork | 全体の進行管理 | Issue / PRの状態確認 |
| Notion(AI開発会社 本部) | 仕様・意思決定・タスク記録 | — |
| Vercel(llm-travel-mvp2) | PR Preview。Production反映は人間承認後のみ | PRごとのPreview URL |

## 開発フロー

1. **Issue作成** — ChatGPT Work(または人間)がIssueテンプレートに沿って作成する
2. **実装ハンドオフ** — Claude Codeに実装させるIssueに `claude` ラベルを付ける
3. **実装** — Claude Codeが検知し、`in-progress` ラベルを付けて着手。`claude/feature-<Issue番号>-<説明>` ブランチで実装する
4. **検証** — `npm run lint` / `npm run typecheck` / `npm run build` を通す
5. **PR作成** — draft PRをテンプレートに沿って作成(`Closes #<Issue番号>` 必須)
6. **CI検査** — `ci.yml`(lint / typecheck / build)と `pr-policy.yml`(ブランチ名・Issue参照・必須セクション)が自動実行される
7. **レビュー** — ChatGPT Work / Codexがレビューし、Claude Codeが修正対応する
8. **Preview確認** — Vercel PR Previewで動作確認し、PR本文にURLを記載する
9. **人間承認** — PR本文の「人間承認チェックリスト」を確認のうえ、人間がmainへmergeする
10. **自動デプロイ** — mainへのmergeでVercelがProductionへデプロイする

## ラベル運用

| ラベル | 意味 | 付ける人 |
|---|---|---|
| `claude` | Claude Codeへの実装ハンドオフスイッチ | ChatGPT Work / 人間 |
| `in-progress` | Claude Codeが着手済み(二重着手防止) | Claude Code(自動) |

## ブランチ命名規約

| プレフィックス | 用途 |
|---|---|
| `claude/feature-<Issue番号>-<説明>` | Claude Codeの機能実装 |
| `claude/fix-<Issue番号>-<説明>` | Claude Codeのバグ修正 |
| `claude/refactor-<Issue番号>-<説明>` | Claude Codeのリファクタリング |
| `codex/<説明>` | Codexの作業ブランチ |
| `chatgpt/<説明>` | ChatGPT Workの作業ブランチ |
| `feature/` `fix/` `refactor/` `chore/` `docs/` `hotfix/` | 人間の作業ブランチ |

- 他の担当のブランチへ上書きpushしない(特に `chatgpt/` `codex/`)
- mainへの直接pushは禁止(branch protectionの有効化を推奨)

## Claude Code向け実装ハンドオフ規約

Issueには以下を必ず含める(Issueテンプレート準拠):

- **背景 / 目的** — なぜ作るか
- **実装内容** — 何を変更するか
- **完了条件** — 何をもって完了か
- **安全境界** — 触ってはいけない範囲

Claude Codeの動作規約:

- Issueの範囲外の変更をしない
- 仕様が曖昧な場合は実装せず、Issueコメントで質問する
- lint / typecheck / build を通してからPRを作成する
- PRは必ずdraftで作成し、レビューを経てからready化する

## Codex向けレビュー規約

- 正当性(バグ・型・エッジケース)と安全境界(secrets・破壊的変更)を優先して見る
- 指摘は「問題点 + 修正案」のセットでPRコメントに残す
- 大きな仕様変更が必要と判断した場合はPRで対応せず、ChatGPT Work / 人間へIssueとして差し戻す

## 安全境界(全担当共通)

自動実行してはいけないこと:

- mainへの直接push
- Vercel Production deploy(mainへのmerge以外の手段での本番反映)
- Stripe等の課金有効化
- APIキー・秘密情報の表示・保存・コミット(`.env.local` はコミット禁止)
- 人間承認なしのDB破壊的変更(DROP / TRUNCATE / migration削除など)
- 人間承認なしの外部サービス設定変更(Supabase / Vercel / GitHub設定など)
- `service_role` キーをクライアント側コードや `NEXT_PUBLIC_` 変数に入れること

## 人間承認が必要な操作

- mainへのmerge(= Production反映)
- GitHub branch protectionの設定変更
- Vercel Production設定の変更
- 環境変数の追加・変更
- DBスキーマの破壊的変更
- Notion / Coworkの外部自動化設定

## Notion / Cowork / Vercelとの境界

- **Notion(AI開発会社 本部)**: 仕様・意思決定・タスクの記録場所。GitHubのIssue / PRが実行の正とし、Notionは記録・参照用とする
- **Fable5 / Cowork**: 進行管理のみ。コード変更・設定変更は行わない
- **Vercel**: PR Previewは自動、Productionはmain merge経由のみ。ダッシュボード上での手動Production deployは人間のみが行う
