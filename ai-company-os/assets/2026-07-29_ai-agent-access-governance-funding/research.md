# 調査: AIエージェントの「権限」に同じ日で計9,000万ドル(2026-07-28)

## 調査目的と問い

2026年7月28日、AIエージェントのアクセス権限・アイデンティティを統制する
セキュリティ企業2社が、同じ日に資金調達を発表した。

- 何が発表されたのか(金額・投資家・製品)
- なぜ今この分野に資金が集まるのか
- 日本の視聴者にとって何が関係するのか
- 確認できなかったことは何か

## 検証済み事実(出典付き)

### 発表1: Act Security、総額6,000万ドルでステルス脱却(2026-07-28)

| 項目 | 内容 | 出典 |
|---|---|---|
| 発表日 | 2026-07-28 | SiliconANGLE(URLに日付) |
| 調達額 | 総額6,000万ドル | SiliconANGLE / Yahoo Finance / FinSMEs |
| 内訳 | シード2,000万ドル(Team8・Bessemer Venture Partners主導、Hetz Ventures・Claltech参加)+ シリーズA 4,000万ドル(Notable Capital主導、Startpoint Capital・SVCI参加) | 検索経由の複数媒体で一致 |
| 創業 | 2025年。医療機器セキュリティのMedigate(Clarotyが約4億ドルで買収)を作ったチーム | SecurityWeek / Calcalist |
| 製品の考え方 | 脆弱性を列挙し続けるのではなく、**攻撃が成立する条件そのもの(過剰なアクセス権限)を減らす**。人・ワークロード・AIエージェントが実際に到達できる範囲に境界を引く | SiliconANGLE / Bessemer |
| キーワード | agentic access sprawl(エージェントによるアクセス範囲の膨張) | SiliconANGLE |

### 発表2: Hush Security、シリーズAで3,000万ドル調達(2026-07-28)

| 項目 | 内容 | 出典 |
|---|---|---|
| 発表日 | 2026-07-28 | PR Newswire(公式リリース) |
| 調達額 | シリーズA 3,000万ドル | PR Newswire / FinSMEs / Ventureburn |
| 投資家 | Akamai Technologies が戦略投資家として新規参加。既存の Battery Ventures・YL Ventures も参加 | PR Newswire / Calcalist |
| 累計調達額 | 4,100万ドル(ステルス脱却から1年未満) | PR Newswire |
| 創業者 | Meta Networks(ネットワークセキュリティ)の創業チーム | Calcalist |
| 製品の考え方 | シークレット・サービスアカウント等の**非人間アイデンティティとAIエージェントを対象に、常時与えっぱなしの権限(standing access)をなくす**。範囲を絞った一時的な権限を都度与え、すべての操作を記録し、1か所から取り消せるようにする | PR Newswire |

### 背景となる数字

| 数字 | 内容 | 出典 | 扱い |
|---|---|---|---|
| 15万超 / 15未満 | 2028年までに平均的なグローバルFortune 500企業は**15万を超えるAIエージェント**を使用する。2025年時点では**15未満** | Gartner 公式プレスリリース(2026-04-28) | 予測であり実績ではない |
| 45対1 | 非人間アイデンティティが人間のアイデンティティを**45対1で上回る** | Security Boulevard(2026-07) | 二次情報。測定対象・母集団は未確認 |
| 64% | 2022年時点で有効だったシークレットのうち、**2026年1月時点でも失効されていなかった割合** | GitGuardian(Security Boulevard経由) | 二次情報経由 |

### 日本語圏での議論

- Okta Japan「AIエージェント時代の到来で高まる『非人間アイデンティティ』管理の重要性」
- 日本総研「AIエージェントへの権限委任 〜拡張される認可の仕組みとKYA(Know Your Agent)の必要性〜」

日本でも同じ論点が、ベンダーとシンクタンクの双方から日本語で提起されている。

## 合理的推測(事実と区別する)

- 同じ日に2社が同じ問題に資金を集めたことは、**投資家側が「エージェントの権限管理」を
  2026年後半の重点領域と見ている**ことを示唆する。ただし2社の発表が事前に調整された
  ものかは不明であり、偶然の同日発表である可能性もある
- Akamai(CDN・セキュリティ大手)が戦略投資家として入ったことは、既存の大手が
  この領域を自社製品に取り込もうとしている動きと読めるが、Akamai側の意図は
  公式には確認できていない

## 不明(確認できなかったこと)

- **各社の公式リリース本文および報道記事の本文**。PR Newswire・SiliconANGLE・
  SecurityWeek・Calcalist・FinSMEs・Ventureburn・Bessemer・Gartner公式・Okta Japan の
  すべてがHTTP 403を返し、本調査環境からは本文を取得できなかった。
  数字は検索エンジンが返した要約経由での確認である
- 両社の日本国内での提供状況・価格・導入事例
- Act Security のシード/シリーズAという内訳の公式な裏付け
- 「AIエージェントのガバナンスが適切だと考える組織は13%」という数字。二次的な要約に
  現れたが出典元を特定できなかったため、**成果物では使用しない**
- 両社の製品が実際にどれだけ効果を上げているかの第三者検証

## 判定

**adopt** — 着手日の前日の発表であり、公式プレスリリースとGartnerの公表予測という
裏付けがある。ただし本文を読めていないため、数字はすべて「報道・公式リリース要約より」
と帰属を明示して扱う。

## 出典一覧

- PR Newswire(Hush Security公式リリース、2026-07-28。本文は403で取得できず): https://www.prnewswire.com/il/news-releases/hush-security-raises-30m-to-close-the-ai-agent-governance-gap-with-akamai-joining-as-strategic-investor-302836307.html
- SiliconANGLE(Act Security、2026-07-28): https://siliconangle.com/2026/07/28/act-security-raises-60m-take-action-agentic-access-sprawl-infrastructure-layer/
- Yahoo Finance(Act Security): https://finance.yahoo.com/technology/ai/articles/act-security-launches-action-centric-110000107.html
- SecurityWeek(Act Security): https://www.securityweek.com/act-security-emerges-from-stealth-to-fight-the-patch-problem/
- Calcalist / CTech(Hush Security): https://www.calcalistech.com/ctechnews/article/sjactjlsfl
- FinSMEs(Hush Security): https://www.finsmes.com/2026/07/hush-security-raises-30m-in-series-a-funding.html
- Ventureburn(Hush Security): https://ventureburn.com/hush-security-raises-30m-ai-agent-governance-gap/
- Bessemer Venture Partners(Act): https://www.bvp.com/news/act-proactive-cloud-security
- Gartner 公式プレスリリース(2026-04-28): https://www.gartner.com/en/newsroom/press-releases/2026-04-28-gartner-identifies-six-steps-to-manage-artificial-intelligence-agent-sprawl
- Okta Japan(非人間アイデンティティ管理): https://www.okta.com/ja-jp/newsroom/articles/nhi-management/
- 日本総研(AIエージェントへの権限委任・KYA): https://www.jri.co.jp/page.jsp?id=114174
- Security Boulevard(非人間アイデンティティ 45対1 / GitGuardian 64%): https://securityboulevard.com/2026/07/the-agent-identity-problem-non-human-identities-outnumber-humans-45-to-1-and-ai-agents-are-making-it-worse/
- ChinaTechNews(2026-07-28 資金調達まとめ): https://www.chinatechnews.com/2026/07/29/126373-venture-capital-startup-funding-roundup-july-28-2026-battery-ventures-bessemer-gradient-team8-y-combinator-more
