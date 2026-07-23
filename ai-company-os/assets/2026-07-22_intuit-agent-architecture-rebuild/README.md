# Intuit、AIエージェントのアーキテクチャを4か月で2度作り直した理由(ChatGPTプロンプト方式・2026-07-22・定期実行17本目)

## 選定理由

- 対象ジャンル「AI/エージェント系」枠(70%)。マルチエージェントシステムの設計に
  関する実例で、AI Company OS自身のミッション(AIエージェント活用)とも直結
- モードB(バイラル優先)の採用条件を満たす: VentureBeat(信頼できる技術専門メディア)が
  VB Transform 2026での実際の登壇内容をIntuit AI担当VPの実名・直接引用付きで一次取材し、
  Cryptopond・Progressive Robot・dataworldbank等、複数サイトに転載・言及され、
  業界内で広く共有された
- 具体的な数字(4か月、60日、20日未満、10エージェント)と実名の直接引用があり、
  検証不能なSEOブログ的主張ではない

## ファイル一覧

| ファイル | 内容 |
|---|---|
| `research.md` | 出典付き調査結果 |
| `chatgpt_prompt.md` | ChatGPTにそのまま貼り付けて使うプロンプト本文 |
| `dialogue_spec.json` | AI対話ナレーション形式(`docs/13_AI_Dialogue_Script.md`)の仕様。同じ`research.md`から作成 |
| `dialogue_script.md` | `generate_dialogue_script.py`で`dialogue_spec.json`から生成した、2AIペルソナ・起承転結の対話ナレーション原稿(2026-07-23追加、機能デモとして本テーマに追加) |

## 出典

VentureBeat(一次取材)。詳細は `research.md`。

## 注意

- VentureBeat記事本文には直接アクセスできず(403エラー)、検索エンジンの要約・引用
  経由での確認である旨を明記した
- 1社の事例であり、業界全体への一般化はできない点をプロンプト内で明示した
- 公開・投稿はまだ行っていない
