#!/usr/bin/env python3
"""Render data/blacklist.json → data/blacklist.md (bilingual, auto-generated)."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

SGT = timezone(timedelta(hours=8))
ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "blacklist.json"
OUT = ROOT / "data" / "blacklist.md"

SEVERITY_LABELS_EN = {
    "rug_pull": "🏃 Rug pull",
    "fake_models": "🎭 Fake models",
    "data_leak": "💧 Data leak",
    "unauthorized_charge": "💳 Unauthorized charge",
    "banned_upstream": "🚫 Upstream banned",
}
SEVERITY_LABELS_ZH = {
    "rug_pull": "🏃 跑路",
    "fake_models": "🎭 假模型",
    "data_leak": "💧 数据泄露",
    "unauthorized_charge": "💳 擅自扣费",
    "banned_upstream": "🚫 上游封号",
}


def render() -> str:
    data = json.loads(SRC.read_text(encoding="utf-8"))
    entries = data.get("entries", [])
    updated = datetime.now(SGT).strftime("%Y-%m-%d")

    lines: list[str] = [
        "# Blacklist | 黑名单",
        "",
        f"_Last updated: {updated} (SGT) · auto-generated from [blacklist.json](./blacklist.json)_",
        "",
        "Gateways flagged for **serious**, **verified** issues. Listing here requires multiple independent reports and public evidence.",
        "",
        "被标注为**严重**并经**验证**的中转站。上榜需多条独立举报 + 公开证据。",
        "",
        "---",
        "",
        f"## Current entries ({len(entries)}) | 当前条目",
        "",
    ]
    if not entries:
        lines += ["*No entries yet.* | *暂无条目。*", ""]
    else:
        lines.append("| Gateway | Severity | Reported | Summary | Evidence | Status |")
        lines.append("|---------|----------|----------|---------|----------|--------|")
        for e in entries:
            sev = SEVERITY_LABELS_EN.get(e["severity"], e["severity"])
            evid_md = " · ".join(f"[{x['source']}]({x['link']})" for x in e.get("evidence", []))
            status = "🟢 Resolved" if e.get("resolved") else ("🟡 Responded" if e.get("operator_response", {}).get("responded") else "🔴 Open")
            lines.append(f"| [{e['slug']}]({e['url']}) | {sev} | {e['reported']} | {e['summary']} | {evid_md} | {status} |")
        lines.append("")

    # Policy section
    policy = data.get("policy", {})
    if policy:
        lines += [
            "---",
            "",
            "## How an entry gets here | 如何被列入",
            "",
        ]
        for crit in policy.get("inclusion_criteria", []):
            lines.append(f"- {crit}")
        lines += [
            "",
            "## Severity types | 严重性分类",
            "",
        ]
        for k, v in policy.get("severities", {}).items():
            lines.append(f"- **{SEVERITY_LABELS_EN.get(k, k)}** — {v}")
        lines += ["", "## Removal | 移除", "", policy.get("removal", ""), ""]

    lines += [
        "---",
        "",
        "## Good-faith disclosure | 善意声明",
        "",
        "This blacklist is a **factual record of complaints**, not defamation. We link to public evidence and allow operators to respond.",
        "",
        "本黑名单是**投诉事实记录**，非诽谤。所有条目均有公开证据并允许当事方答辩。",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    OUT.write_text(render(), encoding="utf-8")
    print(f"[ok] blacklist.md rendered → {OUT}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
