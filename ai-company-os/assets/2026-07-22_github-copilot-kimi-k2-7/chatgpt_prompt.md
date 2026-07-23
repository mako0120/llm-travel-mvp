# ChatGPT投入用プロンプト

<!-- コードブロックをそのままChatGPTに貼り付けて使う -->

```
あなたはプロのプレゼンテーションデザイナー兼リサーチャーです。以下の情報をもとに、
日本語のビジネス向けPowerPointプレゼンテーションを作成してください。

# テーマ
「GitHub Copilotに初のオープンウェイトモデル。Kimi K2.7 Codeが変える開発者の選択肢」
— OpenAI・Anthropic・Google・Microsoft・Moonshot AIの「5ラボ体制」が意味すること

# 想定視聴者
20〜45歳。ソフトウェアエンジニア、開発チームのマネージャー、AI開発ツールの
選定に関わるビジネスパーソン。専門用語は初出時に短く説明する。

# 必ず使う事実(すべて出典付き。この範囲を超えて数字を創作しないでください)

- 2026年7月1日、Moonshot AI(北京拠点の研究機関)が開発したオープンウェイトモデル
  「Kimi K2.7 Code」が、GitHub Copilotのモデル選択機能で選べる「初のオープンウェイト
  モデル」として一般提供(GA)開始(出典: GitHub公式Changelog
  https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot/ )
- Copilot Pro・Pro+・Maxプランへの提供が始まり、Visual Studio Codeのモデル選択機能
  から選択可能。Business・Enterprise向けは今後数週間で展開予定(出典: 同上)
- 料金は入力100万トークンあたり0.95ドル(出典: TechTimes
  https://www.techtimes.com/articles/319556/20260702/open-weight-ai-enters-github-copilot-kimi-k27-code-costs-less-audits-differently.htm )
- アーキテクチャはMixture-of-Experts(MoE)方式で、総パラメータ数1兆・トークンごとの
  活性化パラメータ数320億、コンテキスト長は256K(出典: Enterprise DNA
  https://enterprisedna.co/resources/news/kimi-k2-7-github-copilot-open-weight-enterprise-developers-2026/ )
- Kimi K2.7 CodeはMicrosoft Azure上でGitHubがホスティングしている(出典: ChatForest
  https://chatforest.com/builders-log/kimi-k2-7-code-github-copilot-ga-five-lab-roster-july-2026-builder-guide/ )
- Moonshot AIは、GitHubが一般提供を開始するわずか19日前に、モデルの重み(ウェイト)を
  Hugging Face上で公開していた(出典: 同上)
- 今回の追加により、Copilotのモデル選択肢はOpenAI・Anthropic・Google・Microsoft・
  Moonshot AIの「5ラボ体制」となった(出典: AlphaSignal
  https://alphasignal.ai/news/github-drops-moonshot-ai-s-open-weight-kimi-k2-7-into-copilot-s-model-picker )

# 不明な点(正直に「不明」として扱ってください。推測で埋めないでください)

- 実際の開発者コミュニティでの採用率・利用実績
- 出力トークン側の料金(入力側の料金のみ確認できている)
- Business・Enterprise向け展開の正確な時期
- GitHub公式Changelog本文(直接アクセスできず、検索エンジンの要約・引用経由での確認)

# スライド構成(目安18〜22枚。内容に応じて増減して構いません)

1. 表紙
2. 今回の結論(Copilot初のオープンウェイトモデル、5ラボ体制へ、の2点)
3. この動画/資料で得られること
4. なぜ今このテーマを扱うのか
5. 「オープンウェイトモデル」とは何か(基礎知識、クローズドモデルとの違い)
6. Kimi K2.7 Codeとは・Moonshot AIとは(基礎知識)
7. GitHub Copilotへの統合を数字で見る(2026年7月1日GA、19日というスピード)
8. 技術仕様を数字で見る(1兆パラメータ、320億活性化、256Kコンテキスト)
9. 料金を数字で見る(入力100万トークンあたり0.95ドル)
10. どのプランで使えるのか(Pro/Pro+/Max、Business/Enterpriseは今後)
11. 5ラボ体制の全体像(OpenAI・Anthropic・Google・Microsoft・Moonshot AI)
12. なぜオープンウェイトモデルの採用が話題になったのか
13. 開発チームにとっての示唆(モデル選択の幅が広がることの意味、一般論として)
14. 注意点(不明点として明記した項目を含め、正直に伝える)
15. 反対意見・弱点(採用実績や出力側料金など、まだ分からないことが多い点)
16. まとめ・次のアクション
17. 出典一覧

# デザイン・品質ルール(必ず守ってください)

- 16:9のスライドサイズ
- 1スライド1メッセージ、本文は最大5ブレット、1ブレット2行以内
- 数字を扱うスライドには出典を必ず明記する
- 全スライドにスピーカーノート(実際に話す内容の下書き、1枚100〜300字程度)を付ける
- 誇張表現は使わない
- 実在企業のロゴ・商標画像は使用しない

# 出力形式

Code Interpreter(Pythonの実行環境)が使える場合は、python-pptxライブラリを使って
実際に .pptx ファイルを生成し、ダウンロードリンクを提示してください。
使えない場合は、スライドごとに「見出し/本文/図解の指示/出典/スピーカーノート」を
テキストで出力してください。

最後に、上記「必ず使う事実」以外の数字を追加していないか、自己チェックした結果を
簡潔に報告してください。
```

## このプロンプトの元データ

`research.md`(同ディレクトリ)を参照。
