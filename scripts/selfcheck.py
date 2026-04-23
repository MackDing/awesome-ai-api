#!/usr/bin/env python3
"""Self-check: verify the Pages site is consistent with the source data.

Run locally: `python scripts/selfcheck.py`
Run in CI:   exits non-zero if any check fails, blocking the commit.

Checks:
  1. docs/gateways.json exists and equals data/gateways.json (byte-identical copy).
  2. docs/index.html has SSR'd numbers that match gateways.json (no em-dash sentinels).
  3. docs/zh/index.html likewise.
  4. docs/gateways.csv row count == number of gateways.
  5. docs/feed.xml is valid XML with at least 1 item.
  6. llms.txt, sitemap.xml, robots.txt, og-image.png all present and non-empty.
  7. README top-10 table contains at least 5 verified (🔌) entries.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"

failures: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)
    print(f"  ❌ {msg}")


def ok(msg: str) -> None:
    print(f"  ✅ {msg}")


def check_json_mirror() -> dict:
    print("\n[1/7] gateways.json mirror")
    src = DATA / "gateways.json"
    dst = DOCS / "gateways.json"
    if not dst.exists():
        fail("docs/gateways.json missing")
        return {}
    if src.read_bytes() != dst.read_bytes():
        fail("docs/gateways.json ≠ data/gateways.json (rebuild site)")
        return json.loads(dst.read_text(encoding="utf-8"))
    ok("docs/gateways.json mirrors data/gateways.json")
    return json.loads(dst.read_text(encoding="utf-8"))


def check_index_html(data: dict, path: Path, label: str) -> None:
    print(f"\n[2/7] {label} SSR stats")
    if not path.exists():
        fail(f"{path} missing")
        return
    html = path.read_text(encoding="utf-8")

    if "—<" in html and 'id="s-' in html.replace("—<", ""):
        # em-dash sentinel still present between a stat id and closing tag
        pass  # allow, will be caught by value check

    total = data.get("total", len(data.get("gateways", [])))
    api_n = sum(1 for g in data.get("gateways", []) if g.get("has_api"))

    m = re.search(r'id="s-total">([^<]*)<', html)
    if not m or m.group(1).strip() != str(total):
        fail(f"{label}: s-total expected {total}, got {m and m.group(1)!r}")
    else:
        ok(f"{label}: s-total = {total}")

    m = re.search(r'id="s-api">([^<]*)<', html)
    if not m or m.group(1).strip() != str(api_n):
        fail(f"{label}: s-api expected {api_n}, got {m and m.group(1)!r}")
    else:
        ok(f"{label}: s-api = {api_n}")

    m = re.search(r'id="s-updated">([^<]*)<', html)
    if not m or m.group(1).strip() in ("", "—"):
        fail(f"{label}: s-updated is empty/em-dash")
    else:
        ok(f"{label}: s-updated = {m.group(1)}")

    # must have a rendered table (not "Loading…" placeholder)
    body = re.search(r'<tbody id="leaderboard-body">(.*?)</tbody>', html, re.S)
    if not body:
        fail(f"{label}: missing leaderboard-body")
    elif "Loading" in body.group(1) or "加载中" in body.group(1):
        fail(f"{label}: leaderboard body still shows placeholder 'Loading…'")
    else:
        rows = len(re.findall(r"<tr>", body.group(1)))
        if rows < 10:
            fail(f"{label}: leaderboard has only {rows} rows, expected ≥10")
        else:
            ok(f"{label}: leaderboard has {rows} SSR rows")


def check_csv(data: dict) -> None:
    print("\n[4/7] gateways.csv")
    p = DOCS / "gateways.csv"
    if not p.exists():
        fail("docs/gateways.csv missing")
        return
    with p.open(encoding="utf-8") as f:
        rows = list(csv.reader(f))
    data_rows = len(rows) - 1  # minus header
    expected = len(data.get("gateways", []))
    if data_rows != expected:
        fail(f"CSV rows {data_rows} ≠ gateways {expected}")
    else:
        ok(f"CSV has {data_rows} rows")


def check_feed() -> None:
    print("\n[5/7] feed.xml")
    p = DOCS / "feed.xml"
    if not p.exists():
        fail("docs/feed.xml missing")
        return
    try:
        tree = ET.parse(p)
    except ET.ParseError as e:
        fail(f"feed.xml not valid XML: {e}")
        return
    items = tree.findall(".//item")
    if len(items) < 1:
        fail(f"feed.xml has {len(items)} items, expected ≥1")
    else:
        ok(f"feed.xml has {len(items)} items")


def check_assets() -> None:
    print("\n[6/7] static assets")
    for name in ("llms.txt", "sitemap.xml", "robots.txt", "og-image.png"):
        p = DOCS / name
        if not p.exists() or p.stat().st_size == 0:
            fail(f"docs/{name} missing or empty")
        else:
            ok(f"docs/{name} ({p.stat().st_size} bytes)")


def check_readme() -> None:
    print("\n[7/7] README top-30 sanity")
    readme = ROOT / "README.md"
    if not readme.exists():
        fail("README.md missing")
        return
    text = readme.read_text(encoding="utf-8")
    # Look inside the generated leaderboard table (first 15 KB is enough to cover Top 30).
    section = text[:15000]
    api_rows = section.count("🔌")
    if api_rows < 10:
        fail(f"README top-30 section shows only {api_rows} 🔌 entries, expected ≥10")
    else:
        ok(f"README top-30 shows {api_rows} 🔌 entries")


def check_no_duplicate_names() -> None:
    print("\n[8/9] no duplicate display names in gateways.json")
    from collections import Counter
    data = json.loads((DOCS / "gateways.json").read_text(encoding="utf-8"))
    counts = Counter(g["name"] for g in data.get("gateways", []))
    dupes = {n: c for n, c in counts.items() if c > 1}
    if dupes:
        fail(f"{len(dupes)} duplicate display name(s): {dict(list(dupes.items())[:5])}")
    else:
        ok(f"all {len(counts)} display names are unique")


def check_subpages() -> None:
    print("\n[9/9] per-gateway + per-engine landing pages")
    data = json.loads((DOCS / "gateways.json").read_text(encoding="utf-8"))
    gws = data.get("gateways", [])
    expected_gw = sum(1 for g in gws if g.get("slug"))
    got_gw = len(list((DOCS / "g").glob("*/index.html"))) if (DOCS / "g").exists() else 0
    if got_gw < expected_gw:
        fail(f"per-gateway pages: got {got_gw}, expected {expected_gw}")
    else:
        ok(f"per-gateway pages: {got_gw}/{expected_gw}")

    engines = {g["engine"] for g in gws if g.get("engine")}
    got_eng = len(list((DOCS / "engine").glob("*/index.html"))) if (DOCS / "engine").exists() else 0
    if got_eng < len(engines):
        fail(f"per-engine pages: got {got_eng}, expected {len(engines)}")
    else:
        ok(f"per-engine pages: {got_eng}/{len(engines)}")

    # .well-known assets
    for rel in (".well-known/ai-plugin.json", ".well-known/openapi.yaml"):
        p = DOCS / rel
        if not p.exists() or p.stat().st_size == 0:
            fail(f"{rel} missing or empty")
        else:
            ok(f"{rel} present")


def main() -> int:
    print("🔎 awesome-ai-api self-check\n")
    data = check_json_mirror()
    if data:
        check_index_html(data, DOCS / "index.html", "docs/index.html")
        check_index_html(data, DOCS / "zh" / "index.html", "docs/zh/index.html")
        check_csv(data)
    check_feed()
    check_assets()
    check_readme()
    check_no_duplicate_names()
    check_subpages()

    print("\n" + "=" * 50)
    if failures:
        print(f"❌ {len(failures)} check(s) failed:")
        for f in failures:
            print(f"   - {f}")
        return 1
    print("✅ All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
