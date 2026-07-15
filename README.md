# Next.js + Supabase Starter

Next.js (App Router) / Supabase / Vercel / GitHub Actions / Codex 用スターター。

## セットアップ

```bash
npm install
cp .env.local.example .env.local   # Supabaseのキーを記入
npm run dev
```

## 構成
- `app/` — App Router のページ
- `lib/supabase/` — Supabaseクライアント(server / client)
- `.github/workflows/ci.yml` — CI(lint / typecheck / build)
- `CONTRIBUTING.md` — 人間・Codex共通の開発ルール
- `docs/` — ChatGPT / Codex の役割とAI開発会社の運用ルール

## デプロイ
mainブランチへのpushでVercelが自動デプロイします。
環境変数(NEXT_PUBLIC_SUPABASE_URL / NEXT_PUBLIC_SUPABASE_ANON_KEY)はVercelのProject Settingsに設定してください。
