# 調査結果: Intuit、AIエージェントのアーキテクチャを4か月で2度作り直した理由

調査日: 2026年7月22日
選定モード: モードB(バイラル優先) — 対象ジャンル「AI/エージェント系」枠(70%)
バイラル性の根拠: VentureBeat(信頼できる技術専門メディア)がVB Transform 2026という
業界カンファレンスでの実際の登壇内容を一次取材し、Intuit AI担当VPの実名・直接引用付きで
報道。同記事がCryptopond・Progressive Robot・dataworldbank等、複数サイトに転載・
言及され、業界内で広く共有された。

## 検証済み事実(出典付き、VP実名の直接引用あり)

| 事実 | 出典 | 確認日 |
|---|---|---|
| Intuit(会計・税務ソフト大手)のAI担当VPであるNhung Ho氏が、VB Transform 2026(業界カンファレンス)の登壇で、自社のAIエージェント・アーキテクチャを約4か月の間に2度作り直したと説明 | [VentureBeat](https://venturebeat.com/orchestration/intuit-scrapped-its-own-ai-agent-architecture-twice-in-four-months-at-vb-transform-2026-its-ai-vp-called-that-the-fast-path) | 2026-07-22 |
| 変遷の内容: 最初は「専門特化型エージェントの集合」→次に「中央のオーケストレーション層」へ移行→そのオーケストレーション層自体が複雑さで機能不全に陥り、最終的に「スキルとツールベースのシステム」へ移行した | 同上 | 2026-07-22 |
| Ho氏の発言引用:「10個のエージェントがあり、それらが互いにやり取り(パス)する場合、パスが発生するたびにエラーが積み重なっていく("If you have 10 agents and they all are passing to each other, every time that pass happens, error compounds.")」 | 同上 | 2026-07-22 |
| Ho氏の発言引用(最終アーキテクチャについて):「大きなタスクをこなす大規模エージェントによるマルチエージェント方式から、ワークフロー・スキル・ツールを基礎レベルまで完全に組み込む方式へ移行した("We went from a multi-agent system where we had large agents that did a lot to fully incorporating workflows, skills and tools down to the base level.")」 | 同上 | 2026-07-22 |
| 2回目の全面的な作り直しには60日を要したが、最初の動作版はそれより早く20日未満で完成した | 同上 | 2026-07-22 |
| オーケストレーション方式の問題点: エージェント間で自然言語による結果の受け渡し(ハンドオフ)を行うたびに、次のエージェントが必要とする文脈情報が失われ、下流のエージェントは上流の推論過程を推測せざるを得ず、この推測の精度がホップの回数に応じて劣化した | 同上 | 2026-07-22 |
| 最終的なアーキテクチャでは、AIと人間の専門家をワークフローに直接組み込む形をとった | 同上 | 2026-07-22 |
| Intuit社はこれらの作り直しを「失敗」ではなく、信頼性の高いエンタープライズAIシステムを構築するための「最速の道」であったと位置づけている | 同上 | 2026-07-22 |

## 合理的推測(事実と区別)

- (推測)複数エージェントを自然言語でつなぐオーケストレーション方式が抱える
  「エラーの積み重ね」問題は、Intuit固有の課題ではなく、同様のマルチエージェント
  構成を採用する他企業にも共通しうる一般的な課題と考えられるが、これはHo氏の
  発言から一般化した推測であり、他社事例で裏付けられたものではない。

## 不明点

- VentureBeat記事本文への直接アクセスができず(403エラー)、検索エンジンが提示する
  要約・引用経由での確認にとどまる
- 「スキルとツールベースのシステム」の技術的な実装詳細(どのフレームワーク・
  ツールを使っているか等)
- この再設計によるコスト削減額・処理速度改善など、定量的な業務指標
- VB Transform 2026の正確な開催日程

## 出典一覧

- VentureBeat(一次取材、Nhung Ho氏実名インタビュー): https://venturebeat.com/orchestration/intuit-scrapped-its-own-ai-agent-architecture-twice-in-four-months-at-vb-transform-2026-its-ai-vp-called-that-the-fast-path
- VentureBeat(関連記事、事前予告): https://venturebeat.com/orchestration/intuit-will-show-off-how-it-rebuilt-its-ai-infrastructure-to-support-fast-and-complex-tasks-at-vb-transform-2026
- Cryptopond(転載): https://cryptopond.com/intuit-scrapped-its-own-ai-agent-architecture-twice-in-four-months-at-vb-transform-2026-its-ai-vp-called-that-the-fast-path/
- Progressive Robot(言及): https://www.progressiverobot.com/2026/07/17/intuit-ai-agent-architecture/
