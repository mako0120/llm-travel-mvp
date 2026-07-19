import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
  title: "見積準備AI（検証用デモ）— リフォーム会社向け",
  description:
    "問い合わせの不足情報・返信優先度・確認事項を整理する、地域密着型リフォーム会社向けの検証用デモです。",
};

const PROBLEMS = [
  {
    number: "01",
    title: "聞き直しが何度も発生",
    body: "工事内容、住所、予算、希望時期がそろわず、電話やLINEの往復が増えてしまう。",
  },
  {
    number: "02",
    title: "急ぎの相談が埋もれる",
    body: "雨漏りなどの緊急案件と、検討段階の相談を同じように扱い、初動が遅れてしまう。",
  },
  {
    number: "03",
    title: "現場への引き継ぎがバラバラ",
    body: "担当者ごとにメモの内容が違い、現地調査の前にもう一度確認が必要になる。",
  },
];

const STEPS = [
  ["問い合わせを入力", "電話・Web・LINEで受けた内容を、分かる範囲だけ入力します。"],
  ["不足と優先度を整理", "見積もり前に足りない情報と、最初に聞く質問をその場で表示します。"],
  ["担当者へ引き継ぐ", "次にやることが明確になり、現地調査までの往復を減らせます。"],
];

export default function Home() {
  return (
    <main className="landing-main">
      <section className="renovation-hero">
        <div className="hero-copy">
          <p className="eyebrow">小規模リフォーム・修繕会社向け</p>
          <h1>問い合わせを、<br /><em>見積もれる状態</em>に。</h1>
          <p className="lead">
            電話やLINEで届く相談から、不足情報・返信優先度・最初に聞くことを3分で整理。
            営業事務が少ない会社の、見積もり前の往復を減らします。
          </p>
          <div className="cta-row">
            <Link href="/estimate-intake" className="button button-primary">
              無料デモを試す
            </Link>
            <a href="#how-it-works" className="button button-secondary">
              できることを見る
            </a>
          </div>
          <ul className="trust-list">
            <li>登録不要</li>
            <li>外部送信なし</li>
            <li>約3分</li>
          </ul>
        </div>
        <div className="hero-preview" aria-label="診断結果の見本">
          <div className="preview-topline"><span>見積準備度</span><strong>71%</strong></div>
          <div className="readiness-track"><span style={{ width: "71%" }} /></div>
          <div className="preview-row"><span className="preview-icon danger">!</span><div><small>不足情報</small><strong>予算・希望時期</strong></div></div>
          <div className="preview-row"><span className="preview-icon warn">→</span><div><small>次にやること</small><strong>不足情報をまとめて確認</strong></div></div>
          <span className="priority-badge priority-medium">優先</span>
        </div>
      </section>

      <section className="landing-section proof-strip" aria-label="サービスの特徴">
        <div><strong>3分</strong><span>で問い合わせ整理</span></div>
        <div><strong>0円</strong><span>でデモを確認</span></div>
        <div><strong>保存なし</strong><span>で安全に試せる</span></div>
      </section>

      <section className="landing-section" aria-labelledby="problems-heading">
        <p className="section-label">よくある課題</p>
        <h2 id="problems-heading">見積もり前の「確認作業」に、時間を取られていませんか？</h2>
        <div className="problem-grid">
          {PROBLEMS.map((problem) => (
            <article className="problem-card" key={problem.number}>
              <span>{problem.number}</span>
              <h3>{problem.title}</h3>
              <p>{problem.body}</p>
            </article>
          ))}
        </div>
      </section>

      <section id="how-it-works" className="landing-section how-section" aria-labelledby="how-heading">
        <p className="section-label">使い方</p>
        <h2 id="how-heading">専門知識は不要。3ステップで整理できます。</h2>
        <ol className="renovation-steps">
          {STEPS.map(([title, body], index) => (
            <li key={title}>
              <span>{index + 1}</span>
              <div><h3>{title}</h3><p>{body}</p></div>
            </li>
          ))}
        </ol>
      </section>

      <section className="landing-section offer-section">
        <div>
          <p className="section-label">先着3社・有料モニター（仮）</p>
          <h2>御社の受付方法に合わせて、30日間試せます。</h2>
          <p>初期設定19,800円・月額4,980円を想定。現在は需要検証中で、契約・決済は行いません。</p>
        </div>
        <Link href="/estimate-intake" className="button button-primary">
          まず無料デモを試す
        </Link>
      </section>
    </main>
  );
}
