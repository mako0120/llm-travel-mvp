# 調査結果: Poolside「Laguna S 2.1」オープンウェイト・コーディングモデル公開(定期実行44本目)

調査日: 2026年7月27日
対象ジャンル: 「AI/エージェント系」枠(70%)

## 選定理由・鮮度についての正直な報告

- 本テーマは2026年7月21日発表で、着手日(7月27日)から6日経過しており、
  `docs/06_Content_R&D.md`2026-07-27追記の鮮度基準(着手日の前日以内)には
  **届いていない**
- 15件以上のWebSearchクエリで着手日・前日の候補を探したが、AI/エージェント系・
  海外で活躍する日本人・急成長アカウントのいずれの枠でも、着手日・前日発表
  かつ70点以上の候補が見つからなかった(詳細は
  `ai-company-os/research/2026-07-24_theme-evaluation-round21.md`の
  「鮮度基準を満たす候補が見つからなかった経緯」を参照)
- 十分に探しても見つからなかったため、鮮度で妥協する理由を正直に明記した
  上で、70点に到達する候補の中で最も評価の高い本テーマを採用する

詳細な評価点は`ai-company-os/research/2026-07-24_theme-evaluation-round21.md`を参照。

## 見送った候補

| テーマ | 判定 | 理由 |
|---|---|---|
| Kimi K3(Moonshot AI) | 見送り | round19で既に採用済み(定期実行42本目)のため重複 |
| OpenAIモデルのHugging Face侵害(GPT-5.6 Sol、続報) | 見送り | 既存テーマ(2026-07-23_openai-model-hugging-face-breach)と同一事案の続報のため重複 |
| Claude Opus 5(Anthropic) | 見送り | 自己言及回避方針により対象外 |
| NAVER・Brookfield・NVIDIAのソブリンAIファクトリー拡大(2026-07-26) | 見送り | 鮮度は高いが日本需要・実用性・訴求力の面で70点に届かず(試算約66点) |
| 大谷翔平選手の通算300号本塁打(2026-07-07) | 見送り | 内容は強いが着手日から3週間以上経過し鮮度基準に大きく届かない |
| 急成長アカウント枠 | 該当なし | 着手時点で具体的な急成長の一次情報を確認できず、正直に候補なしと報告する |

## 必ず使う事実(出典付き)

| 事実 | 出典 |
|---|---|
| AIスタートアップのPoolsideは2026年7月21日、オープンウェイトのコーディング特化AIモデル「Laguna S 2.1」をHugging Face上で公開した | [Poolside公式ブログ](https://poolside.ai/blog/introducing-laguna-s-2-1), [VentureBeat](https://venturebeat.com/infrastructure/poolside-drops-laguna-s-2-1-an-open-weight-coding-model-that-beats-rivals-10x-its-size) |
| Laguna S 2.1は総パラメータ数118億(118B)のMixture-of-Experts(MoE)構造で、実際に活性化するのは約80億(8B)パラメータ。256個のルーティングエキスパートと1個の共有エキスパートを持つ | [the-decoder](https://the-decoder.com/poolsides-laguna-s-2-1-is-a-small-open-weight-coding-model-that-punches-well-above-its-size/) |
| コンテキスト長は最大約104万8576トークン(約100万トークン) | [the-decoder](https://the-decoder.com/poolsides-laguna-s-2-1-is-a-small-open-weight-coding-model-that-punches-well-above-its-size/) |
| Poolside自身のベンチマークで、Terminal-Bench 2.1で70.2%、SWE-Bench Proで59.4%、DeepSWEで40.4%のスコアを記録し、複数倍規模の他モデルに匹敵・上回る結果だったと報じられている | [VentureBeat](https://venturebeat.com/infrastructure/poolside-drops-laguna-s-2-1-an-open-weight-coding-model-that-beats-rivals-10x-its-size), [MarkTechPost](https://www.marktechpost.com/2026/07/21/poolside-releases-laguna-s-2-1/) |
| モデルの重みは商用利用も可能な寛容なライセンス「OpenMDW-1.1」で公開されている | [MarkTechPost](https://www.marktechpost.com/2026/07/21/poolside-releases-laguna-s-2-1/) |
| Laguna S 2.1に先立ち、2026年7月2日には小型版の「Laguna XS 2.1」(総パラメータ330億、活性化30億)が公開されており、単体のデスクトップ・ノートPCのGPUでも動作する規模とされている | [TechTimes](https://www.techtimes.com/articles/319676/20260704/poolside-releases-free-open-weight-coding-model-july-9-upgrade-deadline.htm) |

## 政治的リスクへの配慮(重要)

一部の海外メディア(TheNextWeb等)は本モデルを「西側諸国によるDeepSeek・Qwen
への回答」という東西対立的な文脈で報じている。本テーマではこの政治的な
フレーミングには一切触れず、モデル自体の技術・製品面の事実(仕様・
ベンチマーク・ライセンス)のみを扱う。Kimi K3(定期実行42本目)を扱った際と
同様の配慮方針である。

## 推測・分析(合理的推測であることを明記)

- (推測)Laguna XS 2.1(小型・個人利用向け)とLaguna S 2.1(大型・高性能)を
  約3週間の間隔で連続公開した背景には、利用者の規模・用途に応じた
  ラインナップを段階的に整備する狙いがあると考えられる(公式に明言された
  理由ではなく、発表順序からの合理的推測)

## 不明点

- 本モデルの学習データの詳細、学習コストは公開情報からは確認できなかった
- Poolside社自身のベンチマーク評価の手法(内部フォーク版のベンチマーク
  フレームワークを使用)であり、第三者による独立検証の有無は本調査時点では
  確認できていない

## 出典一覧

- Poolside公式ブログ: https://poolside.ai/blog/introducing-laguna-s-2-1
- VentureBeat: https://venturebeat.com/infrastructure/poolside-drops-laguna-s-2-1-an-open-weight-coding-model-that-beats-rivals-10x-its-size
- the-decoder: https://the-decoder.com/poolsides-laguna-s-2-1-is-a-small-open-weight-coding-model-that-punches-well-above-its-size/
- MarkTechPost: https://www.marktechpost.com/2026/07/21/poolside-releases-laguna-s-2-1/
- TechTimes(Laguna XS 2.1について): https://www.techtimes.com/articles/319676/20260704/poolside-releases-free-open-weight-coding-model-july-9-upgrade-deadline.htm

## 注意

- 個別記事本文には直接アクセスできず、検索エンジンの要約経由での確認である。
  ただし複数の独立系技術メディアが同一の仕様・ベンチマーク数値を報じており、
  内容の整合性は確認できている
- ベンチマークスコアはPoolside自身の内部評価であり、第三者による独立検証の
  有無は確認できていないため、断定的な優劣比較としては扱わない
- 「西側諸国 vs 中国」といった政治的なフレーミングには一切触れない
- 本テーマは着手日から6日前の発表であり、鮮度基準(1日前まで)には届いて
  いないことを正直に明記する(`ai-company-os/research/2026-07-24_theme-evaluation-round21.md`参照)
- 公開・投稿はまだ行っていない
