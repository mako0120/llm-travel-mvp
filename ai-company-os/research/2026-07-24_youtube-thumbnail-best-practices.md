# 調査結果: 伸びるYouTubeサムネイルの設計原則

調査日: 2026年7月24日
目的: 定期実行サイクルの成果物に「サムネイル生成」を追加するための設計指針を、
複数の情報源を横断して整理する。

## 調査で確認できた主な知見(出典付き)

| 知見 | 出典 |
|---|---|
| 2026年の傾向は「シンプルさ」。1つの被写体・1つのメッセージ・1秒で理解できることが原則。ごちゃついたサムネイルは処理速度が追いつかず失敗する | [Ampifire](https://ampifire.com/blog/best-youtube-thumbnail-guide-examples-best-practices-2026-for-high-ctr/) |
| デザインの3原則は「明確な焦点が1つ」「高コントラストな配色」「4単語未満の太字テキスト」。色そのものよりコントラストが重要 | [Ampifire](https://ampifire.com/blog/best-youtube-thumbnail-guide-examples-best-practices-2026-for-high-ctr/) |
| 表情豊かな人物の顔はCTRを20〜30%押し上げるとVidIQは分析している(ただし本プロジェクトは実在人物の写真を使用しない方針のため採用不可) | [Awisee](https://awisee.com/blog/youtube-thumbnail-best-practices/) |
| 文字を最小限にしたサムネイルは、文字が多いデザインよりCTRが30%高いという調査結果がある | [Awisee](https://awisee.com/blog/youtube-thumbnail-best-practices/) |
| サムネイルとタイトルは1セットで設計し、サムネイルは好奇心のギャップを開き、タイトルがその文脈を与える(内容を重複させない) | [Ampifire](https://ampifire.com/blog/best-youtube-thumbnail-guide-examples-best-practices-2026-for-high-ctr/) |
| サムネイルでCTRが高くても内容と乖離していると視聴維持率が下がり、YouTubeのレコメンドで結果的に不利になる(「サムネイル・コンテンツ整合性のパラドックス」) | [Ampifire](https://ampifire.com/blog/best-youtube-thumbnail-guide-examples-best-practices-2026-for-high-ctr/) |
| トップクリエイターはサムネイルのA/Bテストで5〜10%のCTRを達成する一方、平均的なチャンネルは3〜4%程度 | [Ampifire](https://ampifire.com/blog/best-youtube-thumbnail-guide-examples-best-practices-2026-for-high-ctr/) |
| 日本語圏では、最も伝えたいメッセージを20文字以内に凝縮することが要点。スマートフォンでは多くの文字情報は読まれずに無視される | [StockSun](https://stock-sun.com/column/thumbnail/) |
| 背景色と被写体の色が大きく異なるほど目立つ。特に補色関係(黄×紫、赤×シアン、青×オレンジ)が効果的で、モバイルサイズでコントラスト比4.5:1を維持するとよい | [1of10](https://1of10.com/blog/youtube-thumbnail-design/) |
| 黄色はYouTubeの白/濃灰色のUIに対して最も視認性が高い色。青は信頼・冷静・権威を示し、教育・テックレビュー・金融系で好成績 | [1of10](https://1of10.com/blog/youtube-thumbnail-design/) |
| 太字サンセリフ体(Impact、Bebas Neue、Montserrat Extra Bold、Oswald Bold等)を60〜80pt以上で使用し、高コントラストのボックス(例: 黒背景に黄文字)に収めると可読性が高い | [1of10](https://1of10.com/blog/youtube-thumbnail-design/) |
| サムネイルを168×94pxに縮小しても文字が読めるかどうかがテキスト量・サイズの目安になる | [1of10](https://1of10.com/blog/youtube-thumbnail-design/) |
| テック系ニュースチャンネルでは、顔ではなく太字タイポグラフィと色使いで注目を集める手法が有効 | [1of10](https://1of10.com/blog/youtube-thumbnail-design/) |

## 本プロジェクトへの適用方針

- **顔は使わない**: 実在人物の写真・肖像は使用しない標準方針(`AGENTS.md`)を
  維持し、表情による訴求は行わない。代わりに「太字タイポグラフィ + 高コントラスト
  配色 + 図形アイコン(円・角丸ボックス等の抽象的な図形のみ、実在ロゴは不使用)」
  で注目を引く
- **1メッセージ・短い文言**: フック文言は日本語で13文字前後、最大でも20文字以内に
  収める。デッキの`title`スライドの見出し(問いかけ形式のフック)をベースに、
  さらに短く凝縮する
- **高コントラスト配色**: `build_deck.py`の`PALETTE_PRESETS`(navy_gold等)を
  ベースに、テキストボックスには背景と補色関係になるアクセント色を使い、
  縁取り・ドロップシャドウで可読性を確保する
- **数字を活かす**: デッキの`big_stat`スライドで扱った象徴的な数字(例: 「$2 vs $30」
  「600億ドル」)を、サムネイル右上・左上などにバッジ状に配置し、好奇心を引く
  要素として使う
- **タイトルとの役割分担**: サムネイルはフックのみを担い、YouTubeタイトル
  (`youtube_assets.md`のタイトル案)が文脈を補う。サムネイル自体に内容を
  詳しく書き込みすぎない
- **誇張・釣りタイトル化の回避**: 「サムネイル・コンテンツ整合性のパラドックス」
  を踏まえ、内容と乖離した誇張・扇動的な文言は使わない(既存の
  `youtube_assets.md`の「誇張表現は避ける」方針を維持)
- **168×94pxでの可読性チェック**: 生成後に縮小表示でテキストが判読できるかを
  確認する運用とする

## 追加調査(2026-07-24・オーナー提示の参考サムネイルを受けて)

オーナーから「全米が泣いた!最強のAIモデル復活」のような赤×黒背景・巨大な
太字・斜め帯バナー・表情豊かな顔を使った実例が提示され、同系統のデザインを
分析した。

| 知見 | 出典 |
|---|---|
| バズるサムネイルの3要素は「人の顔・テキスト・高コントラスト」 | [LOCUS](https://www.locus-inc.co.jp/blog/thumbnail) |
| MrBeastの定番構成は「口を開けた驚き顔・太字の黄or赤文字・謎めいた要素・シンプルな背景」 | [Artiphik](https://artiphik.com/blog/mrbeast-thumbnail-analysis) |
| 赤は緊急感・興奮を、黄は赤の補色として高コントラストを生む。両者の組み合わせが注目を集める | [1of10(MrBeast分析記事)](https://1of10.com/blog/how-to-make-thumbnails-like-mrbeast/) |
| 表情は脳内で文字より6万倍速く処理され、MIT の研究では顔の処理は100ミリ秒程度とされる。誇張された表情はサムネイルの小さいサイズでも「情報」として読み取れる | [touhfa.art](https://touhfa.art/blog/thumbnails/mrbeast-thumbnail-article/) |
| 一方でMrBeast自身は「驚き顔」の効果が薄れてきたことをA/Bテストで確認し、口を閉じた表情の方が成果が良い場合があるとコメントしている(流行は固定的ではない) | [dotesports](https://dotesports.com/streaming/news/mrbeast-seemingly-discovers-new-youtube-thumbnail-meta-that-could-change-the-face-of-the-site) |
| 色の効果は一律ではなく、業界・ターゲット層によって最適な配色は異なるためA/Bテストが推奨される | [Off Beat](https://www.offbeat-inc.co.jp/column/banner-design-ctr-improvement-trends-2026-1776301374500) |

### 本プロジェクトでの反映

- `build_thumbnail.py`に、赤×黒×黄の高コントラスト配色(`impact_red`パレット)・
  放射状バースト(漫画的な衝撃線)・斜め帯バナーを組み合わせた`style: "impact"`
  を追加した
- **顔は追加していない**。「表情は訴求力が高い」という知見は確認したが、(1)実在
  人物の写真は使わない方針を維持する必要があり、(2)架空のAI生成キャラクターを
  作るには本環境で未検証・未承認の画像生成ツールが必要なため、放射状バーストを
  表情の代替として採用するにとどめた。画像生成ツールの導入可否はオーナー確認待ち
- 参考例にあった「全米が泣いた」のような誇張表現は、本プロジェクトの正直さ・
  誇張回避ルールと衝突するため採用せず、斜め帯バナーには事実の要約のみを使う

## 出典一覧

- Ampifire: https://ampifire.com/blog/best-youtube-thumbnail-guide-examples-best-practices-2026-for-high-ctr/
- Awisee: https://awisee.com/blog/youtube-thumbnail-best-practices/
- 1of10: https://1of10.com/blog/youtube-thumbnail-design/
- StockSun: https://stock-sun.com/column/thumbnail/
- LOCUS: https://www.locus-inc.co.jp/blog/thumbnail
- Artiphik: https://artiphik.com/blog/mrbeast-thumbnail-analysis
- 1of10(MrBeast分析): https://1of10.com/blog/how-to-make-thumbnails-like-mrbeast/
- touhfa.art: https://touhfa.art/blog/thumbnails/mrbeast-thumbnail-article/
- dotesports: https://dotesports.com/streaming/news/mrbeast-seemingly-discovers-new-youtube-thumbnail-meta-that-could-change-the-face-of-the-site
- Off Beat: https://www.offbeat-inc.co.jp/column/banner-design-ctr-improvement-trends-2026-1776301374500

## 注意

- CTR数値(20〜30%向上、30%高い、5〜10% vs 3〜4%等)はいずれも各情報源が
  独自に集計・分析した数値であり、本プロジェクトの実測値ではない。参考値として
  扱い、本プロジェクトの成果物で断定的な効果を主張しない
