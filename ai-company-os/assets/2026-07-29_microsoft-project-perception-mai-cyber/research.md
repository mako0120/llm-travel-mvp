# 調査: Microsoft「Project Perception」+ 初のサイバーセキュリティモデル「MAI-Cyber-1-Flash」(2026-07-27)

## 調査目的と問い

`research/2026-07-24_theme-evaluation-round30.md`(2026-07-29実施)で、本候補は75点の次点として
「次サイクル以降の候補として残す」と記録されていた。定期実行52本目の着手にあたり、
`docs/06_Content_R&D.md`の「常に最新の原則」(2026-07-24追記)に従い、過去の候補をそのまま
使い回さず、着手時点(2026-07-29)の最新ニュースを再確認したうえで、なお本候補が最良かを判断する。

- 着手日(2026-07-29)時点で、本候補を上回るAI/エージェント系の新規候補は見つかるか
- Microsoft「MAI-Cyber-1-Flash」「Project Perception」は何を発表したのか
- 「90%のタスクを処理」「コスト半減」「ベンチマークで高スコア」という数字はどこまで確かか
- 確認できなかったことは何か

## 着手時点の再調査(常に最新の原則)

2026-07-29時点でのAI/エージェント系ニュースをあらためて検索した(2クエリ)。
Businessolver(オンボーディングAI・データゲートウェイ、2026-07-28)、Cyabra
「Coordinated Activity」(協調的な不審行動を調査するAIエージェント、2026-07-28)、
RHA Technologies「RHA OneAI」(2026-07-27、大口顧客4社と契約)、Unstop(採用向け
AIエージェント7種、2026-07-27)を確認したが、いずれも一次情報の厚み・著名度・
視聴者関心の広さでMicrosoftの公式発表(著名メディア多数が報じる大手ベンダーの
自社開発モデル発表)に及ばないと判断した。round30時点の評価(75点)を覆す
新規候補は見つからなかったため、本候補の採用を維持する。

## 検証済み事実(出典付き)

### 発表: MAI-Cyber-1-Flash + Project Perception(2026-07-27、サンフランシスコでのイベント)

| 項目 | 内容 | 出典 |
|---|---|---|
| 発表日 | 2026-07-27(月、サンフランシスコでのイベント) | Microsoft AI 公式ニュース(本文403、検索結果の要約経由) / TechCrunch / Axios |
| MAI-Cyber-1-Flashとは | Microsoft初のサイバーセキュリティ専用AIモデル | Microsoft AI公式 / SecurityWeek / Help Net Security |
| 組み込み先 | MDASH(Microsoftの脆弱性検出・修復を行うマルチエージェントシステム) | 同上 |
| レビュー体制 | Microsoft AI Red Teamによるレビュー、敵対的テスト、外部機関による評価を実施したと説明 | Microsoft AI公式(検索結果要約経由) |
| Project Perceptionとは | Red・Blue・Greenの3エージェントが連携し、攻撃シミュレーション・リスク評価・パッチ作成と展開を行うエージェント型セキュリティ基盤 | TechCrunch / Axios / Constellation Research |
| 一般提供(パブリックプレビュー) | 2026年8月3日開始と報じられている | winbuzzer |

### モデルの技術仕様(検索結果による報道経由、モデルカード由来とされる)

| 項目 | 内容 |
|---|---|
| アーキテクチャ | Sparse Mixture-of-Expertsトランスフォーマー |
| 総パラメータ数 | 1,370億(137B) |
| アクティブパラメータ数 | 50億(5B) |
| コンテキスト長 | 256,000トークン |
| 系譜 | 「MAI-Thinking-1」系列から派生 |
| 学習・参照データ | ID・エンドポイント・クラウド・ネットワーク領域で1日あたり100兆件超のセキュリティ信号を参照するとされる |

出典: Help Net Security / SecurityWeek / winbuzzer(いずれも検索結果の要約経由。本文は403で直接確認できず)

### 性能・コストに関する主張(Microsoft側の説明)

| 数字 | 内容 | 注記 |
|---|---|---|
| 約90% | MAI-Cyber-1-Flashが日常的なセキュリティタスクの約90%を処理し、GPT-5.4は残り約10%の難しい判断だけを担うとされる | Microsoft側の設計意図の説明 |
| 50%削減 | MDASHの現行構成と比べてコストを50%削減できるとされる | 比較対象は「Microsoft自身の現行MDASH構成」であり、他社製品との比較ではない |
| CyberGymベンチマーク | GPT-5.4と組み合わせた場合のスコアとして、報道により**「96%」とする記事と「95.95%」とする記事の2種類が見られた** | **数値が記事間で一致しておらず、原典(モデルカード)を直接確認できていないため、本成果物ではどちらか一方を断定しない** |

## 合理的推測(事実と区別する)

- 「専用の小型モデルに大半の仕事を任せ、汎用の大型モデルは難しい判断だけに使う」という
  役割分担は、コスト最適化の一般的な設計思想と合致するが、Microsoftがこれを業界の
  トレンドとして意図的に主導しているとまで断定はできない
- Project Perceptionの3エージェント名(Red/Blue/Green)は、セキュリティ業界で
  一般的な「レッドチーム/ブルーチーム」の用語を踏襲したものと推測されるが、
  この命名意図についてMicrosoftが明言したことは確認できていない

## 不明(確認できなかったこと)

- **公式ニュース(microsoft.ai)・TechCrunch・SecurityWeek・Help Net Security・
  The Hacker News・winbuzzerの6サイトすべてにWebFetchで本文取得を試みたが、
  いずれもHTTP 403で本調査環境から取得できなかった。** 本研究の事実はすべて
  検索エンジンが返した要約経由での確認であり、通常より事実誤認のリスクが高い
  ことを明記する
- CyberGymベンチマークの正確なスコア(96%か95.95%か)。原典のモデルカードを
  確認できていない
- 検索結果の一部に、他社の特定モデルとの比較値(ポイント差)を示す記述が
  見られたが、**モデル名・数値ともに一次情報で確認できないため、本成果物では
  使用しない**
- MDASHの正式名称(略称の展開)
- 日本国内での提供時期・価格・日本語対応状況
- 「約90%」「50%削減」という数字の第三者による独立検証(いずれもMicrosoft自身の説明)
- Project Perceptionの3エージェントという名称の命名意図

## 判定

**adopt** — round30で75点と評価され「次サイクル以降の候補」として明示的に残されていた候補であり、
着手時点(2026-07-29)で再確認した最新ニュースの中にもこれを上回る候補は見つからなかった。
大手ベンダー(Microsoft)による公式発表であり複数の独立した専門メディアが報じている点で
裏付けは十分だが、発表から2日後の着手であること、ベンチマーク数値に記事間の食い違いが
あること、他社比較の数値は使用しないことを成果物内で明示する。

## 出典一覧

- Microsoft AI 公式ニュース(2026-07-27、本文403で直接取得できず): https://microsoft.ai/news/introducing-mai-cyber-1-flash-inside-mdash/
- TechCrunch(2026-07-27): https://techcrunch.com/2026/07/27/microsoft-launches-its-first-cyber-model-and-a-new-agentic-cybersecurity-system/
- Axios(2026-07-27): https://www.axios.com/2026/07/27/microsoft-unveils-new-cyber-model-agentic-security-tools-to-fight-hackers
- SecurityWeek: https://www.securityweek.com/microsoft-unveils-mai-cyber-1-flash-its-first-cybersecurity-ai-model/
- Help Net Security(2026-07-27): https://www.helpnetsecurity.com/2026/07/27/microsoft-mai-cyber-1-flash-ai-model/
- The Hacker News: https://thehackernews.com/2026/07/microsoft-says-new-cybersecurity-ai.html
- winbuzzer(2026-07-28、パブリックプレビュー日程): https://winbuzzer.com/2026/07/28/microsoft-says-cyber-ai-can-cut-bug-finding-costs-xcxwbn/
- Constellation Research: https://www.constellationr.com/insights/news/microsoft-launches-mai-cyber-1-flash-security-model-project-perception
- 次点評価の記録: `ai-company-os/research/2026-07-24_theme-evaluation-round30.md`
