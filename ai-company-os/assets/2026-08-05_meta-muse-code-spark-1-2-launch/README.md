# Meta、AIコーディングエージェント「Muse Code」と新モデル「Muse Spark 1.2」を発表(2026-08-05〜07・定期実行158本目)

生成方式A(30枚・エンゲージメント設計ルール・初心者配慮ルール・文字を減らし図解で
伝えるルール)+ AI対話ナレーション・スライド連動モードで制作。

## 選定理由

- 対象ジャンル「AI/エージェント系」枠(70%)
- `research/2026-08-10_theme-evaluation-round93.md`の候補2として、round93の
  トレンド調査(26件前後のWebSearchクエリ)で採用
- Metaにとって初の専用コーディングエージェント「Muse Code」と、これと共同学習させた
  新モデル「Muse Spark 1.2」の同時発表という、業界競争構図の変化を示す事象
- 「学習データ提供と引き換えの大幅値引き」という料金体系の意外性がフックになる

## 鮮度基準の例外運用について(正直な開示、必読)

**本テーマは、`docs/06_Content_R&D.md`が定める通常の鮮度基準(着手日を含めて2日以内)
を満たしていない。**

- 発表日: 2026年8月5日〜7日(MarkTechPostが8/5、Forbes・VentureBeatが8/6、
  Technology.orgが8/7とメディアにより報道日が分散)
- 着手日(2026-08-10)からの経過: **3〜5日前**
- round93では26件前後のクエリでWebSearchを実施したが、候補1(Anthropic Auto Mode、
  157本目、1日前で鮮度基準を満たす)以外に2日以内の代替候補が見つからなかった
- オーナー指示(2026-08-05追記)の「探索を尽くしてもなお2日以内の候補が1本も
  見つからない場合に限り、次点として最も新しい候補を暫定的に採用してよい」という
  **例外的最終手段**の規定に基づき採用した
- **この例外運用は、round90(152本目)・round91(154本目)・round92(156本目)に
  続き4ラウンド連続である。** 「常態化させない」というオーナー指示の趣旨に照らして
  懸念があり、次回以降も2日以内の候補が見つからない場合は、2本ではなく1本のみの
  制作に切り替えることを優先的に検討する(詳細は`research.md`・
  `research/2026-08-10_theme-evaluation-round93.md`参照)

この開示は、`research.md`・本README・デッキ本編(スライド4「なぜ今、このニュースを
扱うのか」)・`youtube_assets.md`の概要欄案の**全てに共通して記載**している。

## 既存テーマとの関係(重複ではないことの説明)

`ai-company-os/assets/2026-07-23_meta-muse-spark-launch/`(24本目)は、Metaが
2026年7月9日に発表した「Muse Spark 1.1」単体の発表と、Zuckerberg氏が3年ぶりにXに
投稿してこれを告知したというバイラル性を扱ったテーマである。

| 観点 | 24本目(既存) | 158本目(本テーマ) |
|---|---|---|
| 発表日 | 2026年7月9日 | 2026年8月5〜7日 |
| 中心となる製品 | Muse Spark 1.1(モデル単体) | Muse Code(専用コーディングエージェント、新規)+ Muse Spark 1.2(共同学習モデル) |
| フック | Zuckerberg氏の3年ぶりのX投稿 | Metaにとって初の専用コーディングエージェント投入、学習データ提供と引き換えの割引という料金体系の意外性 |
| 料金 | 標準ティアのみ | 標準ティアに加え、「contributor」ティア(学習データ提供で割引)が新設 |

同一プロダクトライン(Muse Spark)の後継バージョンではあるが、「モデル単体の発表」から
「モデル+専用エージェント製品の同時投入」という異なる具体的事象であり、内容の重複を
避けて構成した(デッキ本編スライド16でも「既存テーマとの関係」として整理している)。

## 見送った候補(round93、詳細は`research/2026-08-10_theme-evaluation-round93.md`)

- Google DeepMind、Jeff Dean氏退社・「Discovery Loop」共同設立 — round89・round90で
  既に検討・不採用済みの「Google DeepMind組織再編」と実質同一の事象のため見送り
- ByteDance「Seedance 2.5」 — 発表日の情報源間の不一致があり、鮮度基準を確実に
  満たすと言い切れないため見送り
- OpenAI ChatGPT Atlasブラウザ終了 — 既存テーマ`2026-07-21_chatgpt-atlas-shutdown`
  と重複のため見送り
- Rippling / HappyRobot / Broadcom — Ripplingは152本目で採用済み、HappyRobotは
  round90で鮮度基準超過により不採用済み、Broadcomは決算日の特定ができず見送り
- コーエーテクモ×SpiralAI「RyzaChat」 — 配信日が未確定のため見送り

## ファイル一覧

| ファイル | 内容 |
|---|---|
| `research.md` | 出典付き調査結果。鮮度基準の例外運用・既存テーマとの関係・不明点を明記 |
| `deck_spec.json` | 30枚のデッキ仕様(同一レイアウト連続なし、bullets比率20.0%、palette_preset: forest_sand) |
| `deck.pptx` | 生成済みの.pptx本体 |
| `narration_script.md` | 単独ナレーション原稿(30スライド、目安約12分) |
| `dialogue_spec.json` | AI対話ナレーション・スライド連動モード仕様(30スライド全カバー、起承転結) |
| `dialogue_script.md` | 対話ナレーション原稿(30スライド、目安約8分) |
| `youtube_assets.md` | YouTube/Shorts向けタイトル案・概要欄・タグ・章立て |
| `canva_brief.md` | Canva移植ブリーフ(レイアウト対応表、`templates/canva_brief_template.md`準拠) |
| `risk-and-quality-review.md` | 著作権・品質自己評価(100点満点中94点、85点以上のため修正不要) |

`dialogue_audio.wav`・`slide_timings.json`・`deck_narrated.mp4`は、本セッションでは
git操作を行わない方針のためpushしておらず、GitHub Actions(`synthesize-dialogue-audio.yml`)
経由の自動生成は本タスクの範囲外(オーケストレーター側の対応待ち)。サムネイル関連
ファイルは、`docs/14_YouTube_Thumbnail.md`(2026-07-24、オーナー指示により定期実行の
自動パイプラインから停止中)に従い、明示的な依頼がない本タスクでは作成していない。

## 適用したルール

- 30枚デッキ、bullets比率20.0%(40%上限クリア)、同一レイアウト連続なし(最大連続2)
- 文字中心の説明はtable/diagram/cards/steps/comparison/big_statで図解・視覚化
  (料金体系は`table`・`big_stat`、サブエージェントの並行処理は`diagram`、
  muse resumeの効果は`cards`で表現)
- 初心者向け前提知識スライド(8枚目)+「これは何を意味するか・どう検討するか」の
  実践セクション(22〜24枚目)
- 進捗バー・カード影・タイトルアクセントの視覚強化(`docs/04_PowerPoint.md`参照)
- 誇張回避・特定企業推奨に関する注記を独立スライド(27枚目)として明示
- palette_presetは`forest_sand`を使用(直近6テーマがimpact_red/indigo_cyan/
  graphite_emerald/cobalt_violet/crimson_gold/slate_azureで使用済みのため、
  ローテーションで割り当て。forest_sandは2026-08-08以来未使用)

## 検品結果

- `verify_pptx.py --min-slides 30 --max-slides 30` → 合格
- `build_deck.py`の同一レイアウト4連続以上チェック・bullets比率40%以下チェック(20.0%) → 合格(ビルド時エラーなし)
- `generate_dialogue_script.py --deck deck_spec.json`のスライド数整合性検証(30枚、1〜30連番) → 合格
- 著作権・品質自己評価: 94点/100点(85点以上のため修正不要)

## リスク配慮

- 政治的テーマではなく、企業(Meta)の製品発表という事実紹介
- 対立を煽る表現・他社比較の誇張を避け、推測部分は「推測」と明示している
- 実在企業名(Meta)は事実として扱うが、ロゴ・商標画像・実在人物の写真・肖像は使用しない
- 特定企業・製品の利用を強く推奨する結論にしていない(スライド27で明記)
- 鮮度基準の例外運用(4ラウンド連続)であることを、research.md・本README・デッキ本編・
  youtube_assets.mdの全てで正直に開示している
- contributorティアの割引率(標準ティアの約12分の1)は1情報源(Pulse2)のみの言及であり、
  確度が低いことを明記した上で慎重に扱っている

## 注意

- Muse Codeの一般提供(GA)時期、Muse Spark 1.2のベンチマークスコアの第三者検証状況、
  contributorティアの正確な値引き率、日本語での利用可否は、いずれも本調査の範囲では
  確認できず「不明」と明記した(創作していない)
- 本セッションではgit操作・GitHub操作・Notion操作・SendUserFileを行っていない
  (タスク指示に基づき、ローカルファイル生成のみ)
- 公開・投稿・main へのマージはまだ行っていない
