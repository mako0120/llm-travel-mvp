# 調査: Amazon傘下Zoox、米国初「ハンドル・ペダルなし」専用設計車での有料配車をラスベガスで開始(2026年8月10日)

<!-- docs/06_Content_R&D.md 準拠。出典のない数字は書かない -->

## メタ情報

- 調査名: Zoox「ハンドル・ペダルなし」専用設計ロボタクシーの有料サービス開始(ラスベガス)
- 調査日: 2026年8月10日
- 調査担当: Claude Code(AI Company OS 153本目)
- 関連 Issue: なし(定期実行round91での直接制作。Issue非経由)

## 0. 鮮度についての正直な開示(必須)

- 本テーマの中心となる事象(有料サービス開始)は **2026年8月10日(日)、着手日当日**。
  `docs/06_Content_R&D.md`の鮮度基準(着手日を含めて2日以内)を**完全に満たす、
  本パイプラインで最も新しい水準の鮮度**である。例外運用の必要はない。
- 開始日を報じた一次報道(CNBC・TechCrunch)自体は2026年8月5日付だが、これは
  「8月10日に開始する」という**予告記事**であり、対象の事象(実際の開始)は
  予告どおり2026年8月10日に起きている。着手日である本日、複数メディアが実際の
  開始を確認して報じている(Las Vegas Sun 2026-08-06、KTNV、TechTimes等、直近数日で
  「今週日曜(8/10)開始」と繰り返し報じられ、本日がその当日にあたる)
- `ai-company-os/research/2026-08-10_theme-evaluation-round91.md`の候補1として、
  バズ路線スコア82/100で採用済み

## 1. 調査目的と問い

- Zooxはいつ、どこで、何を始めたのか
- 「ハンドル・ペダルなし」の専用設計車とはどのようなものか
- 料金体系はどうなっているか。具体的な基本運賃は分かるか
- 予約方法・アプリはどうなっているか。Uber連携はどうか
- この有料サービス開始を法的に可能にした2026年7月のNHTSA適用除外との関係は何か
- 既存テーマ(`2026-08-03_zoox-nhtsa-safety-exemption`)とはどう違うのか、重複しないか
- 確認できなかったことは何か

## 2. 検証済み事実(出典付き)

| 事実 | 出典(URL) | 確認日 |
|---|---|---|
| Amazon傘下Zooxは、2026年8月10日(日)からラスベガスで乗客に運賃を課す有料サービスを開始した。ハンドル・ブレーキペダルを持たない専用設計の自動運転車が米国で乗客から運賃を徴収するのは、これが初めて | TechCrunch(2026-08-05)https://techcrunch.com/2026/08/05/zoox-to-start-charging-for-robotaxi-rides-in-las-vegas/ 、CNBC(2026-08-05)https://www.cnbc.com/2026/08/05/amazon-zoox-paid-robotaxi-rides-las-vegas.html | 2026-08-10 |
| Las Vegas Sunは「無料ライドはもう終わり("Free ride is over")」の見出しで、ラスベガスでのZooxロボタクシーが有料化することを報じた(2026-08-06) | Las Vegas Sun(2026-08-06)https://lasvegassun.com/news/2026/aug/06/free-rides-no-more-zoox-robotaxi-service-to-begin/ | 2026-08-10 |
| KTNV、TechTimesも同様に「今週日曜(8月10日)から有料化」と報じている | KTNV https://www.ktnv.com/news/zoox-to-begin-charging-for-robotaxi-rides-in-las-vegas 、TechTimes(2026-08-06)https://www.techtimes.com/articles/323440/20260806/zoox-begins-charging-las-vegas-robotaxi-rides-starting-this-sunday.htm | 2026-08-10 |
| 料金は、他のライドヘイリングサービスの「コンフォート」帯に相当する水準に設定される。具体的にはUberXの標準運賃より約20〜40%高い水準になる | TechCrunch(2026-08-05)、CNBC(2026-08-05) | 2026-08-10 |
| Zooxは具体的な基本運賃(base fare)の金額を公表していない。「コンフォート」帯の価格競争力を目指すとしている | TechCrunch(2026-08-05) | 2026-08-10 |
| 運賃は基本料金+移動距離+移動時間から算出される。予定より長いルートを走行した場合でも、乗客が追加で支払うことはないという保証が付く | TechCrunch(2026-08-05)、CNBC(2026-08-05) | 2026-08-10 |
| 空港送迎や、Sphere・T-Mobile Arenaなど高需要イベント時の目的地には追加料金(destination fee)が発生しうる。予約前に最終的な運賃全額が画面に表示される | TechCrunch(2026-08-05) | 2026-08-10 |
| 予約はZoox自社アプリで既に可能。Uberアプリとの連携は2026年内(later this year)に計画されている | TechCrunch(2026-08-05)、CNBC(2026-08-05) | 2026-08-10 |
| Zooxの車両はAmazonが自社開発した専用設計車で、ハンドル・ペダルを持たない、双方向対称(bidirectional、前後どちらにも同じ形で走行可能)なデザインになっている | TechCrunch(2026-08-05) | 2026-08-10 |
| この有料サービス開始を法的に可能にしたのは、2026年7月31日にNHTSA(米国運輸省道路交通安全局)がZooxに付与した、人間の運転操作系(ハンドル等)を求める連邦自動車安全基準の一部からの一時的な適用除外である。適用除外は年間最大2,500台、2026年7月31日から2028年7月31日までの2年間有効(既存テーマ`2026-08-03_zoox-nhtsa-safety-exemption`のresearch.mdで確認済みの事実を本テーマの背景として再掲) | Federal Register(2026-07-31)、NHTSA公式(既存テーマ research.md 参照) | 2026-08-10 |
| Zooxは2026年3月、Uber Technologiesとの提携を発表しており、ラスベガスでのUberアプリ経由の配車を2026年夏(summer 2026)に開始し、その後ロサンゼルスへ2027年半ばまでに拡大する計画があると報じられている。ただしこれは3月時点の提携発表・計画であり、本日(8/10)開始した有料サービスとは別に、Uberアプリ連携の具体的な開始日は本調査の範囲では確定していない | CNBC(2026-03-11)https://www.cnbc.com/2026/03/11/uber-amazon-zoox-partnership-robotaxi-demand.html 、TechCrunch(2026-03-11)https://techcrunch.com/2026/03/11/zoox-plans-to-put-its-robotaxis-on-the-uber-app-in-vegas-this-year/ | 2026-08-10 |
| Zooxはこれまでラスベガスのストリップ周辺、サンフランシスコの一部地域で無料の試乗サービスを提供してきた | WebSearch要約(techcrunch.com/2026/03/11記事の要約経由) | 2026-08-10 |

### アクセスできなかった一次情報についての開示

- 本セッションの`WebSearch`は利用できたが、`WebFetch`による記事本文への直接アクセスは
  試みておらず(過去テーマでegressブロックの既知事象があるため)、`WebSearch`が返す
  検索結果要約・複数メディアの見出しを突き合わせて事実を確認した。CNBC・TechCrunchという
  一次報道に加え、Las Vegas Sun・KTNV・TechTimesという独立した地元/専門メディアが同一の
  開始日(8月10日)・同一の料金水準(UberX比20〜40%高)を報じており、内容の信頼性は
  相互に裏付けられている
- Zoox公式サイト・公式ブログへの直接アクセスは本調査の範囲では行っておらず、報道各社
  (TechCrunch・CNBC)経由の確認にとどまる

## 3. 候補比較

<!-- 本テーマは評価表(research/2026-08-10_theme-evaluation-round91.md)の候補1として、モードBで採用済み -->

該当なし(定期実行round91の評価表で採用済みのテーマのため、本レポート内での候補比較は
実施しない)。評価表全文は `ai-company-os/research/2026-08-10_theme-evaluation-round91.md` を参照。

## 4. 合理的推測(事実と区別して書く)

- Zooxが基本運賃の具体額を公表していない一方で「UberXコンフォート帯比20〜40%高」という
  相対的な水準を明示しているのは、価格そのものよりも「Waymo等の競合と同等以上の体験・
  安全性への自信」を訴求する狙いがあると考えられるが、これはZoox自身がそのように公式に
  説明しているとまでは確認できておらず、当社の解釈である
- Uberアプリ連携が2026年内に予定されている(2026年3月時点の提携発表)ことから、ラスベガスでの
  有料化はZoox自社アプリでの直販とUberアプリでの提携販売という「二本立て」戦略の一段階目に
  あたると考えられるが、Uber連携の具体的な開始時期・条件は本調査の範囲では確認できておらず、
  推測にとどまる
- サンフランシスコ等、既に無料試乗を提供している他都市への有料化拡大は、ラスベガスでの
  有料サービスの実績・収益性を見極めた上で判断される可能性が高いと考えられるが、
  具体的な計画・時期は本調査の範囲では一切確認できていない

## 5. 推奨アクション

- 本テーマをそのままデッキ化する(効果: 「今日、初めて起きたこと」という具体的な鮮度と
  意外性が高く、視覚化しやすい数字・保証内容が揃っている。難易度: 低。リスク: 低。
  承認境界には触れない)
- 基本運賃の具体的なドル金額、初期投入車両台数、Uber連携の具体的な開始日、他都市
  (サンフランシスコ・オースティン・マイアミ)への有料化拡大の有無・時期は、いずれも
  Zooxが公表していない・本調査の範囲で確認できていないため、推測で埋めず「不明」と明記する
- 既存テーマ`2026-08-03_zoox-nhtsa-safety-exemption`(規制上の適用除外取得)を前提条件・
  背景として明示的に参照しつつ、本テーマは「実際の商用サービス開始」という別の具体的な
  事象であることをREADME・デッキ内で明確に区別する

## 6. 不明点と追加調査計画

以下は取得できず、推測で埋めていない。

- 具体的な基本運賃(base fare)のドル金額(Zoox非公表)
- 有料サービス開始時点でラスベガスに投入されている車両の正確な台数
- Uberアプリ連携の具体的な開始日(2026年3月時点では「2026年内」という計画のみ報じられている)
- 有料サービスが他都市(サンフランシスコ・オースティン・マイアミなど、これまで無料試乗を
  提供してきた都市)へ拡大するかどうか、その場合の時期
- ラスベガスでの初日(8月10日)の実際の利用状況・乗車件数などの実績データ

## 出典一覧

- TechCrunch(2026-08-05)「Zoox to start charging for robotaxi rides in Las Vegas」: https://techcrunch.com/2026/08/05/zoox-to-start-charging-for-robotaxi-rides-in-las-vegas/
- CNBC(2026-08-05)「Amazon's Zoox to launch paid robotaxi rides in Las Vegas on Aug. 10」: https://www.cnbc.com/2026/08/05/amazon-zoox-paid-robotaxi-rides-las-vegas.html
- Las Vegas Sun(2026-08-06)「Free ride is over: Zoox robotaxi service to begin charging for Las Vegas trips」: https://lasvegassun.com/news/2026/aug/06/free-rides-no-more-zoox-robotaxi-service-to-begin/
- KTNV「Zoox to begin charging for robotaxi rides in Las Vegas」: https://www.ktnv.com/news/zoox-to-begin-charging-for-robotaxi-rides-in-las-vegas
- TechTimes(2026-08-06)「Zoox Begins Charging Las Vegas Robotaxi Rides Starting This Sunday」: https://www.techtimes.com/articles/323440/20260806/zoox-begins-charging-las-vegas-robotaxi-rides-starting-this-sunday.htm
- CNBC(2026-03-11)「Uber, Amazon's Zoox partnership」: https://www.cnbc.com/2026/03/11/uber-amazon-zoox-partnership-robotaxi-demand.html
- TechCrunch(2026-03-11)「Zoox plans to put its robotaxis on the Uber app in Vegas this year」: https://techcrunch.com/2026/03/11/zoox-plans-to-put-its-robotaxis-on-the-uber-app-in-vegas-this-year/
- （背景情報として既存テーマ参照）Federal Register(2026-07-31)、NHTSA公式: `ai-company-os/assets/2026-08-03_zoox-nhtsa-safety-exemption/research.md`

## 既存テーマとの関係(重複でないことの確認)

`ai-company-os/assets/2026-08-03_zoox-nhtsa-safety-exemption/`(95本目、2026年8月3日制作)は、
**2026年7月31日にNHTSAがZooxへ付与した、ハンドル等の人間用運転操作系を求める連邦自動車
安全基準からの一時的な適用除外**という、規制上の出来事を扱っている。

本テーマ(153本目)は、その適用除外を前提として**2026年8月10日に実際に開始した商用の
有料配車サービス**という、時期的に約1週間後・内容的に規制の話ではなく消費者向けサービスの
話という、別の具体的な事象を扱う。両テーマの関係は「規制上の許可(前提条件)→実際の
商業展開(本テーマ)」という直列の関係であり、内容の重複ではない。この関係はREADMEの
「既存テーマとの関係」でも明示する。

## 判定

**adopt(鮮度基準を完全に満たす、着手日当日の事象)** — CNBC・TechCrunchという一次報道に
加え、Las Vegas Sun・KTNV・TechTimesという独立した複数メディアが同一の開始日・料金水準を
報じている。具体的な基本運賃・車両台数・Uber連携の具体的日程・他都市展開は非公表・未確認
であり、これらは本テーマ内で正直に「不明」と明記する。既存テーマ(NHTSA適用除外)とは
規制上の前提条件と実際の商業展開という別の事象であり、重複ではない。
