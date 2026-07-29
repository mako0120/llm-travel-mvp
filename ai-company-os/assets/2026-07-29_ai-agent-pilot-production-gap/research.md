# 調査: AIエージェントの実証実験、88%が本番に届かない(2026-07-28)

## 調査目的と問い

2026年7月28日、CognizantがEMEA(欧州・中東・アフリカ)向けのAI専門組織を新設した。
その発表の背景として「AIエージェントの実証実験の大半が本番運用に届いていない」という
IDCの数字が引用されている。

- 何が発表されたのか
- 「88%が本番に届かない」という数字はどこまで確かなのか
- 何が原因とされているのか
- 確認できなかったことは何か

## 検証済み事実(出典付き)

### 発表: Cognizant「EMEA AI Unit」新設(2026-07-28)

| 項目 | 内容 | 出典 |
|---|---|---|
| 発表日 | 2026-07-28 | Cognizant 公式ニュースルーム(URLに日付) / PR Newswire |
| 内容 | EMEA(欧州・中東・アフリカ)の企業がAIエージェントを本番運用へ広げるのを支援する専門組織を新設 | 公式リリース |
| 提供体制の名称 | Frontier Deployed Engineering(3層モデル) | 公式リリース / aithority |
| 立場 | 特定のクラウド・モデル・エコシステムに依存しない中立を掲げる | 公式リリース |
| 発言者 | Manoj Mehta氏(Cognizant EMEA プレジデント) | 公式リリース |

### Frontier Deployed Engineering の3層

| 層 | 対処する段階 | 内容 |
|---|---|---|
| Foundation | 構想・土台づくり | AI戦略、ガバナンス設計、技術選定、エージェントが事実を取り違えないようにするための情報の裏付け(RAG)の層 |
| Accelerate | 統合 | 既存システムとのつなぎ込み。エージェントが最も止まりやすい段階を「AIファクトリー」として再利用可能な形にし、開発期間を数か月から数日に圧縮するとされる |
| Transform | 全体設計の作り直し | 複数エージェントによる開発チームで業務そのものを設計し直し、成果に対する責任まで担う |

※ 「数か月から数日」はCognizant側の説明であり、第三者検証ではない。

### 背景の数字

| 数字 | 内容 | 出典 | 扱い |
|---|---|---|---|
| 88% | AIエージェントの実証実験(PoC)の88%が、広範な本番運用に到達しない | IDC(TechTimes・CIO等が引用) | 二次情報経由。原典は未確認 |
| 33件 → 4件 | 企業が33件のパイロットを立ち上げても、実際の運用に入るのは4件 | 同上 | 88%と同じ調査に基づく表現 |
| 原因 | モデルの品質ではなく、**データ・業務プロセス・IT基盤という組織側の準備の低さ**にIDCは原因を帰している | 同上 | この帰属が本テーマの要点 |

### 発言(引用)

> EMEA全域で、多くの組織がAIに前向きである一方、その勢いを実際の事業価値へ
> どう変えるかを模索している段階にある。

— Manoj Mehta氏(Cognizant EMEA プレジデント)。公式リリースより要約。

## 合理的推測(事実と区別する)

- コンサルティング会社が専門組織を新設したこと自体は、**この分野に需要があると
  同社が判断した**ことを示すが、需要の大きさや成約実績を示すものではない
- 3層モデルのうち「統合(Accelerate)」を独立した層として置いていることは、
  IDCの指摘(組織側の準備が原因)と整合するが、両者を結びつけているのは
  この調査の解釈であり、Cognizantが明示的にそう述べたかは確認できていない

## 不明(確認できなかったこと)

- **公式ニュースルーム・PR Newswire・TechTimes・aithority・StockTitan・CIO の
  本文はすべてHTTP 403で本調査環境から取得できなかった。** 内容は検索エンジンが
  返した要約経由での確認である
- **IDC調査の原典**(調査年・標本数・対象国・「広範な本番運用」の定義)。
  二次情報では「IDCがLenovoと2025年に実施」とされるが、原典にはあたれていない
- 「Cognizant株が7%上昇」という見出しが複数の株式情報サイトに現れたが、
  一次情報で確認できず、発表との因果関係も不明なため**成果物では使用しない**
- 別の調査(Gartner)に「89%」という近い数字があるとする記事もあったが、
  IDCの88%と同一の調査かどうか確認できないため**混ぜて使わない**
- 日本国内における同種の統計
- 新設組織の規模(人員数・投資額)

## 判定

**adopt** — 着手日の前日の発表であり、公式ニュースルームとPR Newswireという一次情報が
存在する。中心となる88%という数字は発表元以外(CIO誌等)でも同じ値が引用されており、
単一ベンダーの主張ではない。ただし原典を読めていないため、数字はすべて
「IDC調査より、報道経由」と帰属を明示して扱う。

## 出典一覧

- Cognizant 公式ニュースルーム(2026-07-28。本文は403で取得できず): https://news.cognizant.com/2026-07-28-Cognizant-launches-EMEA-AI-Unit-to-help-enterprises-scale-agentic-AI-adoption
- PR Newswire(公式リリース、2026-07-28): https://www.prnewswire.com/news-releases/cognizant-launches-emea-ai-unit-to-help-enterprises-scale-agentic-ai-adoption-302835936.html
- TechTimes(2026-07-28、IDCの数字を引用): https://www.techtimes.com/articles/321781/20260728/cognizant-launches-emea-ai-unit-enterprise-agent-pilots-fail-scale.htm
- aithority(3層モデルの説明): https://aithority.com/machine-learning/cognizant-launches-emea-ai-unit-to-help-enterprises-scale-agentic-ai-adoption/
- StockTitan(CTSH): https://www.stocktitan.net/news/CTSH/cognizant-launches-emea-ai-unit-to-help-enterprises-scale-agentic-ai-m8d3c107psy3.html
- CanadianSME: https://canadiansme.ca/cognizant-launches-emea-ai-unit-to-help-enterprises-scale-agentic-ai-adoption/
- CIO(「88%のAIパイロットが本番に届かない」): https://www.cio.com/article/3850763/88-of-ai-pilots-fail-to-reach-production-but-thats-not-all-on-it.html
