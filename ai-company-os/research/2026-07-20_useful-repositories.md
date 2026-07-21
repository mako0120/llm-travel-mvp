# 調査レポート: AI Company OS に役立つ外部リポジトリ

<!-- templates/research_report_template.md 準拠 -->

## メタ情報

- 調査名: Claude Code / Cowork 公式エコシステムの有用リポジトリ調査
- 調査日: 2026-07-20
- 調査担当: Claude Code(主実装担当セッション)
- 関連 Issue: #65

## 1. 調査目的と問い

- AI Company OS(PowerPoint・Canva・教育教材・調査レポート制作)を強化できる外部リポジトリはあるか。
- 「GitHubでClaudeを無限に使える」系の調査の延長として、公式(anthropics)エコシステムに他の有用な資産がないか。
- 未確認の機能を使えると断定しないため、README・LICENSE を実際に取得して確認した。

## 2. 検証済み事実(出典付き)

| 事実 | 出典(URL) | 確認日 |
|---|---|---|
| `anthropics/skills` は Claude が動的に読み込む「スキル」の公式実装例集。PowerPoint/Excel/Word/PDF のドキュメント処理スキルを含む。GitHub上で16.3万star、本日(2026-07-21)も更新されている | https://github.com/anthropics/skills | 2026-07-20 |
| 同リポジトリの多くのスキルは Apache 2.0 だが、**ドキュメント処理系スキル(pptx/docx/xlsx/pdf)は "source-available, not open source"** と明記されている | https://raw.githubusercontent.com/anthropics/skills/main/README.md | 2026-07-20 |
| 本セッションで既に使える `pptx`/`docx`/`xlsx`/`pdf` スキルは、この `anthropics/skills` 由来のものと一致する(Claude Code に標準搭載) | 本セッションのツール一覧(Skill) | 2026-07-20 |
| `anthropics/knowledge-work-plugins` は Claude Cowork 向けの職務別プラグイン集(営業・顧客支援・製品管理・マーケティング・法務・財務・データ分析等11領域)。Apache License 2.0。2.29万star、本日更新 | https://github.com/anthropics/knowledge-work-plugins ​/ LICENSE: https://raw.githubusercontent.com/anthropics/knowledge-work-plugins/main/LICENSE | 2026-07-20 |
| `anthropics/k12-teacher-skills` は K-12教員向けスキル(`k12-lesson-planning`: 学習指導要領準拠の授業計画作成 / `k12-lesson-differentiation`: 習熟度別教材への調整)。2026-07-10作成の新しい公式リポジトリで、学習支援機関との協働と明記 | https://github.com/anthropics/k12-teacher-skills | 2026-07-20 |
| `anthropics/claude-plugins-official` は Anthropic公式管理のプラグインディレクトリ。3.2万star | https://github.com/anthropics/claude-plugins-official | 2026-07-20 |
| `anthropics/claude-cookbooks` はClaude API活用のノートブック集。4.9万star、長期メンテナンス継続中(2023年〜) | https://github.com/anthropics/claude-cookbooks | 2026-07-20 |
| `hesreallyhim/awesome-claude-code` はコミュニティ運営のキュレーションリスト(非公式)。5.05万star | https://github.com/hesreallyhim/awesome-claude-code | 2026-07-20 |

## 3. 候補比較

| 候補 | 提供元 | 用途 | 導入条件 | ライセンス | 更新状況 | セキュリティ | 期待効果 | リスク | 判定 |
|---|---|---|---|---|---|---|---|---|---|
| anthropics/skills | Anthropic公式 | PowerPoint/Word/Excel/PDF生成・編集の参照実装 | 追加インストール不要(Claude Code に同梱のpptx/docx/xlsx/pdfスキルとして既に利用中) | 大半Apache 2.0、文書系スキルはsource-available | 活発(当日更新) | 公式一次配布、高 | 既に `verify_pptx.py`/`build_deck.py` と役割分担して運用中 | source-availableスキルの改変・再配布は不可の可能性→再配布しない前提で利用 | **adopt(継続採用・既に運用中)** |
| anthropics/knowledge-work-plugins(marketing) | Anthropic公式 | 競合調査・キャンペーン企画・コンテンツ下書き(/competitive-brief /campaign-plan /draft-content 等) | claude.ai プラグインカードからインストール(2026-07-21 オーナー承認済み) | Apache 2.0 | 活発(当日更新) | 公式、高 | 調査レポート・デッキ構成づくりの型をプラグイン単位で流用でき、docs/06の型を強化できる | 連携先(Canva/Slack/HubSpot等)は必要なものだけ個別に有効化する | **adopt(承認済み・試用開始)** |
| anthropics/k12-teacher-skills | Anthropic公式(学習支援機関と協働) | 授業計画・習熟度別教材調整 | GitHubから取得して手動統合、または Claude for Teachers アカウントで標準搭載 | 確認要(リポジトリ側に明記なし、他リポジトリ同様Apache系の可能性が高いが未確認) | 非常に新しい(2026-07-10〜)、活発 | 公式、高 | docs/07_AI_Education.md の「対象レベル別教材設計」を具体的なスキルとして補強できる | ライセンス未確定のため断定回避。教育現場向けの評価ルーブリックは要件が特殊で直接転用は要検証 | **watch(ライセンス確認後にtrial検討)** |
| anthropics/claude-plugins-official | Anthropic公式 | 高品質プラグインの公式ディレクトリ | `claude.com/plugins` からインストール | 個別プラグインごとに確認要 | 活発 | 公式、高 | 汎用。特定ニーズが出た時点で個別プラグインを調査 | 個別プラグイン単位でしか評価できない(ディレクトリ自体は評価対象外) | **watch** |
| anthropics/claude-cookbooks | Anthropic公式 | Claude API活用パターン集(Jupyter Notebook) | リポジトリ参照のみ、インストール不要 | 要確認(cookbooks配下は概ねMIT系が一般的だが本調査では未確認) | 活発(2023年〜継続) | 公式、高 | Claude API直接呼び出しが必要になった際の実装パターン集として有用 | 現状 Claude Code/Cowork 経由の運用のみで API直叩きの予定なし→優先度低 | **watch** |
| hesreallyhim/awesome-claude-code | コミュニティ(非公式) | Claude Code関連ツールの発見用キュレーションリスト | リンク集を読むのみ | リスト自体はCC0系が一般的(個別ツールは各自確認) | 非常に活発 | 非公式・記載内容の一次検証は都度必要 | 新しいツールの「発見」入口として有用(docs/06の情報源優先順位where「コミュニティは発見用途のみ」に合致) | 個々のリンク先ツールの安全性・ライセンスは記載を鵜呑みにしない | **watch(発見用途限定)** |

## 4. 合理的推測(事実と区別して記載)

- `anthropics/skills` の文書系スキル(pptx等)が "source-available" である以上、AI Company OS の `scripts/build_deck.py` のような**自前の生成ロジック**を持つことには、公式スキルだけに依存しないという意味で継続的な価値がある(推測: 公式スキルの仕様変更や利用条件変更の影響を受けにくい)。
- `knowledge-work-plugins` は Cowork 向けだが、プラグイン本体は Markdown ベースであるため、Claude Code セッションでも構成を参考にテンプレート化できる可能性が高い(推測: 未検証、trial時に確認要)。

## 5. 推奨アクション

1. **knowledge-work-plugins / marketing の試験導入(2026-07-21、オーナー承認済み)**: `/competitive-brief` `/campaign-plan` が `docs/06_Content_R&D.md`(調査レポート)・デッキ構成づくりに直結すると判断し推薦。`design`(Figma中心・PPT機能なし)は比較のうえ除外。オーナーが承認し、claude.ai のプラグインインストールカードを提示済み(UI操作で完了)。連携先(Slack/Canva/Figma/HubSpot/Amplitude/Notion/Ahrefs/Similarweb/Klaviyo/Supermetrics)は必要なものだけ個別に有効化する。判定を **trial → adopt(試用開始)** に更新。
2. **k12-teacher-skills のライセンス確認(低優先度)**: AI教育教材(docs/07)の対象が将来K-12に広がる場合のみ、正式なライセンス文言を再確認してから判定を trial に格上げする。
3. **anthropics/skills との役割分担を docs に明記**: 既に採用済みだが、「なぜ build_deck.py を自前で持つか」の理由をどこにも書いていなかったため、`docs/04_PowerPoint.md` に一文追記する(本レポートと合わせてこのPRで実施)。

## 6. 不明点と追加調査計画

- `k12-teacher-skills` と `claude-cookbooks` の正確なライセンス文言(LICENSEファイルが見つからなかった/未取得)。→ 次回、Claude for Teachers 導入を具体的に検討するタイミングで再取得する。
- `knowledge-work-plugins` の個別プラグイン(11領域)ごとの詳細な権限要求(外部ツール連携の有無)は未調査。trial実行時に該当プラグインのみ詳細確認する。
- 「GitHubでClaudeを無限に使える」の当初の調査(claude-code-action + サブスクOAuth)との重複はなし。本レポートは別軸(コンテンツ生成強化)の調査。
