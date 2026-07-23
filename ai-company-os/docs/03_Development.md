# 03. Development(開発規約)

## 環境の前提

- 実行環境はセッションごとに異なる。**起動時に必ず能力検証を行う**(CLAUDE.md の Startup protocol)。
- 検証済みの既知事実(2026-07 時点の記録。再検証してから使うこと):
  - `python-pptx` は `pip install python-pptx` で導入可能(PowerPoint 生成の第一選択)。
  - `pptxgenjs` は npm install が必要で、無承認インストールは不可。
  - LibreOffice の Impress インポートフィルタが壊れている環境がある(pptx→画像のレンダリング検証は不可の場合あり)。その場合は `scripts/verify_pptx.py` によるプログラム検証で代替し、限界を明記する。
  - Chromium + Playwright は利用可能(`/opt/pw-browsers/chromium`)。

## コーディング規約

- スクリプトは Python 3.10+ / 標準ライブラリ + python-pptx を基本とする。
- すべてのスクリプトは CLI から単体実行でき、終了コードで成否を返す。
- 乱数・日時に依存する出力を作らない(再現性)。
- 生成スクリプトには「入力(構成Markdown等)→ 出力(pptx)」の対応をヘッダコメントで書く。

## 検証(コミット前に必ず実行)

```text
git diff --check                     # 空白・コンフリクトマーカー
python scripts/verify_pptx.py --self-test   # 検証スクリプト自体の健全性
python scripts/build_deck.py templates/deck_spec_example.json /tmp/sample.pptx  # 生成パイプライン
python scripts/verify_pptx.py /tmp/sample.pptx --min-slides 6 --max-slides 6    # 生成物の検品
python scripts/verify_pptx.py <生成した .pptx>  # 実制作物の検品
```

CI(`.github/workflows/ci.yml`)は同じチェックを PR ごとに実行する。

## コミット・PR

- コミットメッセージは変更内容を1行で要約し、本文に検証結果を書く。
- PR 本文の必須セクション: 目的 / 変更内容 / 変更していないこと / テスト結果 / リスク / 人間承認が必要な事項。
- Draft PR 作成後は停止し、レビューと承認を待つ。
