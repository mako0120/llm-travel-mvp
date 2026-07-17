@AGENTS.md

# Claude Code

このファイルはClaude専用の短い入口です。共通の安全規則と役割分担は
`AGENTS.md`を優先してください。

## プロジェクト概要
- Next.js 15 (App Router, TypeScript) + Supabase
- デプロイ: Vercel(mainブランチへのpushで自動デプロイ)
- CI: GitHub Actions(.github/workflows/ci.yml — lint / typecheck / build)

## コマンド
- `npm run dev` — 開発サーバー起動
- `npm run lint` — ESLint
- `npm run typecheck` — 型チェック
- `npm run build` — 本番ビルド

## 実装規約
- 実装対象は open かつ `claude` ラベル付きのGitHub Issueに限る
- GitHub Actionが用意した現在のブランチを使い、新しいブランチを作らない
- PRはDraftで作成し、本文に `Closes #<Issue番号>` を記載する
- Issueに書かれた変更予定ファイルを先に読み、範囲外を探索しない
- unrelatedなリファクタリングや改善を追加しない
- mainへのmerge、Production deploy、課金、認証・DB・環境変数の変更は人間承認なしに行わない
- Supabaseクライアントは lib/supabase/ のものを使う
  - Server Components / Route Handlers → `lib/supabase/server.ts`
  - Client Components → `lib/supabase/client.ts`
- 環境変数は .env.local(コミット禁止)。テンプレートは .env.local.example
- service_role キーは絶対にクライアント側コードや NEXT_PUBLIC_ 変数に入れない
- コミット前にIssue指定テスト、lint、typecheck、buildを実行する
- Draft PRを作成したら停止する

## Compact instructions

コンテキスト圧縮時は、Issueの完了条件、変更ファイル、テスト結果、未解決事項を残す。
