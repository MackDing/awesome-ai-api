#!/usr/bin/env python3
"""Build auxiliary exports for GitHub Pages / SEO / GEO.

Outputs (all under docs/):
  - gateways.json        (copied from data/)
  - gateways.csv         (flat spreadsheet form)
  - feed.xml             (RSS of daily snapshot)
  - llms-full.txt        (LLM-friendly dump of the full leaderboard)

Also copies llms.txt to docs/ so GitHub Pages serves it at the site root.
"""
from __future__ import annotations

import csv
import json
import re
import shutil
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from xml.sax.saxutils import escape

SGT = timezone(timedelta(hours=8))
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"
DOCS.mkdir(exist_ok=True)


def copy_gateways():
    src = DATA / "gateways.json"
    dst = DOCS / "gateways.json"
    shutil.copyfile(src, dst)
    # also copy llms.txt to site root
    llms = ROOT / "llms.txt"
    if llms.exists():
        shutil.copyfile(llms, DOCS / "llms.txt")
    print(f"[ok] copied {dst.name} + llms.txt")


def build_csv():
    data = json.loads((DOCS / "gateways.json").read_text(encoding="utf-8"))
    gws = data.get("gateways", [])
    out = DOCS / "gateways.csv"
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "rank", "name", "url", "region", "score", "verdict",
            "has_api", "engine", "http_status", "latency_ms",
            "real_models_count", "models_signaled", "payment",
            "uptime_pct", "streak_days", "last_verified",
        ])
        for i, g in enumerate(gws, start=1):
            up = g.get("uptime") or {}
            w.writerow([
                i, g.get("name", ""), g.get("url", ""), g.get("region", ""),
                g.get("score", ""), g.get("verdict", ""),
                "Y" if g.get("has_api") else "N",
                g.get("engine") or "",
                g.get("http_status", ""),
                g.get("took_ms", ""),
                g.get("real_models_count", 0),
                "|".join(g.get("models_signaled") or []),
                "|".join(g.get("payment") or []),
                up.get("uptime_pct", ""),
                up.get("streak_days", ""),
                g.get("last_verified", ""),
            ])
    print(f"[ok] {out.name} ({len(gws)} rows)")


def build_rss():
    data = json.loads((DOCS / "gateways.json").read_text(encoding="utf-8"))
    gws = data.get("gateways", [])
    updated = data.get("updated_at", datetime.now(SGT).strftime("%Y-%m-%d %H:%M SGT"))
    top = gws[:20]

    items_xml = []
    for g in top:
        title = f"#{top.index(g)+1} {g.get('name','?')} — score {g.get('score','?')}"
        url = g.get("url", "https://github.com/MackDing/awesome-ai-api")
        desc = (
            f"Region: {g.get('region','?')} · "
            f"API: {'verified' if g.get('has_api') else 'unconfirmed'} · "
            f"Engine: {g.get('engine') or 'unknown'} · "
            f"Latency: {g.get('took_ms','?')}ms · "
            f"Models: {', '.join((g.get('models_signaled') or [])[:5]) or '-'}"
        )
        items_xml.append(
            f"""  <item>
    <title>{escape(title)}</title>
    <link>{escape(url)}</link>
    <guid isPermaLink="false">awesome-ai-api:{escape(g.get('slug','?'))}:{data.get('updated','?')}</guid>
    <description>{escape(desc)}</description>
    <pubDate>{datetime.now(SGT).strftime('%a, %d %b %Y %H:%M:%S +0800')}</pubDate>
  </item>"""
        )

    rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel>
  <title>awesome-ai-api — daily leaderboard</title>
  <link>https://mackding.github.io/awesome-ai-api/</link>
  <description>Daily-refreshed leaderboard of AI API gateways. Updated: {escape(updated)}.</description>
  <language>en</language>
  <lastBuildDate>{datetime.now(SGT).strftime('%a, %d %b %Y %H:%M:%S +0800')}</lastBuildDate>
{chr(10).join(items_xml)}
</channel></rss>
"""
    (DOCS / "feed.xml").write_text(rss, encoding="utf-8")
    print(f"[ok] feed.xml ({len(top)} items)")


def build_llms_full():
    data = json.loads((DOCS / "gateways.json").read_text(encoding="utf-8"))
    gws = data.get("gateways", [])
    api_count = sum(1 for g in gws if g.get("has_api"))
    top = gws[:50]

    lines = [
        "# awesome-ai-api (full dump for LLMs)",
        "",
        "> Full, machine-readable leaderboard of AI API gateways, formatted for LLM ingestion.",
        f"> Snapshot: {data.get('updated_at','?')}. Total: {len(gws)}. API-confirmed: {api_count}.",
        "> Canonical site: https://mackding.github.io/awesome-ai-api/",
        "> Source repo: https://github.com/MackDing/awesome-ai-api",
        "> License: MIT (code) + CC0 (data)",
        "",
        "## Top 50 Gateways (sorted by score)",
        "",
    ]
    for i, g in enumerate(top, start=1):
        up = g.get("uptime") or {}
        lines.append(
            f"{i}. {g.get('name','?')} — {g.get('url')} — "
            f"score {g.get('score')}, "
            f"{'API verified' if g.get('has_api') else 'API unconfirmed'}, "
            f"region {g.get('region','?')}, "
            f"engine {g.get('engine') or 'unknown'}, "
            f"latency {g.get('took_ms','?')}ms, "
            f"uptime {up.get('uptime_pct','?')}% over {up.get('samples', '?')} samples, "
            f"models: {', '.join((g.get('models_signaled') or [])[:6]) or '-'}"
        )
    lines += [
        "",
        "## Citation",
        "",
        "> awesome-ai-api (Mack Ding, 2026). https://github.com/MackDing/awesome-ai-api",
    ]
    (DOCS / "llms-full.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[ok] llms-full.txt ({len(top)} entries)")


def build_stats():
    """Server-side render top stats + top 20 table into docs/index.html and zh/index.html.

    This means crawlers (and in-app browsers that choke on JS) see real numbers,
    and the site renders instantly without waiting on fetch().
    """
    data = json.loads((DOCS / "gateways.json").read_text(encoding="utf-8"))
    gws = data.get("gateways", [])
    total = data.get("total", len(gws))
    api_n = sum(1 for g in gws if g.get("has_api"))
    engines = len({g.get("engine") for g in gws if g.get("engine")})
    updated = (data.get("updated_at") or data.get("updated") or "—")[:16]
    updated_badge_en = f"updated {data.get('updated','—')}"
    updated_badge_zh = f"更新于 {data.get('updated','—')}"

    def row_html(g: dict, i: int, lang: str = "en") -> str:
        medal = {0: "🥇", 1: "🥈", 2: "🥉"}.get(i, str(i + 1))
        api = "🔌" if g.get("has_api") else "·"
        region = g.get("region") or "—"
        rc = g.get("real_models_count") or 0
        if rc:
            models_cell = f"<b>{rc}</b>"
        else:
            models_cell = ", ".join((g.get("models_signaled") or [])[:3]) or "—"
        name = g.get("name", "?")
        url = g.get("url", "#")
        return (
            f'<tr><td>{medal}</td>'
            f'<td><a href="{url}" rel="noopener">{name}</a></td>'
            f'<td>{region}</td><td>{api}</td><td>{models_cell}</td>'
            f'<td>{g.get("score", "—")}</td></tr>'
        )

    top = gws[:20]
    rows_en = "\n".join(row_html(g, i, "en") for i, g in enumerate(top))
    rows_zh = rows_en  # same data, links/numbers are language-neutral

    for html_path, rows, badge in (
        (DOCS / "index.html", rows_en, updated_badge_en),
        (DOCS / "zh" / "index.html", rows_zh, updated_badge_zh),
    ):
        if not html_path.exists():
            continue
        html = html_path.read_text(encoding="utf-8")

        # Inject the 4 stat numbers (idempotent: matches any prior value, not just em-dash)
        html = re.sub(r'(id="s-total">)[^<]*(<)',    lambda m: f'{m.group(1)}{total}{m.group(2)}',   html)
        html = re.sub(r'(id="s-api">)[^<]*(<)',      lambda m: f'{m.group(1)}{api_n}{m.group(2)}',   html)
        html = re.sub(r'(id="s-engines">)[^<]*(<)',  lambda m: f'{m.group(1)}{engines}{m.group(2)}', html)
        html = re.sub(r'(id="s-updated">)[^<]*(<)',  lambda m: f'{m.group(1)}{updated}{m.group(2)}', html)

        # Inject the updated badge text
        html = re.sub(
            r'(<span class="badge" id="updated-badge">)[^<]*(</span>)',
            lambda m: m.group(1) + badge + m.group(2),
            html,
        )

        # Inject the top-20 table body
        html = re.sub(
            r'<tbody id="leaderboard-body">.*?</tbody>',
            f'<tbody id="leaderboard-body">{rows}</tbody>',
            html,
            flags=re.DOTALL,
        )

        html_path.write_text(html, encoding="utf-8")

    print(f"[ok] SSR stats injected into index.html + zh/index.html (total={total}, api={api_n}, engines={engines})")


def main() -> int:
    copy_gateways()
    build_csv()
    build_rss()
    build_llms_full()
    build_stats()
    return 0


if __name__ == "__main__":
    sys.exit(main())
