# リサーチ: Perplexity、ローカル動作AIエージェント「Portable Computer」をWindowsに提供開始

## 0. 鮮度についての正直な開示

- 着手日: 2026年9月16日(水・JST)。本件は2026年9月14日に発表・提供開始されており、
  着手日から2日前の情報である(基本方針の「2日以内」を満たす)

## 1. 確定している事実(出典付き)

- Perplexityは2026年9月14日、ローカル動作のAIエージェント「Portable Computer」を
  Windows版Perplexityアプリで利用可能にした(Unite.AI、NVIDIA公式ブログ、Tom's Hardware)
- Portable Computerは、モデル・エージェントハーネス・オーケストレーター・スケジューラーの
  すべてをWindows端末上でローカル実行する(NVIDIA公式ブログ)
- 対応にはNVIDIA GeForce RTXまたはRTX PROシリーズのGPUで、VRAM 24GB以上が必要
  (Unite.AI、Tom's Hardware、Yahoo Tech)
- デフォルトではPerplexityがPortable Computer向けに追加学習・RTX GPU向けに最適化した
  「Qwen 3.8 27B」が搭載され、自社開発モデル「PPLX 27B」や、今後追加予定の
  「NVIDIA Nemotron 3.5 Lightning」(300億パラメータ)、音声認識用の
  「Nemotron 3.5 ASR」も利用できる(Unite.AI)
- 利用はPerplexityのProまたはMaxプラン契約者(個人・法人問わず)向けで、Windows版
  Perplexityアプリ(Microsoft Store配信)から利用する(Unite.AI)
- 定期実行タスクのスケジュール設定や、デスクトップアプリ向けのローカルMCPサーバー
  機能も追加された。NVIDIAはMicrosoft Word・Google Drive・Gmail・Slack・GitHubなどへの
  コネクタを紹介している(NVIDIA公式ブログ)

## 2. 数字の混同防止チェック(本テーマ固有)

- 「VRAM要件(24GB以上)」と「モデルのパラメータ数(Qwen 3.8 27B=270億、Nemotron
  3.5 Lightning=300億)」を混同しない
- 「クラウド版Perplexity Computer」と「ローカル動作版Portable Computer」を区別する
  (本稿はローカル動作版が対象)

## 3. 合理的推測(事実と区別)

- (推測)VRAM 24GB以上という要件は、一般的な家庭用PCでは対応が難しく、主にハイエンド
  ゲーミングPCやクリエイター向けワークステーションを持つユーザーが対象になると考えられるが、
  これはPerplexity・NVIDIAが対象ユーザー層を明示的に述べたものではなく、要件からの推測である

## 4. 不明(確認できなかったこと)

- Windows以外のOS(Mac・Linux)への提供時期
- Pro/Maxプランそれぞれの具体的な月額料金(本稿執筆時点で未確認)
- 日本語での動作・応答品質の詳細

## 5. 重複チェック(既存テーマとの区別、必須)

- `ai-company-os/assets/`配下を`grep -ril -i "Portable Computer"`で検索した結果、
  既存テーマはヒットせず、重複は確認されなかった

## 6. 判定

**adopt** — Unite.AI・NVIDIA公式ブログ・Tom's Hardwareを含む複数の独立した媒体で
確認できた。着手日から2日前という高い鮮度を確保しており、「自分のPCで動くAIエージェント」
という視聴者に直接関係する具体的な有益性を持つ(対応GPUを持つ層に限られる点は明示する)。

## 出典一覧

- Unite.AI: Perplexity Brings Its Local Portable Computer Agent to Windows PCs
- NVIDIA公式ブログ: Perplexity Portable Computer Is Now Available on Windows, Powered by NVIDIA RTX
- Tom's Hardware: Perplexity's local AI agent comes to Windows, but only for RTX GPUs with at least 24GB of VRAM
- Yahoo Tech: Perplexity's local AI agent comes to Windows, but only for RTX GPUs with at least 24GB of VRAM
