# リサーチ: 商売敵が、手を組んだ。GoogleとAnthropicの技術が「同じ屋根の下」に

## 0. 鮮度についての正直な開示

- 着手日: 2026年8月25日(火・JST)。本件は複数の海外メディアで
  2026年8月20日発表と報じられており、着手日から5日前の情報である。
  一部メディア(Causely)は2026年8月17日と記載しており、発表日に
  ついて数日の揺れが情報源間に見られる。本テーマでは、より多くの
  独立した情報源(Forkast・Axios・Forbes・DevOpsDigest等)が一致
  して報じる「2026年8月20日」を採用する

## 1. 確定している事実(出典付き)

- Linux Foundation傘下の「Agentic AI Foundation(AAIF)」に、Google
  の「A2A(Agent2Agent)」プロトコルが正式に加わったことが発表された
- AAIFには、Anthropicが提供する「MCP(Model Context Protocol)」も
  既に参加しており、AIエージェント関連の主要プロトコルが同一の
  中立的なガバナンスの下に集約された形となる
- MCPは「エージェント⇔ツール・データ」間の接続を担う規格、A2Aは
  「エージェント⇔エージェント」間の、信頼境界をまたいだ連携を担う
  規格とされ、両者は役割が異なる
- AAIFは2025年12月9日に設立が発表され、発足時は40社未満だった
  参加企業・団体数が、今回時点で250社以上に拡大している
- 主要な参加企業として、Google・Microsoft・Amazon(AWS)・
  Anthropic・OpenAI・Bloomberg・Shopify・Blockなどが挙げられている
- A2Aはもともと2025年6月23日にGoogleからLinux Foundationへ移管
  されており、今回はさらにAAIFの正式なホストプロジェクトとなった
  という位置づけである
- MCPは2025年12月9日、AnthropicからAAIFへ提供された

## 2. 数字の混同防止チェック(本テーマ固有)

- 「AAIF発足時の参加企業・団体数(40社未満)」と「今回時点での参加
  企業・団体数(250社以上)」を、異なる時点の数字として明確に区別する
- 「MCP(エージェント⇔ツール)」と「A2A(エージェント⇔エージェント)」
  という役割の異なる2つのプロトコルを混同しない

## 3. 確認できなかったこと(正直な開示)

- 発表の正確な日付(情報源により2026年8月17日・20日の揺れがあり、
  本テーマでは多数の情報源が一致する8月20日を採用しているが、
  厳密な一次発表時刻までは確認できていない)
- 今回の統合による、開発者・企業の具体的な実務上のメリットの定量的
  な効果
- 各企業がAAIFに参加した個別の意図・出資規模等の詳細

## 4. 独自性・重複回避

- `ai-company-os/assets/`配下を`.md`ファイル限定で
  `grep -ril -i "AAIF|Agentic AI Foundation|A2A protocol"`で検索した
  結果、既存テーマは見つからなかった。新規テーマとして採用する

## 5. 出典

- Forkast News(2026-08-20)「Google's A2A Protocol Joins AAIF,
  Consolidating the Agent Economy's Protocol Layer Under One Roof」
- Forbes(2026-08-19)「Agent2Agent Joins The Agentic AI Foundation
  Alongside MCP」
- Axios(2026-08-17)「Exclusive: AI agents inch toward
  interoperability」
- Linux Foundation公式(2025-12-09)「Linux Foundation Announces the
  Formation of the Agentic AI Foundation(AAIF)」(設立時の背景確認用)
- AAIF公式ブログ「A2A joins AAIF's open agentic stack」

## 6. 政治的中立性・著作権配慮

- 本テーマは業界団体・標準化の動向という事実のみを扱い、政治的な
  論点には一切立ち入らない
- 実在企業(Google・Anthropic・Microsoft・Amazon・OpenAI等)のロゴ・
  商標は使用せず、テキストベースの図解のみで構成する
- 特定企業・特定プロトコルの利用を強く推奨する表現は用いず、業界
  全体の動きとして中立的に紹介する
