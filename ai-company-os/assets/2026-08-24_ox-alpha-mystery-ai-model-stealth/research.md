# リサーチ: 「Ox Alpha」——正体不明のAIモデルが開発者を熱狂させた理由

- 調査担当: Claude Code(AI Company OS)
- 着手日: 2026-08-24(JST)
- 事象発生日: 2026-08-23(Bloomberg・TechCrunch等の報道日)
- 鮮度判定: 着手日の前日。基準(着手日または前日のみ)を満たす。

## 要旨

2026年8月20日、AIモデル比較サイト「OpenRouter」に、開発元を一切明かさない
匿名のAIモデル「Ox Alpha」(ラベル表記は「stealth」)が突如登場した。
無償で利用でき、約105万トークンという大きなコンテキストウィンドウを
持ち、コーディング・複雑な推論・長時間のエージェント的タスクに強いと
される。開発元が非公開であることから、コミュニティによる「正体探し」が
過熱し、2026年8月23日にはBloomberg・TechCrunchなど主要メディアがこの
現象そのものを報じた。本テーマは、この「正体探し」報道(8月23日)を
主題として扱う。

## 独立性の確認(重複テーマでないことの確認)

`ai-company-os/assets/`配下を`grep -ril -i "ox alpha|stealth model"`で
検索した結果、既存テーマは存在しないことを確認した(2026-08-24時点)。

## 核心となる事実

| 項目 | 内容 |
|---|--:|
| OpenRouter登場日 | 2026年8月20日 |
| 主要メディアによる『正体探し』報道日 | 2026年8月23日(Bloomberg・TechCrunch) |
| コンテキストウィンドウ | 約104万8,576トークン |
| 最大出力トークン数 | 131,072トークン |
| 対応する入力形式 | テキスト・画像・動画 |
| 利用料金 | 無償(2026年8月27日頃に終了する見通し) |

出典: Bloomberg(2026-08-23)、TechCrunch(2026-08-23)、OpenRouter公式ページ

## なぜ「正体探し」が過熱したのか

- OpenRouter上での表示名は開発元を伏せた「stealth」ラベルのみで、
  一切の公式情報が付随していない
- この情報の空白が、コミュニティによる技術的な「フォレンジック(鑑定)」
  分析を誘発した
- 具体的な技術的手がかりとして、意図的に不正な形式のAPIリクエストを
  送った際に返されるJavaのスタックトレースが、中国のAI企業Zhipu
  (智譜、GLMシリーズの開発元)の公式APIエンドポイントのパス
  (`paas/v4/chat`)と一致したとの分析結果が複数の独立した研究者から
  報告されている
- 動画エンコーダーのトークン消費パターンがGLM-5V-Turboと一致する点、
  トークナイザーの挙動がGLM-5.3と整合する点、特定のエラーコード
  (1214番、ロール情報不正)の返され方がZhipu公式ホスティングの
  GLMモデルと一致する点なども、Zhipu説を補強する技術的根拠として
  挙げられている

出典: techtimes.com、explainx.ai、BigGo Finance等による技術分析記事の要約(2026-08-23)

## ベンチマーク性能に関する情報(留保つき)

- コミュニティによる計測(公式のArtificial Analysis等の評価機関による
  スコアではない)によれば、Ox AlphaはKingbenchで87.5%を記録し、
  GLM-5.3の91.25%をやや下回るとされる
- DeepSWEベンチマークでは、10タスクのサブセットで80%という見出し
  スコアが出た一方、113タスク全体を対象とした別の計測では約63%と
  なったとの報告があり、計測条件によって数字が大きく変動する点に
  留意が必要である
- 一部のコミュニティ記事では他の主要モデルとの比較でOx Alphaが上回る
  場面があるとする報告も見られるが、本テーマでは特定モデルとの
  直接比較を核心的な内容とはせず、あくまで「コーディング・エージェント
  タスクで competitive(競争力がある)な水準」という一般的な評価に
  とどめる

出典: Day.dev等のコミュニティ計測記事の要約(2026-08-23)

## 重要な留保事項(正直な開示・誇張しない)

- 開発元がZhipu(智譜)であるという説は、本調査時点(2026年8月24日)で
  Zhipu自身またはOpenRouterによる公式確認は一切得られていない
- 技術的な「フィンガープリント」分析はあくまで個々の研究者・
  コミュニティによる推測であり、確定した事実ではない
- ベンチマークスコアはコミュニティによる非公式な計測であり、公式な
  評価機関のスコアカードとしては確認できていない
- 無償提供の終了予定日(2026年8月27日頃)は報道時点での見通しであり、
  実際にその日に開発元が明かされるかどうかは確認できていない
- モデルの正式名称、パラメータ数、学習データの詳細等は一切公開されて
  おらず、本調査の範囲でも確認できていない

## AI・ビジネス業界における位置づけ

- 開発元を明かさずにモデルを公開する「ステルスモデル」という手法自体が
  近年のAI業界で見られる現象であり、新モデルの実力を市場に静かに
  問う目的で用いられることがあるとされる
- 今回の事例は、コミュニティによる技術的な「鑑定」文化(APIのエラー
  コードやスタックトレースからの推測)が、AI業界特有の情報収集手法
  として存在することを示す事例としても注目される

出典: 本調査による整理

## 政治的中立性・推奨表明の回避

本テーマはAIモデルの公開・コミュニティ分析という客観的事実の紹介で
あり、米中のAI技術競争に関する政治的評価には触れない。特定企業
(Zhipu等)のモデル・製品の利用を推奨する表現は用いない。

## 著作権・肖像リスク

Zhipu等の企業ロゴ・商標、経営陣の写真・肖像は使用しない。抽象的な
図解のみで構成する。

## 出典

- Bloomberg: "Mystery AI Model Ox Alpha Draws Developers With Free Access"
  https://www.bloomberg.com/news/articles/2026-08-23/mystery-ai-model-ox-alpha-draws-developers-with-free-access
- TechCrunch: "Who's behind the new 'stealth model' Ox Alpha?"
  https://techcrunch.com/2026/08/23/whos-behind-the-new-stealth-model-ox-alpha/
- Tekedia: "Mysterious Ox Alpha AI Model Fuels Speculation Over Possible Chinese Origins"
  https://www.tekedia.com/mysterious-ox-alpha-ai-model-fuels-speculation-over-possible-chinese-origins/
- Tech Times: "Coding Model Ox Alpha Retains Every Prompt: You Cannot Name Company Holding Them"
  https://www.techtimes.com/articles/325244/20260823/coding-model-ox-alpha-retains-every-prompt-you-cannot-name-company-holding-them.htm
- OpenRouter公式ページ(モデル仕様): https://openrouter.ai/stealth/ox-alpha

## 特記事項(正直な開示)

各出典記事には検索結果経由での要約という形でアクセスしており、原文
全体を直接確認した訳ではない。Zhipu説を裏付ける技術的根拠は、複数の
独立した技術系メディア(techtimes.com、explainx.ai、BigGo Finance等)
で概ね一致する内容として重複確認できたが、これらもいずれも一次情報
(Zhipu自身またはOpenRouterの公式発表)ではなく、コミュニティによる
推測の域を出ないことを明確にしておく。
