# リサーチ: Anthropicアプリ内に「Claude Money」(家計管理機能)の未発表要素を複数メディアが発見

## 0. 鮮度についての正直な開示

- 着手日: 2026年9月16日(水・JST)。本件は2026年9月14日に複数メディアが報じており、
  着手日から2日前の情報である
- 【重要な性質の違い】本テーマはAnthropicの公式発表ではなく、アプリ内の未公開UI要素を
  リーク調査メディア(TestingCatalog)が発見し、複数の技術メディアが後追い報道した
  「未発表機能の発見」である。Anthropic自身はこの機能を正式発表しておらず、
  提供時期も明らかにしていない

## 1. 確定している事実(出典付き)

- 未発表機能トラッカー「TestingCatalog」が、Claudeの iOSアプリ内に「Claude Money」という
  未公開の機能タブを発見したと報じた(Android Authority、TestingCatalog、CoinDesk)
- オンボーディング画面には「Understand your money with Claude」という文言があり、
  銀行口座を連携して支出・予算などについてClaudeに質問できる機能として設計されている
  ように見える(Android Authority)
- 銀行口座を連携すると、一回限りの明細アップロードではなく、継続的にデータへ
  アクセスできるようになり、支出パターンの分析・定期支払いの検出・残高要約・
  推移の可視化などをClaudeが行える可能性がある(Android Authority)
- 「Money」タブはモバイル版のナビゲーションに独立した項目として表示されているが、
  Web版には同等の機能は確認されていない(Android Authority)
- Anthropicはこの機能についてまだ公式に発表しておらず、提供時期も明らかにしていない
  (Android Authority、CoinDesk)

## 2. 数字の混同防止チェック(本テーマ固有)

- 「発見・報道日(2026年9月14日)」と「実際の提供開始日」を混同しない。後者は
  本稿執筆時点で不明であり、未定・未発表である
- 本件は確定した「新機能の提供開始」ではなく「未公開要素の発見」であることを、
  本文中でも明確に区別して伝える

## 3. 合理的推測(事実と区別)

- (推測)Anthropicが家計管理領域に進出しようとしている背景には、ChatGPTなど競合
  アシスタントとの機能差別化の狙いがあると考えられるが、これはAnthropic自身が
  意図を説明したものではなく、報道の文脈からの推測である

## 4. 不明(確認できなかったこと)

- 正式な提供開始時期・対象地域(Android Authorityは「米国のみが濃厚」と推測しているが確定情報ではない)
- 銀行連携の具体的な仕組み(Plaid等の外部サービス経由かどうかを含む)
- セキュリティ・プライバシー面の設計詳細

## 5. 重複チェック(既存テーマとの区別、必須)

- `ai-company-os/assets/`配下を`grep -ril -i "Claude Money"`で検索した結果、
  既存テーマはヒットせず、重複は確認されなかった
- 2026-09-15に扱った「Claude for Financial Advisors」(Enterprise向け金融アドバイザー支援)
  とは対象・性質が異なる(あちらは正式発表済みのEnterprise向け機能、本件は個人向けの
  未発表・未確認機能)ため、重複ではないと判断した

## 6. 判定

**adopt(ただし性質を明確に区別して伝える)** — Android Authority・TestingCatalog・
CoinDeskを含む複数の独立した媒体で発見内容自体は確認できた。着手日から2日前という
高い鮮度も確保している。「家計管理をAIに任せられる未来が近いかもしれない」という
視聴者への話題性・有益性はあるが、Anthropicの公式発表ではなく未公開要素の発見である
という性質の違いを本文・キャプションの両方で明確に開示することを条件に採用する。

## 出典一覧

- Android Authority: Claude could soon get a feature that lets it peep into your bank account
- TestingCatalog(一次発見元、Android Authority等の記事内で言及)
- CoinDesk: Anthropic prepares Claude Money feature for iOS app launch
- testingcatalog.com: Anthropic prepares Claude Money for personal finance
