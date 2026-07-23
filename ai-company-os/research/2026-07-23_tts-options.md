# 調査結果: AI対話ナレーションを音声化する(TTS)手段の比較

調査日: 2026年7月23日
調査目的: 「対話音声どこできくの」というオーナーからの質問を受け、`dialogue_script.md`
(テキスト台本)を実際の音声(2AIペルソナ分の声)にする方法を比較検討する。
現時点ではまだ何も導入・実装しておらず、比較検討の段階。

## 検証済み事実(出典付き)

| 事実 | 出典 |
|---|---|
| 現在このセッションにTTS(音声合成)系のMCPコネクタは接続されていない | `ListConnectors`実行結果(2026-07-23) |
| ElevenLabsのMCPコネクタ(未インストール)はClaudeの登録済みコネクタ一覧に存在するが、公開されているツール一覧(create_agent, get_agent等)は、電話・チャット向けの「会話型音声エージェント」機能が中心で、単純な「テキスト→音声ファイル」変換とは用途が異なる可能性が高い | `SearchMcpRegistry`実行結果(2026-07-23) |
| ElevenLabs社は、会話型エージェントとは別に、素のテキスト読み上げ(TTS)REST API(`api.elevenlabs.io/v1/text-to-speech`)も提供しており、こちらはナレーション・eラーニング向けの用途を明示している | [ElevenLabs公式ドキュメント](https://elevenlabs.io/docs/overview/capabilities/text-to-speech) |
| API提供があり自動化しやすいTTSサービスとして、Google Cloud TTS・Azure AI Speech・Amazon Polly・CoeFont・VOICEVOX・ElevenLabsの6社が挙げられている | [Qiita比較記事](https://qiita.com/0h-n0/items/8f78f7acd31000612d13) |
| VOICEVOX・AivisSpeechはセルフホスト(ローカル実行)可能でGPU不要、完全無料。日本語コンテンツ制作で広く使われているキャラクターボイス(ずんだもん等)を持つ | 同上 / [AI音声生成ガイド2026](https://techcreate.balubo.jp/articles/ai-voice-generation-tts-guide-2026) |
| Google Cloud TTS・Amazon Polly(Standard)は最安クラス(100万文字あたり4ドル程度)で、クレジット表記なしでの商用利用が可能 | [AIエージェントナビ](https://aiagent-navi.com/special/tts-api-pricing/) |

## 比較表

| 候補 | 提供元 | 導入条件 | ライセンス/商用利用 | 費用目安 | 期待効果 | リスク | 判定 |
|---|---|---|---|---|---|---|---|
| Google Cloud TTS | Google | Google Cloudアカウント+APIキー(課金設定必要) | クレジット表記不要、商用利用可 | 最安クラス($4/100万文字〜) | 安定運用・自動化しやすい、日本語品質良好 | 課金アカウント作成が必要(承認事項) | **trial候補** |
| VOICEVOX / AivisSpeech | 各キャラクター権利者(OSS) | セルフホスト(エンジンの起動が必要) | キャラクターごとに規約あり(概ね商用利用可・クレジット表記推奨) | 無料 | 完全無料、日本語コンテンツで実績豊富、AIキャラらしい声質 | このセッション(一時的なコンテナ)での永続ホストが難しい。キャラクター規約の個別確認が必要 | **watch**(将来、常設環境ができれば有力) |
| ElevenLabs(素のTTS API) | ElevenLabs | APIキー取得(要アカウント・課金) | 多くのプランで商用利用可(プラン規約要確認) | 中〜高(高品質だが単価は高め) | 音質・多言語対応は最高水準 | 費用がやや高い。今回見つかったMCPコネクタは会話型エージェント用で、素のTTSには別途API連携が必要 | **trial候補** |
| ElevenLabsのMCPコネクタ(会話型エージェント) | ElevenLabs | claude.ai上でコネクタ接続 | 同上 | 同上 | 導入は簡単(ワンクリック接続) | 用途が「会話型音声エージェント」であり、事前収録ナレーションの一括生成には不向きな可能性が高い | **reject(この用途には)** |
| Amazon Polly / Azure AI Speech | AWS / Microsoft | クラウドアカウント+APIキー | クレジット表記不要、商用利用可 | 最安クラス | 安定運用、実績豊富 | Google Cloud TTSと機能的に大差なく、二重導入は不要 | **watch** |

## 推奨(合理的推測を含む)

- (推奨)自動化パイプラインへの組み込みやすさ・コストの低さから、**Google Cloud TTS**
  を最有力候補とする。ナビAI役とリサーチAI役にそれぞれ異なる日本語ニューラルボイスを
  割り当てれば、2ペルソナの声を作れる
- (推奨)無料・日本語コンテンツとの相性を重視するなら**VOICEVOX**も有力だが、この
  セッションはコンテナが一時的なため、エンジンを常設できる環境(オーナー側のPC/サーバー等)
  が必要になる
- いずれの場合も、APIキーの取得・課金設定はオーナー自身の判断・操作が必要(AGENTS.mdの
  「新規外部連携は人間承認必須」ルールに基づく)。取得後は`.env.local`に保存し、
  リポジトリにはコミットしない

## 不明点

- ElevenLabsの素のTTS APIとMCPコネクタの関係(コネクタ経由で素のTTSも呼び出せるかは
  今回のツール一覧からは確認できていない)
- 実際の1テーマ(30スライド、対話原稿約2000〜3000字)あたりの音声化コストの具体的な試算
  (プロバイダ確定後に別途試算が必要)
- VOICEVOXキャラクターごとの利用規約の詳細(候補に絞った時点で個別確認が必要)

## 出典一覧

- Qiita比較記事: https://qiita.com/0h-n0/items/8f78f7acd31000612d13
- AI音声生成ガイド2026: https://techcreate.balubo.jp/articles/ai-voice-generation-tts-guide-2026
- AIエージェントナビ(料金比較): https://aiagent-navi.com/special/tts-api-pricing/
- ElevenLabs公式ドキュメント: https://elevenlabs.io/docs/overview/capabilities/text-to-speech
