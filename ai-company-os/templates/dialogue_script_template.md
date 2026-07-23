# AI対話ナレーション原稿 テンプレート

2人のAIペルソナが掛け合いで時事ニュースを解説する動画向けナレーション形式。
「起承転結」の4幕構成で、`research.md` で調査済みの事実を配分する。
`scripts/generate_dialogue_script.py` で `dialogue_spec.json` から自動生成する
(仕様・検証ルールは `docs/13_AI_Dialogue_Script.md` を参照)。

## 使い方(スライド連動モード、標準)

1. `research.md` で検証済み事実・不明点を整理する(既存フロー通り)
2. 生成方式A(`docs/04_PowerPoint.md`)で `deck_spec.json` → `.pptx` を作成する
3. `deck_spec.json` の全スライドを1枚ずつ確認し、`templates/dialogue_spec_example.json`
   (スライド連動モードの実例)を見ながら `dialogue_spec.json` を書く。各スライドを
   起承転結いずれかの幕の `slides` セグメントに割り付け、そのスライドの内容を
   2AIペルソナの掛け合いに変換する
4. `python scripts/generate_dialogue_script.py dialogue_spec.json script.md --deck deck_spec.json`
   で原稿を生成する(`--deck`指定で見出し自動取得・スライド数の整合性検証まで行われる)
5. エラーが出たら仕様(起承転結の順序・スライド番号の連番・speaker・text)を修正する

短いハイライトだけで十分な場合は、`slides` の代わりに `lines` を直接書く
フラットモードも使える(`--deck` は不要)。

## 4幕の役割

| 幕 | 役割 | 割り付けるスライドの目安 |
|---|---|---|
| 起(導入) | 話題の提示・なぜ今扱うのか | 表紙・結論・背景データ・時系列など |
| 承(展開) | 事実・数字の解説 | 基礎知識・比較・具体的な数字・グラフなど、`research.md`の「検証済み事実」中心 |
| 転(転換) | 別の角度・反論・注意点 | 活用方法・成功/失敗パターン・「不明点」「反対意見・弱点」を活かすスライド |
| 結(結論) | まとめ・示唆 | 今後の予測・CTA・出典一覧など |

## ペルソナ設計ルール

- ペルソナは2つのAI(例: 進行役 × 解説役)とし、実在の人物・タレント・声優を
  模した名前や口調にしない(AIキャラクターであることが分かる名称にする)
- 役割を明確に分ける(例: 「疑問を投げる役」と「事実を解説する役」)
- 掛け合いは自然な会話のテンポを意識し、1行(1発言)を長くしすぎない目安

## 品質ルール(既存ルールを踏襲)

- 数字を扱う発言には `source` フィールドで出典を明記する
- 調査で確認できなかった点は「転」の幕で正直に「不明」として扱う(推測で埋めない)
- 誇張表現("ヤバい"「最強」等の煽り言葉)は避け、事実を整理するトーンにする
- 政治・高リスク領域の話題は、他のテーマ制作と同じ人間承認ルールに従う

## JSON仕様(`dialogue_spec.json`)の構造

### スライド連動モード(標準)

```json
{
  "meta": {
    "title": "テーマ名",
    "personas": [
      { "id": "host", "name": "ペルソナ名", "role": "役割の説明" },
      { "id": "analyst", "name": "ペルソナ名", "role": "役割の説明" }
    ],
    "deck_spec": "deck_spec.json",
    "sources": ["https://..."]
  },
  "acts": [
    { "act": "起", "label": "導入", "slides": [
      { "slide": 1, "lines": [ { "speaker": "host", "text": "..." } ] },
      { "slide": 2, "lines": [ { "speaker": "analyst", "text": "...", "source": "https://..." } ] }
    ] },
    { "act": "承", "label": "展開", "slides": [ { "slide": 3, "lines": [ { "speaker": "analyst", "text": "..." } ] } ] },
    { "act": "転", "label": "転換", "slides": [ { "slide": 4, "lines": [ { "speaker": "host", "text": "..." } ] } ] },
    { "act": "結", "label": "結論", "slides": [ { "slide": 5, "lines": [ { "speaker": "analyst", "text": "..." } ] } ] }
  ]
}
```

`slide` は `deck_spec.json` の何枚目のスライドかを表す整数。全幕を通じて 1 から始まる
連番(抜け・重複・逆順なし)である必要がある。見出しは `--deck` 指定時に自動取得されるため、
JSON側で重複して書く必要はない。

### フラットモード(短いハイライトのみで十分な場合)

```json
{
  "meta": { "title": "テーマ名", "personas": [ ... ], "sources": ["https://..."] },
  "acts": [
    { "act": "起", "label": "導入", "lines": [ { "speaker": "host", "text": "..." } ] },
    { "act": "承", "label": "展開", "lines": [ { "speaker": "analyst", "text": "...", "source": "https://..." } ] },
    { "act": "転", "label": "転換", "lines": [ { "speaker": "host", "text": "..." } ] },
    { "act": "結", "label": "結論", "lines": [ { "speaker": "analyst", "text": "..." } ] }
  ]
}
```

実例は `templates/dialogue_spec_example.json`(スライド連動モード)を参照。
