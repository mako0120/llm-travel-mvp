# リサーチ: Google、会話しながら考える音声AI「Gemini 3.8 Live」「Extended Thinking」を発表

## 0. 鮮度についての正直な開示

- 着手日: 2026年9月17日(木・JST)。本件は2026年9月15日に発表・提供開始されており、
  着手日から2日前の情報である(基本方針の「2日以内」を満たす)

## 1. 確定している事実(出典付き)

- Googleは2026年9月15日、リアルタイム音声対話モデル「Gemini 3.8 Live」と
  「Gemini 3.8 Live Extended Thinking」を発表した(Unite.AI、MarkTechPost)
- 「Gemini 3.8 Live」は視覚情報をほぼリアルタイムで処理でき、ユーザーが見せたものを
  会話に反映できるほか、会話を止めずにバックグラウンドでツール呼び出しやAPIリクエストを
  実行できる(Unite.AI)
- 「Gemini 3.8 Live Extended Thinking」は、考えながら同時に話すことができ、
  バックグラウンドの処理状況を「ちょっと確認しますね」のような言葉で伝えながら
  作業を進める(Unite.AI)
- 97言語に対応し、会話の途中でも言語を自動的に切り替えられる(tech-noisy.com、
  BigGo Finance)
- 開発者向けにはGemini APIとGoogle AI Studioで利用可能。企業向けにはGemini
  Enterpriseでプライベートプレビュー中。「Gemini 3.8 Live」は検索Liveで一般ユーザーも
  利用でき、「Extended Thinking」はGemini Liveで利用できる(Unite.AI)

## 2. 数字の混同防止チェック(本テーマ固有)

- 「Gemini 3.8 Live」(視覚処理・バックグラウンドツール実行)と「Gemini 3.8 Live
  Extended Thinking」(考えながら話す)は別モデルであり、提供範囲も異なる
  (前者は検索Liveで一般提供、後者はGemini Liveで提供)ことを混同しない
- 「対応言語数(97言語)」と「開発者向け提供範囲(Gemini API・AI Studio)」を
  混同しない

## 3. 合理的推測(事実と区別)

- (推測)「考えながら話す」機能は、従来の音声AIが処理中に無言になってしまう
  不自然さを解消する狙いがあると考えられるが、これはGoogleが明示的に述べた
  開発意図ではなく、機能説明からの推測である

## 4. 不明(確認できなかったこと)

- 日本語での「Extended Thinking」の具体的な応答品質・自然さ
- Gemini Enterpriseでのプライベートプレビューの正式提供時期
- 無料版と有料版での機能差の詳細

## 5. 重複チェック(既存テーマとの区別、必須)

- `ai-company-os/assets/`配下を`grep -ril -i "Gemini 3.8"`で検索した結果、
  既存テーマはヒットせず、重複は確認されなかった
- 2026-09-13に扱った「Google Geminiデスクトップアプリ」(会話記録上確認)とは
  別機能(音声対話モデル vs デスクトップアプリ)であり、重複ではない

## 6. 判定

**adopt** — Unite.AI・MarkTechPostを含む複数の独立した媒体で確認できた。着手日から
2日前という高い鮮度も確保しており、「話しながら止まらないAI音声アシスタント」という
視聴者に直接関係する具体的な有益性を持つ。

## 出典一覧

- Unite.AI: Google Launches Gemini 3.8 Live and Extended Thinking Voice Models
- MarkTechPost: Google Releases Gemini 3.8 Live and 3.8 Live Extended Thinking for Production Grade Voice Agents
- tech-noisy.com: Gemini 3.8 Live - Extended Thinkingとの違い・97言語対応・提供範囲を整理
