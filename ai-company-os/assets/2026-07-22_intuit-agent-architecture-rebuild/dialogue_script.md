# 10個のエージェントをつなぐと、エラーは掛け算で増える(Intuit事例) — AI対話ナレーション原稿(起承転結)

<!-- generate_dialogue_script.py により dialogue_spec.json から自動生成 -->

**合計目安時間: 約2分**(4幕、350字/分換算)

## 登場AIペルソナ

- **ナビAI**: 進行役。視聴者目線で疑問を投げかけ、話を整理する
- **リサーチAI**: 出典付きの事実・引用を解説する

## 起(導入) — 導入
*目安 0.5分*

**ナビAI**: 今日はちょっと面白い話があるんだけど、大手企業がAIエージェントのアーキテクチャを4か月で2回も作り直したらしいんだよね。
**リサーチAI**: はい、会計・税務ソフト大手のIntuitの話です。VB Transform 2026というカンファレンスで、AI担当VPのNhung Ho氏が本人の口から説明しています。 (出典: https://venturebeat.com/orchestration/intuit-scrapped-its-own-ai-agent-architecture-twice-in-four-months-at-vb-transform-2026-its-ai-vp-called-that-the-fast-path)
**ナビAI**: 4か月で2回って、普通に考えるとかなり大変そうだけど。

## 承(展開) — 展開
*目安 0.6分*

**リサーチAI**: 変遷はこうです。最初は専門特化型エージェントの集合、次に中央のオーケストレーション層、そして最終的にスキルとツールベースのシステムへ移行しました。 (出典: https://venturebeat.com/orchestration/intuit-scrapped-its-own-ai-agent-architecture-twice-in-four-months-at-vb-transform-2026-its-ai-vp-called-that-the-fast-path)
**ナビAI**: なんでオーケストレーション層がダメだったの？
**リサーチAI**: Ho氏本人の言葉を借りると、「10個のエージェントが互いにやり取りする場合、やり取りが発生するたびにエラーが積み重なっていく」んです。自然言語でのハンドオフのたびに文脈が失われる、という問題でした。 (出典: https://venturebeat.com/orchestration/intuit-scrapped-its-own-ai-agent-architecture-twice-in-four-months-at-vb-transform-2026-its-ai-vp-called-that-the-fast-path)
**ナビAI**: エラーが掛け算みたいに増えていくってことか。

## 転(転換) — 転換
*目安 0.5分*

**ナビAI**: でもさ、この作り直し、コストや処理速度がどれだけ改善したかは分かってるの？
**リサーチAI**: そこは正直に「不明」です。2回目の全面的な作り直しには60日を要し、最初の動作版は20日未満で完成した、という開発スピードの数字は分かっていますが、コスト削減額や処理速度改善といった定量的な業務指標は今回の取材では確認できていません。 (出典: https://venturebeat.com/orchestration/intuit-scrapped-its-own-ai-agent-architecture-twice-in-four-months-at-vb-transform-2026-its-ai-vp-called-that-the-fast-path)
**ナビAI**: 1社の事例でもあるし、他の企業にそのまま当てはまるとは限らないよね。

## 結(結論) — 結論
*目安 0.3分*

**リサーチAI**: その通りです。それでもIntuitは、この2度の作り直しを「失敗」ではなく、信頼性の高いエンタープライズAIを作るための「最速の道」だったと位置づけています。 (出典: https://venturebeat.com/orchestration/intuit-scrapped-its-own-ai-agent-architecture-twice-in-four-months-at-vb-transform-2026-its-ai-vp-called-that-the-fast-path)
**ナビAI**: 自社のエージェント設計を見直すきっかけになりそうな話だったね。今日はここまで。

## 出典一覧

- https://venturebeat.com/orchestration/intuit-scrapped-its-own-ai-agent-architecture-twice-in-four-months-at-vb-transform-2026-its-ai-vp-called-that-the-fast-path
- https://venturebeat.com/orchestration/intuit-will-show-off-how-it-rebuilt-its-ai-infrastructure-to-support-fast-and-complex-tasks-at-vb-transform-2026
