# 調査: Hush Securityのシリーズ A調達・「AIエージェント統治」プラットフォーム(2026-07-29発表)

## 調査目的と問い

2026年7月29日、企業内で稼働するAIエージェントに厳格なID・権限管理を与える
「非人間ID統治」プラットフォームを開発するHush Security(イスラエル・テル
アビブ)が、シリーズAで3,000万ドルを調達したと発表した。セキュリティ大手
Akamai Technologiesが戦略投資家として参加した点が特徴的。

- 何が発表されたのか。Hush Securityは何をする製品なのか
- 「AIエージェントの統治」とは具体的に何を指すのか
- Akamaiが戦略投資家として参加する意味は何か
- 創業チームの経歴・成長スピードはどこまで確かか
- 引用されているGartner・Omdiaの統計はどの発表由来か
- 確認できなかったことは何か

## 検証済み事実(出典付き)

### 発表: Hush Security シリーズA調達(2026-07-29)

| 項目 | 内容 | 出典 |
|---|---|---|
| 発表日 | 2026-07-28/29 | PRNewswire(一次発表) / SecurityWeek / fintech.global |
| 調達額 | シリーズAとして3,000万ドル | PRNewswire / SecurityWeek / fintech.global |
| 既存投資家(継続) | Battery Ventures、YL Ventures | SecurityWeek / fintech.global |
| 新規の戦略投資家 | Akamai Technologies | PRNewswire / SecurityWeek / cioinfluence |
| 累計調達額 | 4,100万ドル(シード1,100万ドル+シリーズA3,000万ドル) | fintech.global / ynetnews |
| ステルス解除・シード調達 | 2025年9月10日にステルス解除、Battery Ventures・YL Ventures主導で1,100万ドルのシード調達を発表 | PRNewswire(2025-09-10付） |
| 創業チーム | Alon Horowitz、Micha Rave、Chen Nisnkorn、Shmulik Ladkaniの4名。全員、2019年にProofpointが買収したMeta Networks出身 | Calcalist/CTech |
| CEO | Micha Rave氏(共同創業者) | SecurityWeek / ynetnews |
| 拠点 | イスラエル・テルアビブ | Calcalist/CTech |
| 製品概要(当初) | 「secretless machine access」= 従来のシークレット管理・Vault(認証情報保管庫)を不要にする、ランタイムでのポリシー駆動型アクセス制御プラットフォーム | PRNewswire(2025-09-10付) |
| 製品概要(現在) | すべてのAIエージェントを中央レジストリに登録し、常設の認証情報(standing credentials)を持たせず、実行時にスコープ限定のJust-In-Time(JIT)権限のみを付与。全アクションをログ記録し、中央集権的な「キルスイッチ」で緊急停止可能 | fintech.global / SecurityWeek |
| CEOコメント | 「企業はすでに人材やアプリケーションのID管理の方法を知っている。しかし今、ソフトウェアが自らの意思で、最も機密性の高いシステム内で自律的に動いている。AIエージェントにはAPIキーではなく、厳格なIDが必要だ」(意訳) | 複数媒体経由の同一引用(SecurityWeek / fintech.global 等) |
| 統計(1) | Gartner予測: 2028年までにFortune 500企業は平均15万体超のAIエージェントを運用する見込み。1年前は15体未満だった | SecurityWeek / fintech.global(いずれもGartnerを引用) |
| 統計(2) | Omdia調査: 組織の96%が、自律型AIエージェント向けに設計されていない統治フレームワークでAIエージェントを運用している | SecurityWeek / fintech.global(いずれもOmdiaを引用) |
| 資金使途(推測を含む) | AI/自律型システム向けID・アクセス管理製品の拡張、Akamaiとの戦略的連携を通じたエンタープライズ展開の加速 | fintech.global(記述に基づく要約) |

## 合理的推測(事実と区別する)

- 創業チームがMeta Networks(2019年Proofpost買収)出身のシリアルアントレプレナー
  であることから、投資家が「実績あるチームへの再投資」として評価した可能性が
  高いと考えられるが、投資判断の具体的な理由は一次情報で明言されていない
- Akamaiが戦略投資家として参加した背景には、AkamaiがCDN・エッジセキュリティ企業
  として、エンタープライズの「非人間ID」領域を将来の製品ラインへ取り込む狙いが
  あると推測されるが、Akamai側の意図は一次情報で確認できていない
- 「secretless machine access」(2025年9月)から「AIエージェント統治」(2026年
  7月)へと製品の打ち出し方が変化しているのは、AIエージェントの急増という
  市場トレンドに合わせたポジショニング変更だと考えられるが、技術的な変更の
  有無は確認できていない

## 不明(確認できなかったこと)

- Hush Securityの具体的な企業評価額(バリュエーション)
- 現在の導入顧客企業名・導入社数(具体的な事例は一次情報で確認できず)
- 日本国内での顧客・展開・提携の有無
- 投資家Battery Ventures・YL Ventures・Akamaiそれぞれの出資比率・出資額の内訳
- 従業員数・チーム規模
- PRNewswire原文および他の主要メディア記事本文全体(SecurityWeek、
  fintech.global、ynetnews、Morningstar、cioinfluence、news4hackers、
  いずれもWebFetchでHTTP 403エラーとなり直接アクセスできず、WebSearchの
  検索結果スニペット経由で複数メディアの記述を突き合わせて確認した)

## 判定

**adopt** — 着手日の前日(2026-07-28/29)のPRNewswire一次発表であり、
SecurityWeek・fintech.global・ynetnews・Morningstar・cioinfluence等の
独立した複数メディアが同じ発表を報じている。「2028年までにFortune 500企業が
平均15万体のAIエージェントを運用(前年は15体未満)」「96%の組織が未整備の
統治モデルで運用」というGartner・Omdia由来の具体的な数字が2つ揃っており、
30枚のスライド化に耐える。創業チームの経歴(Meta Networks→Proofpost買収)と
「シード1,100万ドル→1年未満でシリーズA3,000万ドル」という成長スピードも
ストーリー性がある。既存57テーマに「AIエージェントの統治・セキュリティ」を
正面から扱ったものはなく差別化できる。ただし日本国内の顧客・拠点、導入事例、
評価額は確認できておらず、成果物内で明示して扱う。

## 出典一覧

- PRNewswire(一次発表, 2026-07-29): https://www.prnewswire.com/news-releases/hush-security-raises-30m-to-close-the-ai-agent-governance-gap-with-akamai-joining-as-strategic-investor-302836307.html
- SecurityWeek(2026-07-29): https://www.securityweek.com/hush-security-raises-30-million-for-ai-agent-governance/
- fintech.global(2026-07-29): https://fintech.global/2026/07/29/hush-lands-30m-as-ai-agents-outpace-enterprise-security/
- ynetnews(2026-07-29): https://www.ynetnews.com/business/article/s1mqixuhfx
- Morningstar/PRNewswire転載(2026-07-28): https://www.morningstar.com/news/pr-newswire/20260728io12536/hush-security-raises-30m-to-close-the-ai-agent-governance-gap-with-akamai-joining-as-strategic-investor
- cioinfluence(2026-07-29): https://cioinfluence.com/security/hush-security-raises-30m-to-close-the-ai-agent-governance-gap-with-akamai-joining-as-strategic-investor/
- Hush Securityステルス解除・シード調達発表(一次発表, 2025-09-10): https://www.prnewswire.com/news-releases/hush-security-emerges-from-stealth-with-secretless-machine-access-platform-ending-the-need-for-vaults-302552285.html
- Calcalist/CTech(創業チーム経歴, シード調達時): https://www.calcalistech.com/ctechnews/article/bjngu11h5gx
- テーマ評価の記録: `ai-company-os/research/2026-07-30_theme-evaluation-round36.md`
