#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""publish_to_social.py — 完成済みテーマ動画をTikTok/Instagramへ自動投稿する

前提: public/videos/<テーマID>.mp4 が publish_theme.py によって既に作られていること。
このスクリプト単体では動画を作らない(publish_theme.pyの後段としてのみ動作する)。

認証情報は環境変数(.env.local、コミット禁止)からのみ読み込む。リポジトリ・ログ・
コミットメッセージに認証情報を書き込むことは絶対にしない。

必要な環境変数:
  TikTok (Content Posting API):
    TIKTOK_CLIENT_KEY
    TIKTOK_CLIENT_SECRET
    TIKTOK_ACCESS_TOKEN       # 投稿権限(video.publish)を持つロングライブトークン
    TIKTOK_OPEN_ID            # 投稿先アカウントのopen_id

  Instagram (Graph API, Reels):
    META_APP_ID
    META_APP_SECRET
    META_ACCESS_TOKEN         # instagram_content_publish 権限を持つロングライブトークン
    INSTAGRAM_BUSINESS_ACCOUNT_ID

いずれのプラットフォームも、対応する環境変数が一つでも欠けていればそのプラットフォームへの
投稿をスキップし、理由を明示して終了する(未設定のまま失敗させたり、空の投稿をしたりしない)。

動画は public/videos/<テーマID>.mp4 のように、インターネットから直接HTTPSで到達できる
URLとして提供されている必要がある(TikTok/Instagramの両APIとも、動画URLを渡す方式か
アップロード方式のいずれかを要求するため、本スクリプトはURL指定方式を使う)。
--video-url でこの動画の公開URLを明示的に渡すこと。

使い方:
  python scripts/publish_to_social.py <テーマディレクトリ名> --video-url https://.../videos/xxx.mp4
      # TikTok・Instagram両方に投稿を試みる(認証情報が揃っている方のみ実行)

  python scripts/publish_to_social.py <テーマディレクトリ名> --video-url https://... --platform tiktok
      # TikTokのみ

  python scripts/publish_to_social.py <テーマディレクトリ名> --video-url https://... --dry-run
      # 実際には投稿せず、送信予定のリクエスト内容とキャプションのみ表示する

  python scripts/publish_to_social.py --self-test
      # 認証情報の読み込みロジック・キャプション生成のみを、ネットワークアクセスなしで確認する

現状(2026年時点)、このリポジトリにはTikTok/InstagramのAPI認証情報が設定されていない。
そのため通常実行しても両プラットフォームともスキップされる。認証情報が用意され次第、
.env.local に上記の環境変数を追加するだけで動作するようにしてある。
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parents[1]
ASSETS_DIR = REPO_ROOT / "ai-company-os" / "assets"

TIKTOK_POST_INIT_URL = "https://open.tiktokapis.com/v2/post/publish/video/init/"
IG_GRAPH_API_VERSION = "v21.0"
IG_GRAPH_BASE_URL = f"https://graph.facebook.com/{IG_GRAPH_API_VERSION}"

# 標準の免責表現。生成AIによる要約であることを明示し、確認できなかった事項があることを
# 前提にした投稿本文にする(ai-company-os/docs/01_Core_Rules.mdの正直さルールに準拠)。
CAPTION_FOOTER = "\n\n※AI研究家ミライ(AI Company OS運営)が構成・制作。出典付きで事実のみを紹介しています。"


class MissingCredentials(Exception):
    """特定プラットフォームの認証情報が環境変数に無い場合に送出する。"""


def read_theme_title(theme_dir: Path) -> str:
    spec_path = theme_dir / "deck_spec.json"
    if not spec_path.is_file():
        return theme_dir.name
    data = json.loads(spec_path.read_text(encoding="utf-8"))
    return data.get("meta", {}).get("title", theme_dir.name)


def build_caption(title: str, max_len: int) -> str:
    footer = CAPTION_FOOTER
    budget = max_len - len(footer)
    if budget < 0:
        return footer[:max_len]
    trimmed = title if len(title) <= budget else title[: max(0, budget - 1)] + "…"
    return trimmed + footer


def tiktok_credentials() -> dict[str, str]:
    required = ["TIKTOK_CLIENT_KEY", "TIKTOK_CLIENT_SECRET", "TIKTOK_ACCESS_TOKEN", "TIKTOK_OPEN_ID"]
    missing = [name for name in required if not os.environ.get(name)]
    if missing:
        raise MissingCredentials(f"TikTok: 環境変数が未設定のためスキップ({', '.join(missing)})")
    return {name: os.environ[name] for name in required}


def instagram_credentials() -> dict[str, str]:
    required = ["META_APP_ID", "META_APP_SECRET", "META_ACCESS_TOKEN", "INSTAGRAM_BUSINESS_ACCOUNT_ID"]
    missing = [name for name in required if not os.environ.get(name)]
    if missing:
        raise MissingCredentials(f"Instagram: 環境変数が未設定のためスキップ({', '.join(missing)})")
    return {name: os.environ[name] for name in required}


def _post_json(url: str, payload: dict, headers: dict) -> dict:
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers={**headers, "Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {detail}") from exc


def publish_to_tiktok(video_url: str, caption: str, dry_run: bool) -> str:
    """TikTok Content Posting APIの「PULL_FROM_URL」方式で動画を投稿する。

    投稿は下書き審査(TikTokアプリ内でのレビュー)を経て公開されるアカウント設定の場合、
    このAPI呼び出し自体は「投稿ジョブの登録」であり、即時の一般公開を保証しない点に注意。
    (これはTikTok側のアプリ審査状況・アカウント設定に依存する仕様であり、本スクリプトの
    挙動を制御する範囲外)
    """
    creds = tiktok_credentials()
    caption = build_caption(caption, max_len=2200)

    payload = {
        "post_info": {
            "title": caption,
            "privacy_level": "SELF_ONLY",  # 認証情報が本物になるまでは自分のみ閲覧可のまま変更しない
            "disable_duet": False,
            "disable_comment": False,
            "disable_stitch": False,
        },
        "source_info": {
            "source": "PULL_FROM_URL",
            "video_url": video_url,
        },
    }
    headers = {"Authorization": f"Bearer {creds['TIKTOK_ACCESS_TOKEN']}"}

    if dry_run:
        print("[dry-run] TikTok へ送信予定のリクエスト:")
        print(json.dumps({"url": TIKTOK_POST_INIT_URL, "payload": payload}, ensure_ascii=False, indent=2))
        return "(dry-run: 未送信)"

    result = _post_json(TIKTOK_POST_INIT_URL, payload, headers)
    publish_id = result.get("data", {}).get("publish_id")
    if not publish_id:
        raise RuntimeError(f"TikTok API応答にpublish_idが含まれない: {result}")
    return publish_id


def publish_to_instagram(video_url: str, caption: str, dry_run: bool) -> str:
    """Instagram Graph APIでReelsコンテナを作成し公開する(2段階: create → publish)。"""
    creds = instagram_credentials()
    caption = build_caption(caption, max_len=2200)
    ig_user_id = creds["INSTAGRAM_BUSINESS_ACCOUNT_ID"]
    token = creds["META_ACCESS_TOKEN"]

    create_url = f"{IG_GRAPH_BASE_URL}/{ig_user_id}/media"
    create_payload = {
        "media_type": "REELS",
        "video_url": video_url,
        "caption": caption,
        "access_token": token,
    }

    if dry_run:
        print("[dry-run] Instagram へ送信予定のリクエスト(コンテナ作成):")
        print(json.dumps({"url": create_url, "payload": create_payload}, ensure_ascii=False, indent=2))
        return "(dry-run: 未送信)"

    created = _post_json(create_url, create_payload, headers={})
    container_id = created.get("id")
    if not container_id:
        raise RuntimeError(f"Instagramコンテナ作成に失敗: {created}")

    publish_url = f"{IG_GRAPH_BASE_URL}/{ig_user_id}/media_publish"
    published = _post_json(publish_url, {"creation_id": container_id, "access_token": token}, headers={})
    media_id = published.get("id")
    if not media_id:
        raise RuntimeError(f"Instagram公開に失敗: {published}")
    return media_id


def self_test() -> int:
    """ネットワークアクセスなしで、認証情報チェックとキャプション生成だけを確認する。"""
    ok = True

    caption = build_caption("GPT-6 Astraは「世界最高の知性」なのか徹底解説する非常に長いタイトル" * 3, max_len=100)
    if len(caption) > 100 or not caption.endswith(CAPTION_FOOTER.strip().split("\n")[-1]):
        print("NG: build_caption が長さ制限またはフッター付与を満たしていない")
        ok = False
    else:
        print("OK: build_caption は長さ制限内でフッターを付与する")

    for name, fn in (("tiktok_credentials", tiktok_credentials), ("instagram_credentials", instagram_credentials)):
        try:
            fn()
            print(f"NG: {name} が例外を送出しなかった(環境変数が意図せず設定されている可能性)")
            ok = False
        except MissingCredentials as exc:
            print(f"OK: {name} は未設定を正しく検出する ({exc})")

    return 0 if ok else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("theme", nargs="?", help="ai-company-os/assets/ 配下のテーマディレクトリ名")
    parser.add_argument("--video-url", help="public/videos/配下の動画を指すHTTPS URL(必須、--self-test時は不要)")
    parser.add_argument("--platform", choices=["tiktok", "instagram", "both"], default="both")
    parser.add_argument("--dry-run", action="store_true", help="実際には投稿せず、送信内容だけを表示する")
    parser.add_argument("--self-test", action="store_true", help="ロジックのみ確認(ネットワークアクセスなし)")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    if not args.theme or not args.video_url:
        parser.error("theme と --video-url は --self-test 以外では必須")

    theme_dir = ASSETS_DIR / args.theme
    if not theme_dir.is_dir():
        parser.error(f"テーマディレクトリが見つからない: {theme_dir}")

    title = read_theme_title(theme_dir)
    print(f"テーマ: {title}")
    print(f"動画URL: {args.video_url}")
    if args.dry_run:
        print("(--dry-run モード: 実際には投稿しません)\n")

    exit_code = 0

    if args.platform in ("tiktok", "both"):
        try:
            result = publish_to_tiktok(args.video_url, title, args.dry_run)
            print(f"TikTok: {result}")
        except MissingCredentials as exc:
            print(str(exc))
        except Exception as exc:  # noqa: BLE001 — CLIとして失敗理由をそのまま出す
            print(f"TikTok: 投稿に失敗しました({exc})")
            exit_code = 1

    if args.platform in ("instagram", "both"):
        try:
            result = publish_to_instagram(args.video_url, title, args.dry_run)
            print(f"Instagram: {result}")
        except MissingCredentials as exc:
            print(str(exc))
        except Exception as exc:  # noqa: BLE001
            print(f"Instagram: 投稿に失敗しました({exc})")
            exit_code = 1

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
