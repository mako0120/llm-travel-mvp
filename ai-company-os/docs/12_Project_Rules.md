# 12. Project Rules(このリポジトリ固有の規則)

## このリポジトリの位置づけ

- `ai-company-os` は成果物制作の**運用OS**。プロダクトコード(例: llm-travel-mvp)は別リポジトリで管理する。
- 他リポジトリの規約とこのリポジトリの規約が矛盾する場合、作業対象リポジトリの規約を優先する。

## ファイル命名

- ドキュメント: `docs/NN_Name.md`(NN は 2桁連番。挿入時は番号を振り直さず末尾に追加)
- テンプレート: `templates/<用途>_template.md`
- スクリプト: `scripts/<動詞>_<対象>.py`(例: `verify_pptx.py`)
- 成果物: `assets/<YYYY-MM-DD>_<slug>/` 配下

## 言語

- ドキュメント・Issue・PR・報告は日本語。コード・コミットメッセージの1行目は英語でもよい。
- 憲章3ファイル(CLAUDE.md / README.md / START_PROMPT_JA.md)は人間のオーナーが管理する。変更提案は PR で行い、直接書き換えない。

## CI

- すべての PR で `.github/workflows/ci.yml` が実行される:
  - `docs/00`〜`docs/12` の13ファイルが揃っているか
  - `git diff --check`(空白エラー・コンフリクトマーカー)
  - `python scripts/verify_pptx.py --self-test`
- CI が red の PR はレビューに回さない。

## 更新責任

このリポジトリのドキュメントを実態と乖離させた者が、その PR で直す。
「あとで直す」を認めない(小さい修正を積む)。
