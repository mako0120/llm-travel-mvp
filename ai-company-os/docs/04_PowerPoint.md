# 04. PowerPoint Standards(PowerPoint 制作標準)

## 基本仕様

- スライドサイズ: 16:9(13.333 × 7.5 インチ)
- フォント: 游ゴシック(Yu Gothic)を基本。英数は同フォントで統一
- 1スライド1メッセージ。本文は最大5ブレット、1ブレット最大2行
- 全スライドにスピーカーノート必須(話す内容の完全な下書き、1枚あたり100〜300字)

## 配色

パレットは3色+背景で固定し、デッキ内で混在させない。`build_deck.py` には3つの既定プリセットがあり、
`meta.palette_preset` で選択する(個別の色は `meta.palette` で上書き可能):

| プリセット | Primary | Base | Accent | 向いている用途 |
|---|---|---|---|---|
| `navy_gold`(既定) | `#1E2761` | `#CADCFC` | `#D9A441` | 信頼・フォーマル(営業・提案資料) |
| `forest_sand` | `#24523F` | `#E7DCC2` | `#C1622D` | サステナ・自然派・教育 |
| `slate_azure` | `#2B3A55` | `#D3E4F5` | `#1F8FD6` | テック・プロダクト紹介 |

## 構成の型(標準11枚)

1. タイトル 2. 課題(共感) 3. 課題の深掘り(データ) 4. 解決策の全体像
5. 機能・デモ 6. 効果(数字) 7. 比較(競合・価格) 8. 導入ステップ
9. 料金 10. リスクと対策 11. CTA・次のアクション

内容によっては「7. 比較」を `comparison`(2軸比較)や `table`(価格表・マトリクス)に、
「1.5 アジェンダ」を `agenda` に、証言・推薦の挿入に `quote` を使うなど、下記レイアウトを組み合わせる。

## データと出典

- 数字を出すスライドには必ず出典をフッターまたはノートに記載する。
- グラフは python-pptx のネイティブチャート(bar_chart / line_chart / pie_chart)で生成する。画像貼り付けのグラフは編集不能になるため避ける。
- 推移データは `line_chart`、構成比は `pie_chart`(カテゴリ5個以下推奨)、量の比較は `bar_chart` を使い分ける。

## 生成と検品(標準パイプライン)

```text
① 調査する        Web検索等で最新情報を集め、出典を記録する(docs/06_Content_R&D.md準拠)
② 構成を書く      templates/deck_outline_template.md(人間が読める構成+ノート)
③ JSON仕様にする  templates/deck_spec_example.json を複製して書き換える
④ 生成する        python scripts/build_deck.py spec.json out.pptx
⑤ 検品する        python scripts/verify_pptx.py out.pptx
⑥ 原稿を出す      python scripts/export_script.py spec.json script.md
```

`export_script.py` は同じ JSON 仕様からスピーカーノートを「読み上げ原稿」として
Markdown に書き出す(スライドごとの見出し・全文ノート・目安発表時間・合計時間)。
PowerPoint を開かずに原稿だけを読んで推敲・リハーサルできる。原稿にノート欠落があれば
`build_deck.py` と同じ規則でエラー終了する。

- `build_deck.py` は 12 レイアウト(title / bullets / cards / steps / agenda / comparison / table /
  quote / bar_chart / line_chart / pie_chart / cta)に対応し、ノート欠落・ブレット6個以上・table の
  列数不一致をビルド時にエラーとして拒否する。全レイアウトの実例は `templates/deck_spec_example.json` を参照。
- 特殊なレイアウトが必要な場合のみ個別スクリプトを書き、スクリプトをリポジトリに残す。
- 生成後は必ず `python scripts/verify_pptx.py <file>` を実行する。検品項目:
  - スライド枚数が構成と一致
  - 全スライドにノートが存在
  - 図形がスライド境界からはみ出していない
  - 空のプレースホルダが残っていない
- レンダリング(見た目)検証ができない環境では、その旨を成果報告に明記する。

## 公式スキルとの役割分担

Claude Code には Anthropic公式 `anthropics/skills` 由来の `pptx` スキルが標準搭載されている(source-available)。
`build_deck.py` を自前で持つ理由:

- 公式スキルの利用条件変更の影響を受けない、再現可能な生成ロジックを持つため
- ノート必須・ブレット上限などの**このリポジトリ固有の品質規則をコードで強制**するため(公式スキルは汎用)
- CI(`ai-company-os-ci.yml`)で毎回 E2E 検証できる形にするため

単発の凝ったデザインが必要な場合は公式 `pptx` スキルを使い、標準フォーマットの反復生産には `build_deck.py` を使う。
詳細な比較は `research/2026-07-20_useful-repositories.md` を参照。
