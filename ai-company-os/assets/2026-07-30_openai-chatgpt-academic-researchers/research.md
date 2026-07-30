# 調査: OpenAI「ChatGPT for Academic Researchers」発表(2026-07-29)

## 調査目的と問い

2026年7月29日、OpenAIが研究者向けの無償AIアクセスプログラム「ChatGPT for
Academic Researchers」を発表した。最終的に10万人の研究者への提供を目指す
という規模の大きさが特徴。

- 何が発表されたのか。誰が対象なのか
- 「2.5億ドル規模の科学支援イニシアチブ」とは何か
- モデル・利用条件はどこまで確かか
- 確認できなかったことは何か

## 検証済み事実(出典付き)

### 発表: OpenAI「ChatGPT for Academic Researchers」(2026-07-29)

| 項目 | 内容 | 出典 |
|---|---|---|
| 発表日 | 2026-07-29(水) | OpenAI公式 / TechTimes / SiliconANGLE / Axios |
| 規模 | 最初のコホート1万人から開始し、2027年までに10万人の研究者へ拡大 | OpenAI公式 / SiliconANGLE / AI Weekly |
| 提供モデル | GPT-5.6 Sol Pro(OpenAIの一般提供モデルの中で最も高性能) | Axios / TheNextWeb |
| 参加中の機関例 | プリンストン高等研究所(IAS)、仏エコール・ノルマル・シュペリウール(ENS) | SiliconANGLE |
| 上位イニシアチブ | 2027年までに2.5億ドル超を外部の科学研究・発見支援に投じるコミットメントの一部 | SiliconANGLE / TheNextWeb |
| 機関の対象条件 | 学位授与を行う、研究活動水準の高い、認定された大学・カレッジであること | OpenAI Help Center |
| 個人応募条件 | 対象機関に所属する研究教員またはポスドク研究者であり、直近3年以内にarXiv・bioRxiv・ChemRxivに投稿された対象分野(生物科学・化学材料・計算機科学・地球惑星科学・工学・数学・物理学)の論文の著者であること | OpenAI Help Center |
| 共同利用者 | 承認された研究者は所属機関から最大4名まで協力者を招待可能(協力者も所属確認が必要で、プログラムの総アカウント数に算入される) | OpenAI Help Center |
| アクセス期間 | 承認された研究者・ポスドクに専用ChatGPTワークスペースへの12か月間の無償アクセスを提供 | OpenAI Help Center |
| モデル重みの扱い | ChatGPTインターフェース経由の無償アクセスであり、モデルの重み自体は引き続き非公開 | TechTimes |

## 合理的推測(事実と区別する)

- 「モデル重みは非公開のまま」という論点は、AI業界で独立検証・再現性・
  安全性評価のために重みの公開を求める研究者コミュニティと、誤用防止を
  理由に非公開を続ける開発企業側の対立軸の一部として報じられている
  (この対立軸自体は複数の開発企業に共通する一般的な論点であり、
  本テーマではOpenAIの対応のみを事実として扱う)
- 複数の独立した媒体(TechTimes、SiliconANGLE、Axios、AI Weekly)が
  同時期に報じていることから、一定のニュースバリューがある発表だったと
  考えられる
- 対象分野が生物科学・化学材料・計算機科学・地球惑星科学・工学・数学・
  物理学に限定されていることから、人文社会科学系の研究者は対象外である
  可能性が高いと考えられるが、これを明言する一次情報は確認できていない

## 不明(確認できなかったこと)

- 日本の大学・研究機関がこのプログラムの対象に含まれるかどうか(調査時点で
  確認できた参加機関はプリンストン高等研究所・仏ENSのみ)
- GPT-5.6 Sol Proの具体的な利用回数上限・レート制限
- 2.5億ドルの科学支援イニシアチブ全体のうち、本プログラムに割り当てられる
  金額の内訳
- 審査・承認にかかる期間や、応募から利用開始までの具体的な所要日数
- 人文社会科学系分野の研究者が対象に含まれるかどうか

## 判定

**adopt** — 着手日の前日の発表であり、OpenAI公式に加えTechTimes・
SiliconANGLE・Axios等の独立した複数のITメディアが同じ発表を報じている。
「1万人→10万人」という具体的なロードマップ、参加機関名、2.5億ドル規模の
予算といった数字の厚みがあり、30枚のスライド化に耐える。既存54テーマに
AI企業の学術アクセス無償開放を扱ったものはなく差別化できる。ただし日本の
研究機関が対象に含まれるかは確認できておらず、成果物内で明示して扱う。

## 出典一覧

- OpenAI公式(2026-07-29): https://openai.com/index/chatgpt-for-academic-researchers/
- OpenAI Help Center(申込条件の詳細): https://help.openai.com/en/articles/20001406
- TechTimes(2026-07-29): https://www.techtimes.com/articles/322124/20260729/openai-launches-free-ai-access-scientists-apply-now-model-weights-still-off-limits.htm
- SiliconANGLE(2026-07-29): https://siliconangle.com/2026/07/29/openai-opens-new-chatgpt-academic-researchers-program-100000-scientists/
- Axios(2026-07-29): https://www.axios.com/2026/07/29/openai-academics-research-chatgpt-sol
- AI Weekly: https://aiweekly.co/alerts/openai-opens-chatgpt-to-100000-academic-researchers-by-2027
- TheNextWeb: https://thenextweb.com/news/openai-chatgpt-academic-researchers-agent-harness-token-costs
- テーマ評価の記録: `ai-company-os/research/2026-07-30_theme-evaluation-round33.md`
