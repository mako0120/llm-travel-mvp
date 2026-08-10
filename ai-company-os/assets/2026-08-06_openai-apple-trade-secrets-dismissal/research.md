# 調査: OpenAI、Appleの営業秘密訴訟の却下を裁判所に申立て——Apple自身のセキュリティ運用を理由に反論(2026年8月6日 Axios/TechCrunch/Bloomberg報道)

<!-- docs/06_Content_R&D.md 準拠。出典のない数字は書かない -->

## メタ情報

- 調査名: OpenAI、Appleの営業秘密訴訟の却下を申立て——「認証情報の隙間」理論による反論
- 調査日: 2026年8月10日
- 調査担当: Claude Code(AI Company OS 154本目)
- 関連 Issue: なし(定期実行round91での直接制作。Issue非経由)

## 0. 鮮度についての正直な開示(必須)

- 本テーマの中心となる申立ての発表日は **2026年8月6日**。続報(claimsjournal.com)は
  **2026年8月7日**。
- 着手日は **2026年8月10日**。申立てから**4日前**(続報から3日前)であり、
  `docs/06_Content_R&D.md`の鮮度基準(2026-08-05追記: 着手日を含めて2日以内を必須とする)を
  **満たしていない**。
- `ai-company-os/research/2026-08-10_theme-evaluation-round91.md`に記録の通り、本ラウンドでは
  13件以上の異なる切り口でWebSearchを実施したが、着手日から2日以内の候補が見つからなかった。
  一部「カリフォルニア州フロンティアAI安全法が本日可決」という有力に見える候補も検索結果に
  現れたが、二次検証の結果、実在しない/古い法案(SB1047・SB53)との混同であることが判明した
  ため不採用とし、正直に評価表へ記録した。
- `docs/06_Content_R&D.md`が定める「探索を尽くしてもなお2日以内の候補が1本も見つからない
  場合に限り、次点として最も新しい候補を暫定的に採用してよい(例外的な最終手段)」という
  規定に基づき、本テーマ(申立てから4日前)を鮮度基準の例外として採用した。
- **これは2ラウンド連続の例外運用である点も、正直に開示する。** 直前のround90(152本目
  `2026-08-07_rippling-ai-spend-console`)も同様に鮮度基準の例外採用だった。連続する例外運用を
  常態化させないよう、次回以降のラウンドでは改めて2日以内の基準を優先して探索する。この点は
  README.mdの「選定理由」にも同様に明記する。

## 1. 調査目的と問い

- Appleは元々OpenAIに対して何を訴えていたのか(背景・経緯)
- OpenAIが2026年8月6日に申立てた「却下申立て」とは具体的に何をどう主張しているのか
- OpenAIの反論の核心とされる「認証情報の隙間」理論とはどのような仕組みか
- OpenAIが挙げる却下の法的根拠は何か
- Apple・OpenAI双方の主張をどのように中立に整理できるか
- 今後のスケジュール(仮差止命令審理・回答期限)はどうなっているか
- 確認できなかったことは何か(元社員の氏名、具体的な営業秘密の内容、Apple側の反論、最終判断)

## 2. 検証済み事実(出典付き)

| 事実 | 出典(URL) | 確認日 |
|---|---|---|
| 2026年8月6日、OpenAIが連邦判事に対し、Appleが起こした営業秘密訴訟の却下を求める動議(motion to dismiss)を提出した | Axios(2026-08-06) https://www.axios.com/2026/08/06/openai-apple-motion-to-dismiss | 2026-08-10 |
| OpenAIの申立ての中心的な主張は、Apple自身のセキュリティ運用が訴訟の根拠を弱めている、というもの | TechCrunch(2026-08-06)「OpenAI says Apple's own security practices undermine its trade secrets case」 https://techcrunch.com/2026/08/06/openai-says-apples-own-security-practices-undermine-its-trade-secrets-case/ | 2026-08-10 |
| Bloombergも同日、OpenAIがAppleの訴訟の却下を裁判所に求めたことを報じた | Bloomberg(2026-08-06)「OpenAI Asks Judge to Toss Apple's Trade Secrets Lawsuit」 https://www.bloomberg.com/news/articles/2026-08-06/openai-asks-judge-to-toss-apple-suit-alleging-trade-secret-theft | 2026-08-10 |
| 9to5Mac・TheNextWeb・TheAIInsiderも同日、同内容を報じ、要点を裏付けている | 9to5Mac(2026-08-06) https://9to5mac.com/2026/08/06/openai-apple-thrown-out-lawsuit/ 、TheNextWeb https://thenextweb.com/news/openai-motion-dismiss-apple-trade-secrets-case 、TheAIInsider https://theaiinsider.tech/2026/08/06/openai-files-motion-to-dismiss-apples-trade-secrets-lawsuit-cites-security-lapses/ | 2026-08-10 |
| claimsjournal.comが2026年8月7日に続報を報じた | claimsjournal.com(2026-08-07) https://www.claimsjournal.com/news/national/2026/08/07/339348.htm | 2026-08-10 |
| OpenAIの申立書は31ページに及ぶ | TechCrunch/Bloomberg(2026-08-06)経由 | 2026-08-10 |
| OpenAIの中心的な反論は、Appleが業務用に個人のiCloudアカウント利用を奨励し、業務データと個人データが混在したことが、元エンジニアの退職後のサーバーアクセスを許した「認証情報の隙間(credential gap)」を生んだ、というもの | TechCrunch(2026-08-06) | 2026-08-10 |
| Appleは業務用端末に残る個人のiMessageを審査していたと申立書は指摘している | TechCrunch(2026-08-06) | 2026-08-10 |
| 申立書には「Apple should not be permitted to use a baseless and pretextual lawsuit to make up for its shortcomings.」(Appleは、根拠のない口実的な訴訟を、自社の力不足を埋め合わせるために利用することを許されるべきではない)という主張が含まれる | 複数メディア経由(Axios/TechCrunch/Bloomberg、2026-08-06) | 2026-08-10 |
| 申立書は、この訴訟がAppleの人材確保・AI競争での苦戦を穴埋めするためのものだとの主張を含む | 複数メディア経由(2026-08-06) | 2026-08-10 |
| 複数の報道によれば、申立書全体で「fail」という語(変化形を含む)がおよそ50回近く使われているという | 複数メディア経由(2026-08-06) | 2026-08-10 |
| OpenAIの却下申立ての法的根拠は、(1)Appleが法的に保護されるべき具体的・有形な営業秘密の存在を立証する基準を満たしていないこと、(2)Appleが、OpenAIや元社員2名による不正行為を具体的かつ説得力を持って主張できていないこと、の2点 | TechCrunch/Bloomberg(2026-08-06)経由 | 2026-08-10 |
| Appleは元々、OpenAIと元Apple社員2名を相手取り、営業秘密の不正利用・求職者への不適切な機密情報提供の勧誘を訴えていた | Axios/TechCrunch/Bloomberg(2026-08-06)経由 | 2026-08-10 |
| この訴訟は、OpenAIの消費者向けハードウェア事業への参入という背景と関連づけられている | Axios/TechCrunch/Bloomberg(2026-08-06)経由 | 2026-08-10 |
| Appleは別途、OpenAIおよび元社員2名による情報のアクセス・利用・開示を差し止める仮差止命令(preliminary injunction)を、2026年8月4〜5日ごろに申立てていた | 提供された事実情報(round91評価表・README指示に基づく背景情報)に基づく。本調査の直接WebSearch検索でも同旨の報道が確認された | 2026-08-10 |
| 仮差止命令についての審理は、2026年10月1日にサンノゼ連邦地裁で予定されている | 同上 | 2026-08-10 |
| OpenAIには、Appleの仮差止命令申立てに正式回答する裁判所指定の期限として2026年8月17日が設定されている | 同上 | 2026-08-10 |

## 3. 候補比較

<!-- 本テーマは評価表(research/2026-08-10_theme-evaluation-round91.md)の候補2として、モードBで採用済み -->

該当なし(定期実行round91の評価表で採用済みのテーマのため、本レポート内での候補比較は
実施しない)。評価表全文は `ai-company-os/research/2026-08-10_theme-evaluation-round91.md` を参照。

## 4. 合理的推測(事実と区別して書く)

- OpenAIが「認証情報の隙間」理論を前面に押し出しているのは、Appleが主張する不正行為の
  「意図性」を否定し、むしろApple自身の管理体制の不備が原因であると論点をずらす訴訟戦略と
  考えられるが、これは当社の解釈であり、OpenAI自身がそのように公式に説明しているとまでは
  確認できていない
- 申立書で「fail」という語が繰り返し使われているという報道は、OpenAIがAppleの人材流出・
  AI競争での苦戦という文脈を強調する意図的なレトリックである可能性が考えられるが、これも
  当社の推測であり、断定はできない
- 仮差止命令の審理(10月1日)に先立ち、却下申立てへの判断がどのタイミングで下されるかは
  本調査の範囲では確認できておらず、両者の法的スケジュールがどう絡み合うかは不明である

## 5. 推奨アクション

- 本テーマをそのままデッキ化する(効果: 「訴えられた側が反論した」という意外性が伝わりやすい。
  難易度: 低。リスク: 中——法的紛争かつ2大企業の対立のため、中立性の徹底が必須。承認境界には
  触れない)
- 鮮度の例外(申立てから4日前)であることをREADME・research.mdの両方で正直に明記し、
  2ラウンド連続の例外運用である点もあわせて開示する
- Apple・OpenAI双方の主張を専用スライド(比較表)で中立に整理し、「どちらが正しいかを判断
  しない」という中立性の明示を専用スライドで行う
- 元社員2名の氏名など確認できていない情報は創作せず、「不明」として明記する

## 6. 不明点と追加調査計画

以下は取得できず、推測で埋めていない。

- Appleが元々訴えていた2名の元Apple社員(現OpenAI在籍)の氏名。信頼できる出典で確認できて
  いないため、本テーマでは特定・言及しない
- Appleが主張する具体的な営業秘密の内容(製品設計・技術情報等の詳細)
- Apple側による、OpenAIの却下申立てへの正式な反論・応答(本調査の時点ではまだ提出されて
  いない)
- 最終的な裁判所の判断・訴訟の結果(審理は2026年10月1日予定で、係属中の案件のため未確定)
- 「fail」という語の正確な出現回数(複数の報道が「およそ50回近く」という表現にとどまり、
  厳密な回数が一次資料で確認できていない)
- 仮差止命令の審理(10月1日)と、却下申立てへの判断がどのようなタイミング・順序で
  進行するかの詳細

## 出典一覧

- Axios(2026-08-06): https://www.axios.com/2026/08/06/openai-apple-motion-to-dismiss
- TechCrunch(2026-08-06): https://techcrunch.com/2026/08/06/openai-says-apples-own-security-practices-undermine-its-trade-secrets-case/
- Bloomberg(2026-08-06): https://www.bloomberg.com/news/articles/2026-08-06/openai-asks-judge-to-toss-apple-suit-alleging-trade-secret-theft
- 9to5Mac(2026-08-06): https://9to5mac.com/2026/08/06/openai-apple-thrown-out-lawsuit/
- claimsjournal.com(2026-08-07): https://www.claimsjournal.com/news/national/2026/08/07/339348.htm
- TheNextWeb: https://thenextweb.com/news/openai-motion-dismiss-apple-trade-secrets-case
- TheAIInsider: https://theaiinsider.tech/2026/08/06/openai-files-motion-to-dismiss-apples-trade-secrets-lawsuit-cites-security-lapses/

## 既存テーマとの関係(重複でないことの確認)

`ai-company-os/assets/` 配下に、AppleとOpenAIの営業秘密訴訟を扱った既存テーマは存在しない
(重複確認済み、README指示に記載の通り)。

## 政治的中立性・法的中立性についての方針(本テーマ固有)

本テーマはApple・OpenAIという2つの私企業間の商業(民事)訴訟に関する事実報道であり、
政府・政治に関する話題ではない。政治的な主張・立場表明は一切行わない。また、Apple側・
OpenAI側のどちらの主張が正しいかについても、本テーマでは判断・断定を行わない。双方の
主張は、それぞれの提出書面・報道内容として出典を明記したうえで並列に紹介する
(deck_spec.jsonのスライド16「比較」・スライド17「中立性の明示」を参照)。

## 判定

**adopt(鮮度基準の例外採用、2ラウンド連続)** — Axios・TechCrunch・Bloombergという主要メディア
3社が同日(2026-08-06)に報じ、9to5Mac・TheNextWeb・TheAIInsiderが要点を裏付け、
claimsjournal.comが翌日(8/7)に続報を出している。AI業界の2大企業(Apple・OpenAI)の法廷闘争
という著名性、「訴えられた側が相手のセキュリティ体制を理由に反論した」という意外性がフックと
なる。一方、申立て日(2026-08-06)は着手日(2026-08-10)から4日前であり、`docs/06_Content_R&D.md`
の通常の鮮度基準(2日以内)を満たさない。探索を尽くしても2日以内の候補が見つからなかったため
の例外的最終手段としての採用であり、かつ直前のround90(152本目)に続く2ラウンド連続の例外運用
である点を、README・research.mdで一貫して正直に開示する。また、私企業間の商業訴訟という
性質上、政治的中立性・法的中立性(どちらが正しいかを判断しない)を徹底する。
