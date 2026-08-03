# 調査: Onyx Security、AIエージェントを制御する「コントロールプレーン」でシリーズB1.13億ドル調達(2026年7月29日発表)

## 調査目的と問い

2026年7月29日、AIエージェントの一つ一つの行動を検査し、必要に応じて
ブロック・修正・人間承認へ転送する「セキュアAIコントロールプレーン」を
提供するイスラエル発のOnyx Securityが、シリーズBとして1億1,300万ドルを
調達、評価額6億4,000万ドルに到達したと発表した。

- 何が発表されたのか。調達額・評価額・投資家はどこまで確かか
- Onyx Securityは具体的に何をする会社なのか。「コントロールプレーン」とは何か
- Anthropicとの統合はどこまで確認できる事実か
- 確認できなかったことは何か
- **鮮度についての正直な報告**: 発表日は着手日(2026-08-03)の5日前であり、
  `docs/06_Content_R&D.md`の鮮度基準(前日以内)を厳密には満たしていない

## 検証済み事実(出典付き)

### 発表: Onyx Security シリーズB調達(2026-07-29)

| 項目 | 内容 | 出典 |
|---|---|---|
| 発表日 | 2026年7月29日 | BusinessWire |
| 調達額 | シリーズBとして1億1,300万ドル | BusinessWire / SecurityWeek |
| 評価額 | 6億4,000万ドル | CTech(Calcalist) |
| 主導投資家 | Bessemer Venture Partners | BusinessWire |
| 参加投資家 | Cyberstarts、TCV、Conviction、FirstMark、Vintage、QuantumLight、G Squared | BusinessWire |
| 累計調達額 | 1億5,300万ドル(創業からちょうど2年) | BusinessWire |
| 創業者・CEO | Maxim Bar Kogan氏 | BusinessWire |
| 事業内容 | AIエージェントの一つ一つの行動を検査し、ブロック・修正・人間承認への転送を行う「セキュアAIコントロールプレーン」 | BusinessWire / 複数媒体 |
| ステルス解除 | 2026年3月11日、4,000万ドルの資金とともにステルスを解除 | BusinessWire(2026-03-11) |

### CEOコメント・実績数値

| 項目 | 内容 | 出典 |
|---|---|---|
| CEOコメント(1) | 「ステルスを解除したことで、広く販売を開始できるようになった」(意訳) | BusinessWire |
| CEOコメント(2) | 「需要が想定を上回るペースで、目標に到達するのも早かった。それが大きな投資家の関心を呼び、想定より早くこのラウンドを調達できた」(意訳) | BusinessWire |
| 収益成長 | ステルス解除から4ヶ月で収益が4倍に成長 | BusinessWire |
| 制御しているエージェント数 | 企業導入全体で110万台超のAIエージェントを保護 | 複数媒体 |
| 解析セッション数 | 6,600万件超のセッションを解析 | 複数媒体 |
| Anthropicとの統合 | 2026年6月、AnthropicがOnyxの技術を統合し、企業顧客の安全なAI導入を支援すると発表。OpenAI・Amazon・Microsoft・Googleなど、既にプラットフォームに統合済みの数十社のAIプロバイダーの一つに加わった | 複数媒体 |

## 合理的推測(事実と区別する)

- 「AIエージェントを制御するためのAI」という需要が急拡大していることは、
  今回の資金調達の規模・スピードから推測できるが、これが業界全体の
  トレンドなのか、Onyx Security固有の成功要因が大きいのかは、本調査の
  範囲では判別できない
- Anthropicとの統合が「数十社のAIプロバイダーの一つ」という位置づけで
  あることから、Onyx側が特別に優遇された関係というより、業界標準的な
  連携の一つと考えられるが、契約条件の詳細は確認できていない

## 不明(確認できなかったこと)

- Onyx Security社自身による公式プレスリリースの原文全体(WebFetchのアクセス
  制限(403)により直接確認できず、複数媒体経由の要約に基づいている)
- 各投資家の出資比率・出資額の内訳
- 「収益4倍」の具体的な金額・算出方法
- Anthropicとの統合契約の詳細な条件
- 110万台・6,600万セッションという数字の集計期間・算出方法

## 鮮度に関する正直な報告(重要)

**本テーマの発表日は2026年7月29日で、着手日(2026-08-03)の5日前である。**
`docs/06_Content_R&D.md`の鮮度基準(着手日の前日以内)を厳密には満たして
いない。2026-08-03に実施したトレンド調査(round45、10クエリ)で、着手日・
前日に該当する70点以上の新規候補が見つからず、検索クエリを変える・回数を
増やす等の努力を尽くしても見つからなかったため、鮮度で妥協してこのテーマを
採用した。詳細はテーマ評価表(round45)を参照。

## 判定

**adopt(鮮度で妥協、正直に開示)** — BusinessWire(一次発表)・SecurityWeek・
Techzine Global・CTech・The Next Web・Times of Israel・VentureBurnという、
独立した複数のテック・セキュリティ専門メディアが同じ発表を報じている。
「AIエージェントを制御するAI」という直感的なコンセプト、110万台超の
エージェント制御・6,600万セッション解析という具体的な数字、Anthropicとの
統合という裏付けが揃っており、30枚のスライド化に耐える。既存71テーマに
「AIエージェント自体を監視・制御するプラットフォーム」を扱ったものはなく
差別化できる(70本目のOpenAI暴走エージェント事件とは、後者が実際に起きた
事故、本テーマがそれを防ぐための製品という関係で、対比する形で扱える)。

## 出典一覧

- BusinessWire(2026-07-29): https://www.businesswire.com/news/home/20260729713522/en/Onyx-Security-Raises-$113M-Series-B-to-Control-Advanced-AI-Quadrupling-Revenue-since-Stealth-Launch-Four-Months-Ago
- SecurityWeek: https://www.securityweek.com/onyx-security-raises-113-million-to-control-ai-agents-in-the-enterprise/amp/
- CTech(Calcalist): https://www.calcalistech.com/ctechnews/article/b1fsjydszg
- Techzine Global: https://www.techzine.eu/news/security/143304/onyx-raises-113-million-for-ai-agent-control/
- The Next Web: https://thenextweb.com/news/onyx-security-113m-series-b-ai-agent-control-plane
- Times of Israel: https://www.timesofisrael.com/israeli-cyber-startup-raises-113m-to-secure-and-control-autonomous-ai-agents/
- 詳細な出典は
  `ai-company-os/research/2026-08-03_theme-evaluation-round45.md`も参照。
