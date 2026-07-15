import { createClient } from "@/lib/supabase/server";

export default async function Home() {
  let supabaseStatus: "connected" | "not-configured" | "error" = "not-configured";

  if (
    process.env.NEXT_PUBLIC_SUPABASE_URL &&
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
  ) {
    try {
      const supabase = await createClient();
      // 認証エンドポイントへの軽い疎通確認(テーブル不要)
      const { error } = await supabase.auth.getSession();
      supabaseStatus = error ? "error" : "connected";
    } catch {
      supabaseStatus = "error";
    }
  }

  return (
    <main>
      <h1>Next.js + Supabase Starter</h1>
      <p>
        このプロジェクトには Next.js (App Router)、Supabase クライアント、GitHub
        Actions の CI、Vercel デプロイ設定が含まれています。
      </p>
      <p className="status">
        Supabase:{" "}
        {supabaseStatus === "connected" && <strong className="ok">接続OK</strong>}
        {supabaseStatus === "not-configured" && (
          <strong className="warn">
            未設定 — <code>.env.local</code> に URL と anon key を設定してください
          </strong>
        )}
        {supabaseStatus === "error" && (
          <strong className="warn">接続エラー — キーとURLを確認してください</strong>
        )}
      </p>
    </main>
  );
}
