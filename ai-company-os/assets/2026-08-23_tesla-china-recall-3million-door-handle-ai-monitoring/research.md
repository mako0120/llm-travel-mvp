# リサーチ: テスラ、中国で300万台リコール——AI運転監視システムの欠陥も

- 調査担当: Claude Code(AI Company OS)
- 着手日: 2026-08-23(JST)
- 事象発生日: 2026-08-22(米国時間金曜日、発表日)
- 鮮度判定: 着手日の前日。基準(着手日または前日のみ)を満たす。

## 要旨

2026年8月22日(金)、テスラと中国の製品安全規制当局は、中国国内で
約300万台の車両を対象とするリコール(自主改修)措置を発表した。対象は
ドアハンドルの安全性の問題と、運転支援システム使用時の「ドライバー
監視」機能の不備の2点。Model 3・Model Y・Model S・Model Xが対象で、
一部輸入車と、2019年3月4日〜2026年4月29日に中国生産された車両が含まれる。
複数の主要メディア(CNBC・Fox Business・Global Times等)がこの件を報じて
いる。

## 独立性の確認(重複テーマでないことの確認)

`ai-company-os/assets/`配下を`grep -ril -i "tesla.*recall|door.*handle"`
で検索した結果、既存テーマは存在しないことを確認した(2026-08-23時点)。

## 核心となる事実

| 項目 | 内容 |
|---|--:|
| 発表日 | 2026年8月22日(金、米国時間) |
| リコール対象台数 | 約300万台(中国国内) |
| 対象車種 | Model 3・Model Y・Model S・Model X |
| 対象期間 | 2019年3月4日〜2026年4月29日に中国生産された車両を含む(一部輸入車も対象) |
| 機械的なドアハンドル改修の開始時期 | 2026年9月25日 |

出典: CNBC(2026-08-21〜22)、Fox Business、Global Times、Insurance Journal

## 問題点(1)ドアハンドルの安全性

- 衝突事故が発生した際、車両の低電圧システムが故障すると、ドアハンドルが
  正常に作動しなくなる可能性があるとテスラは説明している
- これにより、車内の乗員がドアを開けて迅速に脱出することが妨げられたり、
  車外からの救助活動が困難になったりする恐れがあるとされる
- 対応として、機械的なドアハンドルの改修が2026年9月25日から開始される
  見通しである

出典: CNBC(2026-08-21〜22)、Insurance Journal

## 問題点(2)AI運転監視システムの不備

- 中国生産のModel 3・Model Yが対象
- 無償のOTA(無線)ソフトウェアアップデートにより、運転支援機能
  「Autosteer」使用中に、キャビン内カメラによる追跡機能とステアリング
  ホイールのトルクセンサーを組み合わせて、運転者が道路を注視しているかを
  確認する仕組みを有効化する
- これは、運転支援システム使用時の運転者監視(ドライバーモニタリング)の
  不備を是正する措置と位置づけられている

出典: CNBC(2026-08-21〜22)、Global Times(2026-08-22)

## 重要な留保事項(正直な開示・誇張しない)

- リコールの対象台数(約300万台)は報道時点での見通しであり、最終的な
  対象台数は中国当局の正式な発表文書で確定する可能性がある
- 「機械的なドアハンドル改修」の開始日(2026年9月25日)は予定であり、
  実施状況の詳細(改修の進捗率等)は本調査の範囲では確認できていない
- 本リコールに起因する実際の事故・負傷者数については、本調査の範囲では
  確認できていない
- AI運転監視システムの不備が、これまでにどの程度の実際の安全上の問題を
  引き起こしていたか(具体的な事故事例等)は確認できていない
- 米国など中国以外の地域で同様のリコールが行われるかどうかは、本調査の
  範囲では確認できていない

## AI・ビジネス業界における位置づけ

- 本リコールのうち「AI運転監視システムの不備」は、自動運転支援技術に
  おける安全性確保(ドライバーモニタリング)の重要性を改めて示す事例として
  注目される
- キャビン内カメラとセンサーを組み合わせた監視システムは、多くの先進運転
  支援システム(ADAS)で採用が進んでいる技術であり、本件はその実装上の
  課題を示す一例として位置づけられる

出典: 本調査による整理

## 政治的中立性・推奨表明の回避

本テーマは製品安全に関するリコールという客観的事実の紹介であり、
米中の自動車産業政策・貿易政策への評価には触れない。テスラという特定
企業の製品の購入・利用を推奨または非推奨とする表現は用いない。

## 著作権・肖像リスク

テスラの企業ロゴ・商標、経営陣(イーロン・マスク氏等)の写真・肖像は
使用しない。車両の実写画像も使用せず、抽象的な図解のみで構成する。

## 出典

- CNBC: "Tesla recalls 3 million vehicles in China over doorhandle safety, driver monitoring"
  https://www.cnbc.com/2026/08/21/tesla-recalls-cars-in-china-over-doorhandle-safety-driver-monitoring.html
- Fox Business: "Tesla recalls nearly 3 million vehicles in China over door handles"
  https://www.foxbusiness.com/lifestyle/tesla-recalls-nearly-3m-vehicles-over-doors-may-difficult-open-after-crashes
- Global Times: "Tesla to recall 3 million EVs in China over door-handle risk, defect in driver-attention monitoring for assisted-driving system"
  https://www.globaltimes.cn/page/202608/1368798.shtml
- Insurance Journal: "Tesla Recalls 3 Million EVs in China Over Door Handle Safety"
  https://www.insurancejournal.com/news/international/2026/08/21/882457.htm
- Briefs.co: "Tesla Recalls 3M Vehicles in China Over Door Handles"
  https://www.briefs.co/news/tesla-china-recall-reaches-3-million-vehicles-over-flush-doo/

## 特記事項(正直な開示)

CNBC記事のURL日付は2026年8月21日となっているが、複数の他メディア
(Fox Business・Global Times等)は「金曜日(2026年8月22日)に発表」と
明記しており、本テーマでは発表日を2026年8月22日(金)として扱った。
この点、情報源間で日付表記に若干の食い違いがあることを正直に開示する。
