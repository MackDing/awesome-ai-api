# Scoring Methodology

> How awesome-ai-api ranks 200+ AI API gateways. Fully open, fully reproducible, no black box.

**TL;DR** — every gateway goes through 3 automated passes daily: reachability, `/v1/models` probe, engine fingerprint. Then we compute a 0–9.9 score from 6 signals. The exact formula lives in [`scripts/generate_leaderboard.py`](../scripts/generate_leaderboard.py).

---

## 1. Pipeline

```
  candidates.txt (350 URLs, community-contributed + auto-discovered)
          │
          ▼
  ┌────────────────────┐
  │ validate_candidates │  ← concurrent HTTP fetches, bilingual keyword lexicon
  └────────────────────┘
          │
          ▼
  ┌────────────────────┐
  │     probe_api      │  ← GET /v1/models + /api/v1/models
  └────────────────────┘
          │
          ▼
  ┌────────────────────┐
  │   detect_engine    │  ← fingerprint: new-api, one-api, dify, litellm, …
  └────────────────────┘
          │
          ▼
  ┌────────────────────┐
  │  compute_uptime    │  ← 30-day rolling % from data/history snapshots
  └────────────────────┘
          │
          ▼
   data/gateways.json   ← structured output, CC0
   data/_leaderboard.md ← README table
```

Source of truth: every step commits its artifact to Git, so the full history of every gateway's score is re-runnable and auditable.

---

## 2. Verdict buckets

| Badge | Verdict | Criteria |
|---|---|---|
| 🟢 | `likely_relay` | ≥ 2 relay keywords AND ≥ 2 model keywords, OR `/v1/models` probe succeeded |
| 🟡 | `probable_relay` | ≥ 1 relay keyword AND ≥ 3 model keywords |
| 🧰 | `open_source_tool` | GitHub repo that self-describes as a gateway |
| 🔍 | `needs_review` | reachable but insufficient signal |
| 🚫 | `unreachable` | HTTP failure, timeout, or no auth-hint on endpoint |

**The `/v1/models` probe** is the ground-truth signal. A gateway that returns JSON model list (or 401/403 "missing api_key") at this path has a real AI API. Everything else is marketing.

---

## 3. Score formula

```python
score = 6.0
  + 1.5   if verdict == "likely_relay"
  + 0.8   if verdict == "probable_relay"
  + 1.5   if has_api            # biggest single factor
  + 0.4   if real_models_count >= 50
  + 0.2   if real_models_count >= 10
  + 0.1 × len(model_keywords)   # capped at +0.5
  + 0.2   if payment_hints
  - 0.3   if latency > 3000 ms
  + 0.5   if uptime_pct >= 99
  + 0.3   if uptime_pct >= 95
  - 0.4   if uptime_pct < 80 (with ≥3 samples)

  (capped at 9.9)
```

Sorting: `has_api` desc → `score` desc → `latency` asc → `name` alpha.

### Why each signal

| Signal | Rationale |
|---|---|
| `verdict` | Captures landing-page authenticity. Keyword density isn't enough on its own but rewards obvious relays. |
| `has_api` | The single most predictive signal. 200 + JSON `data:[...]`, or 401 `missing api_key`, = real API. |
| `real_models_count` | Open `/v1/models` responses often list every real model. Quantifies scope. |
| `payment_hints` | Indicates a consumer product, not a dev toy. |
| `latency` | Proxy for operator seriousness (CDN, region choice, caching). |
| `uptime_pct` | 30-day rolling from daily snapshots. New gateways take ~3 samples to start accruing. |

---

## 4. Engine fingerprinting

Most Chinese 中转站 are thin skins on one of ≤ 15 OSS projects. We scan the landing page HTML and response headers for signatures:

| Engine | Signatures |
|---|---|
| `new-api` | `/static/js/new-api`, `NewAPI`, `Calcium-Ion`, `QuantumNous` |
| `one-api` | `songquanpeng/one-api`, `one-api-web`, `One API` |
| `dify` | `Dify`, `langgenius`, `dify.ai` |
| `litellm` | `LiteLLM`, `BerriAI` |
| `openrouter` | `openrouter.ai` in content |
| `portkey`, `fastgpt`, `helicone`, `langdb`, `chatnext-web`, `lobe-chat` | … |

Why it matters: knowing the engine lets users predict update cadence, security posture, and Claude-Code compatibility. A site running year-old One API unpatched is a liability regardless of its UI.

---

## 5. What we don't measure (yet)

- **Actual token latency / TTFT** — would require live API keys; planned for P3.
- **Pricing per model** — hard to scrape reliably without HTML-specific parsers.
- **Solvency / rug-pull risk** — no automated signal; users report to the [blacklist](../data/blacklist.json).

---

## 6. Reproducibility

Every daily run produces:
- `data/gateways.json` — current state
- `data/history/YYYY-MM-DD.json` — immutable snapshot
- `data/uptime.json` — rolling 30-day window

Re-run locally: `python scripts/validate_candidates.py && python scripts/compute_uptime.py && python scripts/render_blacklist.py && python scripts/generate_leaderboard.py && python scripts/build_site.py`.

---

## 7. Responsible use

- Scores describe **current reachability**, not **future solvency**. Start small.
- We reach each gateway once per day with a clearly-identified bot UA.
- We do **not** scrape behind any login wall or use harvested API keys.
- Operators who want off the list can PR `data/sites.yaml` with `verdict: hidden`.

---

_Last reviewed: 2026-04-23. Changes to the formula are tagged in `CHANGELOG.md` and announced in [GitHub Discussions](https://github.com/MackDing/awesome-ai-api/discussions)._
