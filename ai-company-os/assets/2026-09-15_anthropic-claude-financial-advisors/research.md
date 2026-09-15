# リサーチ: Anthropic、「Claude for Financial Advisors」を発表

## 0. 鮮度についての正直な開示

- 着手日: 2026年9月15日(火・JST)。本件は2026年9月14日に発表されており、
  着手日から1日前の情報である

## 1. 確定している事実(出典付き)

- Anthropicは2026年9月14日、「Claude for Financial Advisors」を発表した。
  カストディアン(資産保管機関)・運用会社・ウェルステック企業へのコネクタと、
  ファイナンシャルアドバイザーの日常業務向けに設計されたスキルをまとめた
  プラグインで、Enterprise顧客向けにCoworkプラグインブラウザから利用できる
  (Unite.AI、Yahoo Finance)
- 含まれるスキルには、アドバイザーのオンボーディング、オルタナティブ投資の
  ブリーフィング、コンプライアンス・AIポリシーレビュー、相続・税務ブリーフィング、
  ポートフォリオのリバランス見直し、面談後のメモ・フォローアップ、面談前の準備、
  見込み客のインテークが含まれる(Unite.AI)
- 連携先はBlackRock・Charles Schwab・Addepar・Envestnet・iCapital・Orion・
  Wealthbox・Wealth.com・Zocksで、アドバイザーが設定時にどれを連携するか選べる。
  既存のClaudeコネクタ(Microsoft 365・Salesforce・DocuSign・Box・FactSet・
  S&P Global・Morningstar)にこれらが加わる形(Unite.AI)
- ライセンスを持たない企業もフォームから申請でき、2026年9月末までに新規
  ライセンスを申請した企業には1回限りの利用クレジットが付与される(Unite.AI)
- この発表は、OpenAIが金融サービス向けChatGPTを発表した後に続く形となった
  (Seeking Alpha)

## 2. 数字の混同防止チェック(本テーマ固有)

- 「発表日(2026年9月14日)」と「クレジット付与の申請期限(2026年9月末)」を、
  それぞれ異なる時点の条件として区別する
- 「新規に追加された連携先(BlackRock等9社)」と「既存の連携先(Microsoft 365等)」を
  混同しない

## 3. 合理的推測(事実と区別)

- (推測)OpenAIの金融サービス向けChatGPT発表に続く形での発表であることから、
  金融アドバイザー向けAI市場での競争を意識した投入タイミングと考えられるが、
  これはAnthropic自身が明示的に競争戦略の意図を説明しているわけではなく、
  報道の文脈からの推測である

## 4. 不明(確認できなかったこと)

- 具体的な料金体系(Enterpriseプランの範囲内かどうかの詳細)
- 日本国内の金融機関・アドバイザーでの利用可否
- 実際の導入社数・具体的な利用事例

## 5. 重複チェック(既存テーマとの区別、必須)

- `ai-company-os/assets/`配下を`.md`ファイル限定で`grep -ril -i "Financial Advisors"`
  で検索した結果、既存テーマはヒットせず、重複は確認されなかった

## 6. 判定

**adopt** — Unite.AI・Seeking Alpha・Yahoo Finance・US Newsを含む複数の独立した
媒体で確認できた。着手日から1日前という高い鮮度も確保しており、金融・アドバイザー
業務に関わる視聴者にとって、面談準備やコンプライアンス確認などの時間を減らせる
という具体的な有益性を持つ(対象は主にEnterprise顧客・専門職向けである点は
明示する)。

## 出典一覧

- Unite.AI: Anthropic Launches Claude for Financial Advisors With Partner Connectors
- Seeking Alpha: Anthropic launches Claude for financial advisors after OpenAI's ChatGPT for financial services
- Yahoo Finance: Anthropic Launches Claude for Financial Advisors
- US News(2026-09-14): Anthropic Targets Financial Advisers With New Claude Tool
