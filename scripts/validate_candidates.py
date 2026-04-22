#!/usr/bin/env python3
"""Validate candidate gateways: reachability + "is this an AI API relay?" heuristic.

Usage:
    python3 scripts/validate_candidates.py [--input data/candidates.txt] [--out data/validated.json]

Heuristic classifies a site as an "AI API gateway / relay" if its HTML
contains at least 2 relay-ish keywords (claude, gpt, gemini, api key,
openai-compatible, 中转, 聚合, relay, gateway, router, ...).

We also record HTTP status, final URL after redirects, and page title.

This is intentionally conservative; ambiguous sites get flagged for
manual review rather than dropped silently.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import re
import sys
import time
from pathlib import Path
from typing import Any

import urllib.request
import urllib.error
import ssl

UA = (
    "Mozilla/5.0 (compatible; awesome-ai-api-bot/0.1; "
    "+https://github.com/MackDing/awesome-ai-api)"
)

RELAY_KEYWORDS_EN = [
    "openai-compatible",
    "openai compatible",
    "unified api",
    "api gateway",
    "llm gateway",
    "llm router",
    "api relay",
    "api reseller",
    "multi-provider",
    "multi provider",
    "aggregator",
    "openrouter",
    "one api",
    "claude api",
    "gpt api",
    "gemini api",
    "deepseek api",
]
RELAY_KEYWORDS_ZH = [
    "中转",
    "中转站",
    "聚合",
    "聚合平台",
    "代理",
    "兼容",
    "大模型",
    "统一接入",
    "国内直连",
    "一站式",
]
MODEL_KEYWORDS = [
    "claude",
    "gpt",
    "gemini",
    "chatgpt",
    "anthropic",
    "openai",
    "deepseek",
    "qwen",
    "mistral",
    "grok",
    "llama",
]
PAYMENT_KEYWORDS = {
    "alipay": ["alipay", "支付宝"],
    "wechat": ["wechat", "微信支付", "微信"],
    "card": ["credit card", "信用卡", "stripe", "paypal"],
    "crypto": ["usdt", "usdc", "crypto", "加密货币", "bitcoin"],
}


def fetch(url: str, timeout: float = 12.0) -> dict[str, Any]:
    start = time.time()
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            body = resp.read(200_000).decode("utf-8", errors="ignore")
            return {
                "ok": True,
                "status": resp.status,
                "final_url": resp.geturl(),
                "body": body,
                "took_ms": int((time.time() - start) * 1000),
            }
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, Exception) as e:
        return {
            "ok": False,
            "status": None,
            "final_url": url,
            "body": "",
            "error": str(e)[:200],
            "took_ms": int((time.time() - start) * 1000),
        }


TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)


def classify(url: str, body: str) -> dict[str, Any]:
    low = body.lower()
    en_hits = [k for k in RELAY_KEYWORDS_EN if k in low]
    zh_hits = [k for k in RELAY_KEYWORDS_ZH if k in body]
    model_hits = [k for k in MODEL_KEYWORDS if k in low]
    payments = []
    for key, needles in PAYMENT_KEYWORDS.items():
        if any(n in body if ord(n[0]) > 127 else n in low for n in needles):
            payments.append(key)
    title_match = TITLE_RE.search(body)
    title = title_match.group(1).strip() if title_match else ""
    total_hits = len(en_hits) + len(zh_hits)
    if total_hits >= 2 and len(model_hits) >= 2:
        verdict = "likely_relay"
    elif total_hits >= 1 and len(model_hits) >= 3:
        verdict = "probable_relay"
    elif "github.com" in url and ("api" in low or "gateway" in low) and len(model_hits) >= 2:
        verdict = "open_source_tool"
    else:
        verdict = "needs_review"
    return {
        "title": title[:200],
        "en_keywords": en_hits,
        "zh_keywords": zh_hits,
        "model_keywords": model_hits,
        "payment_hints": payments,
        "verdict": verdict,
    }


def load_candidates(path: Path) -> list[str]:
    urls: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        urls.append(line)
    # de-dupe preserving order
    seen: set[str] = set()
    out: list[str] = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="data/candidates.txt")
    ap.add_argument("--out", default="data/validated.json")
    ap.add_argument("--concurrency", type=int, default=8)
    args = ap.parse_args()

    root = Path(__file__).resolve().parent.parent
    in_path = root / args.input
    out_path = root / args.out

    urls = load_candidates(in_path)
    print(f"[info] validating {len(urls)} candidates …", file=sys.stderr)

    results: list[dict[str, Any]] = []
    with cf.ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        futures = {ex.submit(fetch, u): u for u in urls}
        for fut in cf.as_completed(futures):
            u = futures[fut]
            r = fut.result()
            if r["ok"]:
                cls = classify(u, r["body"])
            else:
                cls = {
                    "title": "",
                    "en_keywords": [],
                    "zh_keywords": [],
                    "model_keywords": [],
                    "payment_hints": [],
                    "verdict": "unreachable",
                }
            results.append(
                {
                    "url": u,
                    "final_url": r.get("final_url"),
                    "status": r.get("status"),
                    "took_ms": r.get("took_ms"),
                    "error": r.get("error"),
                    **cls,
                }
            )
            print(f"  [{cls['verdict']:>16}] {r.get('status')} {u}", file=sys.stderr)

    # sort by verdict priority, then url
    priority = {
        "likely_relay": 0,
        "probable_relay": 1,
        "open_source_tool": 2,
        "needs_review": 3,
        "unreachable": 4,
    }
    results.sort(key=lambda x: (priority.get(x["verdict"], 99), x["url"]))

    out_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[ok] wrote {out_path}", file=sys.stderr)

    # summary
    from collections import Counter

    counts = Counter(r["verdict"] for r in results)
    for v, c in counts.most_common():
        print(f"  {v:>16}: {c}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
