# 14. YouTube Thumbnail(サムネイル生成)

## 背景

2026-07-24、オーナー指示により追加した第4の標準成果物。「ネットで伸びている
サムネイルを徹底的に分析し、その知見を踏まえたサムネイルを自動生成すること」が
指示内容であり、その調査結果は
`ai-company-os/research/2026-07-24_youtube-thumbnail-best-practices.md` にまとめている。

## いつ使うか

**2026-07-24〜、以後のテーマ制作(定期実行含む)では毎回、確認を挟まず自動で
サムネイルを生成する。** PowerPoint(方式A)・AI対話ナレーション動画と並行して
使う独立した成果物であり、`youtube_assets.md` の一部として扱う。

## 設計原則(調査に基づく)

- **1メッセージ・1秒で理解できる構成**: フック文言は1つ、最大2行。デッキの
  `title`スライドの問いかけをさらに凝縮した、13〜20文字程度の短い文言にする
- **顔は使わない**: 実在人物の写真・肖像は使用しない標準方針(`AGENTS.md`)を
  維持する。表情による訴求の代わりに、太字タイポグラフィ + 高コントラスト配色 +
  抽象図形アイコン(実在ロゴ・商標は不使用)で注目を引く
- **高コントラスト配色**: `build_deck.py`の`PALETTE_PRESETS`を再利用し、
  背景色に対して文字は補色に近い高コントラストな色にする。文字には縁取り
  (stroke)を付けて可読性を確保する
- **数字を活かす**: デッキの`big_stat`スライドで扱った象徴的な数字があれば、
  角丸バッジとしてサムネイルに配置する(例:「$2→$30」)
- **タイトルとの役割分担**: サムネイルはフック(好奇心のギャップ)のみを担い、
  YouTubeタイトル案(`youtube_assets.md`)が文脈を補う。内容を書き込みすぎない
- **誇張・釣り化の回避**: 動画本編の内容と乖離した誇張・扇動的な文言は使わない
  (「サムネイル・コンテンツ整合性のパラドックス」を踏まえた既存方針を維持)
- **可読性チェック**: 168×94pxに縮小してもフック文言が判読できることを、
  `build_thumbnail.py`の自己診断で毎回確認する

## 生成パイプライン

```text
thumbnail_spec.json (hook / stat_badge / tag / palette_preset)
        │  build_thumbnail.py
        ▼
thumbnail.png (1280x720)
```

- `python scripts/build_thumbnail.py <theme_dir>/thumbnail_spec.json <theme_dir>/thumbnail.png`
- `python scripts/build_thumbnail.py --self-test` で健全性を確認できる(168x94への
  縮小保存も自動で行う)
- `thumbnail_brief.md`(`templates/thumbnail_brief_template.md`準拠)に、フック
  文言の設計根拠・検品チェックを記録する

## 成果物の配置

`ai-company-os/assets/<日付>_<slug>/` 配下に以下を追加する:

- `thumbnail_spec.json`
- `thumbnail.png`
- `thumbnail_brief.md`

`thumbnail.png`は静的な生成画像(数百KB程度)のため、`deck.pptx`と同様に
リポジトリにコミットする(動画ファイルのような大容量バイナリではないため)。

## 承認境界

サムネイル生成はPowerPoint・ナレーション動画の生成と同じ「制作」工程に含まれる
ため、`AGENTS.md`の承認境界(mainマージ・公開投稿・課金・新規外部連携は
人間承認が必要)をそのまま適用する。サムネイル画像の生成・コミット・Draft PR
作成までは自動で行ってよいが、YouTubeへの実際のアップロード・公開は行わない。
