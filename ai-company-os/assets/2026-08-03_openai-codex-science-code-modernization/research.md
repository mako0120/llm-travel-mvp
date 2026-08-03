# 調査: OpenAIがAIコーディングエージェントで科学研究コードを近代化した実地報告(RNA解析60倍高速化、2026年7月28日発表)

## 調査目的と問い

2026年7月28日、OpenAIはGPT-5.5/GPT-5.6によるCodexを中心に、一部案件では
AnthropicのClaude Codeも併用し、8つの実案件で老朽化した科学研究用
ソフトウェアを近代化した実地報告(field report)を公開した。

- 何が発表されたのか。8つの案件の内容・成果はどこまで確かか
- 「ボトルネックがレビューに移った」という指摘は何を意味するのか
- 確認できなかったことは何か
- **鮮度についての正直な報告**: 発表日は着手日(2026-08-03)の6日前であり、
  `docs/06_Content_R&D.md`の鮮度基準(前日以内)を厳密には満たしていない

## 検証済み事実(出典付き)

### 発表: OpenAIの実地報告(2026-07-28)

| 項目 | 内容 | 出典 |
|---|---|---|
| 発表日 | 2026年7月28日 | TechTimes |
| 発表元 | OpenAI(field report、実地報告) | TechTimes / the-decoder / artificialintelligence-news |
| 使用モデル・ツール | GPT-5.5・GPT-5.6によるCodex(5案件は単独)、3案件はAnthropicのClaude Codeも併用 | the-decoder |
| 対象 | 老朽化した科学研究用ソフトウェア(genomics=ゲノム解析分野が中心) | TechTimes |
| 代表的な成果(1) | RNA配列解析(RNA-sequencing)の品質管理パイプラインで60倍の高速化 | TechTimes |
| 代表的な成果(2) | 2万行のC/C++ゲノムアライナー(STAR)をゼロからRustで書き直し、99.8%の精度一致を達成(rustar-alignerプロジェクト) | the-decoder |
| 代表的な成果(3) | 合成ゲノム生成処理をGPU向けに再設計し、1,610秒から27秒に短縮 | TechTimes |
| 具体案件(1) | cyvcf2(遺伝子データ読み込み用Pythonライブラリ)のビルド・インストール手順をGPT-5.5が最新化 | the-decoder |
| 具体案件(2) | MHCflurry(免疫モデル)で、Claude CodeとCodexが開発者・レビュー役を交代しながら、約1万行をTensorFlowからPyTorchに移植 | the-decoder |
| 具体案件(3) | STARを一からRustで再構築するrustar-alignerプロジェクト(配列読み取りをゲノム上の位置に対応させるツール) | the-decoder |

### 重要な知見(限界の開示)

| 項目 | 内容 | 出典 |
|---|---|---|
| ボトルネックの変化 | 「コードを書くこと」から「レビューすること」にボトルネックが移ったとOpenAIが指摘 | the-decoder |
| 正しさの判断基準 | 科学研究ソフトウェアの正しさは、テストの合否ではなく物理法則との整合性で決まり、それはAIには判断できないとOpenAIが明記 | the-decoder |
| 人間の役割 | 研究者による結果の確認・検証が引き続き必須とされている | TechTimes |

## 合理的推測(事実と区別する)

- 「ボトルネックがレビューに移った」という指摘は、AIコーディングエージェント
  の生産性向上が、単純作業の代替にとどまらず、人間側の役割そのものを
  変化させつつあることを示唆すると考えられるが、これがゲノム解析分野に
  固有の現象か、より広い科学研究ソフトウェア全般に当てはまるかまでは、
  本調査の範囲では判別できない
- OpenAI自身の一次報告であるため、成果を強調する方向のバイアスが
  かかっている可能性はあるが、限界(レビューのボトルネック、AIには
  科学的正しさを判断できない)についても同じ報告内で率直に触れている点は
  評価できる

## 不明(確認できなかったこと)

- OpenAIの一次発表(field report原文)の全体(WebFetchのアクセス制限(403)
  により直接確認できず、複数媒体経由の要約に基づいている)
- 8案件全ての詳細な内訳(本調査ではcyvcf2・MHCflurry・rustar-alignerの
  3件のみ具体的に確認できた)
- 各案件にかかった実際の開発期間・人的コスト
- 「99.8%の精度一致」の判定基準・検証方法の詳細

## 鮮度に関する正直な報告(重要)

**本テーマの発表日は2026年7月28日で、着手日(2026-08-03)の6日前である。**
`docs/06_Content_R&D.md`の鮮度基準(着手日の前日以内)を厳密には満たして
いない。2026-08-03に実施したトレンド調査(round45、10クエリ)で、着手日・
前日に該当する70点以上の新規候補が見つからず、検索クエリを変える・回数を
増やす等の努力を尽くしても見つからなかったため、鮮度で妥協してこのテーマを
採用した。詳細はテーマ評価表(round45)を参照。

## 判定

**adopt(鮮度で妥協、正直に開示)** — TechTimes・the-decoder・
artificialintelligence-news・IntuitionLabsという独立した複数のテック専門
メディアが、OpenAI自身の一次報告(field report)を引用して報じている。
「AIが20年もののレガシーコードを書き換えた」という数字のインパクトと、
「それでも科学的な正しさはAIには判断できない」という誠実な限界の両方を
扱える題材であり、バズる人気路線と誠実さの両立に適する。既存72テーマに
「AIコーディングエージェントによる科学研究コードの近代化」を扱ったものは
なく差別化できる。

## 出典一覧

- TechTimes(2026-07-28): https://www.techtimes.com/articles/321880/20260728/ai-agents-rewrote-20000-lines-dead-genomics-code-scientists-still-checked-every-result.htm
- the-decoder: https://the-decoder.com/ai-coding-agents-can-modernize-research-software-but-cant-judge-if-the-science-is-right/
- artificialintelligence-news: https://www.artificialintelligence-news.com/news/openai-report-coding-agents-faster-science-software-builds/
- 詳細な出典は
  `ai-company-os/research/2026-08-03_theme-evaluation-round45.md`も参照。
