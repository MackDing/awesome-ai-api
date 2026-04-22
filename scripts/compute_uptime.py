#!/usr/bin/env python3
"""Compute 30-day uptime from data/history/*.json snapshots.

For each gateway URL, look at the last N days of snapshots and compute:
  - samples:   number of days we have data
  - uptime_%:  % of samples where gateway was reachable + has_api (if ever true)
  - avg_ms:    average latency across reachable samples
  - streak:    current consecutive-days reachable streak

Writes: data/uptime.json  (keyed by url)

This is cheap (O(files * gateways)) and can be run after every validator run
or independently in the daily cron.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from statistics import mean

SGT = timezone(timedelta(hours=8))
WINDOW_DAYS = 30
ROOT = Path(__file__).resolve().parent.parent
HIST = ROOT / "data" / "history"
OUT = ROOT / "data" / "uptime.json"


def main() -> int:
    if not HIST.exists():
        print("[warn] no history dir", file=sys.stderr)
        OUT.write_text(json.dumps({}), encoding="utf-8")
        return 0

    today = datetime.now(SGT).date()
    cutoff = today - timedelta(days=WINDOW_DAYS - 1)

    # (url) -> {samples, reachable_days, api_days, latencies, last_day_reachable?, recent_streak}
    agg: dict[str, dict] = {}

    files = sorted(HIST.glob("*.json"))
    for f in files:
        try:
            day = datetime.strptime(f.stem, "%Y-%m-%d").date()
        except ValueError:
            continue
        if day < cutoff or day > today:
            continue
        try:
            snap = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        seen_urls = set()
        for g in snap.get("gateways", []):
            url = g.get("url")
            if not url or url in seen_urls:
                continue
            seen_urls.add(url)
            slot = agg.setdefault(
                url,
                {"samples": 0, "reachable_days": 0, "api_days": 0, "latencies": [], "days_list": []},
            )
            slot["samples"] += 1
            # reachable = entry exists in snapshot (generator excludes unreachable)
            slot["reachable_days"] += 1
            slot["days_list"].append(day.isoformat())
            if g.get("has_api"):
                slot["api_days"] += 1
            if g.get("took_ms"):
                slot["latencies"].append(int(g["took_ms"]))

    # compute stats
    n_windows = min(WINDOW_DAYS, len(files))
    out: dict[str, dict] = {}
    for url, slot in agg.items():
        uptime_pct = round(slot["reachable_days"] / n_windows * 100, 1) if n_windows else 0.0
        api_pct = round(slot["api_days"] / n_windows * 100, 1) if n_windows else 0.0
        avg_ms = int(mean(slot["latencies"])) if slot["latencies"] else None
        # recent streak: consecutive trailing days present
        days_seen = set(slot["days_list"])
        streak = 0
        probe_day = today
        while probe_day.isoformat() in days_seen:
            streak += 1
            probe_day -= timedelta(days=1)
        out[url] = {
            "samples": slot["samples"],
            "window_days": n_windows,
            "uptime_pct": uptime_pct,
            "api_uptime_pct": api_pct,
            "avg_latency_ms": avg_ms,
            "streak_days": streak,
        }

    OUT.write_text(json.dumps({"window_days": n_windows, "updated": today.isoformat(), "gateways": out}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[ok] uptime for {len(out)} gateways over {n_windows} days → {OUT}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
