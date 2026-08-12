# 調査: xAI、常時稼働の自律型AIエージェント「Grok Bot」ベータ版を発表

## メタ情報

- 調査名: xAI「Grok Bot」ベータ版発表(常時稼働の自律型AIエージェント、専用クラウドコンピュータ付き)
- 調査日: 2026年8月12日
- 調査担当: Claude Code(AI Company OS)
- 関連 Issue: なし(コンテンツパイプライン制作、182本目)

## 1. 調査目的と問い

2026年8月11日、xAIが常時稼働(always-on)の自律型AIエージェント群「Grok Bot」のベータ版を
発表した。

- 何が、いつ、どのように発表されたのか
- 「Grok Bot」はどのような仕組みか(専用クラウドコンピュータ・既存ツールへのサインイン等)
- どの契約プランに、どのプラットフォームで提供されるのか
- xAI社内でのBotの利用例はどのようなものか
- Grok 4.6との関係、今後の展開予告はどう報じられているか
- 確認できなかったことは何か
- 既存テーマ(GPT-5.6とGrok 4.5の発表競争、Grok Voiceの既定化)との関係はどうか

## 2. 検証済み事実(出典付き)

| 事実 | 出典(URL) | 確認日 |
|---|---|---|
| 2026年8月11日、xAIが常時稼働の自律型AIエージェント群「Grok Bot」のベータ版を発表した | Unite.AI「xAI Launches Grok Bot, Always-On AI Teammates With Their Own Cloud Computers」 https://www.unite.ai/xai-launches-grok-bot-always-on-ai-teammates-with-their-own-cloud-computers/ | 2026-08-12 |
| 同日、Yahoo Financeが「SpaceXAI Unveils Grok Bot to Work Like a Team of AI Agents」として報じた | Yahoo Finance https://finance.yahoo.com/news/spacexai-unveils-grok-bot-work-team-ai-agents | 2026-08-12 |
| x.ai公式ニュースページでも本発表が掲載されている | x.ai公式ニュースページ https://x.ai/news | 2026-08-12 |
| Basenorが「Grok Bot Public Beta Is Live — What You Need to Know」として解説記事を掲載した | Basenor https://www.basenor.com/grok-bot-public-beta-is-live-what-you-need-to-know/ | 2026-08-12 |
| 各Grok Botは、専用のクラウドコンピュータ(自身専用の実行環境)を持つ | Unite.AI前掲 / x.ai公式ニュースページ前掲 | 2026-08-12 |
| Grok Botは、顧客の既存ツールにサインインし、監督なしに(unsupervised)複数ステップの業務を完了する | Unite.AI前掲 / Yahoo Finance前掲 | 2026-08-12 |
| SuperGrok Heavy・Cursor Ultra・Cursor Teams Premiumという既存契約プランに組み込まれる形で提供される | Unite.AI前掲 / Basenor前掲 | 2026-08-12 |
| デスクトップ版(Linux版を含む)とiOS版で利用可能 | Unite.AI前掲 / Basenor前掲 | 2026-08-12 |
| xAI社内の利用例として、夜間にアカウントを調査し個別化した営業メールを作成する「outbound Bot」がある | Unite.AI前掲 / x.ai公式ニュースページ前掲 | 2026-08-12 |
| xAI社内の利用例として、デモ環境の不具合を検知・修正する「demo-readiness Bot」がある | Unite.AI前掲 / x.ai公式ニュースページ前掲 | 2026-08-12 |
| xAI社内の利用例として、CRM記録の整備・通話メモの更新・請求書処理・バグ再現を行うBotがある | Unite.AI前掲 / Basenor前掲 | 2026-08-12 |
| イーロン・マスク氏は、今週後半に予定されている「Grok 4.6」のリリースに合わせた、より広範な展開を予告した | Unite.AI前掲 / Yahoo Finance前掲 | 2026-08-12 |

## 3. 候補比較

<!-- 本テーマはツール導入候補の比較ではなく、ニュース系コンテンツテーマのため、
     docs/06_Content_R&Dのモードで採用可否のみを判定する（候補比較表は該当なし）。 -->

該当なし(コンテンツテーマの採用可否判定は「4. 判定」を参照)。

## 4. 合理的推測(事実と区別する)

- 「専用のクラウドコンピュータを持つ」という設計は、複数のBotが並行して長時間・
  監督なしで動くことを前提にした構成であると考えられるが、xAIがこの設計意図を
  明言した一次情報の文言は本調査の範囲では確認できておらず、これは当社の解釈である
- SuperGrok Heavy・Cursor Ultra・Cursor Teamsという既存の上位プランへの組み込みである
  ことから、当面は無料利用者を含む全ユーザー向けではなく、既存の高単価プラン利用者を
  中心とした限定的なベータ展開である可能性が高いと考えられるが、対象範囲の詳細
  (利用者数・国別展開等)は公表されておらず、これも当社の推測である
- xAI社内の利用例(outbound Bot・demo-readiness Bot等)は、自律型AIエージェントの
  一般的な業務適用例として紹介されたものであり、外部顧客が同様の成果を得られるかは
  本調査の範囲では確認できていない

## 5. 推奨アクション

- 本テーマを182本目として採用する(効果: 「常時稼働・専用クラウドコンピュータ・
  監督なしで複数ステップ業務を完了」という具体的な仕組みの新しさ、xAI社内の
  具体的な利用例(outbound Bot・demo-readiness Bot等)が分かりやすいフックになる。
  難易度: 通常の30枚デッキ制作で対応可能。リスク: 「自律型AIエージェント」という
  テーマ上、権限・セキュリティ面の懸念に踏み込みすぎず、公表された事実の範囲で
  整理する必要がある)
- 既存テーマ(`2026-07-24_gpt56-grok45-launch-race`・`2026-08-03_grok-voice-think-fast-2-default`)
  との違いを、README・research.mdの両方で明示する(下記「6. 既存テーマとの関係」参照)

## 6. 既存テーマとの関係(重複でないことの確認)

| 既存テーマ | 主題 | 本テーマとの違い |
|---|---|---|
| `2026-07-24_gpt56-grok45-launch-race`(既存・26本目) | 2026年7月8日にxAIが「Grok 4.5」、翌7月9日にOpenAIが「GPT-5.6」を発表した、1日違いの競合発表を比較したテーマ | **対象製品が異なる**: あちらは基盤モデル「Grok 4.5」自体の発表と、OpenAIの「GPT-5.6」との比較。本テーマは基盤モデルではなく、その上に構築された新製品「Grok Bot」(常時稼働の自律型エージェント)であり、発表時期も約1か月離れている。競合比較という構成でもなく、xAI単独の新製品発表として扱う |
| `2026-08-03_grok-voice-think-fast-2-default`(既存・109本目) | Grokの音声対話機能「Grok Voice」が、新モデル「Think Fast 2.0」へデフォルト切り替えされる予定を扱ったテーマ | **対象製品が異なる**: あちらは既存の音声対話機能(Grok Voice)の内部モデル切り替えという、既存製品のアップデート。本テーマは音声機能とは無関係で、常時稼働・専用クラウドコンピュータを持つ自律型エージェントという**新製品**の立ち上げを扱う。機能領域(音声対話 対 自律業務エージェント)も異なる |

これまでのテーマ(既存180テーマ超)にも、「Grok Bot」を主題としたものはなく、
`ai-company-os/assets/`の既存ディレクトリ一覧で重複がないことを確認済み。

## 7. 不明点と追加調査計画

- ベータ版の具体的な料金体系(SuperGrok Heavy・Cursor Ultra・Cursor Teams Premium
  各プランに組み込まれる形とされるが、Grok Bot単体の追加課金の有無・金額は本調査の
  範囲では確認できていない。不明)
- ベータ版の利用者数・導入企業数の具体的な数字(不明。公表された数値は確認できていない)
- Grok 4.6の正確なリリース日(「今週後半」との予告のみで、具体的な日付は本調査の
  範囲では確認できていない。不明)
- ベータ版利用者からの実際の評価・フィードバック(第三者による独立したレビュー・
  検証は本調査の範囲では確認できていない。不明)
- Grok Botが扱える業務範囲の上限・セキュリティ上の制約(権限管理・監査ログ等)の
  詳細(不明)
- 追加調査計画: Grok 4.6のリリース、およびGrok Botのより広範な展開が発表された
  段階で、本テーマの内容を更新する必要がある

## 政治的中立性・誇張回避についての方針(本テーマ特有の留意事項)

- 「AIが人間の仕事を奪う」といった扇動的な結論には踏み込まず、公表された事実
  (常時稼働・専用クラウドコンピュータ・既存ツールへのサインイン・社内利用例)の
  範囲で整理する
- xAI・イーロン・マスク氏個人への政治的評価は一切行わない
- 特定企業・製品の利用を強く推奨する結論にはしない
- Anthropic・OpenAIへの言及がある場合は、公平でバランスの取れた扱いとする

## 鮮度についての明記

着手日は2026年8月12日。中心となる発表(2026年8月11日、Unite.AI・Yahoo Finance・
x.ai公式ニュースページ・Basenorの報道)は着手日の1日前であり、`docs/06_Content_R&D.md`の
「着手日を含めて2日以内」という鮮度基準を満たす。

## 出典一覧

- Unite.AI「xAI Launches Grok Bot, Always-On AI Teammates With Their Own Cloud Computers」(2026-08-11): https://www.unite.ai/xai-launches-grok-bot-always-on-ai-teammates-with-their-own-cloud-computers/
- Yahoo Finance「SpaceXAI Unveils Grok Bot to Work Like a Team of AI Agents」(2026-08-11): https://finance.yahoo.com/news/spacexai-unveils-grok-bot-work-team-ai-agents
- x.ai公式ニュースページ: https://x.ai/news
- Basenor「Grok Bot Public Beta Is Live — What You Need to Know」: https://www.basenor.com/grok-bot-public-beta-is-live-what-you-need-to-know/

## 判定

**adopt** — 2026年8月11日(着手日2026-08-12の1日前)にUnite.AI・Yahoo Finance・
x.ai公式ニュースページ・Basenorの報道が出ており、「着手日を含めて2日以内」という
鮮度基準を満たす。常時稼働・専用クラウドコンピュータ・監督なしでの複数ステップ業務
完了という具体的な仕組みの新しさ、xAI社内の具体的な利用例がフックになり、既存テーマ
(26本目・109本目)との重複もない。
