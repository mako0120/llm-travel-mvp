# テーマ評価表(2026-07-28実施・第26ラウンド)

## 経緯

`round25`では70点以上の候補が見つからず新規採用を見送った。着手時点
(2026-07-28、round25から数時間後)で改めて最新ニュースを調査した
(`docs/06_Content_R&D.md`の「常に最新」原則・2026-07-27追記の数値基準に基づく)。

## 調査範囲

AI/エージェント系(9クエリ: 総合AIニュース、OpenAI、Google DeepMind、Meta、
Microsoft、ロボティクス、xAI、AWS、Alibaba/Baidu/Tencent、Apple)、海外で
活躍する日本人(3クエリ: MLB日本人選手、サッカー日本人選手、大谷・鈴木・
ダルビッシュ個別)、急成長アカウント(1クエリ: TikTokトレンド)、および
横断的な「本日のテック速報」クエリ2件の、計15クエリを実施した。

## 上位候補2件の比較

| テーマ | 日本需要(20) | 新しさ(15) | 参入余地(15) | 実用性(15) | 継続性(10) | 差別化(10) | スライド化(5) | Shorts性(5) | 収益化(5) | 合計 |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **AI需要によるメモリ高騰でGoogle Pixel 11が値上げ、スマホ業界全体に波及 ✅採用** | 15 | 14 | 11 | 11 | 8 | 9 | 5 | 4 | 3 | **80** |
| Appleのスマートグラス、プライバシー懸念で2027年に延期(参考・不採用) | 12 | 14 | 8 | 7 | 5 | 8 | 3 | 3 | 4 | 64 |

## 採用テーマ

**「AIデータセンター需要がメモリ(RAM)価格を高騰させ、Google Pixel 11を
はじめスマートフォン業界全体の値上げに波及している」**
(Google幹部Shakil Barkat氏が9to5Googleのインタビューで2026年7月24日に
価格改定を認め、その後7月25〜27日にかけて英語圏・日本語圏の多数のメディアが
追随報道)

### 採用理由

- 着手日から1〜4日前の一次情報(9to5Googleの独占インタビュー、Google幹部の
  実名コメント)があり、鮮度・確度ともに高い
- Google公式見解として「RAM価格が2025年の1GBあたり$2.80から2026年に$12へ
  6倍に高騰した」という具体的な数字があり、Morgan Stanleyのデータが出典として
  明記されている
- 「AIがスマホの値段を上げている」という、AI業界の裏側を一般消費者の生活に
  直結させる分かりやすいフックがあり、日本語メディア(ギズモード・ジャパン、
  HelenTech、livedoor等)も既に取り上げており日本の関心も確認できる
- 数字が豊富(6倍、$45→$192のBOM試算、Pixel 11 Proの16GB→12GB縮小観測、
  IDC予測の出荷12.9%減)で、big_stat/cards/bar_chartでの視覚化に適している
- 本シリーズの既存47テーマと重複しない新規テーマである

### 見送った候補の詳細

- **Appleのスマートグラス延期**: 英語圏の主要テック媒体8社以上が既に深堀り
  報道済みで参入余地が小さく、また「延期」という性質上、具体的な数字に乏しく
  スライド化(視覚化)がしづらいため見送り
- **DeepSeek V4 / Kimi K3 / Alibaba Qwen3.8等の中国AIモデル群**: 既存テーマ
  (Kimi K3等)と重複、またはround24以前で見送り済み
- **Microsoft Copilot統合・Autopilotエージェント**: 発表自体は2026年6月2日
  (Build 2026)・メモ報道が7月2〜3日であり、着手日から3週間以上経過しており
  鮮度基準に大きく届かないため見送り
- **RoboCup 2026・Booster Robotics優勝**: 実際の報道日は2026年7月9日で
  鮮度基準に届かず見送り
- **佐々木朗希投手の続報、山本由伸投手の続報**: 既存テーマ(直近2日以内に
  制作済み)と人物が重複するため見送り
- **上田綺世選手のエバートン移籍交渉**: オファー拒否という交渉途中の段階で
  確定事実に乏しく、金額観測も情報源により差があるため見送り

## 出典一覧(一次情報優先)

- 9to5Google(一次インタビュー): https://9to5google.com/2026/07/24/google-pixel-11-price-increase/
- Android Central: https://www.androidcentral.com/phones/google-pixel/google-confirms-price-hike-for-pixel-11-series
- Android Headlines: https://www.androidheadlines.com/2026/07/google-confirms-pixel-11-price-increases-ram-crisis.html
- The Next Web: https://thenextweb.com/news/google-pixel-11-price-hike-ram-memory-crisis
- HNGN: https://www.hngn.com/articles/272381/20260727/google-confirms-pixel-11-price-hike-citing-sixfold-surge-ram-costs-ai-demand.htm
- ギズモード・ジャパン(Yahoo!ニュース転載): https://news.yahoo.co.jp/articles/3f74a12b08c9902f230ca77e097001707633ed5b
- HelenTech: https://helentech.jp/news-pixel-price-increase-ram-crisis-89193/
- 詳細な出典は
  `ai-company-os/assets/2026-07-28_ai-ram-shortage-pixel-price-hike/research.md`を参照。
