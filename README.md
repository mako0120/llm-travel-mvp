# 宿泊施設向け多言語返信AI(構想LP・検証用デモ)

Next.js (App Router) / Supabase / Vercel / GitHub Actions / Claude Code 用スターターの上に、
小規模宿泊施設向け多言語返信AIの市場検証用LPと固定サンプルによるクリックデモを実装しています。

## デモについて

- `/` — 課題・対象・価値・使い方・仮価格・注意事項を掲載したLP
- `/demo` — 4種類の固定サンプル(英語・中国語・韓国語)から選び、日本語要約・緊急度・規約確認・外国語返信案の見え方を確認できるクリックデモ
- 固定サンプルのみを扱う検証用デモであり、外部AI・外部API・認証・データベース・データ保存・自動送信は一切行いません
- 返信案はあくまで参考表示であり、実際の送信は必ず人が内容を確認したうえで行うことを前提にしています
- 価格は仮のものであり、正式な価格ではありません

## セットアップ

```bash
npm install
cp .env.local.example .env.local   # Supabaseのキーを記入(LP・デモ自体はSupabase未設定でも動作します)
npm run dev
```

## 構成
- `app/page.tsx` — LP(課題・対象・価値・使い方・仮価格・注意事項)
- `app/demo/` — 固定サンプルによるクリックデモ(`page.tsx` / `reply-demo.tsx`)
- `app/layout.tsx` / `app/globals.css` — 共通レイアウトとスタイル、検証用デモである旨のバナー
- `lib/supabase/` — Supabaseクライアント(server / client。現在のLP・デモでは未使用)
- `.github/workflows/ci.yml` — CI(lint / typecheck / build)
- `CLAUDE.md` / `AGENTS.md` — Claude Code / AI開発ワークフロー用ガイド

## デプロイ
mainブランチへのpushでVercelが自動デプロイします。
環境変数(NEXT_PUBLIC_SUPABASE_URL / NEXT_PUBLIC_SUPABASE_ANON_KEY)はVercelのProject Settingsに設定してください(LP・デモ自体は未設定でも動作します)。
