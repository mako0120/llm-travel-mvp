# CLAUDE.md

Claude Code がこのリポジトリで作業する際のガイドです。ブランチ命名・Issue駆動・安全境界などの共通規約は @AGENTS.md を参照してください(ここではこのアプリ固有の技術情報のみ記載します)。

## プロジェクト概要
- Next.js 15 (App Router, TypeScript) + Supabase
- デプロイ: Vercel(mainブランチへのpushで自動デプロイ)
- CI: GitHub Actions(.github/workflows/ci.yml — lint / typecheck / build)

## コマンド
- `npm run dev` — 開発サーバー起動
- `npm run lint` — ESLint
- `npm run typecheck` — 型チェック
- `npm run build` — 本番ビルド
- `npm run test` — `.github/scripts/` 配下のpreflightロジック単体テスト(Node標準テストランナー)

## このアプリ固有の規約
- Supabaseクライアントは lib/supabase/ のものを使う
  - Server Components / Route Handlers → `lib/supabase/server.ts`
  - Client Components → `lib/supabase/client.ts`
- 環境変数は .env.local(コミット禁止)。テンプレートは .env.local.example
- service_role キーは絶対にクライアント側コードや NEXT_PUBLIC_ 変数に入れない
- コミット前に lint と typecheck を通すこと
