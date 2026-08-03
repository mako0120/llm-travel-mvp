# 調査: groundcoverの「AI時代の観測性」シリーズC調達(2026年7月29日発表)

## 調査目的と問い

2026年7月29日、eBPF・OpenTelemetryネイティブの観測性(オブザーバビリティ)
プラットフォームを提供するgroundcoverが、シリーズCとして1億ドルを調達したと
発表した。

- 何が発表されたのか。調達額・投資家・累計調達額はどこまで確かか
- groundcoverは何をする会社なのか。「AI時代の観測性」とは何を指すのか
- 「Datadogを置き換える」という強気の発言はどこまで確認できる事実か
- 確認できなかったことは何か
- **鮮度についての正直な報告**: 発表日は着手日(2026-08-03)の5日前であり、
  `docs/06_Content_R&D.md`の鮮度基準(前日以内)を厳密には満たしていない

## 検証済み事実(出典付き)

### 発表: groundcover シリーズC調達(2026-07-29)

| 項目 | 内容 | 出典 |
|---|---|---|
| 発表日 | 2026年7月29日 | BusinessWire(一次発表) / SiliconANGLE |
| 調達額 | シリーズCとして1億ドル | BusinessWire / Morgan Stanley |
| 累計調達額 | 1億6,000万ドル | BusinessWire |
| 主導投資家 | One Peak | BusinessWire |
| 参加投資家 | Morgan Stanley Expansion Capital(新規)、Zeev Ventures・Angular Ventures・Heavybit・Jibe(継続) | BusinessWire |
| 創業年 | 2021年 | groundcover公式サイト |
| CEO・共同創業者 | Shahar Azulay氏 | groundcover公式サイト |
| 事業内容 | eBPF(Linuxカーネル技術)とOpenTelemetry(テレメトリ収集のオープン標準)を用いた観測性プラットフォームを提供。「Bring Your Own Cloud」方式で、顧客データを自社クラウド環境内にとどめる設計 | BusinessWire / Axios |
| 成長数値 | 過去1年で年間経常収益(ARR)が3倍、従業員数が2倍に成長(自社発表値) | BusinessWire |
| 顧客数 | 有料顧客250社超(アーリーステージの技術企業からFortune 5企業まで)、過去1年で7桁ドル規模の契約を複数締結(自社発表値) | BusinessWire |

### CEOコメント・競合への言及(重要・慎重に扱う)

| 項目 | 内容 | 出典 |
|---|---|---|
| 強気の発言 | 「Datadogを置き換える。New Relicを置き換える。より良いスタックを構築している」(意訳) | groundcover公式ブログ / CTech |
| 価格モデルへの批判 | 「Datadogの価格モデルは老朽化が目立ち始めており、顧客はコストを正当化するのが難しくなっている」(意訳、Shahar Azulay氏) | CTech |
| 業界構造への言及 | 「既存のソリューションはすべて同じ原則の上に成り立っている。コードの挙動を理解するには膨大な量のデータが必要だが、情報量は増え続ける一方で、実際には企業は比例して大きな価値を得られないまま、より多くの費用を払っている」(意訳、Shahar Azulay氏) | TFiR |
| **「Datadogがアーキテクチャを模倣した」という見出し** | TechTimesが「Datadog Copied Its Challenger's Architecture」という見出しで報じているが、**これは同メディアの見出し・切り口による表現であり、Datadog社自身が模倣を認めたという意味ではない。groundcover側の視点に基づく主張として扱う** | TechTimes(2026-07-29) |

## 合理的推測(事実と区別する)

- 「Datadogを置き換える」という発言は、観測性市場の大手であるDatadogを
  名指しした強気なポジショニング戦略と考えられるが、実際の市場シェアの
  推移や顧客の乗り換え実績の具体的な数字は確認できていない
- 「AI時代の観測性」という打ち出し方から、AIエージェントの動作ログ・
  トレーシングという新しい需要を取り込もうとしていると考えられるが、
  具体的にどのAI関連顧客がどのように使っているかの個別事例は確認できて
  いない

## 不明(確認できなかったこと)

- groundcover社の公式プレスリリース(BusinessWire)原文全体はWebFetchの
  アクセス制限(403)により直接確認できず、複数媒体経由の要約に基づいている
  (ただしBusinessWireのURL自体は一次情報源として確認できている)
- 各投資家の出資比率・出資額の内訳
- 有料顧客250社の具体的な企業名(Fortune 5企業という言及はあるが個別の
  企業名は非公表)
- 「ARR3倍・従業員2倍」の算出期間の正確な起点・終点
- Datadogとの間で実際にどの程度の顧客の乗り換えが起きているかの独立した数字

## 鮮度に関する正直な報告(重要)

**本テーマの発表日は2026年7月29日で、着手日(2026-08-03)の5日前である。**
`docs/06_Content_R&D.md`の鮮度基準(着手日の前日以内)を厳密には満たして
いない。2026-08-03に3ラウンド実施したトレンド調査(round43)で、着手日・
前日に該当する70点以上の新規候補が見つからず、検索クエリを変える・回数を
増やす等の努力を尽くしても見つからなかったため、鮮度で妥協してこのテーマを
採用した。詳細はテーマ評価表(round43)を参照。

## 判定

**adopt(鮮度で妥協、正直に開示)** — BusinessWire(一次発表)に加え、
SiliconANGLE・Morgan Stanley・Axios・CTech・TechTimesという独立した複数の
テック専門メディアが同じ発表を報じている。「調達額1億ドル・累計1.6億ドル」
「ARR3倍・従業員2倍」「有料顧客250社超」「Datadogを名指しした強気な発言」
という具体的で検証しやすい内容が揃っており、30枚のスライド化に耐える。
既存64本目(DataBahn、データコントロールプレーン)とは対象領域(観測性 vs
データパイプライン管理)が異なり差別化できる。ただし発表日が着手日の5日前
であるという鮮度の妥協点、および「Datadogがアーキテクチャを模倣した」という
見出しがgroundcover側・一部メディアの視点による表現である点を、成果物内で
明示して扱う。

## 出典一覧

- BusinessWire(一次発表, 2026-07-29): https://www.businesswire.com/news/home/20260729686071/en/groundcover-Raises-$100-Million-Series-C-to-Create-the-Observability-Platform-Built-for-the-AI-Era
- SiliconANGLE(2026-07-29): https://siliconangle.com/2026/07/29/cloud-observability-startup-groundcover-raises-100m-funding/
- Morgan Stanley: https://www.morganstanley.com/im/en-ch/intermediary-investor/insights/press-release/groundcover-raises-100m-series-c-to-create-the-observability-platform-built-for-the-ai-era.html
- Axios(2026-07-29): https://www.axios.com/pro/enterprise-software-deals/2026/07/29/observability-groundcover-100-million-one-peak
- CTech: https://www.calcalistech.com/ctechnews/article/r19aupvrme
- TechTimes(2026-07-29): https://www.techtimes.com/articles/322149/20260729/datadog-copied-its-challengers-architecture-that-challenger-just-raised-100m.htm
- TFiR: https://tfir.io/we-are-building-a-better-stack-than-datadog-and-new-relic-shahar-azulay-groundcover/
- 詳細な出典は
  `ai-company-os/research/2026-08-03_theme-evaluation-round43.md`も参照。
