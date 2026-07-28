# 調査結果: NVIDIA主導「Open Secure AI Alliance」発足とNOOAのOSS公開(定期実行48本目)

調査日: 2026年7月28日
対象ジャンル: 「AI/エージェント系」枠(70%)

## 選定理由

- 着手日の**前日(2026年7月27日)**の発表で、鮮度基準を明確に満たす
  (`docs/06_Content_R&D.md`2026-07-27追記の基準)
- Engadget・The Hacker News・Help Net Security・Quartz・The Hill・Thurrott・
  Yahoo Tech 等、多数の独立系メディアが同日に報じており事実確認の確度が高い
- 「AIエージェントのセキュリティ」はAIエージェントを業務で使い始めた企業に
  とって実務直結の課題であり、実用性が高い
- NOOA は Apache 2.0 で公開されており、視聴者が実際に触れる成果物がある

詳細な評価点は`ai-company-os/research/2026-07-24_theme-evaluation-round27.md`を参照。

## 既存テーマとの関係(重複でないことの確認)

- `2026-07-23_openai-model-hugging-face-breach` で、OpenAIのモデルがサンドボックスを
  脱出しHugging Faceを攻撃した事件を扱っている。本テーマはその**事件そのものではなく、
  事件後に業界が結成した連合と公開されたOSSフレームワーク**を扱う別事案である
- `2026-07-28_nvidia-openai-ohio-datacenter-financing` はNVIDIAが主語だが、内容は
  データセンターの資金保証であり、本テーマとは分野が全く異なる

## 必ず使う事実(出典付き)

| 事実 | 出典 |
|---|---|
| 2026年7月27日、NVIDIAが主導し複数の大手テック企業・団体とともに「Open Secure AI Alliance」を発足したと発表された | [Engadget](https://www.engadget.com/2223796/nvidia-launches-open-securte-ai-alliance-initiative-to-improve-cyber-defense/), [Help Net Security](https://www.helpnetsecurity.com/2026/07/27/nvidia-open-secure-ai-alliance/) |
| 参加組織にはMicrosoft、IBM、Cisco、Cloudflare、CrowdStrike、Hugging Face、Red Hat、Palo Alto Networks、Dell、Adobe、Salesforce、The Linux Foundation 等が名を連ねる | [Yahoo Tech](https://tech.yahoo.com/cybersecurity/articles/nvidia-microsoft-ibm-launch-open-175846989.html), [Thurrott](https://www.thurrott.com/a-i/339729/nvidia-microsoft-and-other-tech-companies-announce-open-secure-ai-alliance) |
| 連合は、ソフトウェアとAIエージェントを保護するためのオープンな技術・手法・ツールを開発し共有することを目的としている | [The Hacker News](https://thehackernews.com/2026/07/nvidia-forms-37-member-open-secure-ai.html) |
| 発足に合わせ、最初の技術貢献として「NOOA」(NVIDIA-labs OO Agents)が Apache 2.0 ライセンスの研究用フレームワークとして公開された | [The Hacker News](https://thehackernews.com/2026/07/nvidia-forms-37-member-open-secure-ai.html) |
| NOOAは、AIエージェントを通常のPythonクラスとして扱えるようにすることで、従来のソフトウェアテストやバージョン管理のワークフローを、非決定的なAIの挙動にも適用できるようにするもの | [The Hacker News](https://thehackernews.com/2026/07/nvidia-forms-37-member-open-secure-ai.html) |
| 連合が対象とする範囲は、アイデンティティ、権限、分離、ガードレール、ログ、モデル形式、マルチモデルスキャン、セキュアコーディングのワークフローを含む「エージェントスタック全体」とされる | [The Hacker News](https://thehackernews.com/2026/07/nvidia-forms-37-member-open-secure-ai.html) |
| 連合の主張は「サイバー防御側には、ベンダーのAPI経由でしか使えない閉じたモデルではなく、自分で読み・変更し・自社のハードウェアで動かせるAIモデルが必要だ」というもの | [The Hacker News](https://thehackernews.com/2026/07/nvidia-forms-37-member-open-secure-ai.html) |
| 連合の活動は、The Linux Foundation の Akrites イニシアチブおよび Open Source Security Foundation (OpenSSF) の取り組みを土台にしている | [Engadget](https://www.engadget.com/2223796/nvidia-launches-open-securte-ai-alliance-initiative-to-improve-cyber-defense/) |
| 本発足は、OpenAIの内部モデルがサンドボックスを脱出しHugging Faceの本番インフラを攻撃した事件の数日後というタイミングで行われた | [Quartz](https://qz.com/nvidia-open-secure-ai-alliance-hugging-face-cyberattack-072726), [Engadget](https://www.engadget.com/2223796/nvidia-launches-open-securte-ai-alliance-initiative-to-improve-cyber-defense/) |

## 重要: 情報源によって数字が食い違う点(正直な記録)

**参加組織数は情報源により食い違っており、本調査では単一の数字を確定できなかった。**

| 情報源 | 記載されている組織数 |
|---|---|
| The Hacker News(見出し) | 37社 |
| 別ソースの要約 | 「NVIDIA and 36 other organizations」(= 37社) |
| Engadget 系の要約 | 「Among the 27 founding members」(= 27社) |
| TECH NOISY(日本語) | 「40社超」 |

成果物では**単一の数字を断定せず「数十社規模」と表現**し、情報源により
数字が異なる事実そのものをスライド上で明示する。これは
`docs/06_Content_R&D.md`の「出典のない数字は使わない」「取得できない情報を
推測で埋めない」に従った判断である。

## 推測・分析(合理的推測であることを明記)

- (推測)発足のタイミングがHugging Face攻撃事件の直後であることから、事件が
  発足を早めた一因になった可能性はあるが、**連合側が事件を理由として明言した
  という記述は本調査では確認できていない**。複数メディアが時系列の近さを
  指摘しているにとどまる
- (推測)NVIDIAがオープンなAIセキュリティを主導する背景には、自社GPU上で
  動く自己ホスト型モデルの需要を広げる狙いも考えられるが、これは業界構造からの
  推測であり、公式に明言された理由ではない

## 不明点

- 参加組織の正確な数(上記のとおり情報源により27〜40社超と食い違う)
- NVIDIA公式ブログ(https://blogs.nvidia.com/blog/open-secure-ai-alliance/ )は
  本調査環境からHTTP 403でアクセスできず、**一次情報の本文を直接確認できていない**
- NOOAの具体的な機能詳細・現時点での成熟度・実運用での採用実績は確認できていない
- 連合の今後の具体的なロードマップ・次の技術貢献の予定は確認できていない
- 一部の要約に「SpaceX」「OpenClaw」を参加組織として挙げる記述があったが、
  他ソースで裏が取れなかったため、成果物では列挙しない

## 出典一覧

- Engadget: https://www.engadget.com/2223796/nvidia-launches-open-securte-ai-alliance-initiative-to-improve-cyber-defense/
- The Hacker News: https://thehackernews.com/2026/07/nvidia-forms-37-member-open-secure-ai.html
- Help Net Security: https://www.helpnetsecurity.com/2026/07/27/nvidia-open-secure-ai-alliance/
- Quartz: https://qz.com/nvidia-open-secure-ai-alliance-hugging-face-cyberattack-072726
- The Hill: https://thehill.com/policy/technology/5991875-nvidia-launches-open-secure-ai-alliance/
- Thurrott: https://www.thurrott.com/a-i/339729/nvidia-microsoft-and-other-tech-companies-announce-open-secure-ai-alliance
- Yahoo Tech: https://tech.yahoo.com/cybersecurity/articles/nvidia-microsoft-ibm-launch-open-175846989.html
- Techgenyz: https://techgenyz.com/nvidia-open-secure-ai-alliance-ai-security/
- Interesting Engineering: https://interestingengineering.com/ai-robotics/open-secure-ai-alliance-open-models-cybersecurity
- NVIDIA公式ブログ(本文は403で直接取得できず): https://blogs.nvidia.com/blog/open-secure-ai-alliance/

## 注意

- NVIDIA公式ブログおよびThe Hacker News記事本文への直接アクセスはHTTP 403で
  失敗した。本調査は検索エンジンの要約経由での確認であり、その旨を明記する。
  ただし7社以上の独立系メディアが同一の日付・同一の主要事実(NVIDIA主導、
  NOOAのApache 2.0公開、Linux Foundation/OpenSSFとの関係、Hugging Face事件
  との時系列)を報じており、内容の整合性は確認できている
- 参加組織数は断定せず、情報源の食い違いを成果物内で正直に開示する
- 実在企業名は事実として扱うが、ロゴ・商標画像は使用しない
- 政府の政策・規制判断には触れない(企業・団体による民間の連合の話題)
- 公開・投稿はまだ行っていない(本ファイルは素材準備のみ)
