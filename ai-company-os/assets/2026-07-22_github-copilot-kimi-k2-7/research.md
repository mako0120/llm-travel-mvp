# 調査結果: GitHub Copilotに初のオープンウェイトモデル「Kimi K2.7 Code」

調査日: 2026年7月22日
選定モード: モードB(バイラル優先) — 対象ジャンル「AI/エージェント系」枠(70%)
バイラル性の根拠: GitHub公式Changelog(一次情報)での発表に加え、Windows Forum・
Enterprise DNA・TechTimes・AlphaSignal・ChatForest等、性質の異なる複数の独立系
メディアが2026年7月1〜2日の短期間に一斉に報道した。

## 前回テーマとの違い(重複確認)

定期実行9本目(`assets/2026-07-21_qwen-kimi-model-race/`)は、Alibaba「Qwen 3.8」と
Moonshot「Kimi K3」のベンチマーク上の競争を扱った(出典の確信度は中、一次情報未確認)。
本テーマは、Moonshot社の別モデル「Kimi K2.7 Code」がGitHub Copilotに正式統合された
という、GitHub公式Changelogに基づく別の出来事であり、内容の重複はない。

## 検証済み事実(出典付き、GitHub公式Changelogが一次情報)

| 事実 | 出典 | 確認日 |
|---|---|---|
| 2026年7月1日、Moonshot AI(北京拠点の研究機関)が開発したオープンウェイトモデル「Kimi K2.7 Code」が、GitHub Copilotのモデル選択機能で選べる「初のオープンウェイトモデル」として一般提供(GA)開始 | [GitHub公式Changelog](https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot/) | 2026-07-22 |
| Copilot Pro・Pro+・Maxプランへの提供が始まり、Visual Studio Codeのモデル選択機能から選択可能。Business・Enterprise向けは今後数週間で展開予定 | 同上 / [Windows Forum](https://windowsforum.com/threads/github-copilot-adds-kimi-k2-7-code-open-weight-model-picker-for-windows-devs.433110/) | 2026-07-22 |
| 料金は入力100万トークンあたり0.95ドル | [TechTimes](https://www.techtimes.com/articles/319556/20260702/open-weight-ai-enters-github-copilot-kimi-k27-code-costs-less-audits-differently.htm) | 2026-07-22 |
| アーキテクチャはMixture-of-Experts(MoE)方式で、総パラメータ数1兆・トークンごとの活性化パラメータ数320億、コンテキスト長は256K | [Enterprise DNA](https://enterprisedna.co/resources/news/kimi-k2-7-github-copilot-open-weight-enterprise-developers-2026/) | 2026-07-22 |
| Kimi K2.7 CodeはMicrosoft Azure上でGitHubがホスティングしている | [ChatForest](https://chatforest.com/builders-log/kimi-k2-7-code-github-copilot-ga-five-lab-roster-july-2026-builder-guide/) | 2026-07-22 |
| Moonshot AIは、GitHubが一般提供を開始するわずか19日前に、モデルの重み(ウェイト)をHugging Face上で公開していた | 同上 | 2026-07-22 |
| 今回の追加により、Copilotのモデル選択肢はOpenAI・Anthropic・Google・Microsoft・Moonshot AIの「5ラボ体制」となった | [AlphaSignal](https://alphasignal.ai/news/github-drops-moonshot-ai-s-open-weight-kimi-k2-7-into-copilot-s-model-picker) | 2026-07-22 |

## 合理的推測(事実と区別)

- (推測)中国発のオープンウェイトモデルが、GitHub Copilotのような主要開発者向け
  ツールに公式採用されたことは、オープンウェイトモデルの実務での信頼性向上を
  示す一例と考えられるが、これは各報道機関が明示的に分析している内容ではなく、
  一般的な業界文脈からの解釈である。

## 不明点

- GitHub公式Changelogの本文(直接アクセスできず、検索エンジンの要約・引用経由での確認)
- 実際の開発者コミュニティでの採用率・利用実績
- 出力トークン側の料金(検索結果では入力側の料金のみ確認できた)
- Business・Enterprise向け展開の正確な時期

## 出典一覧

- GitHub公式Changelog(一次情報): https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot/
- Windows Forum: https://windowsforum.com/threads/github-copilot-adds-kimi-k2-7-code-open-weight-model-picker-for-windows-devs.433110/
- Enterprise DNA: https://enterprisedna.co/resources/news/kimi-k2-7-github-copilot-open-weight-enterprise-developers-2026/
- TechTimes: https://www.techtimes.com/articles/319556/20260702/open-weight-ai-enters-github-copilot-kimi-k27-code-costs-less-audits-differently.htm
- ChatForest: https://chatforest.com/builders-log/kimi-k2-7-code-github-copilot-ga-five-lab-roster-july-2026-builder-guide/
- AlphaSignal: https://alphasignal.ai/news/github-drops-moonshot-ai-s-open-weight-kimi-k2-7-into-copilot-s-model-picker
