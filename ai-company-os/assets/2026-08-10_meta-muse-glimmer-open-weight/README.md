# Meta、初のオープンウェイト型エージェントAIモデル「Muse Glimmer」を無償公開(2026-08-10・定期実行163本目)

生成方式A(30枚・エンゲージメント設計ルール・初心者配慮ルール・文字を減らし図解で
伝えるルール)+ AI対話ナレーション・スライド連動モードで制作。

## 選定理由

- 対象ジャンル「AI/エージェント系」枠(70%)
- `ai-company-os/research/2026-08-11_theme-evaluation-round97.md`の候補1として、
  round97のトレンド調査(約7件のWebSearchクエリ)で採用
- 発表日は2026年8月10日、着手日(2026-08-11)から1日前で鮮度基準(着手日を含めて
  2日以内)を満たす
- Bloomberg・CNBC・TechCrunch・MarkTechPost・Phoronix・Open Source For You・
  Yahoo Financeと複数の独立系メディアが同時期に報道しており、話題性の裏付けがある
- 「自分のノートPCでAIエージェントが動く」という具体性のあるフック、Meta株価が
  本発表を受けて上昇したという市場の反応、OpenAI・Anthropicのプロプライエタリ
  路線への対抗という業界構図の変化がバズ路線のフックになる(バズ路線スコア77/100)

## 見送った候補

round97で比較した候補のうち、本テーマ以外の詳細は
`ai-company-os/research/2026-08-11_theme-evaluation-round97.md`を参照。

- Zenity・Obsidian Security・Oligo Securityの資金調達 — 既存テーマ
  `2026-08-03_zenity-ai-agent-security-125m`・`2026-08-04_obsidian-security-85m-unicorn`
  と個別に重複するため見送り
- LeapXpertの資金調達 — 具体的な発表日が特定できず見送り
- 久保建英選手の実戦復帰は、同ラウンドの候補2(164本目)として別テーマで
  並行採用しており、本テーマとは別ファイルで制作する

## 既存テーマとの関係(3件目のMeta Museライン関連テーマであることの開示)

`ai-company-os/assets/`に、Muse Glimmerを主題とした既存ディレクトリはない
(2026-08-11時点で確認済み)。ただし同じMeta Museプロダクトラインを扱った
過去テーマが2件あり、これらとの関係を明確にしておく。

| テーマ | 発表日 | 中心となる製品 | フック |
|---|---|---|---|
| `2026-07-23_meta-muse-spark-launch`(24本目) | 2026年7月9日 | Muse Spark 1.1(モデル単体) | Zuckerberg氏の3年ぶりのX投稿 |
| `2026-08-05_meta-muse-code-spark-1-2-launch`(158本目) | 2026年8月5〜7日 | Muse Code(専用コーディングエージェント)+ Muse Spark 1.2(共同学習モデル) | 学習データ提供と引き換えの割引料金体系 |
| 本テーマ(163本目) | 2026年8月10日 | Muse Glimmer(オープンウェイト・30B・24GB GPU1枚で動作) | 「自分のノートPCでAIエージェントが動く」という具体性、OSS対プロプライエタリの業界構図 |

本テーマは、既報2件が扱った「モデル単体の発表」「専用コーディングエージェント+
料金体系」とは異なり、「オープンウェイトでコンシューマーGPU上のローカル実行が
できる」という全く別の戦略軸(オープンソース対プロプライエタリの競争構図)を
扱っている。この関連性はデッキ本編(スライド20「Meta Museラインの歩み」・
スライド21「既存2テーマとの違い」)でも明示し、内容の重複を避けて構成した。

## ファイル一覧

| ファイル | 内容 |
|---|---|
| `research.md` | 出典付き調査結果(既存テーマとの関係・不明点の明記を含む) |
| `deck_spec.json` | 30枚のデッキ仕様(同一レイアウト最大連続3、bullets比率30.0%、palette_preset: indigo_cyan) |
| `deck.pptx` | 生成済みの.pptx本体 |
| `narration_script.md` | 単独ナレーション原稿(30スライド、目安約11分) |
| `dialogue_spec.json` | AI対話ナレーション・スライド連動モード仕様(30スライド全カバー、起承転結) |
| `dialogue_script.md` | 対話ナレーション原稿(30スライド、目安約6分) |
| `youtube_assets.md` | YouTube/Shorts向けタイトル案・概要欄・タグ・章立て |
| `canva_brief.md` | Canva移植ブリーフ(レイアウト対応表、`templates/canva_brief_template.md`準拠) |
| `risk-and-quality-review.md` | 著作権・品質自己評価(100点満点中94点、85点以上のため修正不要) |

`dialogue_audio.wav`・`slide_timings.json`・`deck_narrated.mp4`は、本セッションでは
git操作を行わない方針のためpushしておらず、GitHub Actions(`synthesize-dialogue-audio.yml`)
経由の自動生成は本タスクの範囲外(オーケストレーター側の対応待ち)。サムネイル関連
ファイルは、`docs/14_YouTube_Thumbnail.md`(2026-07-24、オーナー指示により定期実行の
自動パイプラインから停止中)に従い、明示的な依頼がない本タスクでは作成していない。

## 適用したルール

- 30枚デッキ、bullets比率30.0%(40%上限クリア)、同一レイアウト最大連続3(4連続なし、
  `build_deck.py`のビルド時検証をパス)
- 文字中心の説明はtable/diagram/cards/steps/comparison/big_stat/bar_chartで
  図解・視覚化(発表を報じたメディア一覧は`table`、業界の対立構図は`diagram`、
  速度向上の3機種比較は`bar_chart`+個別`big_stat`3枚に分解、スペックは`table`で整理)
- 「動画としてのテンポ」ルールに従い、速度向上の数字(RTX 5090/M5 Max/M4 Max)は
  1枚のcardsにまとめず、bar_chartの全体像スライド+big_stat単体3枚に分解した
- 初心者向け前提知識スライド(9・10枚目:オープンウェイトモデル・エージェントAIとは)
  + 「これは何を意味するか・どう検討するか」の実践セクション(23〜25枚目)
- 進捗バー・カード影・タイトルアクセントの視覚強化(`docs/04_PowerPoint.md`参照)
- 誇張回避・特定企業推奨に関する注記を独立スライド(29枚目のCTA)として明示
- palette_presetは`indigo_cyan`を使用(直近5テーマがforest_sand/navy_gold/
  graphite_emerald/cobalt_violet/slate_azureで使用済みのため、ローテーションで割り当て)

## 検品結果

- `verify_pptx.py --min-slides 30 --max-slides 30` → 合格(問題は検出されず)
- `build_deck.py`の同一レイアウト4連続以上チェック・bullets比率40%以下チェック
  (実測30.0%、最大連続3) → 合格(ビルド時エラーなし)
- `generate_dialogue_script.py --deck deck_spec.json`のスライド数整合性検証
  (30枚、1〜30連番、抜け・重複・逆順なし) → 合格
- 著作権・品質自己評価: 94点/100点(85点以上のため修正不要)

## リスク配慮

- 政治的テーマではなく、企業(Meta)の製品発表という事実紹介
- 対立を煽る表現・他社比較の誇張を避け、業界構図は報道の要約にとどめている
  (OpenAI・Anthropicとの優劣を断定していない)
- 実在企業名(Meta)は事実として扱うが、ロゴ・商標画像・実在人物の写真・肖像は使用しない
- 特定企業・製品の利用を強く推奨する結論にしていない(スライド29で明記)
- Meta株価上昇の具体的な変動幅・一般提供後のダウンロード数・速度向上の測定条件の詳細は
  すべて「不明」と明記し、数字を創作していない
- 既存2件のMeta Museラインテーマとの関係を正直に開示し、焦点の違いをREADME・
  research.md・デッキ本編の全てで明示している

## 注意

- 本セッションは、タスク指示に列挙された確定済み事実・出典名(Bloomberg・CNBC・
  TechCrunch等)をそのまま使用しており、記事原文への直接アクセス(WebFetch等)による
  再確認は行っていない
- 速度向上の数値(RTX 5090で3.1倍・M5 Maxで1.8倍・M4 Maxで1.5倍)はMeta社の自社測定値
  であり、比較対象・測定条件の詳細・第三者検証の有無は不明であることをデッキ本編
  (スライド19)・research.mdで明記している
- 本セッションではgit操作・GitHub操作・Notion操作・SendUserFileを行っていない
  (タスク指示に基づき、ローカルファイル生成のみ)
- 公開・投稿・main へのマージはまだ行っていない
