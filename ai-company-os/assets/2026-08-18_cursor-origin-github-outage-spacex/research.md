# リサーチ: SpaceX傘下Cursorが「Origin」始動、まさかGitHub大規模障害と同日

- 調査担当: Claude Code(AI Company OS)
- 着手日: 2026-08-19(JST)
- 事象発生日: 2026-08-18(米国時間、発表・障害とも)
- 鮮度判定: 着手日の前日(1日前)。基準(着手日または前日のみ)を満たす。

## 要旨

AIコーディングエディタ「Cursor」を展開するAnysphere(2026年8月14日にSpaceXが
600億ドルの全株式交換で買収完了、社内新部門「SpaceXAI」として統合済み)が、
2026年8月18日、GitHubに対抗する独自のコードホスティングサービス
「Origin」を有料プラン向けに早期ベータとして展開開始した。偶然にも同じ
2026年8月18日、GitHub側で約8時間に及ぶ大規模障害が発生し、Web・APIの
エラー率が約20%、一部のリポジトリコンテンツ・アーカイブダウンロードでは
約50%に達したと報じられた。本テーマでは、この2つの出来事とその背景を
出典付きで整理する。

## Origin(Cursor)の内容

| 項目 | 内容 |
|---|---|
| 発表日 | 2026年8月18日(月) |
| 展開範囲 | Cursorの全有料プラン向けに早期ベータとして展開開始 |
| 主要機能 | リポジトリ管理・プルリクエスト・コードレビュー・GitHubとの双方向同期 |
| 連携済みサービス | Vercel(PRごとのプレビューデプロイ)・Depot・Buildkite(既存のGitHub Actionsワークフローをそのまま実行するCI) |
| 位置づけ | GitHubを完全に置き換えるものではなく、既存のGitHubリポジトリと同期しながら利用できる設計 |

出典: VentureBeat・SiliconANGLE・TestingCatalog・Techzine Global(2026-08-18)

## GitHub大規模障害の内容

| 項目 | 内容 |
|---|---|
| 発生日 | 2026年8月18日 |
| 継続時間 | 約8時間(米国東部時間午前9時40分頃〜午後5時15分頃まで断続的に) |
| エラー率 | Web・APIトラフィックで約20%、一部リポジトリコンテンツ・アーカイブダウンロードで約50% |
| 影響範囲 | API・リポジトリダウンロード・GitHub Actions・Webhooks・Pages・Copilot等 |
| 原因 | 本調査時点で技術的な原因の詳細は公式に開示されていない。AIコーディングツールの利用急増によるトラフィック負荷増大が背景として指摘されている |

出典: DevOps.com・IT Pro・BleepingComputer・Engadget(2026-08-18)

## 「同日発生」という偶然性について(正直な開示)

- Cursor Originの発表とGitHub障害は、いずれも2026年8月18日に発生した
- 複数の報道(VentureBeat等)がこの2つを結び付けて報じているが、Origin自体の
  開発・ベータ展開のタイミングがGitHub障害を見越して意図的に合わせられた
  ものかどうかは、本調査の範囲では確認できていない。あくまで結果的に同日と
  なった可能性が高いと考えられ、断定はしない
- GitHubは前日(8月17日)にも別の障害への修正実施を発表しており(Forbes報道)、
  今回の障害は「一連の信頼性問題」の最新の一つと位置づけられている

## Anysphere(Cursor運営会社)のSpaceX買収について

| 項目 | 内容 |
|---|---|
| 買収発表日 | 2026年6月16日 |
| 買収完了日 | 2026年8月14日(Origin発表の4日前) |
| 買収形態 | 全株式交換によるリバース・トライアングル・マージャー |
| 買収額 | 600億ドル(直近のシリーズD時点の評価額293億ドルからほぼ倍増) |
| 買収後の位置づけ | SpaceX社内の新部門「SpaceXAI」として統合 |

出典: CNBC・Yahoo Finance・Qz(2026年6月16日発表分・8月14日完了分の報道)

## 重要な留保事項(正直な開示・誇張しない)

- Origin発表とGitHub障害の同日発生について、意図的な狙い撃ちかどうかは
  確認できていない。断定的な「GitHubを狙い撃ちした」という表現は用いない
- GitHub障害の技術的な根本原因は、本調査時点で公式には開示されていない
- Cursor Originはあくまり早期ベータであり、「エージェント向け機能は近日提供」
  とされている段階の機能も含まれる。全機能が現時点で利用可能というわけでは
  ない
- 一部報道では「Origin利用時のデータ取り扱い条件が明示されていない」との
  指摘があるが、この点の正確な契約条件までは本調査の範囲では確認できて
  いない
- 本テーマは特定企業(Cursor/Anysphere、GitHub/Microsoft)の製品利用を
  推奨・批判するものではなく、報じられた事実の紹介にとどめる

## 独立性の確認(重複テーマでないことの確認)

`ai-company-os/assets/` 配下を`--include="*.md" --include="*.json"`で
「cursor origin」「github outage」等を検索した結果、既存テーマは存在しない
ことを確認済み(2026-08-19時点)。

## 政治的中立性・推奨表明の回避

本テーマは製品発表・システム障害という客観的事実の紹介であり、政治的な
論点は含まない。特定企業の製品利用を強く推奨する、または他社を貶める
ような表現は用いない。

## 出典

- VentureBeat: "Cursor launches Origin code hosting platform as GitHub outage exposes opening in AI coding race"
  https://venturebeat.com/infrastructure/cursor-launches-origin-code-hosting-platform-as-github-outage-exposes-opening-in-ai-coding-race
- SiliconANGLE: "Cursor launches Origin code hosting service to compete with GitHub"
  https://siliconangle.com/2026/08/17/cursor-launches-origin-code-hosting-service-to-compete-with-github/
- TestingCatalog: "Cursor begins Origin code hosting rollout for paid plans"
  https://www.testingcatalog.com/cursor-begins-origin-code-hosting-rollout-for-paid-plans/
- DevOps.com: "Microsoft's GitHub Hit by Major Outage as AI-Driven Demand Strains Infrastructure"
  https://devops.com/microsofts-github-hit-by-major-outage-as-ai-driven-demand-strains-infrastructure/
- IT Pro: "The GitHub outage explained: What happened, who was affected, and how long did it last?"
  https://www.itpro.com/software/development/the-github-outage-explained-what-happened-who-was-affected-and-how-long-did-it-last
- CNBC: "SpaceX to acquire the AI coding startup Cursor for $60 billion"
  https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html
- Yahoo Finance: "SpaceX completes record $60 billion acquisition of AI coding platform Cursor"
  https://finance.yahoo.com/technology/ai/articles/spacex-completes-record-60-billion-131311785.html
- Techtimes: "Cursor Origin Ships With No Data Terms: SpaceX Now Holds Paid Developers Code"
  https://www.techtimes.com/articles/324838/20260818/cursor-origin-ships-no-data-terms-spacex-now-holds-paid-developers-code.htm
