# 調査: Uber CTO、「tokenmaxxing」時代の終焉を発言(2026年8月7日 Fortune報道)

<!-- docs/06_Content_R&D.md 準拠。出典のない数字は書かない -->

## メタ情報

- 調査名: UberのCTO Praveen Neppalli Naga氏、「tokenmaxxing」時代の終わりを発言
- 調査日: 2026年8月10日(制作再開日)。当初着手は2026年8月9日(定期実行round89)
- 調査担当: Claude Code(AI Company OS 150本目)
- 関連 Issue: なし(定期実行round89での直接制作。Issue非経由)

## 0. 鮮度と制作経緯についての正直な開示(必須)

- 本テーマの中心となる報道(Fortune)の発表日は **2026年8月7日(金)**。
- 本テーマは `ai-company-os/research/2026-08-09_theme-evaluation-round89.md` の
  「候補1(150本目)」として、**2026年8月9日** の定期実行サイクルで評価・採用された
  (着手日から2日前の発表であり、`docs/06_Content_R&D.md` の鮮度基準「着手日を含めて
  2日以内」を満たす)。
- 採用直後、ファイルを1つも作成しないうちにAPIセッション上限のエラーで制作が中断した
  (`ai-company-os/assets/2026-08-07_uber-tokenmaxxing-era-ending/` ディレクトリが
  存在しないことを2026-08-10の再開時点で確認済み。中断前の重複・欠落ファイルはない)。
- **2026年8月10日、制作を再開した。** 評価表(round89)の内容自体は着手日
  (2026-08-09)時点でのトレンド調査結果であり、その後の1日で本件について新たな
  重要な続報が出ていないかを再確認したが(下記WebSearch実施)、2026-08-07の
  Fortune報道内容を覆す・更新するような続報は確認できなかった。よって
  round89の評価内容をそのまま採用し、鮮度の基準日は当初の着手日(2026-08-09、
  発表から2日前)を正としてそのまま記載する。実際のファイル生成日(2026-08-10)との
  差は1日であり、`docs/06_Content_R&D.md`の鮮度基準(2日以内)の範囲内に収まる。

## 1. 調査目的と問い

- Uber CTOのPraveen Neppalli Naga氏は何を、いつ、どこで発言したのか
- 「tokenmaxxing」とは何か。いつ、どのように広まった言葉か
- Uber自身がこの言葉の火付け役とされる根拠は何か(2026年4月の発言)
- 発言の具体的な引用内容は何か
- コストが下がった/利用者が増えたという主張の裏付けとなる数字はあるか、それは
  第三者検証済みか自己申告か
- 既存2テーマ(127本目Weave・142本目Microsoft)との関係はどう整理すべきか
- 確認できなかったことは何か

## 2. 検証済み事実(出典付き)

| 事実 | 出典(URL) | 確認日 |
|---|---|---|
| 2026年8月7日(金)、Fortuneが「Uberが2026年のAI予算を数か月で使い切った後、CTOが『いわゆるtokenmaxxing時代の終わりに近づいている』と発言した」と報じた | Fortune(2026-08-07)"After blowing through its entire 2026 AI budget in months, Uber CTO says, 'We're coming to the end of the so-called tokenmaxxing era'" https://fortune.com/2026/08/07/uber-ai-spending-tokenmaxxing-is-over-cto/ | 2026-08-10 |
| UberのCTO Praveen Neppalli Naga氏は、水曜日(2026年8月5日)のX(旧Twitter)投稿で、AIコストについて「very interesting trends(非常に興味深い傾向)」が見られるとし、これを「いわゆる『tokenmaxxing』時代の終わりに近づいているもう一つのシグナルだと思う」と述べた | Fortune(2026-08-07)、Yahoo Finance(米国) https://finance.yahoo.com/technology/ai/articles/blowing-entire-2026-ai-budget-174815792.html 、AOL https://www.aol.com/articles/ubers-cto-says-company-coming-052313000.html 、Yahoo Finance(英国) https://uk.finance.yahoo.com/news/ubers-cto-says-company-coming-052313786.html | 2026-08-10 |
| Naga氏の直接引用(その1): "I think it's another signal that we're coming to the end of the so-called tokenmaxxing era."(いわゆるtokenmaxxing時代の終わりに近づいているもう一つのシグナルだと思う) | Fortune経由、Yahoo Finance(米国)ほか複数メディアで一致して引用 | 2026-08-10 |
| Naga氏の直接引用(その2): "The next phase, whatever we call it, will not be characterized by who spends the most tokens, but about how people use them as efficiently as possible."(次の段階が何と呼ばれるにせよ、誰が一番トークンを使ったかではなく、いかに効率的に使うかによって特徴づけられるだろう) | Fortune経由、Yahoo Finance(米国)ほか複数メディアで一致して引用 | 2026-08-10 |
| 「tokenmaxxing」は2026年上半期に広まった企業向けAI活用トレンドで、企業が従業員に業務でのAI利用を最大限に増やすよう促す動き。多くの企業は、支出に見合う投資対効果(ROI)が得られないと判断し、この方針から後退しているとされる | Yahoo Finance(米国、2026-08-07)、TheNextWeb https://thenextweb.com/news/uber-cto-tokenmaxxing-era-ending-ai-spending | 2026-08-10 |
| Uberは2026年前半、「tokenmaxxing」の火付け役となった企業の一つとされる。従業員にAnthropicのClaude Code等のツールをできる限り使うよう奨励し、AI利用量でソフトウェアエンジニアを順位付けする「リーダーボード(leaderboard)」まで作っていた | Yahoo Finance(米国、2026-08-07)、AOL(2026-08-07) | 2026-08-10 |
| Naga氏は2026年4月時点で、AnthropicのAIコーディングツール「Claude Code」について、2026年通年分として確保していた予算をその時点ですでに使い切っていたと述べていたとされる | Fortune経由、Yahoo Finance(米国、2026-08-07) | 2026-08-10 |
| Naga氏は、割り当てていた支出計画について「振り出しに戻った("back to the drawing board")」と認めた | Yahoo Finance(米国、2026-08-07) | 2026-08-10 |
| 2026年年始以降、Uber社内でフロンティア級AIツールを利用する従業員の数は4倍(quadrupled)に増えた一方、AIトークン1件あたりのコストは低下しているという(Uber側の自己申告) | Yahoo Finance(米国、2026-08-07)、TheNextWeb | 2026-08-10 |
| コスト低下の要因として、プロンプトキャッシュ(prompt caching)処理の改善、デフォルトで使うAIモデルの見直し、エンジニアが自分のAI利用状況・コストを可視化できるようにしたこと、オープンウェイトモデルの試験導入、が挙げられている | Yahoo Finance(米国、2026-08-07) | 2026-08-10 |
| The Hans India、Briefs.co、WDC TV Newsも同内容(CTOの発言・tokenmaxxing終焉の主張)を報じている | The Hans India https://www.thehansindia.com/tech/uber-cto-says-tokenmaxxing-era-is-ending-after-ai-budget-burnout-1106069 、Briefs.co https://www.briefs.co/news/uber-tech-chief-heaviest-ai-token-expenses-are-behind-us/ | 2026-08-10 |

### アクセスできなかった一次情報についての開示

- Fortune記事本文への直接アクセス(`WebFetch`)を試みたところ、本セッションの
  ネットワーク制約(プロキシによるegressブロック)により `EGRESS_BLOCKED` となり、
  記事本文を直接読むことはできなかった。上記の事実・引用は、`WebSearch` が返す
  複数メディア(Yahoo Finance米国/英国、AOL、TheNextWeb、The Hans India、Briefs.co、
  WDC TV News)の要約・引用を突き合わせて確認したものであり、Naga氏の直接引用
  (その1・その2)は複数の独立したメディアで文言が一致していることを確認している。
- Naga氏本人のX投稿そのもの(一次ソース)は本セッションから直接閲覧できていない。
  投稿日は「水曜日」という報道表現から2026年8月5日(水)と推定される(Fortune記事の
  公開日である2026年8月7日(金)の直前の水曜日であるため)。この推定は複数メディアの
  記述と矛盾しないが、Naga氏のX投稿そのもので日付を直接確認したわけではない点を
  明記する。

## 3. 候補比較

<!-- 本テーマは評価表(research/2026-08-09_theme-evaluation-round89.md)の候補1として、モードBで採用済み -->

該当なし(定期実行round89の評価表で採用済みのテーマのため、本レポート内での
候補比較は実施しない)。評価表全文は
`ai-company-os/research/2026-08-09_theme-evaluation-round89.md` を参照。

## 4. 合理的推測(事実と区別して書く)

- 「tokenmaxxing」という言葉を2026年前半に広めた張本人の一社とされるUber自身が、
  自らその終焉を発言したことは、企業のAI活用が「使用量の最大化」から「効率性・
  費用対効果」を重視する段階へ移りつつあることを示す一つの事例と考えられるが、
  これがUber一社の方針転換にとどまるのか、業界全体の傾向を先取りしたものなのかは、
  本調査の範囲では確認できていない
- コストの低下がプロンプトキャッシュ改善・モデル見直し等の技術的な要因による
  ものだとすれば、AI利用量自体を抑制するのではなく「同じ、あるいはより多い利用を
  より安く行う」方向への転換だと考えられるが、これはNaga氏の発言内容から読み取れる
  当社の解釈であり、Uberが公式にそのように位置づけているとまでは確認できていない
- 「次の段階」の名称・具体的な社内制度(リーダーボードを廃止するのか、別の指標に
  置き換えるのか等)については、Naga氏の発言では言及されておらず、今後の続報を
  待つ必要があると考えられる

## 5. 推奨アクション

- 本テーマをそのままデッキ化する(効果: 「tokenmaxxingの火付け役が、自ら終焉を
  宣言する」という一連の流れに『オチ』がつく展開で、既存2テーマの読者にも新規性を
  提供できる。難易度: 低。リスク: 低。承認境界には触れない)
- 既存2テーマ(127本目Weave・142本目Microsoft)との関係を、README・
  youtube_assets.md・canva_brief.mdで一貫して明記し、3件目であることを隠さず開示する
- 予算の具体的な金額、Naga氏が言及した「傾向」の定量的な数字(コスト減少率等)は
  未公表であり、本テーマ内で「不明」として明記する
- Naga氏の直接引用は、複数の独立メディアで文言が一致していることを確認したうえで
  そのまま使用し、要約による意味の変質を避ける

## 6. 不明点と追加調査計画

以下は取得できず、推測で埋めていない。

- Uberの2026年AI予算(Claude Code分を含む)の具体的な金額
- Naga氏が「very interesting trends」と表現したAIコストの傾向を示す具体的な数値
  (下落率・下落幅など、定量化された数字は報道内で確認できなかった)
- 「tokenmaxxing」に代わる次の段階の具体的な名称・社内制度(リーダーボードの
  扱いを含む)
- この動きがUber一社にとどまるのか、業界全体のAIコスト管理トレンドの一部なのか
- フロンティアAIツール利用者「4倍」・AIトークン単価の低下という数字について、
  Uber以外の第三者による検証があるかどうか(現時点ではUber側の自己申告として
  報じられている)
- Naga氏のX投稿そのものの正確な投稿日時・投稿全文(一次ソースへの直接アクセス不可のため)

## 出典一覧

- Fortune(2026-08-07): https://fortune.com/2026/08/07/uber-ai-spending-tokenmaxxing-is-over-cto/
- AOL(2026-08-07): https://www.aol.com/articles/ubers-cto-says-company-coming-052313000.html
- TheNextWeb: https://thenextweb.com/news/uber-cto-tokenmaxxing-era-ending-ai-spending
- The Hans India: https://www.thehansindia.com/tech/uber-cto-says-tokenmaxxing-era-is-ending-after-ai-budget-burnout-1106069
- Yahoo Finance(英国): https://uk.finance.yahoo.com/news/ubers-cto-says-company-coming-052313786.html
- Yahoo Finance(米国): https://finance.yahoo.com/technology/ai/articles/blowing-entire-2026-ai-budget-174815792.html
- Briefs.co: https://www.briefs.co/news/uber-tech-chief-heaviest-ai-token-expenses-are-behind-us/

## 既存テーマとの関係(重複でないことの確認)

`ai-company-os/assets/` 配下に、Uber・本CTO発言を扱った既存テーマは存在しない
(重複確認済み)。ただし「tokenmaxxing」という同一の用語を扱う既存テーマが2件ある:

| # | ディレクトリ | 主体 | 内容 | 本テーマとの関係 |
|---|---|---|---|---|
| 127本目 | `2026-07-29_weave-tokenmaxxing-engineering-intelligence` | スタートアップWeave社 | 「AIをたくさん使った」ことと「成果」が比例しない、という測定問題を提起する資金調達ニュース | 第三者(Weave)が概念を分析する立場。本テーマとは主体・事象が異なる |
| 142本目 | `2026-08-04_microsoft-tokenmaxxing-ai-budget` | Microsoft(EVP Jay Parikh氏) | 自社の社内AIコスト管理方針として「tokenmaxxingは最適化目標ではない」と通達 | 大企業が自社の内部方針としてtokenmaxxingを否定する立場。本テーマとは別の企業・別の文脈 |
| 150本目(本テーマ) | `2026-08-07_uber-tokenmaxxing-era-ending` | Uber(CTO Praveen Neppalli Naga氏) | **2026年前半にtokenmaxxingの火付け役とされた当のUber自身**が、自らその終焉を発言 | 用語の「発祥・火付け役」とされる企業自身が終焉を語るという、一連の流れに閉幕・オチをつける展開 |

同じ「tokenmaxxing」という言葉を扱う3件目のテーマであることを正直に開示する。
ただし主体(Weave→Microsoft→Uber)・立場(概念提起者→内部での引き締め→火付け役
自身の終焉宣言)がそれぞれ異なり、内容の重複はないと判断する。この関係は
README・youtube_assets.md・canva_brief.mdで一貫して明記する。

## 判定

**adopt** — Fortune(2026-08-07)を筆頭に、AOL・TheNextWeb・The Hans India・
Yahoo Finance(米国/英国)・Briefs.coという独立した複数メディアが同内容を報じており、
Naga氏の直接引用も複数メディアで文言が一致している。着手日(2026-08-09)から見て
2日前の発表であり鮮度基準を満たす。「tokenmaxxingという言葉の火付け役自身が、
その終わりを語る」という展開は、既存2テーマ(Weave・Microsoft)を知る視聴者にも
新規性のある『オチ』を提供する。一方、予算の具体的な金額・コスト傾向の定量数値・
次の段階の具体的な制度は非公開・未確認であり、これらは正直に「不明」として開示する。
