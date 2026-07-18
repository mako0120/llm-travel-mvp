import Link from "next/link";

const PROBLEMS = [
  {
    title: "言語の壁で対応が遅れる",
    body: "外国語のメッセージを翻訳ツールと辞書を行き来しながら読み解くだけで時間がかかり、他の業務が止まってしまう。",
  },
  {
    title: "返信が遅れて評価が下がる",
    body: "確認・翻訳・返信文の作成に時間がかかるうちにレビュー評価が下がったり、予約のキャンセルにつながることがある。",
  },
  {
    title: "規約確認が漏れがちになる",
    body: "キャンセルポリシーや追加料金など、施設ごとの規約を都度確認する余裕がなく、対応が施設ルールとずれてしまう。",
  },
];

const VALUE_STEPS = [
  {
    title: "メッセージを貼り付け",
    body: "ゲストから届いた外国語メッセージをそのまま貼り付けます。",
  },
  {
    title: "AIが要点を整理",
    body: "日本語要約・緊急度・規約確認ポイント・外国語の返信案を数秒で提示します。",
  },
  {
    title: "人が確認して送信",
    body: "内容を確認し、必要なら編集してから、必ず人の判断でご自身で送信します。自動送信は行いません。",
  },
];

const TARGETS = [
  "外国語対応スタッフが少ない、または不在の小規模宿泊施設",
  "民泊・ゲストハウス・小規模ホテルを運営するオーナー・スタッフ",
  "予約サイトやSNS経由で外国語メッセージを受け取ることが増えている施設",
];

export default function Home() {
  return (
    <main>
      <section className="hero">
        <p className="eyebrow">宿泊施設向け 多言語返信AI(構想デモ)</p>
        <h1>外国語メッセージへの返信、もう迷わない。</h1>
        <p className="lead">
          ゲストからの外国語メッセージを貼るだけで、日本語要約・緊急度・規約確認・外国語の返信案を提示します。
          最終確認と送信は、いつも通りあなたが行います。
        </p>
        <div className="cta-row">
          <Link href="/demo" className="button button-primary">
            固定サンプルのデモを試す
          </Link>
          <Link href="/roi-demo" className="button button-secondary">
            ROI計算デモを試す
          </Link>
          <Link href="/workbench" className="button button-secondary">
            実運用に近いワークベンチを試す
          </Link>
        </div>
        <p className="hero-note">
          このLPとデモは市場検証用の構想段階の資料です。デモは固定サンプルのみを扱い、外部AI・外部送信・データ保存は行いません。
        </p>
      </section>

      <section className="section" aria-labelledby="problems-heading">
        <h2 id="problems-heading">こんな課題はありませんか</h2>
        <div className="card-grid">
          {PROBLEMS.map((problem) => (
            <div className="card" key={problem.title}>
              <h3>{problem.title}</h3>
              <p>{problem.body}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="section" aria-labelledby="target-heading">
        <h2 id="target-heading">対象施設</h2>
        <ul className="check-list">
          {TARGETS.map((target) => (
            <li key={target}>{target}</li>
          ))}
        </ul>
      </section>

      <section className="section" aria-labelledby="value-heading">
        <h2 id="value-heading">使い方(3ステップ)</h2>
        <ol className="step-list">
          {VALUE_STEPS.map((step, index) => (
            <li key={step.title}>
              <span className="step-number" aria-hidden="true">
                {index + 1}
              </span>
              <div>
                <h3>{step.title}</h3>
                <p>{step.body}</p>
              </div>
            </li>
          ))}
        </ol>
      </section>

      <section className="section" aria-labelledby="pricing-heading">
        <h2 id="pricing-heading">想定価格(仮)</h2>
        <p className="price">
          月額 <strong>仮 ¥5,000〜</strong>(施設規模により変動)
        </p>
        <p className="muted">
          正式な価格ではありません。今後のヒアリングと検証を踏まえて決定します。
        </p>
      </section>

      <section className="section notice-section" aria-labelledby="notice-heading">
        <h2 id="notice-heading">ご利用にあたっての注意事項</h2>
        <ul className="notice-list">
          <li>本ページと `/demo` は市場検証用の構想LP・固定サンプルによる検証用デモです。</li>
          <li>外部AI・外部API・認証・データベースへの通信や保存は一切行いません。</li>
          <li>返信案は参考情報です。内容を確認したうえで、必ず人が判断して送信してください。自動送信は行いません。</li>
          <li>価格・仕様は仮のものであり、今後変更される可能性があります。</li>
        </ul>
      </section>

      <section className="section cta-section" aria-labelledby="cta-heading">
        <h2 id="cta-heading">3分でデモを試す</h2>
        <p>3種類以上の固定サンプルから選んで、実際の見え方を確認できます。</p>
        <Link href="/demo" className="button button-primary">
          固定サンプルのデモを試す
        </Link>
      </section>
    </main>
  );
}
