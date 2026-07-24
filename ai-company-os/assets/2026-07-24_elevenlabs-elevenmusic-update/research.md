# 調査結果: ElevenLabs「ElevenMusic」大型アップデート(定期実行28本目)

調査日: 2026年7月24日
対象ジャンル: 「AI/エージェント系」枠(70%)

## 選定理由

- オーナーより「未制作の候補を使い回すのではなく、常に最新のニュースを
  提供したい」との指示を受け、本サイクルの着手時点(2026年7月24日)で改めて
  最新ニュースを確認した
- 本日分の最新候補として「DeepSeek V4安定版」の話題も確認したが、調査した
  ところ「7月24日」という日付は実際にはレガシーAPIエイリアス(deepseek-chat/
  deepseek-reasoner)の廃止日であり、V4正式版そのものの日付は情報源間で
  依然食い違っていた(`round4`で一度見送った理由と同じ問題が解消していない)。
  正直さ・出典必須ルールに基づき、確度の低い情報を断定的に扱わないため
  見送った
- 結果として、2026年7月23日発表のElevenLabs「ElevenMusic」アップデートが、
  現時点で確認できる最も新しく、かつ複数の独立系メディアで明確に裏付けられた
  候補であるため採用する(`round6`での評価: 83点)
- 2026年7月23日、ElevenLabsがAI音楽生成サービス「ElevenMusic」の大型アップデート
  を発表。「References」「Vocals」という2つの新機能が追加され、話題性・新しさが高い
- 複数の独立系メディア(TechCrunch、DigitalToday等)が報道しており事実確認が取れる
- 音声・音楽生成という切り口は、これまでの定期実行(コーディングAIモデル・
  スポーツ)と異なる差別化にもなる

## 見送った候補

このサイクルでは新規のトレンド調査を行っていない(round6の未制作候補を採用)。
round6で見送った候補は以下の通り:

| テーマ | 判定 | 理由 |
|---|---|---|
| 岡本和真選手の月間最優秀新人受賞 | 定期実行27本目で採用済み | - |
| Netchex「Mesh」(AI HR担当者チーム) | 見送り | 日本での知名度が低い米国のHR SaaS企業のため |

## 必ず使う事実(出典付き)

| 事実 | 出典 |
|---|---|
| 2026年7月23日、ElevenLabsがAI音楽生成サービス「ElevenMusic」をアップデートした | [DigitalToday](https://www.digitaltoday.co.kr/en/view/84703/elevenlabs-upgrades-ai-music-generation-service-adds-vocals-references) |
| 新機能「References」は、参照音声(10秒〜5分)をアップロードすると、Music v2モデルがその曲のスタイル・雰囲気に合わせて音楽を生成する機能。6月のMusic v2発表時にプレビューされていた機能の正式版 | [DigitalToday](https://www.digitaltoday.co.kr/en/view/84703/elevenlabs-upgrades-ai-music-generation-service-adds-vocals-references) |
| 新機能「Vocals」は、ユーザー自身の声、または用意された音声ライブラリの声を使って、オリジナルの歌を生成する機能 | [DigitalToday](https://www.digitaltoday.co.kr/en/view/84703/elevenlabs-upgrades-ai-music-generation-service-adds-vocals-references) |
| 「Styles」機能が、最新モデルの「Music v2」に正式対応した | [DigitalToday](https://www.digitaltoday.co.kr/en/view/84703/elevenlabs-upgrades-ai-music-generation-service-adds-vocals-references) |
| ElevenLabsは、アップロードされた音声・楽曲が使用前に厳格な著作権チェックを通過する必要があると説明している | [DigitalToday](https://www.digitaltoday.co.kr/en/view/84703/elevenlabs-upgrades-ai-music-generation-service-adds-vocals-references) |
| Music v2モデル自体は2026年5月27日に発表されており、曲の途中でジャンルを切り替えられる機能が特徴とされていた | [TechCrunch](https://techcrunch.com/2026/05/27/elevenlabss-new-music-generation-model-can-switch-genres-mid-track/) |

## 推測・分析(合理的推測であることを明記)

- (推測)「Vocals」機能に厳格な著作権チェックを設けているのは、無断の声の
  利用・既存楽曲の権利侵害を防ぐための安全対策だと考えられる(公式に明言された
  設計思想ではなく、機能説明からの合理的推測)

## 不明点

- ElevenMusicの料金体系・「Vocals」機能の具体的な提供条件(無料枠の有無等)は、
  公開情報からは確認できなかった
- 「Vocals」で使用できる「音声ライブラリ」の具体的な収録内容・ライセンス形態は
  本調査時点では不明

## 出典一覧

- DigitalToday: https://www.digitaltoday.co.kr/en/view/84703/elevenlabs-upgrades-ai-music-generation-service-adds-vocals-references
- TechCrunch(Music v2発表): https://techcrunch.com/2026/05/27/elevenlabss-new-music-generation-model-can-switch-genres-mid-track/
- ElevenLabs公式ドキュメント(Music概要): https://elevenlabs.io/docs/overview/capabilities/music

## 注意

- 一部のニュース記事本文には直接アクセスできず、検索エンジンの要約経由での
  確認である
- 「Vocals」機能は声の生成に関する技術であり、実在人物の声を無断で模倣する
  用途への懸念があり得るため、本資料・成果物では機能の仕組みを事実として
  紹介するにとどめ、悪用方法の具体的な手順には触れない
- 公開・投稿はまだ行っていない
