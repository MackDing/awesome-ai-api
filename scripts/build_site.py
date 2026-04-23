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


def build_gateway_pages():
    """Generate /g/<slug>/index.html for every gateway.

    Each page is keyword-targeted at the gateway's brand name + 'API 中转站'
    + '/v1/models' so it ranks for brand queries on Google/Bing/Baidu.
    """
    data = json.loads((DOCS / "gateways.json").read_text(encoding="utf-8"))
    gws = data.get("gateways", [])
    out_dir = DOCS / "g"
    out_dir.mkdir(exist_ok=True)

    count = 0
    for g in gws:
        slug = g.get("slug")
        if not slug:
            continue
        d = out_dir / slug
        d.mkdir(exist_ok=True)

        name = g.get("name", slug)
        url = g.get("url", "")
        score = g.get("score", "—")
        region = g.get("region", "—")
        engine = g.get("engine") or "unknown"
        api = g.get("has_api")
        api_txt_en = "✅ confirmed /v1/models endpoint" if api else "⏳ endpoint not publicly verified"
        api_txt_zh = "✅ 已验证 /v1/models 接口" if api else "⏳ 接口未公开验证"
        latency = g.get("took_ms") or "—"
        up = g.get("uptime") or {}
        uptime_pct = up.get("uptime_pct") or "—"
        samples = up.get("samples") or 0
        models = (g.get("models_signaled") or [])[:8]
        real_count = g.get("real_models_count") or 0
        verdict = g.get("verdict", "—").replace("_", " ")

        # Schema.org: SoftwareApplication so Google recognizes this as an API service listing
        jsonld = {
            "@context": "https://schema.org",
            "@type": "SoftwareApplication",
            "name": name,
            "url": url,
            "applicationCategory": "DeveloperApplication",
            "operatingSystem": "Any (REST API)",
            "description": f"{name} — AI API gateway / relay. Region: {region}. Engine: {engine}. Score {score}/10 on awesome-ai-api leaderboard.",
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": str(score) if isinstance(score, (int, float)) else "0",
                "bestRating": "10",
                "worstRating": "0",
                "ratingCount": max(samples, 1),
            },
            "isPartOf": {
                "@type": "Dataset",
                "name": "awesome-ai-api leaderboard",
                "url": "https://mackding.github.io/awesome-ai-api/",
            },
        }

        models_str = ", ".join(models) or "—"
        page_url = f"https://mackding.github.io/awesome-ai-api/g/{slug}/"

        html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(name)} — AI API gateway review, score, uptime | awesome-ai-api</title>
<meta name="description" content="{escape(name)} ({region}) scores {score}/10 on the awesome-ai-api leaderboard. Engine: {engine}. {'Verified /v1/models' if api else 'Unverified endpoint'}. Updated daily. {escape(name)} 中转站评测 / 可用性监控 / 分数 {score}/10.">
<meta name="keywords" content="{escape(name)}, {escape(name)} 中转, {escape(name)} API, AI API gateway, {engine}, /v1/models, OpenAI compatible, Claude relay, GPT API">
<link rel="canonical" href="{page_url}">
<meta property="og:title" content="{escape(name)} — score {score}/10 on awesome-ai-api">
<meta property="og:description" content="{region} · {engine} · {api_txt_en}">
<meta property="og:url" content="{page_url}">
<meta property="og:image" content="https://mackding.github.io/awesome-ai-api/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<!-- Chinese search engines -->
<meta name="baidu-site-verification" content="">
<meta name="sogou_site_verification" content="">
<meta name="360-site-verification" content="">
<meta name="shenma-site-verification" content="">
<style>
  body{{font-family:-apple-system,Segoe UI,Helvetica Neue,sans-serif;max-width:740px;margin:0 auto;padding:2rem 1rem;color:#e0e6f0;background:#0d1117;line-height:1.55}}
  a{{color:#58a6ff}} a:hover{{text-decoration:underline}}
  h1{{font-size:1.8rem;margin-bottom:.3rem}}
  .sub{{color:#8b949e;font-size:.95rem;margin-bottom:1.5rem}}
  .score{{font-size:3rem;font-weight:700;color:{'#3fb950' if isinstance(score,(int,float)) and score>=8 else '#d29922' if isinstance(score,(int,float)) and score>=6 else '#f85149'};line-height:1}}
  .grid{{display:grid;grid-template-columns:1fr 1fr;gap:.75rem 1.5rem;margin:1.5rem 0;padding:1rem;background:#161b22;border:1px solid #30363d;border-radius:8px}}
  .grid dt{{color:#8b949e;font-size:.85rem}} .grid dd{{margin:0;margin-bottom:.5rem}}
  nav{{margin-bottom:1.5rem;font-size:.85rem;color:#8b949e}}
  .cta{{display:inline-block;padding:.6rem 1.2rem;background:#238636;color:white;border-radius:6px;text-decoration:none;font-weight:600;margin-top:.5rem}}
  .cta:hover{{background:#2ea043;text-decoration:none}}
  hr{{border:none;border-top:1px solid #30363d;margin:2rem 0}}
  .note{{font-size:.85rem;color:#8b949e;font-style:italic}}
</style>
<script type="application/ld+json">{escape(json.dumps(jsonld, ensure_ascii=False))}</script>
</head>
<body>
<nav>
  <a href="/awesome-ai-api/">← awesome-ai-api</a> ·
  <a href="/awesome-ai-api/zh/">中文</a> ·
  <a href="/awesome-ai-api/engine/{engine}/">more {engine} gateways</a>
</nav>

<h1>{escape(name)}</h1>
<p class="sub">AI API gateway review · Region: <b>{region}</b> · Verdict: <b>{verdict}</b></p>

<div class="score">{score}<span style="color:#8b949e;font-size:1.2rem;font-weight:400">/10</span></div>
<p class="sub">awesome-ai-api leaderboard score, updated {data.get('updated','—')}.</p>

<dl class="grid">
  <dt>Upstream</dt><dd><a href="{escape(url)}" rel="nofollow noopener">{escape(url)}</a></dd>
  <dt>API endpoint</dt><dd>{api_txt_en}</dd>
  <dt>Engine</dt><dd>{engine}</dd>
  <dt>Latency</dt><dd>{latency} ms</dd>
  <dt>30-day uptime</dt><dd>{uptime_pct}% (n={samples})</dd>
  <dt>Models observed</dt><dd>{real_count or len(models)}</dd>
</dl>

<h2>Models signaled</h2>
<p>{escape(models_str)}</p>

<h2>How we verify {escape(name)}</h2>
<p>Every 24 hours we probe <code>{escape(url)}/v1/models</code> and <code>/api/v1/models</code>, measure latency, fingerprint the underlying OSS engine, and compute a 30-day rolling uptime from daily snapshots. See the <a href="/awesome-ai-api/reviews/methodology.md">methodology</a> for the full scoring formula.</p>

<h2>Is {escape(name)} safe to use?</h2>
<p>This page measures <b>reachability</b>, not <b>solvency</b>. A gateway can be online and still lose your deposit. Always start with a small top-up, verify Claude-Code / OpenAI-SDK compatibility, and keep an eye on the <a href="/awesome-ai-api/#blacklist">community blacklist</a>.</p>

<p><a class="cta" href="{escape(url)}" rel="nofollow noopener">Visit {escape(name)} →</a></p>

<hr>
<p class="note">Data licensed CC0. This page is auto-generated from <a href="https://github.com/MackDing/awesome-ai-api">awesome-ai-api</a>. Operator of {escape(name)} can request removal via PR to <code>data/sites.yaml</code>.</p>
</body>
</html>
"""
        (d / "index.html").write_text(html, encoding="utf-8")
        count += 1

    print(f"[ok] generated {count} per-gateway pages under docs/g/")


def build_engine_pages():
    """Generate /engine/<engine>/index.html listing all gateways running that engine."""
    data = json.loads((DOCS / "gateways.json").read_text(encoding="utf-8"))
    gws = data.get("gateways", [])
    out_dir = DOCS / "engine"
    out_dir.mkdir(exist_ok=True)

    by_engine: dict[str, list[dict]] = {}
    for g in gws:
        e = g.get("engine")
        if e:
            by_engine.setdefault(e, []).append(g)

    blurbs = {
        "new-api": "New API is a popular open-source fork of One API (QuantumNous / Calcium-Ion), adding Claude, MidJourney, and Suno relay support. Over half of Chinese 中转站 run on it.",
        "one-api": "One API (songquanpeng) is the original OpenAI-compatible aggregation gateway. MIT-licensed, 23k+ GitHub stars, the genesis of the CN relay ecosystem.",
        "dify": "Dify (langgenius) is an LLM app platform with a built-in gateway. Apache-2.0, 60k+ stars. Broader scope than pure relays — includes RAG, workflows, agents.",
        "litellm": "LiteLLM (BerriAI) is a Python SDK + proxy that unifies 100+ LLM APIs behind a single OpenAI-compatible interface. Strong observability story.",
        "openrouter": "OpenRouter pioneered the 'one key, any model' pattern. Hosted service, not self-hostable.",
        "portkey": "Portkey is an AI gateway with heavy enterprise observability, prompt versioning, and fallback chains.",
        "helicone": "Helicone is primarily an LLM observability tool that includes a proxy layer. MIT, YC-backed.",
        "fastgpt": "FastGPT (labring) is a Chinese knowledge-base app framework that exposes OpenAI-compatible endpoints.",
        "chatnext-web": "ChatGPT-Next-Web is a chat UI that often ships with its own API key management and can act as a thin gateway.",
    }

    count = 0
    for engine, entries in sorted(by_engine.items()):
        entries.sort(key=lambda g: (-(g.get("score") or 0), g.get("took_ms") or 9999))
        d = out_dir / engine
        d.mkdir(exist_ok=True)

        blurb = blurbs.get(engine, f"Gateways running the {engine} engine, tracked daily by awesome-ai-api.")
        page_url = f"https://mackding.github.io/awesome-ai-api/engine/{engine}/"

        rows = []
        for i, g in enumerate(entries[:50], start=1):
            medal = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, str(i))
            name = g.get("name", "?")
            slug = g.get("slug", "")
            api = "🔌" if g.get("has_api") else "·"
            rows.append(
                f'<tr><td>{medal}</td>'
                f'<td><a href="/awesome-ai-api/g/{slug}/">{escape(name)}</a></td>'
                f'<td>{g.get("region","—")}</td>'
                f'<td>{api}</td>'
                f'<td>{g.get("score","—")}</td></tr>'
            )

        jsonld = {
            "@context": "https://schema.org",
            "@type": "ItemList",
            "name": f"AI API gateways running {engine}",
            "url": page_url,
            "numberOfItems": len(entries),
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": i + 1,
                    "url": g.get("url"),
                    "name": g.get("name"),
                }
                for i, g in enumerate(entries[:20])
            ],
        }

        html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{len(entries)} gateways running {engine} — awesome-ai-api</title>
<meta name="description" content="{len(entries)} AI API gateways running the {engine} engine, verified daily. {blurb[:120]}">
<meta name="keywords" content="{engine}, {engine} gateway, {engine} API, AI relay, OpenAI compatible gateway, {engine} 中转站">
<link rel="canonical" href="{page_url}">
<meta property="og:title" content="{len(entries)} gateways running {engine}">
<meta property="og:description" content="{blurb[:160]}">
<meta property="og:url" content="{page_url}">
<meta property="og:image" content="https://mackding.github.io/awesome-ai-api/og-image.png">
<style>
  body{{font-family:-apple-system,Segoe UI,Helvetica Neue,sans-serif;max-width:820px;margin:0 auto;padding:2rem 1rem;color:#e0e6f0;background:#0d1117;line-height:1.55}}
  a{{color:#58a6ff}}
  h1{{font-size:1.8rem}}
  table{{width:100%;border-collapse:collapse;margin:1rem 0;font-size:.95rem}}
  th,td{{padding:.5rem;border-bottom:1px solid #30363d;text-align:left}}
  th{{color:#8b949e;font-weight:500}}
  nav{{margin-bottom:1.5rem;font-size:.85rem;color:#8b949e}}
</style>
<script type="application/ld+json">{escape(json.dumps(jsonld, ensure_ascii=False))}</script>
</head>
<body>
<nav><a href="/awesome-ai-api/">← awesome-ai-api</a></nav>
<h1>{len(entries)} gateways running <code>{engine}</code></h1>
<p>{blurb}</p>

<table>
  <thead><tr><th>#</th><th>Gateway</th><th>Region</th><th>API</th><th>Score</th></tr></thead>
  <tbody>
  {chr(10).join(rows)}
  </tbody>
</table>

<p><small>Data CC0 · Updated {data.get('updated','—')} · <a href="/awesome-ai-api/reviews/methodology.md">methodology</a></small></p>
</body>
</html>
"""
        (d / "index.html").write_text(html, encoding="utf-8")
        count += 1

    print(f"[ok] generated {count} per-engine pages under docs/engine/")


def build_sitemap():
    """Regenerate docs/sitemap.xml to include all gateway + engine pages."""
    data = json.loads((DOCS / "gateways.json").read_text(encoding="utf-8"))
    gws = data.get("gateways", [])
    engines = sorted({g.get("engine") for g in gws if g.get("engine")})
    today = datetime.now(SGT).strftime("%Y-%m-%d")

    urls = [
        ("https://mackding.github.io/awesome-ai-api/", "1.0", "daily"),
        ("https://mackding.github.io/awesome-ai-api/zh/", "1.0", "daily"),
    ]
    for g in gws:
        slug = g.get("slug")
        if slug:
            urls.append((f"https://mackding.github.io/awesome-ai-api/g/{slug}/", "0.6", "weekly"))
    for e in engines:
        urls.append((f"https://mackding.github.io/awesome-ai-api/engine/{e}/", "0.7", "weekly"))

    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]
    for u, prio, freq in urls:
        parts.append(
            f"  <url><loc>{u}</loc><lastmod>{today}</lastmod>"
            f"<changefreq>{freq}</changefreq><priority>{prio}</priority></url>"
        )
    # EN ↔ ZH hreflang for the two main pages
    parts[2] = (
        '  <url>\n'
        '    <loc>https://mackding.github.io/awesome-ai-api/</loc>\n'
        f'    <lastmod>{today}</lastmod><changefreq>daily</changefreq><priority>1.0</priority>\n'
        '    <xhtml:link rel="alternate" hreflang="en" href="https://mackding.github.io/awesome-ai-api/"/>\n'
        '    <xhtml:link rel="alternate" hreflang="zh" href="https://mackding.github.io/awesome-ai-api/zh/"/>\n'
        '  </url>'
    )
    parts[3] = (
        '  <url>\n'
        '    <loc>https://mackding.github.io/awesome-ai-api/zh/</loc>\n'
        f'    <lastmod>{today}</lastmod><changefreq>daily</changefreq><priority>1.0</priority>\n'
        '    <xhtml:link rel="alternate" hreflang="en" href="https://mackding.github.io/awesome-ai-api/"/>\n'
        '    <xhtml:link rel="alternate" hreflang="zh" href="https://mackding.github.io/awesome-ai-api/zh/"/>\n'
        '  </url>'
    )
    parts.append("</urlset>")
    (DOCS / "sitemap.xml").write_text("\n".join(parts) + "\n", encoding="utf-8")
    print(f"[ok] sitemap.xml ({len(urls)} URLs)")


def build_ai_manifest():
    """GEO assets: ai-plugin.json (OpenAI) + openapi.yaml + enriched llms.txt."""
    wk = DOCS / ".well-known"
    wk.mkdir(exist_ok=True)

    plugin = {
        "schema_version": "v1",
        "name_for_human": "awesome-ai-api",
        "name_for_model": "awesome_ai_api",
        "description_for_human": "Daily-refreshed leaderboard of 200+ AI API gateways, CC0 data.",
        "description_for_model": "Use this dataset to look up AI API gateways (OpenAI-compatible relays). Each entry includes URL, 30-day uptime, latency, OSS engine, score, and models observed. Ground truth: the /v1/models probe runs daily.",
        "auth": {"type": "none"},
        "api": {
            "type": "openapi",
            "url": "https://mackding.github.io/awesome-ai-api/.well-known/openapi.yaml",
        },
        "logo_url": "https://mackding.github.io/awesome-ai-api/og-image.png",
        "contact_email": "noreply@github.com",
        "legal_info_url": "https://github.com/MackDing/awesome-ai-api",
    }
    (wk / "ai-plugin.json").write_text(json.dumps(plugin, indent=2), encoding="utf-8")

    openapi = """openapi: 3.1.0
info:
  title: awesome-ai-api
  version: '1.0'
  description: Static JSON dataset of AI API gateways, refreshed daily.
  license: { name: CC0, url: https://creativecommons.org/publicdomain/zero/1.0/ }
servers:
  - url: https://mackding.github.io/awesome-ai-api
paths:
  /gateways.json:
    get:
      summary: Full leaderboard snapshot
      responses:
        '200':
          description: JSON array of gateway records
          content:
            application/json: {}
  /gateways.csv:
    get:
      summary: Same data, CSV
      responses: { '200': { description: CSV } }
  /feed.xml:
    get:
      summary: RSS of Top-20 daily
      responses: { '200': { description: RSS 2.0 } }
  /llms-full.txt:
    get:
      summary: LLM-friendly plaintext dump
      responses: { '200': { description: text/plain } }
"""
    (wk / "openapi.yaml").write_text(openapi, encoding="utf-8")

    # Enrich llms.txt at site root with direct links to per-gateway pages for the Top 20
    data = json.loads((DOCS / "gateways.json").read_text(encoding="utf-8"))
    top = data.get("gateways", [])[:20]
    lines = [
        "# awesome-ai-api",
        "",
        "> Daily-refreshed leaderboard of 200+ AI API gateways (OpenAI-compatible relays).",
        "> License: MIT (code) + CC0 (data). Canonical: https://mackding.github.io/awesome-ai-api/",
        "",
        "## Primary resources",
        "- [Full dataset JSON](https://mackding.github.io/awesome-ai-api/gateways.json)",
        "- [Full dataset CSV](https://mackding.github.io/awesome-ai-api/gateways.csv)",
        "- [RSS feed (Top 20)](https://mackding.github.io/awesome-ai-api/feed.xml)",
        "- [Full plaintext dump](https://mackding.github.io/awesome-ai-api/llms-full.txt)",
        "- [OpenAPI spec](https://mackding.github.io/awesome-ai-api/.well-known/openapi.yaml)",
        "- [Scoring methodology](https://github.com/MackDing/awesome-ai-api/blob/master/reviews/methodology.md)",
        "",
        "## Top 20 gateways (detailed pages)",
    ]
    for i, g in enumerate(top, start=1):
        lines.append(
            f"- [{g.get('name','?')}](https://mackding.github.io/awesome-ai-api/g/{g.get('slug')}/) "
            f"— score {g.get('score','—')}, {'API✓' if g.get('has_api') else 'unverified'}, engine {g.get('engine') or 'unknown'}"
        )
    (DOCS / "llms.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("[ok] .well-known/ai-plugin.json + openapi.yaml + enriched llms.txt")


def main() -> int:
    copy_gateways()
    build_csv()
    build_rss()
    build_llms_full()
    build_stats()
    build_gateway_pages()
    build_engine_pages()
    build_sitemap()
    build_ai_manifest()
    return 0


if __name__ == "__main__":
    sys.exit(main())
