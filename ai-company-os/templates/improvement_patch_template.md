# Improvement Patch テンプレート

<!-- docs/15_PPT_Handoff.md 準拠。chatgpt_review.json の指摘を deck_spec.json に
     反映した際、「どこを・なぜ・どう変えたか」を記録する。
     assets/<日付>_<slug>/improvement_patch.md として保存する。
     Claude Code が chatgpt_review.json を精査した後に作成する(ChatGPT Work
     本人はこのファイルを直接書かない)。 -->

## 対応元レビュー

- `chatgpt_review.json` の `review_date`:
- `overall_verdict`:

## 反映した変更

<!-- chatgpt_review.json の issues 1件につき1エントリ。critical は必ず記載する -->

### スライド N: `<category>`(`critical` / `minor`)

- 指摘内容:
- `deck_spec.json` 上の変更箇所(スライド配列のインデックス・フィールド名):
- 変更前:
- 変更後:
- 対応状況: 反映済み / 対応見送り(理由を明記)

## 反映しなかった指摘とその理由

<!-- 対応見送りにした指摘がある場合のみ。critical を見送る場合は理由を具体的に書く -->

## 再生成後の検証

- [ ] `python scripts/verify_pptx.py deck.chatgpt-reviewed.pptx` が PASS した
- [ ] 上記「反映した変更」と `deck_spec.json` の実際の差分が一致している
- [ ] critical 指摘がすべて「反映済み」または理由付きで見送りとして記録されている
