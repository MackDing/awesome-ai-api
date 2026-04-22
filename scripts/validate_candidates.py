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

import html as _html
import json as _json
import urllib.request
import urllib.error
import ssl
from urllib.parse import urlparse

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


def _ssl_ctx() -> ssl.SSLContext:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


def fetch(url: str, timeout: float = 12.0, read_bytes: int = 200_000) -> dict[str, Any]:
    start = time.time()
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=_ssl_ctx()) as resp:
            body = resp.read(read_bytes).decode("utf-8", errors="ignore")
            return {
                "ok": True,
                "status": resp.status,
                "final_url": resp.geturl(),
                "body": body,
                "headers": {k.lower(): v for k, v in resp.headers.items()},
                "took_ms": int((time.time() - start) * 1000),
            }
    except urllib.error.HTTPError as e:
        # HTTPError still carries a useful status + body (e.g. 401 from /v1/models)
        try:
            body = e.read(read_bytes).decode("utf-8", errors="ignore")
        except Exception:
            body = ""
        return {
            "ok": True,
            "status": e.code,
            "final_url": url,
            "body": body,
            "headers": {k.lower(): v for k, v in (e.headers.items() if e.headers else [])},
            "took_ms": int((time.time() - start) * 1000),
        }
    except (urllib.error.URLError, TimeoutError, Exception) as e:
        return {
            "ok": False,
            "status": None,
            "final_url": url,
            "body": "",
            "headers": {},
            "error": str(e)[:200],
            "took_ms": int((time.time() - start) * 1000),
        }


# --- Upstream engine fingerprint -------------------------------------------
# Most CN relays are thin skins on top of a handful of OSS projects.
# Knowing which one lets users predict: update cadence, security posture,
# Claude-Code compatibility, etc.
_ENGINE_SIGNATURES = [
    # (engine_id, list of substrings to match against html/body/headers)
    ("new-api", ["/static/js/new-api", "\"New API\"", "new-api-web", "NewAPI", "Calcium-Ion", "QuantumNous"]),
    ("one-api", ["one-api-web", "songquanpeng/one-api", "One API", "\"oneapi\""]),
    ("one-hub", ["MartialBE/one-hub", "OneHub", "one-hub-web"]),
    ("fastgpt", ["FastGPT", "fastgpt", "labring"]),
    ("dify", ["Dify", "dify.ai", "langgenius"]),
    ("litellm", ["LiteLLM", "BerriAI", "litellm"]),
    ("openrouter", ["openrouter.ai", "OpenRouter"]),
    ("apipie", ["APIpie", "apipie.ai"]),
    ("helicone", ["helicone", "Helicone"]),
    ("portkey", ["Portkey-AI", "portkey.ai"]),
    ("langdb", ["langdb"]),
    ("uni-api", ["uni-api", "yym68686"]),
    ("chatnext-web", ["NextChat", "ChatGPTNextWeb"]),
    ("lobe-chat", ["LobeChat", "lobehub"]),
    ("vercel-ai-gateway", ["vercel-ai-sdk", "aigateway.vercel"]),
]


def detect_engine(url: str, body: str, headers: dict[str, str]) -> str | None:
    hay = body + " " + " ".join(f"{k}:{v}" for k, v in (headers or {}).items())
    low = hay.lower()
    for engine_id, sigs in _ENGINE_SIGNATURES:
        for s in sigs:
            if s.lower() in low:
                return engine_id
    # Check a few /v1/models and /about endpoints for additional signal
    return None


# --- OpenAI-compatible endpoint probe --------------------------------------
# Any real AI API relay must expose /v1/models. Fake / directory sites don't.
# Expected outcome shape (success = relay behaviour confirmed):
#   - 200 + JSON body with "data":[...] or "object":"list"
#   - 401 / 403 with JSON mentioning "api_key" / "unauthorized" / "invalid"
# Anything else (404 HTML, 200 HTML, redirects to marketing) → not a real API.

_PROBE_SUFFIXES = ["/v1/models", "/api/v1/models"]


def probe_api(url: str, timeout: float = 8.0) -> dict[str, Any]:
    """Return {has_api, probe_status, probe_path, probe_hint, real_models}."""
    parsed = urlparse(url)
    # Skip probes for github.com etc. — they're OSS repos, not live APIs
    if parsed.netloc.endswith("github.com"):
        return {"has_api": False, "probe_status": None, "probe_path": None, "probe_hint": "github-repo", "real_models": []}
    base = f"{parsed.scheme}://{parsed.netloc}"
    for suffix in _PROBE_SUFFIXES:
        target = base + suffix
        r = fetch(target, timeout=timeout, read_bytes=100_000)
        status = r.get("status")
        body = r.get("body") or ""
        low = body.lower()
        if status is None:
            continue
        hint = ""
        has_api = False
        real_models: list[str] = []
        if status in (200,):
            # Must look like JSON models list, not a marketing page
            if body.lstrip().startswith("{") and ("\"data\"" in low or "\"object\"" in low or "\"models\"" in low):
                has_api = True
                hint = "openai-models-json"
                # Extract real model ids — the ground truth of what this gateway sells
                try:
                    parsed_json = _json.loads(body)
                    items = parsed_json.get("data") or parsed_json.get("models") or []
                    if isinstance(items, list):
                        for it in items[:500]:
                            if isinstance(it, dict):
                                mid = it.get("id") or it.get("model") or it.get("name")
                                if mid and isinstance(mid, str):
                                    real_models.append(mid)
                            elif isinstance(it, str):
                                real_models.append(it)
                except Exception:
                    pass
            elif "<html" in low or "<!doctype" in low:
                hint = "html-on-/v1/models"
        elif status in (401, 403):
            # Classic "missing api key" — definitive relay signal
            if any(k in low for k in ("api_key", "api key", "unauthorized", "invalid", "missing", "authentication")):
                has_api = True
                hint = f"{status}-need-key"
            else:
                # Still a hint (auth wall present)
                has_api = True
                hint = f"{status}-auth"
        elif status == 405:
            has_api = True
            hint = "405-method-not-allowed"
        elif status in (429,):
            has_api = True
            hint = "429-rate-limited"
        if has_api or status in (200, 401, 403, 405, 429):
            return {
                "has_api": has_api,
                "probe_status": status,
                "probe_path": suffix,
                "probe_hint": hint,
                "real_models": real_models,
            }
    return {"has_api": False, "probe_status": None, "probe_path": None, "probe_hint": "no-endpoint", "real_models": []}


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
    raw_title = title_match.group(1).strip() if title_match else ""
    # Strip HTML entities (&amp;, &#8211; etc.) and normalise whitespace
    title = _html.unescape(re.sub(r"\s+", " ", raw_title))
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


def _load_overrides(path: Path) -> dict[str, dict[str, Any]]:
    """sites.yaml uses a tiny subset we parse without PyYAML dependency."""
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    out: dict[str, dict[str, Any]] = {}
    cur_key: str | None = None
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not line.startswith(" "):
            # top-level key: url-or-domain
            cur_key = line.rstrip(":").strip()
            out[cur_key] = {}
        elif cur_key is not None:
            m = re.match(r"\s+([a-zA-Z_]+):\s*(.+)", line)
            if m:
                k, v = m.group(1), m.group(2).strip()
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                out[cur_key][k] = v
    return out


def _apply_override(url: str, entry: dict[str, Any], overrides: dict[str, dict[str, Any]]) -> None:
    if not overrides:
        return
    parsed = urlparse(url)
    for key in (url, parsed.netloc, parsed.netloc.removeprefix("www.")):
        if key in overrides:
            ov = overrides[key]
            if "name" in ov:
                entry["title"] = ov["name"]
            if "region" in ov:
                entry["override_region"] = ov["region"]
            if "verdict" in ov:
                entry["verdict"] = ov["verdict"]
            if "upstream" in ov:
                entry["upstream"] = ov["upstream"]
            if "note" in ov:
                entry["note"] = ov["note"]
            break


def _check_one(url: str, overrides: dict[str, dict[str, Any]]) -> dict[str, Any]:
    r = fetch(url)
    if r["ok"] and r.get("status") and 200 <= r["status"] < 400:
        cls = classify(url, r["body"])
        probe = probe_api(url)
        engine = detect_engine(url, r["body"], r.get("headers", {}))
    else:
        cls = {
            "title": "",
            "en_keywords": [],
            "zh_keywords": [],
            "model_keywords": [],
            "payment_hints": [],
            "verdict": "unreachable",
        }
        probe = {"has_api": False, "probe_status": None, "probe_path": None, "probe_hint": "skip-unreachable", "real_models": []}
        engine = None
    entry: dict[str, Any] = {
        "url": url,
        "final_url": r.get("final_url"),
        "status": r.get("status"),
        "took_ms": r.get("took_ms"),
        "error": r.get("error"),
        "engine": engine,
        **cls,
        **probe,
    }
    # Promote verdict when the API probe confirms a real relay.
    # Demote when we have *no* API endpoint and no keyword evidence.
    if entry.get("has_api") and entry["verdict"] in ("needs_review", "probable_relay"):
        entry["verdict"] = "likely_relay"
        entry["promoted_by"] = "api-probe"
    elif (
        not entry.get("has_api")
        and entry["verdict"] in ("likely_relay", "probable_relay")
        and len(entry.get("model_keywords", [])) < 3
    ):
        entry["verdict"] = "needs_review"
        entry["demoted_by"] = "no-api-endpoint"
    _apply_override(url, entry, overrides)
    return entry


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="data/candidates.txt")
    ap.add_argument("--out", default="data/validated.json")
    ap.add_argument("--overrides", default="data/sites.yaml")
    ap.add_argument("--concurrency", type=int, default=16)
    args = ap.parse_args()

    root = Path(__file__).resolve().parent.parent
    in_path = root / args.input
    out_path = root / args.out
    overrides = _load_overrides(root / args.overrides)

    urls = load_candidates(in_path)
    print(f"[info] validating {len(urls)} candidates (overrides: {len(overrides)}) …", file=sys.stderr)

    results: list[dict[str, Any]] = []
    with cf.ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        futures = {ex.submit(_check_one, u, overrides): u for u in urls}
        for fut in cf.as_completed(futures):
            entry = fut.result()
            results.append(entry)
            api_flag = "🔌" if entry.get("has_api") else "  "
            print(
                f"  [{entry['verdict']:>16}] {entry.get('status')} {api_flag} {entry['url']}",
                file=sys.stderr,
            )

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
