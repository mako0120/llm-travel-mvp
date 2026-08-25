# リサーチ: レストランの電話に出るのは、もう人間じゃない。AWS公式が公開した「AIホスト」設計図

## 0. 鮮度についての正直な開示

- 着手日: 2026年8月25日(火・JST)。本件は2026年8月24日、AWS公式の
  Machine Learningブログに掲載されており、着手日の1日前という鮮度の
  高い情報である

## 1. 確定している事実(出典付き)

- AWSは2026年8月24日、公式Machine Learningブログで
  「Building a restaurant telephony AI host with Amazon Connect」と
  題した記事を公開した
- 内容は、電話をかけた顧客の注文を、アプリ・Webサイト・サインイン
  不要で、電話の会話だけで一気通貫に受け付ける音声注文システムの
  構築方法を解説する技術ブループリント(設計図・参考実装)である
- システムは、電話回線を扱う「Amazon Connect」、リアルタイム音声を
  扱う「Amazon Connect Agentic Voice」、推論を担う「Amazon Connect
  AI agent」、バックエンドのツールをMCP経由で呼び出す
  「Amazon Bedrock AgentCore Gateway」を組み合わせて構成される
- AIエージェントは、Anthropicの「Claude Haiku 4.5」をシステム
  プロンプトに用いて定義され、ガードレールが付与されている
- セキュリティプロファイルにより、エージェントは合計10個のMCP
  ツール(バックエンド機能)へのアクセス権を付与されている
- 実装手順として、AgentCore GatewayをAmazon AppIntegrations上に
  MCPサーバーとして登録し、Amazon Lex V2ボットを作成し、Claude
  Haiku 4.5のシステムプロンプトでオーケストレーションエージェントを
  定義・公開する、という流れが解説されている
- 本記事に対応するサンプルコード一式が、AWS公式のGitHubリポジトリ
  (aws-samples)として公開されている

## 2. 数字の混同防止チェック(本テーマ固有)

- 「MCPツールの総数(10個)」と「システムを構成する主要コンポーネント
  数(Amazon Connect・Agentic Voice・AI agent・AgentCore Gatewayの
  4つ)」を、異なる種類の数字として明確に区別する

## 3. 確認できなかったこと(正直な開示)

- 実際にこのシステムを導入した具体的な飲食店・企業名(本記事は
  設計図・参考実装であり、特定企業による商用導入事例としては
  確認できていない)
- 注文の受付精度・応答速度などの具体的な性能数値
- 運用にかかる具体的なコスト

## 4. 独自性・重複回避

- `ai-company-os/assets/`配下を`.md`ファイル限定で
  `grep -ril -i "Amazon Connect|telephony AI host"`で検索した結果、
  既存テーマは見つからなかった。新規テーマとして採用する

## 5. 出典

- AWS Machine Learning Blog(公式、2026-08-24)「Building a restaurant
  telephony AI host with Amazon Connect」
- GitHub(aws-samples、公式サンプルリポジトリ)
  「sample-restaurant-telephony-ai-host-using-amazon-connect-customer」

## 6. 政治的中立性・著作権配慮

- 本テーマは企業が公開した技術解説記事という事実のみを扱い、政治的な
  論点には一切立ち入らない
- 実在企業(AWS・Anthropic等)のロゴ・商標は使用せず、テキストベース
  の図解のみで構成する
- 本記事はAWS公式の設計図(参考実装)であり、特定企業の商用導入事例
  ではない点を明確に区別し、実際の導入があったかのような誤解を
  招く表現は用いない
