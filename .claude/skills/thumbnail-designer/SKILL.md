---
name: thumbnail-designer
description: >
  AI Company OS(ai-company-os/配下)のテーマ制作でYouTubeサムネイル(1280x720)を
  生成・再生成するときに使う。「サムネイルを作って」「サムネイル作成して」
  「定期実行でテーマを作った」「新しいテーマの成果物一式を揃えて」のように、
  ai-company-os/assets/配下に新しいテーマディレクトリ(deck.pptx・dialogue_audio.wav等)
  を作った直後は、指示されなくてもこのスキルを使ってサムネイルまで自動生成する。
  既存テーマのサムネイルの作り直しを頼まれたときにも使う。2026-07-24以降、
  Canva MCP(generate-design/edit-design)経由での生成が標準(Canva未接続時のみ
  ai-company-os/scripts/build_thumbnail.pyのPillow版にフォールバック)。
  「Canvaで」「Canvaサムネイル」等の言及がなくても、テーマ制作の一環として
  自動的にこのスキルを経由すること。守るべき禁止事項(実在人物の写真・誇張文言・
  Claude/Anthropic自体を主題にした自己宣伝の禁止)があるため必ずこの手順を通す。
---

# サムネイル・デザイナー(AI Company OS)

テーマごとのYouTubeサムネイルを生成する。2026-07-24にCanvaコネクタが接続され、
オーナーから「今後はこのやり方(Canva)で」と明示的な指示があったため、
**Canva MCP経由での生成を標準ルート(A)**、`ai-company-os/scripts/build_thumbnail.py`
のPillow版を**Canva未接続時のフォールバック(B)**とする。まずCanvaツール
(`mcp__Canva__*`)が使えるかをToolSearch等で確認し、使えるならルートAに進む。

## なぜこの手順を守る必要があるか

このリポジトリの成果物は「事実整理型・出典必須・誇張なし」を軸にした継続シリーズ
(`AGENTS.md` / `ai-company-os/CLAUDE.md`)。サムネイルも例外ではなく、過去に
オーナーへ提示した参考サムネイル(実在のYouTuberの写真・「全米が泣いた」的な
誇張文言)を分析した上で、**レイアウトの手法だけを借りて、中身は事実に基づいた
ものに置き換える**という方針で設計した(経緯: `ai-company-os/docs/14_YouTube_Thumbnail.md`、
調査: `ai-company-os/research/2026-07-24_youtube-thumbnail-best-practices.md`)。
この方針を毎回自分で再導出しなくて済むように、スキルとして固定している。

## 絶対に守ること

- **実在人物の写真・肖像は使わない**(`AGENTS.md`の肖像リスク回避方針)。人物が
  必要な箇所(`hype`スタイルの人物枠)は、円形の抽象アイコン + 既存のAI対話
  ペルソナ名(`dialogue_spec.json`の`meta.personas`、例:「リサーチAI」)を使う
- **バナー文言・再生時間バッジは実データのみ**。発表日はそのテーマの
  `research.md`/`deck_spec.json`の事実、再生時間は`dialogue_audio.wav`の実測値を
  使う。架空の「期間限定」「〇〇人が驚いた」のような数字・煽り文句は作らない
- **誇張・釣り文言を避ける**。フック文言は`deck_spec.json`のtitleスライドの
  見出しを凝縮したもので、動画本編の内容と乖離させない
- 生成は1280×720。`build_thumbnail.py --self-test`が168×94への縮小確認まで
  自動でやってくれるので、迷ったら流用する

## ルートA: Canva経由(標準、2026-07-24〜)

1. 対象テーマの`deck_spec.json`(1枚目titleの見出し)・`research.md`(発表日等の
   事実)・`dialogue_audio.wav`の実測秒数(手順は下記ルートBの3と同じ)を確認する
2. `mcp__Canva__generate-design`を`design_type: "youtube_thumbnail"`で呼ぶ。
   クエリには必ず含める:
   - 実データのみ(発表日・見出し・実測の動画尺)。架空の煽り文句は書かない
   - 「実在の有名人・実在人物の写真ではなく、汎用のイラスト/ベクター調
     キャラクターを使うこと」を明記(実在人物の肖像を生成させないため)
   - 配色・レイアウトの方向性(例: 赤×黒×黄の高コントラスト、上部の斜め帯
     バナー、階層見出し、再生時間バッジ)
   - 実例のクエリ文面は本ファイルのgitログ(2026-07-24のコミット)か、
     `ai-company-os/docs/14_YouTube_Thumbnail.md`の追記部分を参照
3. 返ってきた`generated_designs`候補から1つを選び、`create-design-from-candidate`
   で編集可能なデザインに変換する(`job_id`と`candidate_id`が必要)
4. `read-design`(`open_transaction: true`, `filter.fields: ["design_content","thumbnails"]`)
   で内容とサムネイル画像を取得し、**必ず目視確認する**。AI生成は次の失敗が
   よく起きる:
   - 日本語の見出しが小さすぎる/黒背景に黒文字のようなコントラスト不足で
     実質見えない → `format_text`で`font_size`を上げ、`color`を背景と対比する
     色に変える(1回では反映されないことがあるので、色/太さを変えて強制的に
     再コンポジットさせると直ることがある)
   - 見出しの一部が装飾用の小さな斜めバナーに押し込まれて読めない →
     `delete_element`で該当要素を消し、`add_text`で見出し列の中に正しいサイズで
     追加し直す
   - 新規追加したテキストは既定で小さい/黒色になるので、`format_text`で
     サイズ・色・太さを設定し、`layer_element`で前面に出す
5. 修正できたら`edit-design`を`operations`省略・`finalize: "commit"`で呼んで確定する
6. `get-export-formats`→`export-design`(`type: "png", width: 1280, height: 720,
   format.as_single_image: true`)で書き出す
7. **この環境からは`design.canva.ai`/`export-download.canva.com`に直接アクセス
   できない(ネットワークポリシーで403)。** ファイルを直接ダウンロード・
   `SendUserFile`で送ることはできないので、Canvaの編集URL(`edit_url`)と
   書き出しURLをそのままオーナーに提示する
8. `thumbnail_brief.md`(`templates/thumbnail_brief_template.md`準拠)に、
   Canvaのデザインid・編集URL・フック文言の根拠を記録する。`thumbnail.png`は
   コミットできない(ダウンロードできないため)ので、テーマの`README.md`には
   Canva編集URLを記載する形にする
9. **既知の制約**: フォントファミリーはAPIから変更できない(`format_text`は
   色・サイズ・太さ等のみ)。日本語らしい書体にしたい場合は手順2のクエリで
   「日本語向けフォントを使うこと」と依頼するのが現状唯一の手段(確実性は
   保証できない)。手動でCanvaエディタの「フォント→矢印→言語別フォント」から
   選び直すことも可能だが、それはオーナー側の操作になる

## ルートB: Canva未接続時のフォールバック(Pillow)

1. 対象テーマのディレクトリ(`ai-company-os/assets/<日付>_<slug>/`)を確認する。
   最低限 `deck_spec.json` が必要。`dialogue_audio.wav` があれば再生時間バッジに使える
2. `deck_spec.json`の1枚目(title)から`heading`(問いかけ・フック)を読む。
   フック文言はここからさらに短く(日本語13〜20文字目安)凝縮する
3. 再生時間を取得する(あれば):
   ```bash
   python3 -c "
   import wave
   with wave.open('ai-company-os/assets/<slug>/dialogue_audio.wav') as w:
       sec = w.getnframes() / w.getframerate()
       print(f'{int(sec)//60}:{int(sec)%60:02d}')
   "
   ```
4. スタイルを選ぶ(特に指示がなければ `hype` を既定にする。詳細は下表):

   | style | 見た目 | 使いどころ |
   |---|---|---|
   | `standard` | 二色斜め背景+見出し+任意の数字バッジ+抽象アイコン | 落ち着いた印象にしたい/デッキ本体のnavy_gold系と統一したいとき |
   | `impact` | 赤×黒の放射状バースト+斜めリボン | インパクト重視だが情報量は絞りたいとき |
   | `hype`(既定) | 上部グラデーション帯バナー+3階層見出し+再生時間バッジ+人物枠(抽象アイコン+ペルソナ名) | オーナーが提示した参考例に最も近い、標準の「伸びる」レイアウト |

5. `thumbnail_spec.json`を作る。`hype`の場合の形(実例は
   `ai-company-os/assets/2026-07-24_gpt56-grok45-launch-race/thumbnail_spec.json`参照):
   ```json
   {
     "palette_preset": "impact_red",
     "style": "hype",
     "banner_text": "2026年7月8日・9日に発表",
     "lines": [
       {"text": "海外2社が", "color": "white", "size": 58},
       {"text": "同じ週に発表", "color": "accent", "size": 92},
       {"text": "GPT-5.6 vs Grok 4.5", "color": "white", "size": 84}
     ],
     "duration_badge": "5:14",
     "avatar_label": "リサーチAI",
     "tag": "AI/テック",
     "footer": "AI Company OS"
   }
   ```
   `lines`は最大3階層(白→アクセント色の強調→白のブランド/トピック名、の順が
   基本形)。`standard`/`impact`スタイルは`hook`/`stat_badge`/`ribbon`を使う
   (`build_thumbnail.py`のdocstringとself_test()に両方の例がある)。
   パレットは `ai-company-os/scripts/build_deck.py` の `PALETTE_PRESETS`
   (`navy_gold` / `impact_red` 等)を共有している
6. 生成する:
   ```bash
   python3 ai-company-os/scripts/build_thumbnail.py \
     ai-company-os/assets/<slug>/thumbnail_spec.json \
     ai-company-os/assets/<slug>/thumbnail.png
   ```
7. `ai-company-os/templates/thumbnail_brief_template.md` を元に
   `thumbnail_brief.md` を書く(フック文言の設計根拠・配色・検品チェック)。
   実例: `ai-company-os/assets/2026-07-24_gpt56-grok45-launch-race/thumbnail_brief.md`
8. 生成した`thumbnail.png`を`Read`ツールで開いて目視確認する(文字が枠から
   はみ出していないか、人物枠と見出しが重なっていないか)。1280×720の全体像に
   加え、`img.resize((168,94))`で縮小した版でも判読できるか確認する
9. テーマの`README.md`のファイル一覧表に`thumbnail.png` / `thumbnail_spec.json` /
   `thumbnail_brief.md`の行を追加する(他の成果物と同じ並び)

## つまずきやすい点

- 日本語の見出しは空白を含まないため、`build_thumbnail.py`内部の見出し折返しは
  文字数の均等2分割で行っている。3階層見出し(`hype`)は自分で短く区切って渡す
  必要がある(自動折返しはしない)
- `ribbon`(`impact`スタイルの斜めリボン)と`hype`の`banner_text`は別物。
  `hype`を使うときは`ribbon`/`stat_badge`は無視される
- コミットする画像は`thumbnail.png`のみでよい(`deck.pptx`と同様、数百KB程度の
  静的ファイルなので動画のようにコミット対象から外す必要はない)
