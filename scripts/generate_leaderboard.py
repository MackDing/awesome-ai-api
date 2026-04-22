#!/usr/bin/env python3
"""Generate gateways.json, leaderboard sections, and history snapshot from validated.json.

- Reads data/validated.json
- Produces:
    data/gateways.json           (structured, current state)
    data/history/YYYY-MM-DD.json (daily snapshot, append-only)
    data/_leaderboard.md         (markdown fragment used by README build)
    data/_leaderboard.zh.md      (Chinese fragment)

The READMEs use BEGIN/END markers so we can overwrite the fragment in place
without touching the rest of the file.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
HISTORY = DATA / "history"
HISTORY.mkdir(exist_ok=True)

# Singapore time (GMT+8)
SGT = timezone(timedelta(hours=8))

BEGIN_EN = "<!-- LEADERBOARD:BEGIN -->"
END_EN = "<!-- LEADERBOARD:END -->"
BEGIN_ZH = "<!-- LEADERBOARD_ZH:BEGIN -->"
END_ZH = "<!-- LEADERBOARD_ZH:END -->"


def slugify(url: str) -> str:
    s = re.sub(r"^https?://(www\.)?", "", url).rstrip("/")
    s = s.replace("/", "-").replace(".", "-")
    return s.lower()


def region_of(title: str, body_hints: list[str]) -> str:
    title_l = title.lower() if title else ""
    zh_hints = any(h for h in body_hints if any(ord(c) > 127 for c in h))
    if zh_hints or any(k in title for k in ["中转", "聚合", "国内"]):
        return "cn"
    if "github.com" in title_l or "self-host" in title_l:
        return "self-hosted"
    return "global"


def score_of(entry: dict[str, Any], uptime: dict | None = None) -> float:
    # Scoring: reachability + API endpoint confirmation + keyword density + uptime.
    base = 6.0
    if entry["verdict"] == "likely_relay":
        base += 1.5
    elif entry["verdict"] == "probable_relay":
        base += 0.8
    # Huge bonus for a real /v1/models endpoint — this is the ground truth signal.
    if entry.get("has_api"):
        base += 1.5
    # Bonus for lots of real models returned (not just keyword matches)
    real_model_count = len(entry.get("real_models") or [])
    if real_model_count >= 50:
        base += 0.4
    elif real_model_count >= 10:
        base += 0.2
    coverage = len(entry.get("model_keywords", []))
    base += min(coverage * 0.1, 0.5)
    if entry.get("payment_hints"):
        base += 0.2
    # Penalise extremely slow sites (> 3s)
    took = entry.get("took_ms") or 0
    if took > 3000:
        base -= 0.3
    # Uptime bonus (if we have >= 3 days of history)
    if uptime and uptime.get("samples") and uptime["samples"] >= 3:
        pct = uptime.get("uptime_pct") or 0
        if pct >= 99:
            base += 0.5
        elif pct >= 95:
            base += 0.3
        elif pct < 80:
            base -= 0.4
    return round(min(base, 9.9), 1)


def build_entries(validated: list[dict[str, Any]], uptime: dict[str, dict] | None = None) -> list[dict[str, Any]]:
    uptime = uptime or {}
    out: list[dict[str, Any]] = []
    for v in validated:
        # Skip unreachable + directory-only sites
        if v["verdict"] in ("unreachable", "directory", "hidden"):
            continue
        url = v["url"]
        slug = slugify(url)
        # Prefer the human-curated name from sites.yaml; fall back to parsed <title>.
        raw = v.get("title", "") or ""
        name = raw.split("|")[0].split(" - ")[0].strip() or slug
        if len(name) > 60:
            name = name[:60].rstrip()
        # Reject obviously garbage titles (HTML entity left overs, extremely short, etc.)
        if "&" in name and ";" not in name:
            name = slug
        # Generic titles ("New API", "首页", "one-api") are useless — prefer the domain slug.
        generic = {"new api", "首页", "one-api", "主页", "one api", "home", "网站首页", "api", "api中转站", "new-api"}
        if name.strip().lower() in generic:
            from urllib.parse import urlparse as _urlparse
            host = _urlparse(url).netloc.removeprefix("www.")
            name = host
        region = v.get("override_region") or region_of(v.get("title", ""), v.get("zh_keywords", []))
        up = uptime.get(url) or {}
        out.append(
            {
                "slug": slug,
                "name": name,
                "url": url,
                "final_url": v.get("final_url"),
                "region": region,
                "payment": v.get("payment_hints", []),
                "models_signaled": v.get("model_keywords", []),
                "real_models_count": len(v.get("real_models") or []),
                "real_models_sample": (v.get("real_models") or [])[:8],
                "engine": v.get("engine"),
                "reachable": True,
                "http_status": v.get("status"),
                "took_ms": v.get("took_ms"),
                "has_api": bool(v.get("has_api")),
                "probe": {
                    "status": v.get("probe_status"),
                    "path": v.get("probe_path"),
                    "hint": v.get("probe_hint"),
                },
                "uptime": {
                    "window_days": up.get("window_days"),
                    "samples": up.get("samples"),
                    "uptime_pct": up.get("uptime_pct"),
                    "streak_days": up.get("streak_days"),
                },
                "upstream": v.get("upstream"),
                "note": v.get("note"),
                "score": score_of(v, up),
                "verdict": v["verdict"],
                "last_verified": datetime.now(SGT).strftime("%Y-%m-%d"),
            }
        )
    # Sort by: has_api desc, score desc, latency asc, name
    out.sort(key=lambda x: (not x["has_api"], -x["score"], x["took_ms"] or 9999, x["name"].lower()))
    return out


TIER_LABELS_EN = {
    "likely_relay": "🟢 Verified",
    "probable_relay": "🟡 Probable",
    "open_source_tool": "🧰 OSS Tool",
    "needs_review": "🔍 Needs review",
}
TIER_LABELS_ZH = {
    "likely_relay": "🟢 已验证",
    "probable_relay": "🟡 疑似",
    "open_source_tool": "🧰 开源工具",
    "needs_review": "🔍 待复核",
}


def render_table(entries: list[dict[str, Any]], lang: str, limit: int | None = None) -> str:
    if lang == "zh":
        header = (
            "| # | 中转站 | 地区 | API | 模型 | 引擎 | 支付 | 评分 | 响应 | 分类 |\n"
            "|---|--------|------|-----|------|------|------|------|------|------|\n"
        )
    else:
        header = (
            "| # | Gateway | Region | API | Models | Engine | Payment | Score | Latency | Tier |\n"
            "|---|---------|--------|-----|--------|--------|---------|-------|---------|------|\n"
        )
    rows = []
    shown = entries if limit is None else entries[:limit]
    tier_labels = TIER_LABELS_ZH if lang == "zh" else TIER_LABELS_EN
    for i, e in enumerate(shown, start=1):
        # Prefer real model count when available
        real_n = e.get("real_models_count") or 0
        if real_n:
            models = f"**{real_n} models**"
        else:
            models = ", ".join(e["models_signaled"][:3]) or "—"
        payment = ", ".join(e["payment"]) or "—"
        medal = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, str(i))
        api_badge = "🔌" if e.get("has_api") else "·"
        latency = f"{e['took_ms']} ms"
        name = f"[{e['name']}]({e['url']})"
        tier = tier_labels.get(e.get("verdict", ""), e.get("verdict", ""))
        engine = e.get("engine") or "—"
        rows.append(
            f"| {medal} | {name} | {e['region']} | {api_badge} | {models} | {engine} | {payment} | {e['score']} | {latency} | {tier} |"
        )
    return header + "\n".join(rows) + "\n"


def splice_readme(path: Path, marker_begin: str, marker_end: str, body: str, stamp: str) -> None:
    text = path.read_text(encoding="utf-8")
    wrapper = f"{marker_begin}\n_Last updated: {stamp} (SGT)_\n\n{body}\n{marker_end}"
    if marker_begin in text and marker_end in text:
        new = re.sub(
            re.escape(marker_begin) + r".*?" + re.escape(marker_end),
            wrapper,
            text,
            count=1,
            flags=re.DOTALL,
        )
    else:
        # Append at bottom if markers missing
        new = text.rstrip() + "\n\n" + wrapper + "\n"
    path.write_text(new, encoding="utf-8")


def _update_stats_badges(path: Path, total: int, api_count: int, lang: str) -> None:
    """Rewrite the shields.io badges between <!-- STATS:BEGIN --> and STATS:END."""
    text = path.read_text(encoding="utf-8")
    if lang == "zh":
        begin, end = "<!-- STATS_ZH:BEGIN -->", "<!-- STATS_ZH:END -->"
        body = (
            f'<img src="https://img.shields.io/badge/%E4%B8%AD%E8%BD%AC%E7%AB%99-{total}-blue" alt="中转站总数">\n'
            f'  <img src="https://img.shields.io/badge/API%E5%B7%B2%E9%AA%8C%E8%AF%81-{api_count}-success" alt="API已验证">\n'
            f'  <img src="https://img.shields.io/badge/%E6%9B%B4%E6%96%B0-%E6%AF%8F%E6%97%A510%3A00_SGT-orange" alt="每日更新">'
        )
    else:
        begin, end = "<!-- STATS:BEGIN -->", "<!-- STATS:END -->"
        body = (
            f'<img src="https://img.shields.io/badge/Gateways-{total}-blue" alt="Total">\n'
            f'  <img src="https://img.shields.io/badge/API_verified-{api_count}-success" alt="API verified">\n'
            f'  <img src="https://img.shields.io/badge/Updated-daily_10:00_SGT-orange" alt="Updated">'
        )
    wrapper = f"{begin}\n  {body}\n  {end}"
    if begin in text and end in text:
        new = re.sub(
            re.escape(begin) + r".*?" + re.escape(end),
            wrapper,
            text,
            count=1,
            flags=re.DOTALL,
        )
        path.write_text(new, encoding="utf-8")


def main() -> int:
    validated = json.loads((DATA / "validated.json").read_text(encoding="utf-8"))
    # Load uptime stats if available
    uptime_path = DATA / "uptime.json"
    uptime = {}
    if uptime_path.exists():
        try:
            uptime = json.loads(uptime_path.read_text(encoding="utf-8")).get("gateways", {})
        except Exception:
            uptime = {}
    entries = build_entries(validated, uptime=uptime)
    stamp = datetime.now(SGT).strftime("%Y-%m-%d %H:%M")
    today = datetime.now(SGT).strftime("%Y-%m-%d")

    # Current state
    current = {
        "$schema": "./gateways.schema.json",
        "updated": today,
        "updated_at": stamp + " SGT",
        "total": len(entries),
        "gateways": entries,
    }
    (DATA / "gateways.json").write_text(
        json.dumps(current, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # History snapshot (one per day, last run wins)
    (HISTORY / f"{today}.json").write_text(
        json.dumps(current, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # Tier summary
    from collections import Counter
    tier_counts = Counter(e["verdict"] for e in entries)
    api_count = sum(1 for e in entries if e.get("has_api"))
    engine_counts = Counter(e["engine"] for e in entries if e.get("engine"))
    top_engines = engine_counts.most_common(5)
    engine_str_en = " · ".join(f"`{k}` × {v}" for k, v in top_engines) or "—"
    engine_str_zh = " · ".join(f"`{k}` × {v}" for k, v in top_engines) or "—"
    summary_en = (
        f"**Total: {len(entries)} gateways** · "
        f"🔌 **{api_count} with confirmed `/v1/models` endpoint** · "
        f"🟢 {tier_counts.get('likely_relay', 0)} Verified · "
        f"🟡 {tier_counts.get('probable_relay', 0)} Probable · "
        f"🧰 {tier_counts.get('open_source_tool', 0)} OSS · "
        f"🔍 {tier_counts.get('needs_review', 0)} Needs review\n\n"
        f"**Top engines detected:** {engine_str_en}\n\n"
    )
    summary_zh = (
        f"**合计 {len(entries)} 个中转站** · "
        f"🔌 **{api_count} 个已确认 `/v1/models` 端点** · "
        f"🟢 已验证 {tier_counts.get('likely_relay', 0)} · "
        f"🟡 疑似 {tier_counts.get('probable_relay', 0)} · "
        f"🧰 开源 {tier_counts.get('open_source_tool', 0)} · "
        f"🔍 待复核 {tier_counts.get('needs_review', 0)}\n\n"
        f"**主流引擎分布：** {engine_str_zh}\n\n"
    )

    # Markdown fragments — full list in data/, top 50 in README
    table_en_full = render_table(entries, "en")
    table_zh_full = render_table(entries, "zh")
    (DATA / "_leaderboard.md").write_text(summary_en + table_en_full, encoding="utf-8")
    (DATA / "_leaderboard.zh.md").write_text(summary_zh + table_zh_full, encoding="utf-8")

    table_en = summary_en + render_table(entries, "en", limit=50) + (
        f"\n> Top 50 shown. See [`data/_leaderboard.md`](data/_leaderboard.md) for the full list of {len(entries)} gateways.\n"
        if len(entries) > 50 else "\n"
    )
    table_zh = summary_zh + render_table(entries, "zh", limit=50) + (
        f"\n> 仅展示 Top 50。完整 {len(entries)} 个榜单见 [`data/_leaderboard.zh.md`](data/_leaderboard.zh.md)。\n"
        if len(entries) > 50 else "\n"
    )

    # Splice into READMEs
    splice_readme(ROOT / "README.md", BEGIN_EN, END_EN, table_en, stamp)
    splice_readme(ROOT / "README.zh-CN.md", BEGIN_ZH, END_ZH, table_zh, stamp)

    # Refresh the dynamic STATS badges in both READMEs
    _update_stats_badges(ROOT / "README.md", len(entries), api_count, lang="en")
    _update_stats_badges(ROOT / "README.zh-CN.md", len(entries), api_count, lang="zh")

    print(f"[ok] {len(entries)} gateways → gateways.json + history/{today}.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
