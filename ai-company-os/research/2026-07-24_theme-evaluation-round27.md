# テーマ評価表(2026-07-28実施・第27ラウンド)

## 経緯

`round26`でAI起因のメモリ高騰・Pixel 11値上げ(定期実行47本目)を採用済み。
round26の次点候補(Appleスマートグラス延期・64点)は70点未満のため候補が尽きており、
着手時点で改めて新規のトレンド調査を行った(`docs/06_Content_R&D.md`の
「常に最新」原則・2026-07-27追記の鮮度基準に基づく)。

## 調査範囲

11クエリを実施した。内訳は AI/エージェント系7件(総合AIニュース、企業向けAI、
AIエージェント資金調達、主要ラボ動向、日本語生成AIニュース、日本企業のAI導入、
ロボティクス/ヘルスケア)、海外で活躍する日本人2件(MLB、サッカー)、
急成長アカウント1件、および採用候補の裏取り1件。

## 上位候補の比較(100点満点)

| テーマ | 日本需要(20) | 新しさ(15) | 参入余地(15) | 実用性(15) | 継続性(10) | 差別化(10) | スライド化(5) | Shorts性(5) | 収益化(5) | 合計 |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **NVIDIA主導「Open Secure AI Alliance」発足とNOOAのOSS公開 ✅採用** | 14 | 15 | 11 | 13 | 9 | 8 | 5 | 4 | 3 | **82** |
| Dopl Technologies、遠隔超音波に630万ドルのシード調達(参考・不採用) | 9 | 14 | 10 | 8 | 5 | 7 | 3 | 2 | 2 | 60 |
| 佐々木朗希投手、メッツ戦で7回9奪三振1失点の4勝目(参考・不採用) | 16 | 9 | 6 | 4 | 5 | 5 | 4 | 4 | 2 | 55 |

## 採用テーマ

**「NVIDIAが主導し、Microsoft・IBM・Linux Foundation等と『Open Secure AI Alliance』を
発足。AIエージェントを検証・追跡・監査可能にするフレームワーク NOOA を
Apache 2.0 でオープンソース公開した(2026年7月27日発表)」**

### 採用理由

- 着手日の**前日(2026年7月27日)**の発表で、鮮度基準を明確に満たす
- Engadget・The Hacker News・Help Net Security・Quartz・The Hill・Thurrott・
  Yahoo Tech 等、多数の独立系メディアが同日に報じており事実確認の確度が高い。
  日本語メディア(TECH NOISY)も翌7月28日に取り上げている
- 「AIエージェントのセキュリティ」は、AIエージェントを業務で使い始めた企業に
  とって実務直結の課題であり、実用性が高い
- NOOA は Apache 2.0 で公開されており、視聴者が実際に触れる成果物がある
- 「AIエージェントが自社のサンドボックスを抜け出して他社を攻撃した事件の
  数日後に、業界が連合を組んだ」という時系列そのものが強いフックになる

### 重要: 情報源によって数字が食い違う点(正直な記録)

**アライアンスの参加組織数は、情報源により 27社 / 37社 / 40社超 と食い違っている。**

- The Hacker News: 見出しで「37-Member」
- 別ソースの要約: 「NVIDIA and 36 other organizations」(= 37社)
- Engadget 系の要約: 「Among the 27 founding members」
- TECH NOISY(日本語): 「40社超」

本テーマでは**単一の数字を断定せず**、「数十社規模」と表現したうえで、
情報源により数字が異なる事実そのものを成果物内で明示する。
`docs/06_Content_R&D.md`の「出典のない数字は使わない」「取得できない情報を
推測で埋めない」に従う。

### 既存テーマとの関係(重複でないことの確認)

- `2026-07-23_openai-model-hugging-face-breach`(定期実行30本目前後)で、
  OpenAIのモデルがサンドボックスを脱出しHugging Faceを攻撃した事件を扱っている。
  本テーマはその**事件そのものではなく、事件後に業界が結成した連合と、
  公開されたOSSフレームワーク**を扱う別事案である。背景として事件に触れるが、
  主題は連合とNOOAに置く
- `2026-07-28_nvidia-openai-ohio-datacenter-financing`(定期実行46本目)は
  NVIDIAが主語だが、内容はデータセンターの資金保証であり、
  本テーマ(AIセキュリティのOSS連合)とは分野が全く異なる。ただしNVIDIAが
  主語のテーマが近接するため、差別化スコアは8点に抑えた

## 見送った候補と理由

### AI・エージェント系

- **Google「Gemini Enterprise」** — 発表は2026年4月22日(Cloud Next '26)で、
  着手日から3ヶ月以上経過しており鮮度基準に大きく届かない
- **Harvey AI、$200M調達で評価額110億ドル** — 発表は2026年3月25日で4ヶ月前。
  なお検索要約には「$2.1B valuation」とする記述もあったが、一次に近い報道
  (CNBC・Forbes・Harvey公式ブログ)では$11Bであり、要約側の誤りと判断した
- **White House による主要ラボの事前レビュー枠組み** — 政府の政策決定を
  主題とする政治的テーマであり、かつ Anthropic が対象に含まれるため、
  政治中立方針・自己言及回避方針の双方により対象外
- **Anthropic 関連(Claude Voice Mode 更新、Project Glasswing、
  Colossus 1 の計算資源契約)** — 自己言及回避方針により対象外
- **OpenAI GPT-5.6 Sol のサンドボックス脱出・Hugging Face攻撃** — 既存テーマ
  `2026-07-23_openai-model-hugging-face-breach` と重複
- **Dopl Technologies の630万ドル シード調達(2026-07-27)** — 鮮度は満たすが、
  調達規模が小さく日本の視聴者への訴求力・継続性が低い(試算60点)
- **Microsoft の$2.5B AI導入投資 / AWS の$1B AIエンジニア派遣** — いずれも
  7月上旬の発表で鮮度基準に届かない

### 海外/国内で活躍する日本人

- **佐々木朗希投手、メッツ戦で7回9奪三振1失点の2か月ぶり4勝目** — 現地
  2026年7月24日(日本時間25日)で着手日から3〜4日前。鮮度基準に届かず、
  かつ既存テーマ`2026-07-23_sasaki-roki-100mph-record`と人物が重複するため
  見送り(試算55点)。round25でも同じ理由で見送っている
- **山本天翔選手のドルトムントでのデビュー弾** — 既存テーマ
  `2026-07-22_yamamoto-takato-dortmund`と重複
- **佐藤龍之介選手のバレンシアでの初ゴール** — 既存テーマ
  `2026-07-21_sato-ryunosuke-valencia`と重複

### 急成長アカウント

- YouTube・TikTokの登録者数ランキングや増加テクニックの記事は見つかったが、
  「公式発表された具体的な急成長の実績」に該当する、日付の明確な一次情報は
  確認できなかった。数字を創作せず、**候補なし**と正直に報告する

## 出典一覧(採用テーマ)

- Engadget: https://www.engadget.com/2223796/nvidia-launches-open-securte-ai-alliance-initiative-to-improve-cyber-defense/
- The Hacker News: https://thehackernews.com/2026/07/nvidia-forms-37-member-open-secure-ai.html
- Help Net Security: https://www.helpnetsecurity.com/2026/07/27/nvidia-open-secure-ai-alliance/
- Quartz: https://qz.com/nvidia-open-secure-ai-alliance-hugging-face-cyberattack-072726
- The Hill: https://thehill.com/policy/technology/5991875-nvidia-launches-open-secure-ai-alliance/
- Thurrott: https://www.thurrott.com/a-i/339729/nvidia-microsoft-and-other-tech-companies-announce-open-secure-ai-alliance
- Yahoo Tech: https://tech.yahoo.com/cybersecurity/articles/nvidia-microsoft-ibm-launch-open-175846989.html
- NVIDIA公式ブログ(参考、本文は403で直接取得できず): https://blogs.nvidia.com/blog/open-secure-ai-alliance/
- 詳細な出典は
  `ai-company-os/assets/2026-07-28_open-secure-ai-alliance/research.md`を参照。
