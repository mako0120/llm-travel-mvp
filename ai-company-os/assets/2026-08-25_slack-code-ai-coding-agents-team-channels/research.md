# リサーチ: あなたのSlackが、AIエージェントの開発現場になる。「Slack Code」始動

## 0. 鮮度についての正直な開示

- 着手日: 2026年8月25日(火・JST)。本件は2026年8月20日(米国時間)、
  Salesforce/Slackが公式発表しており、着手日から5日前の情報である。
  複数の独立した海外メディア(Salesforce公式・VentureBeat・
  Computerworld等)で継続的に報じられており、内容の確度は高い

## 1. 確定している事実(出典付き)

- Salesforce(Slack)は2026年8月20日、AIコーディングエージェントを
  チームのSlackチャンネルに直接組み込む新機能「Slack Code」を発表した
- 対応するAIコーディングエージェントは、Anthropicの「Claude Code」、
  Cognitionの「Devin」、GitHub Copilot、Vercelのエージェントの4つ
- 使い方は、会話の中でコーディングエージェントをタグ付けすると、
  専用の「コードチャンネル」が立ち上がる仕組み
- コードチャンネルには、会話・計画(プラン)・コード差分(diff)・
  ライブプレビューの4つのタブが用意されている
- エンジニアだけでなく、プロダクトマネージャー・デザイナー・
  非技術者のチームメンバーも同じワークスペースでエージェントと
  共同作業できる設計になっている
- 業界で「バイブコーディング」と呼ばれる開発スタイルを製品化した
  ものとされ、コード差分の監査・ライブプレビューの確認・フィード
  バック・承認までを行える
- 承認(コードが実際にリリースされる前に、チャンネル内の人間が承認
  すること)が制御ポイントとされ、人間の承認なしにコードは出荷
  されない
- タスクが完了するとチャンネルは自動的にアーカイブされ、記録は
  監査ログとして残る
- Slack Codeは発表と同日から、いずれのSlackプランでも利用可能

## 2. 数字の混同防止チェック(本テーマ固有)

- 「Slack Codeという機能自体の利用可否(いずれのSlackプランでも
  利用可能)」と「連携する各AIコーディングエージェント自体の利用
  ライセンス・料金(顧客が別途保有する必要がある)」を、異なる種類の
  条件として明確に区別する

## 3. 確認できなかったこと(正直な開示)

- Slack Code経由でのAIエージェント利用に伴う追加課金の有無・料金体系
- 発表時点での具体的な導入企業数・利用実績
- セキュリティ・コンプライアンス面での詳細な設計(規制業界向けの
  対応状況等)

## 4. 独自性・重複回避

- `ai-company-os/assets/`配下を`.md`ファイル限定で
  `grep -ril -i "Slack Code"`で検索した結果、既存テーマは見つから
  なかった。新規テーマとして採用する

## 5. 出典

- Salesforce公式(2026-08-20)「Introducing Slack Code: Agentic Coding
  for Teams」
- VentureBeat(2026-08-20)「Slack wants to drag AI coding out of the
  terminal and into the group chat」
- Computerworld(2026-08-20)「New 'Slack Code' turns AI coding into a
  team activity」
- Salesforce Ben(2026-08-21)「Salesforce Brings Vibe-Coding to Slack
  With New 'Slack Code'」

## 6. 政治的中立性・著作権配慮

- 本テーマは企業の製品発表という事実のみを扱い、政治的な論点には
  一切立ち入らない
- 実在企業(Salesforce・Slack・Anthropic・Cognition・GitHub・Vercel等)
  のロゴ・商標は使用せず、テキストベースの図解のみで構成する
- 特定のAIコーディングエージェント(Claude Code等)の利用を強く推奨
  する表現は用いず、事実として並列に紹介する
