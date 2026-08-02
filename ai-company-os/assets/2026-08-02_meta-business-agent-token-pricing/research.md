# 調査: Meta Business Agentのトークン課金移行(2026年8月1日発効)

## 調査目的と問い

2026年8月1日、Meta社がWhatsApp・Instagram・Messenger上で提供するAIエージェント
「Meta Business Agent」の料金体系が、無料お試し期間からトークン単位の従量課金
(100万トークンあたり2.00ドル)へ移行した。

- Meta Business Agentとは何か。いつから、どこで使われてきたのか
- 何が変わったのか。新料金体系の具体的な数字はどこまで確かか
- なぜこのタイミングで課金化するのか(今後の予定を含む)
- 確認できなかったことは何か

## 検証済み事実(出典付き)

### 製品: Meta Business Agent

| 項目 | 内容 | 出典 |
|---|---|---|
| 対応プラットフォーム | WhatsApp、Instagram、Messenger | TechTimes / Enterprise DNA |
| グローバル展開開始日 | 2026年6月3日 | Enterprise DNA |
| 展開前のテスト期間 | インド・メキシコ・ブラジルで約2年間のテストを実施 | Enterprise DNA |
| 展開時点の利用実績 | 100万以上の事業者が利用、Meta各メッセージングサービス全体で1日あたり10億件超のビジネス関連スレッドが発生 | Enterprise DNA |
| 主な機能 | 商品カタログ・Webサイト・FAQに基づく質問応答、商品レコメンド、カレンダー連携による予約受付、見込み顧客の選別(クオリファイ)、取引の完了まで、人手を介さず自律的・複数ステップで実行 | Enterprise DNA / Pragma-Code |

### 発表: トークン課金への移行(発効日2026-08-01)

| 項目 | 内容 | 出典 |
|---|---|---|
| 発効日 | 2026年8月1日 | TechTimes / BusinessToday / Thrumos |
| 新料金体系 | トークン単位の従量課金、100万トークンあたり2.00ドル | TechTimes / Thrumos |
| 目安のメッセージ単価 | 1メッセージあたり2万〜2万5,000トークン消費、概算で1メッセージあたり4〜5セント | TechTimes / Enterprise DNA |
| 複雑な会話の単価 | 複雑な会話では最大約0.24ドル程度になる場合がある | TechTimes(要約) |
| 課金の統合 | 従来は「AI処理料金」と「メッセージ配信料金」が別々の項目だったが、今回のトークン単位料金に一本化される | Enterprise DNA |
| 対象範囲 | WhatsApp・Instagram・Messengerの全世界で適用 | TechTimes / BusinessToday |
| 今後の予定 | 2026年10月1日、テンプレート外のサービスメッセージについても課金を再開する予定(過去2年間停止されていた課金) | Enterprise DNA |

## 合理的推測(事実と区別する)

- 100万以上の事業者・1日10億件超のスレッドという利用規模の大きさから、Meta社は
  無料お試し期間を通じて十分な利用実績とデータを蓄積した上で、収益化に踏み切った
  と考えられるが、収益化の意思決定の具体的な社内的理由(投資回収計画等)は
  一次情報から確認できていない
- 課金体系を「AI処理料金」と「メッセージ配信料金」に分けず一本化したことから、
  料金体系のシンプル化・分かりやすさを意図していると考えられるが、これも推測で
  あり、Meta社自身がそのように説明しているかは確認できていない

## 不明(確認できなかったこと)

- Meta社自身による公式プレスリリース・ヘルプセンター記事の原文全体
  (WebFetchのアクセス制限(403)により直接確認できず、複数の解説メディア経由の
  要約に基づいている)
- 有料化後、実際にどの程度の事業者が利用を継続・解約したかという定量データ
  (制度変更の発効直後であり、影響の実測値はまだ存在しないと考えられる)
- 日本国内での具体的な導入事業者数・利用実態(WhatsAppは日本国内での利用率が
  他国に比べて低く、Instagram・Messenger経由の日本国内利用実態も個別の数字は
  確認できていない)
- トークン単価($2.00/100万トークン)の算出根拠・原価との関係

## 判定

**adopt** — 課金制度の発効日が2026年8月1日(着手日の前日)であり、鮮度基準
(前日以内)を満たす。TechTimes・Enterprise DNA・BusinessToday・GREEN-API・
Thrumos・Mintec等の独立した複数のテック/ビジネス専門メディアが同じ制度変更を
報じている。「1メッセージ2万〜2万5,000トークン」「100万トークン2.00ドル」
「1会話4〜5セント」という具体的な数字と、100万事業者・1日10億スレッドという
利用規模の数字が揃っており、30枚のスライド化に耐える。既存64テーマに
「AIエージェントの無料から有料への移行」という料金制度の変化を扱ったものは
なく差別化できる。ただし公式原文全体・有料化後の実測影響・日本国内の利用実態は
確認できておらず、成果物内で明示して扱う。

## 出典一覧

- TechTimes(2026-07-16): https://www.techtimes.com/articles/320787/20260716/meta-business-agent-billing-starts-aug-1-free-test-window-ends-days.htm
- Enterprise DNA: https://enterprisedna.co/resources/news/meta-business-agent-billing-august-1-token-pricing-2026/
- Enterprise DNA(製品概要): https://enterprisedna.co/resources/news/meta-whatsapp-business-agent-enterprise-solutions-2026/
- BusinessToday(2026-07-03): https://www.businesstoday.in/technology/artificial-intelligence/story/whatsapp-introduces-token-based-pricing-for-ai-agents-from-august-1-540699-2026-07-03
- GREEN-API: https://green-api.com/articles/en/whatsapp-changes-rates-for-companies-and-business/
- Thrumos: https://www.thrumos.com/insights/meta-whatsapp-business-ai-agent-token-pricing-august-2026
- Pragma-Code: https://www.pragma-code.de/en/blog-whatsapp-business-ai-agent
- テーマ評価の記録: `ai-company-os/research/2026-08-02_theme-evaluation-round40.md`
