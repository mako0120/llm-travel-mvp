# 09. Notion Operations(Notion 運用)

## 前提

- Notion コネクタは環境により接続状態が異なる。使用前に必ず検証する(未接続なら記録は Markdown で `docs/` 配下に残し、接続後に転記する)。

## 記録のタイミング

- 結果が**確定してから**記録する(PR merge 後、レビュー完了後)。見込みで書かない。
- 1作業1レコード。後から検索できるよう Issue/PR の URL を必ず入れる。

## 記録する内容

| 項目 | 内容 |
|---|---|
| タイトル | 成果物または Issue の名前 |
| ステータス | Backlog / Ready / In Progress / PR Open / Reviewing / Released |
| リンク | GitHub Issue / PR / 成果物 |
| 結果 | 完了・中断・失敗と、その一行理由 |
| 学び | 次に活かす教訓(失敗時は必須) |

## 学習ログ

失敗・手戻り・環境の罠(例: LibreOffice フィルタ破損、npm install 不可)は
「リリース・学習ログ」に記録し、`docs/03_Development.md` の既知事実にも反映する。
記録先が二重になる場合はリポジトリ側(`docs/`)を一次情報とする。
