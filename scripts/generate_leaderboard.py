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


def score_of(entry: dict[str, Any]) -> float:
    # Very simple heuristic: reachability + keyword density + model coverage.
    base = 7.0
    if entry["verdict"] == "likely_relay":
        base += 1.5
    elif entry["verdict"] == "probable_relay":
        base += 0.8
    coverage = len(entry.get("model_keywords", []))
    base += min(coverage * 0.1, 0.5)
    if entry.get("payment_hints"):
        base += 0.2
    return round(min(base, 9.8), 1)


def build_entries(validated: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for v in validated:
        if v["verdict"] not in ("likely_relay", "probable_relay"):
            continue
        url = v["url"]
        slug = slugify(url)
        name = v.get("title", "").split("|")[0].split(" - ")[0].strip() or slug
        # Trim overly long auto-titles
        if len(name) > 60:
            name = name[:60].rstrip()
        out.append(
            {
                "slug": slug,
                "name": name,
                "url": url,
                "final_url": v.get("final_url"),
                "region": region_of(v.get("title", ""), v.get("zh_keywords", [])),
                "payment": v.get("payment_hints", []),
                "models_signaled": v.get("model_keywords", []),
                "reachable": True,
                "http_status": v.get("status"),
                "took_ms": v.get("took_ms"),
                "score": score_of(v),
                "verdict": v["verdict"],
                "last_verified": datetime.now(SGT).strftime("%Y-%m-%d"),
            }
        )
    # Sort by score desc, then by name
    out.sort(key=lambda x: (-x["score"], x["name"].lower()))
    return out


def render_table(entries: list[dict[str, Any]], lang: str) -> str:
    if lang == "zh":
        header = (
            "| 排名 | 中转站 | 地区 | 模型信号 | 支付 | 评分 | 访问 | 响应 |\n"
            "|------|--------|------|----------|------|------|------|--------|\n"
        )
    else:
        header = (
            "| # | Gateway | Region | Model signals | Payment | Score | Reach | Latency |\n"
            "|---|---------|--------|---------------|---------|-------|-------|---------|\n"
        )
    rows = []
    for i, e in enumerate(entries, start=1):
        models = ", ".join(e["models_signaled"][:5]) or "—"
        payment = ", ".join(e["payment"]) or "—"
        medal = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, str(i))
        status = f"✅ {e['http_status']}"
        latency = f"{e['took_ms']} ms"
        name = f"[{e['name']}]({e['url']})"
        rows.append(
            f"| {medal} | {name} | {e['region']} | {models} | {payment} | {e['score']} | {status} | {latency} |"
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


def main() -> int:
    validated = json.loads((DATA / "validated.json").read_text(encoding="utf-8"))
    entries = build_entries(validated)
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

    # Markdown fragments
    table_en = render_table(entries, "en")
    table_zh = render_table(entries, "zh")
    (DATA / "_leaderboard.md").write_text(table_en, encoding="utf-8")
    (DATA / "_leaderboard.zh.md").write_text(table_zh, encoding="utf-8")

    # Splice into READMEs
    splice_readme(ROOT / "README.md", BEGIN_EN, END_EN, table_en, stamp)
    splice_readme(ROOT / "README.zh-CN.md", BEGIN_ZH, END_ZH, table_zh, stamp)

    print(f"[ok] {len(entries)} gateways → gateways.json + history/{today}.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
