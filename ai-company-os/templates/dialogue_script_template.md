# AI対話ナレーション原稿 テンプレート

2人のAIペルソナが掛け合いで時事ニュースを解説する動画向けナレーション形式。
「起承転結」の4幕構成で、`research.md` で調査済みの事実を配分する。
`scripts/generate_dialogue_script.py` で `dialogue_spec.json` から自動生成する
(仕様・検証ルールは `docs/13_AI_Dialogue_Script.md` を参照)。

## 使い方

1. `research.md` で検証済み事実・不明点を整理する(既存フロー通り)
2. このテンプレートを見ながら `dialogue_spec.json` を書く(`templates/dialogue_spec_example.json` を複製して書き換えるのが早い)
3. `python scripts/generate_dialogue_script.py dialogue_spec.json script.md` で原稿を生成する
4. エラーが出たら仕様(起承転結の順序・speaker・text)を修正する

## 4幕の役割

| 幕 | 役割 | 書く内容の目安 |
|---|---|---|
| 起(導入) | 話題の提示・なぜ今扱うのか | フックになる問いかけ、テーマの一言紹介 |
| 承(展開) | 事実・数字の解説 | `research.md` の「検証済み事実」を中心に、出典付きで |
| 転(転換) | 別の角度・反論・注意点 | 「不明点」「見送った候補」「反対意見・弱点」を活かす |
| 結(結論) | まとめ・示唆 | 視聴者が持ち帰れる一言、次のアクション |

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

```json
{
  "meta": {
    "title": "テーマ名",
    "personas": [
      { "id": "host", "name": "ペルソナ名", "role": "役割の説明" },
      { "id": "analyst", "name": "ペルソナ名", "role": "役割の説明" }
    ],
    "sources": ["https://..."]
  },
  "acts": [
    { "act": "起", "label": "導入", "lines": [ { "speaker": "host", "text": "..." } ] },
    { "act": "承", "label": "展開", "lines": [ { "speaker": "analyst", "text": "...", "source": "https://..." } ] },
    { "act": "転", "label": "転換", "lines": [ { "speaker": "host", "text": "..." } ] },
    { "act": "結", "label": "結論", "lines": [ { "speaker": "analyst", "text": "..." } ] }
  ]
}
```

実例は `templates/dialogue_spec_example.json` を参照。
