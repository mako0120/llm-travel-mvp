# Jack Dorsey氏のBuzz、Slack・GitHubへの挑戦(2026-07-23・定期実行21本目)

生成方式A(30枚標準・エンゲージメント設計ルール)+ AI対話ナレーション・スライド連動モードで
制作。

## 選定理由

- 対象ジャンル「AI/エージェント系」枠(70%)
- モードB(バイラル優先)の採用条件を満たす: TechCrunchの一次取材報道に加え、
  Slashdot・Yahoo Tech・Cryptopolitan・BigGo Finance・incrypted・digitaltoday.co.kr・
  smartcompany.com.au等、非常に多くの独立系メディアが2026年7月21〜22日に一斉に報道
- 著名起業家(Jack Dorsey氏)による発表という注目度と、「AIエージェントをメンバーとして
  扱う」という設計思想の新しさ

## 見送った候補

- 三笘薫選手の自動車事故関連報道 — 本人の意図しないセンシティブな話題のため見送り
- 久保建英選手・佐野海舟選手の移籍市場価値報道 — 憶測・噂の域を出ないため見送り
- Microsoft×Mistralの提携拡大 — 有力候補だったが、Buzzの方がより幅広いメディアで
  独自性の高い切り口で報じられていたため今回は見送り

## ファイル一覧

| ファイル | 内容 |
|---|---|
| `research.md` | 出典付き調査結果(見送った候補の記録を含む) |
| `deck_spec.json` | 30枚のデッキ仕様(同一レイアウト4連続以上なし) |
| `narration_script.md` | 単独ナレーション原稿(30スライド、目安約6分) |
| `dialogue_spec.json` | AI対話ナレーション・スライド連動モード仕様(30スライド全カバー) |
| `dialogue_script.md` | 対話ナレーション原稿(30スライド、目安約10分) |
| `deck.pptx` | 生成済みの.pptx本体。オーナーへチャットで直接送付済み(`docs/09_Notion.md`参照) |
| `dialogue_audio.wav` | 対話ナレーションの音声(VOICEVOX、host=ずんだもん/analyst=四国めたん、約10分)。GitHub Actions(`synthesize-dialogue-audio.yml`)上でVOICEVOXを起動して生成し、オーナーへチャットで直接送付済み |

## 追記(2026-07-23): 音声化(VOICEVOX、GitHub Actions経由)

Claude Codeのリモートセッション自体はegressポリシーでVOICEVOX(Docker Hub)を起動できないため、
手動トリガー(workflow_dispatch)の`synthesize-dialogue-audio.yml`をGitHub Actions上で実行し、
`dialogue_spec.json`(61発言、スライド連動モード)を音声化した。生成物はActions Artifact
(ダウンロード元のblob.core.windows.netも当セッションからは接続不可)ではなく、ワークフロー
自身がリポジトリへ直接コミットする形で取り出した。

## 追記(2026-07-23): 文字を減らし、図解・グラフ中心に作り直し

オーナーから「文字が多いので、図形・グラフでもっと見てわかるようにしてほしい」との
フィードバックを受け、`build_deck.py`に新レイアウト`big_stat`(1数字に焦点)・`diagram`
(ノードを矢印でつなぐ概念図)を追加し、`steps`にも矢印を追加。bulletsを9枚
cards/diagram/comparisonに置き換え、**bullets比率を53%→23%に削減**した
(新設の「bullets比率40%上限」ルールにも適合)。事実・数字は変更していない。

## 検品結果

- `verify_pptx.py --min-slides 30 --max-slides 30` → 合格
- `build_deck.py`の同一レイアウト4連続以上チェック・bullets比率40%以下チェック → 合格
- `generate_dialogue_script.py --deck`のスライド数整合性検証(30枚、1〜30連番) → 合格

## リスク配慮

- 特定の国・政府・政党を扱う政治的テーマではなく、企業(Block社)の製品発表という事実紹介
- 実在企業名・実在人物名(Jack Dorsey氏)は事実として扱うが、写真・ロゴ・商標画像は使用しない

## 注意

- TechCrunch等の記事本文には直接アクセスできず(403エラー)、検索エンジンの要約・引用
  経由での確認である旨を`research.md`に明記した
- 公開・投稿はまだ行っていない
