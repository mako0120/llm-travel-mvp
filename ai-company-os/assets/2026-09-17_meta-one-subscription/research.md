# リサーチ: Meta、Instagram/Facebook/WhatsApp横断のAI機能付き有料サブスク「Meta One」を発表

## 0. 鮮度についての正直な開示

- 着手日: 2026年9月17日(木・JST)。本件は2026年9月15日に発表されており、
  着手日から2日前の情報である(基本方針の「2日以内」を満たす)

## 1. 確定している事実(出典付き)

- Metaは2026年9月15日、Facebook・Instagram・WhatsAppを横断して使える有料
  サブスクリプション「Meta One」を発表した(about.fb.com、TechCrunch)
- 個人向けプランは月額7.99ドルの「Core」と月額19.99ドルの「Premium」の2段階で、
  Facebook Plus・Instagram Plus・WhatsApp Plusの機能に加え、画像・動画生成機能
  「Muse Image」「Muse Video」が利用できる(techrepublic.com)
- 契約者はInstagramストーリーの編集でAI編集機能「Restyle」や、音声エフェクトなどの
  クリエイティブツールをより多く利用できる。Premiumの方がCoreより利用可能量が多い
  (techrepublic.com)
- 個人向けプランとは別に、法人・クリエイター向けプランとしてEssential(月額14.99ドル)・
  Advanced(月額49.99ドル)・Expert(月額149ドル)・Max(月額499ドル)があり、
  自動応答AIツール「Meta Business Agent」・認証バッジ・分析機能・チーム管理機能が
  追加される(techrepublic.com)

## 2. 数字の混同防止チェック(本テーマ固有)

- 個人向けプラン「Core(7.99ドル)」「Premium(19.99ドル)」と、法人向けプラン
  「Essential(14.99ドル)」〜「Max(499ドル)」を混同しない(対象・料金体系が異なる)
- 「Muse Image」「Muse Video」(生成機能)と「Restyle」(既存写真の編集機能)を
  混同しない

## 3. 合理的推測(事実と区別)

- (推測)Facebook・Instagram・WhatsAppを横断する統一サブスクリプションという
  設計は、複数アプリでのAI機能利用を一本化し契約継続率を高める狙いがあると
  考えられるが、これはMetaが明示的に述べた戦略意図ではなく、サービス設計からの
  推測である

## 4. 不明(確認できなかったこと)

- 日本での提供開始時期・日本円での価格
- Core/Premiumそれぞれの具体的な月間生成上限(枚数・秒数など)
- 既存の無料AI機能との具体的な差分(何が無料のままで、何が有料限定になるか)

## 5. 重複チェック(既存テーマとの区別、必須)

- `ai-company-os/assets/`配下を`grep -ril -i "Meta One"`で検索した結果、
  既存テーマはヒットせず、重複は確認されなかった
- 2026-09-11に扱った「Meta Muse」(パーソナルAIエージェント、会話記録上確認)とは
  別サービスであり、Muse Image/Muse VideoはMeta Oneのプラン内で使える機能の
  一部という位置づけであるため、重複ではないと判断した

## 6. 判定

**adopt** — about.fb.comという一次情報源に加え、TechCrunch・TechRepublicという
複数の独立した媒体で確認できた。着手日から2日前という高い鮮度も確保しており、
「AI機能に課金するといくらで何ができるのか」という視聴者に直接関係する具体的な
有益性を持つ。

## 出典一覧

- about.fb.com: Introducing Meta One: A Subscription Service With More Features and AI to Create, Connect, and Stand Out
- TechCrunch: Meta expands subscription push with new AI-focused plans
- TechRepublic: Meta One Pricing Explained: What $2.99, $7.99 and $19.99 Get You
