# 13. AI Dialogue Script(AI対話ナレーション形式)

## 背景

「AI時短ラボ」(YouTube)等、AIニュースを煽らず・事実整理型で伝えるチャンネルを参考に、
2026-07-23、オーナー指示により追加した第3の成果物形式。既存の研究フロー(`docs/06_Content_R&D.md`)
と出典ルールはそのまま流用し、**出力形式だけ**を「2人のAIペルソナが起承転結で掛け合う
ナレーション原稿」に変える。PowerPoint(生成方式A/B)と並行して使える、独立した成果物。

## いつ使うか

**2026-07-23〜、オーナー指示によりテーマ制作の標準成果物**とする。以後のテーマ制作
(定期実行含む)では、`research.md` / `chatgpt_prompt.md` / `README.md` に加えて、
`dialogue_spec.json` / `dialogue_script.md` も毎回作成する。

**2026-07-23の追加指示により、以後は必ずスライド連動モードを使う**(PowerPointの
全30枚と対応させる)。フラットモードは、対話ナレーションだけを単独で求められた場合の
補助手段とする。

- YouTube/Shorts向けのナレーション音声・字幕として使いたいとき
- PowerPoint(方式A)に加えて、動画コンテンツとしても展開したいとき

## 2つのモード

- **フラットモード**(短いハイライト向け): 各幕に `lines` を直接書く。起承転結それぞれの
  要点だけを短く紹介する台本になる。
- **スライド連動モード**(2026-07-23〜、標準):PowerPoint(生成方式A)の`deck_spec.json`と
  1対1で対応させ、**全スライドを漏れなく解説する**台本を作る。各幕に `slides`(スライド単位の
  セグメント)を書き、各セグメントが `deck_spec.json` の特定のスライド番号(`slide`)に対応する。
  `generate_dialogue_script.py --deck deck_spec.json` を指定すると:
  - スライドの見出しを `deck_spec.json` から自動取得して原稿に表示する(見出しの二重管理が不要)
  - 対話原稿がカバーするスライド数と `deck_spec.json` のスライド数が一致するか検証する
  - 全幕を通じたスライド番号が 1 から始まる連番(抜け・重複・逆順なし)になっているか検証する

  これにより、「PowerPointの何枚目を、対話のどの部分で説明しているか」が仕組みとして
  保証される。30枚規模のデッキでも、1枚も取りこぼさず解説する台本を機械的に作れる。

## 生成パイプライン(スライド連動モード)

```text
① 調査する      research.md に検証済み事実/推測/不明点を分けて記録する(既存フローと同じ)
② デッキを作る  生成方式A(docs/04_PowerPoint.md)で deck_spec.json → .pptx を作成
③ 仕様を書く    deck_spec.json の各スライドを1つずつ、起承転結のいずれかの幕に割り付け、
                そのスライドの内容を2AIペルソナの掛け合いに変換した dialogue_spec.json を書く
                (割り付けの目安は下表)
④ 生成する      python scripts/generate_dialogue_script.py dialogue_spec.json script.md \
                  --deck deck_spec.json
⑤ 検品する      生成時のバリデーションで自動的に検査される(下記「検証項目」参照)
⑥ 納品する      script.md をユーザーに送付する(SendUserFile)
```

短いハイライトだけで十分な場合は、従来通りフラットモード(`lines`)も使える。

## 起承転結への事実(スライド)の割り付け方

| 幕 | 対応するスライドの内容 |
|---|---|
| 起(導入) | 表紙・結論・なぜ今扱うのか・背景データ・時系列など、導入部のスライド群 |
| 承(展開) | 基礎知識・用語解説・比較・具体的な数字・グラフなど、本編中心のスライド群 |
| 転(転換) | 活用方法・成功/失敗パターン・注意点・反対意見や弱点のスライド群 |
| 結(結論) | 今後の予測・CTA・出典一覧など、まとめのスライド群 |

デッキの実際の構成に応じて、各幕に何枚割り付けるかは調整してよい(4幕である必要はあるが、
各幕のスライド枚数は均等でなくてよい)。

## ペルソナ設計ルール

- 2つのAIペルソナ(進行役 × 解説役、など役割を分ける)を基本とする
- 実在の人物・タレント・声優を模した名前・口調・そっくり声(音声合成含む)は使わない。
  AIキャラクターであると分かる名称・トーンにする
- 「最強」「ヤバい」等の煽り表現を避け、事実を整理して伝えるトーンにする(参考にした
  チャンネルのスタンスを踏襲)

## エンゲージメント設計ルール(離脱防止、2026-07-23〜)

`research/2026-07-23_audience-retention-techniques.md` の調査に基づく。単独ナレーション
動画のノウハウが中心のため、対話形式への適用は調査担当による応用であることに留意する。

- **冒頭フック**: 起の最初の発言は挨拶・自己紹介にせず、フックになる問いかけや
  驚きの一言にする(例: 「大手企業がAIエージェントの設計を4か月で2回作り直したらしい」)
- **パターンインタラプト**: 「事実→相槌」の同じパターンを機械的に繰り返さない。
  驚き・ツッコミ・問い直し・共感など、ナビAIの反応のトーンに意図的な起伏をつける
- **見せる化**: 数字を話す行では、対応スライドの図解・グラフ・表を指す一言
  (「グラフにするとこうです」等)を添え、聞くだけでなく見る動機を作る
- **約束→提供→次の約束(オープンループ)**: 各幕の最後の発言は、単なるまとめで
  終わらせず、次の幕への引きになる一言にする(例: 「ここまでが前提。ここからは
  中身に入っていこう」)

## 検証項目(`generate_dialogue_script.py` がビルド時に強制)

1. `meta.personas` が2人以上定義されている
2. `acts` が「起・承・転・結」の4幕をこの順序ですべて含む
3. 各行の `speaker` が `meta.personas` に定義された persona id である
4. 各行の `text` が空でない
5. (スライド連動モード)全幕を通じたスライド番号が 1 から始まる連番になっている
   (抜け・重複・逆順を検出)
6. (スライド連動モード、`--deck` 指定時)対話原稿がカバーするスライド数が
   `deck_spec.json` の実際のスライド数と一致する

上記に違反する仕様はビルド時にエラー終了し、修正箇所を一覧表示する。
`python scripts/generate_dialogue_script.py --self-test` で検証ロジック自体を確認できる
(フラットモード・スライド連動モードの両方、および deck とのスライド数不一致の検出を含む)。

## 音声化(TTS)(2026-07-23〜、標準化済み: GitHub Actions経由のVOICEVOX)

`research/2026-07-23_tts-options.md` の比較検討を経てVOICEVOXを採用。Claude Codeの
リモートセッション自体はegressポリシーでDocker Hubにアクセスできずセルフホスト
不可(`dockerd`起動・`docker pull`・`pip install`いずれも失敗を確認済み)だが、
**GitHub Actionsのubuntu-latestランナーは通常のインターネットアクセスを持つため、
そこでVOICEVOX Engineを起動して音声化する**運用を2026-07-23にmainマージ済み
(`.github/workflows/synthesize-dialogue-audio.yml`)。

以後、新しいテーマの`dialogue_spec.json`ができたら**都度確認を挟まず、以下を標準手順として
自動で実行する**:

```text
① dialogue_spec.jsonを作成・pushする
② actions_run_trigger(workflow_dispatch)でsynthesize-dialogue-audio.ymlを実行する
   (ref: 作業ブランチ, theme_dir: テーマディレクトリ名)
③ 完了を待つ(CPU版VOICEVOXで61発言・約5分程度が目安)
④ git pullしてassets/<テーマ>/dialogue_audio.wavを取得する
⑤ SendUserFileでオーナーに直接送付する(Notionには添付せず、パスを明記するだけ)
```

**設計上の注意点(2026-07-23の初回実行で判明した既知の罠)**:
- Actions Artifact(`actions/upload-artifact`)のダウンロード元はAzure Blob Storage
  (`blob.core.windows.net`)だが、このホストもClaude Codeのセッションからは接続不可。
  そのため音声ファイルはArtifactではなく、ワークフロー自身が`git commit`+`git push`で
  リポジトリへ直接コミットする形で取り出す
- ワークフローの`workflow_dispatch`はデフォルトブランチ(main)に存在しないと
  API経由でトリガーできない(GitHubの仕様)。ワークフローファイル自体の追加・変更は
  必ずmainへの反映(=人間承認)が必要
- CI実行中に別コミットを同じブランチへpushすると、CI側のpushが競合して失敗する。
  ワークフロー側でpush前に`git fetch && git rebase`する対策を入れている
- VOICEVOX Engineへのリクエストのtext/speakerパラメータは`urllib.parse.urlencode`で
  URLエンコードすること(日本語・記号を含むテキストをエンコードせず渡すと
  `http.client.InvalidURL`で失敗する)

```text
(ローカルで確認する場合)
① 話者を確認する  python scripts/synthesize_dialogue_audio.py --list-speakers
② 音声化する      python scripts/synthesize_dialogue_audio.py dialogue_spec.json out.wav \
                     --voice-map host=3,analyst=2
```

`synthesize_dialogue_audio.py` は dialogue_spec.json(フラット・スライド連動どちらの
モードも対応)を読み、行ごとにVOICEVOX Engineの `/audio_query` → `/synthesis` を呼び出し、
1本の`.wav`に結合する。エンジンに接続できない場合はエラーメッセージで起動を促す。
`--self-test` でエンジンなしに検証できるロジック(仕様パース・WAV結合)のみ確認できる。

## PowerPoint方式との関係

- 出典ルール・正直さのルール(推測で埋めない、不明点は不明と書く)は`docs/06_Content_R&D.md`と共通
- 同じ`research.md`から、PowerPoint用の`chatgpt_prompt.md`と、この`dialogue_spec.json`/`script.md`の
  両方を作ることができる(二重取材の必要はない)
- テーマ選定(モードA/モードB)のルールは変更しない

## 未検証・今後の課題

- 実際にこの形式で生成した動画の再生数・エンゲージメントの効果測定は未実施
- 音声合成(TTS)との連携は本ドキュメントの範囲外(別途、人間承認のうえ検討)
- 「AI時短ラボ」のチャンネル自体の詳細な動画構成は、YouTube本体への自動アクセスが
  できず未確認。本形式はオーナーからのヒアリング内容(起承転結・AI同士の会話)を
  もとに独自設計したものであり、同チャンネルの内容をそのまま模倣したものではない
