# 調査: カリフォルニア州「AI透明性法」の発効(2026年8月2日)

## 調査目的と問い

2026年8月2日、米カリフォルニア州の「AI Transparency Act」(SB 942、
AB 853による改正)が施行(operative)となった。大規模な生成AIサービスに
電子透かし・検出ツールの提供を義務付ける法律である。

- 何が施行されたのか。具体的にどのような義務が生じたのか
- 罰則はどの程度か。対象はどの事業者か
- Midjourneyが未対応と報じられているが、どこまで確からしい情報か
- 前日(66本目)に扱ったEU AI Act透明性義務と何が違うのか
- 確認できなかったことは何か

## 検証済み事実(出典付き)

### 施行: カリフォルニア州AI透明性法(2026-08-02)

| 項目 | 内容 | 出典 |
|---|---|---|
| 施行日(operative date) | 2026年8月2日(着手日の前日) | TechTimes / steg.ai |
| 法律の正式な経緯 | SB 942として制定後、AB 853により改正・施行日が変更された | steg.ai / Digital Democracy |
| 対象事業者 | 月間利用者100万人超の大規模な生成AI提供者 | Regulations.ai |
| 義務(1) | 無料のAI検出ツールを提供し、利用者がコンテンツの生成・改変の有無を確認できるようにする | steg.ai |
| 義務(2) | AI生成画像・動画・音声に潜在的開示(latent disclosure、法的証拠として機能する電子透かし等)を埋め込む | steg.ai |
| 義務(3) | 利用者が選択できる可視的開示(manifest disclosure、目に見える透かし)のオプションを提供する | steg.ai |
| 義務(4) | 透明性義務をサードパーティのライセンス先にも及ぼす(flow down) | steg.ai |
| 罰則 | 違反1件・1日あたり5,000ドルの民事罰。州司法長官・市検事・郡検事が提訴でき、勝訴した原告側には弁護士費用も認められる | steg.ai |
| 罰則の特徴 | 違反が続く限り、1日ごとに別個の違反とみなされ、罰金が累積する | steg.ai |

### Midjourneyの対応状況について(単一情報源、要注意)

| 項目 | 内容 | 出典 |
|---|---|---|
| 報じられている内容 | Midjourneyは、法律が施行された2026年8月2日時点で、C2PA(コンテンツ来歴)の証明情報も、既知のピクセル電子透かしも実装していないと報じられている | TechTimes(2026-08-02) |
| 背景 | Midjourneyは2023年からContent Authenticity Initiative(コンテンツ真正性イニシアチブ)の会員だが、その実装を出荷していないと報じられている | TechTimes(2026-08-02) |
| **情報源についての注意** | **この具体的な指摘は、確認できた範囲ではTechTimesの記事が唯一の情報源であり、他の独立した媒体による裏付け報道は確認できていない。断定的な事実として扱わず、「TechTimesが報じている内容」として扱う** | (自己申告) |

### 比較: EU AI Act(66本目)とカリフォルニア州AI透明性法(本テーマ)の違い

| 区分 | EU AI Act 第50条(66本目) | カリフォルニア州AI透明性法(本テーマ) |
|---|---|---|
| 施行日 | 2026年8月2日 | 2026年8月2日(同日) |
| 規制主体 | EU(欧州委員会・加盟国当局) | カリフォルニア州(司法長官・市検事・郡検事) |
| 主な義務 | チャットボットの名乗り義務、ディープフェイクのラベル表示義務 | 無料検出ツールの提供、電子透かし(潜在的・可視的)の実装義務 |
| 罰則の仕組み | 最大1,500万ユーロまたは全世界売上高3%(一括方式) | 1件・1日あたり5,000ドル(累積方式) |
| 対象の絞り込み | 分野・機能ごとに規定(直接対話・生成コンテンツ・感情認識・ディープフェイク) | 月間利用者100万人超の大規模事業者に限定 |

## 合理的推測(事実と区別する)

- カリフォルニア州の施行日がEUと同じ2026年8月2日である背景として、
  グローバル企業にとって複数地域の対応スケジュールを揃えやすくする意図が
  あった可能性が考えられるが、両者の施行日一致が意図的な調整によるものか
  偶然かは一次情報から確認できていない
- Midjourneyのような大手生成AIサービスが施行初日時点で未対応に見える背景
  として、電子透かし実装の技術的コストや、法解釈の不確実性が影響している
  可能性が考えられるが、Midjourney自身の公式コメントは確認できていない

## 不明(確認できなかったこと)

- カリフォルニア州法(AB 853・SB 942)の条文原文全体(WebFetchのアクセス
  制限(403)により直接確認できず、複数の法律専門メディア経由の要約に
  基づいている)
- Midjourneyの対応状況について、TechTimes以外の独立した裏付け報道
- 実際に執行(罰金賦課等)された具体的な事例(施行直後のため、まだ存在しないと
  考えられる)
- カリフォルニア州法の対象となる具体的な事業者数・企業名の一覧

## 判定

**adopt** — 法律の施行日が2026年8月2日(着手日の前日)であり、鮮度基準
(前日以内)を満たす。TechTimes・steg.ai・Secure Privacy・National Law
Review・Hintze Lawという独立した複数の法律専門メディアが同じ内容を報じて
いる。「違反1日あたり5,000ドル」「月間利用者100万人超が対象」「検出ツール・
電子透かしの義務」という具体的で検証しやすい制度内容があり、30枚のスライド
化に耐える。前日(66本目)のEU AI Act透明性義務と同じ「AI透明性規制」という
カテゴリだが、規制主体・罰則構造・具体的な技術要件が明確に異なるため、
デッキ内でEUとカリフォルニアを比較するスライドを設けることで差別化した。
ただし条文原文全体・Midjourneyの対応状況の裏付け・実際の執行事例は確認
できておらず、成果物内で明示して扱う。

## 出典一覧

- TechTimes(2026-08-02): https://www.techtimes.com/articles/322713/20260802/california-ai-transparency-act-operative-midjourney-has-no-watermark-fines-start-today.htm
- steg.ai: https://steg.ai/news/ai-transparency-act-ab-853/
- Secure Privacy: https://secureprivacy.ai/blog/california-ai-transparency-law
- National Law Review: https://natlawreview.com/article/californias-ongoing-ai-regulation-key-deadlines-arriving-2026-and-beyond
- Hintze Law(2025-10-19): https://hintzelaw.com/blog/2025/10/19/california-amends-artificial-intelligence-transparency-act-and-passes-ai-defenses-act
- California州議会(条文): https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB853
- Regulations.ai: https://regulations.ai/regulations/RAI-US-CA-AB85300-2025
- テーマ評価の記録: `ai-company-os/research/2026-08-03_theme-evaluation-round42.md`
