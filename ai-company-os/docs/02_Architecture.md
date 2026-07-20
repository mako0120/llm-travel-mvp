# 02. Architecture(リポジトリ構成と役割分担)

## ディレクトリ構成

```text
ai-company-os/
├── CLAUDE.md              # Claude Code の入口(憲章)
├── README.md              # 人間向け概要
├── START_PROMPT_JA.md     # セッション開始時の実行指示
├── docs/                  # 00〜12 の運用ドキュメント(必読順)
├── templates/             # デッキ構成・Canvaブリーフ・調査レポートの雛形
├── scripts/               # 検証スクリプト(verify_pptx.py など)
├── assets/                # 生成した成果物(デッキ・図版)。大容量はコミットしない
└── .github/workflows/     # CI(ドキュメント整合・スクリプト検証)
```

## 役割分担

| 役割 | 担当 | 責務 |
|---|---|---|
| CEO / 最終承認 | 人間 | 承認境界の判断、公開・課金・マージの決定 |
| 企画・設計 | ChatGPT Work | Issue 設計、要件定義 |
| 実装・生成 | Claude Code | 成果物生成、スクリプト実装、検証、Draft PR |
| レビュー | Codex | スコープ・安全・品質の検査 |
| 全体管理 | Cowork (Fable 5) | 優先順位、進行、記録、改善提案 |

## 作業フロー

1. Issue(open, `claude` ラベル)を起点に開始する。
2. `claude/feature-<N>-<slug>` ブランチで実装する。
3. 成果物は `scripts/` の検証スクリプトを通す。
4. Draft PR を作成し、レビューと人間承認を待つ。
5. 結果(成功・失敗・学び)を Notion と `docs/10_Self_Improvement.md` の手順で記録する。

## 成果物の置き場所

- 完成デッキ(.pptx)は原則 GitHub Release または外部ストレージへ。リポジトリには生成スクリプトと構成 Markdown を残す(再現性優先)。
- 10MB を超えるバイナリはコミットしない。
