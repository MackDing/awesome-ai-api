---
license: mit
task_categories:
- text-classification
- question-answering
language:
- en
- zh
tags:
- ai-api
- llm
- gateway
- openai-compatible
- claude
- gpt
- gemini
- deepseek
- china
- resellers
pretty_name: awesome-ai-api gateway leaderboard
size_categories:
- n<1K
---

# awesome-ai-api: The Open Leaderboard of AI API Gateways

Daily-refreshed, machine-verified dataset of 200+ AI API gateways and relays
(OpenAI-compatible services that expose Claude, GPT, Gemini, DeepSeek, Qwen, etc.).

- **Source repo:** https://github.com/MackDing/awesome-ai-api
- **Live site:** https://mackding.github.io/awesome-ai-api/
- **License:** MIT (code) + CC0 (data)
- **Update cadence:** daily, 10:00 SGT (UTC+8)

## What's inside

| Column | Meaning |
|---|---|
| `name`         | Human-curated gateway name |
| `url`          | Canonical URL |
| `region`       | `cn` / `global` / `self-hosted` |
| `score`        | 0–9.9 composite (reachability + API + models + uptime) |
| `verdict`      | `likely_relay` / `probable_relay` / `open_source_tool` / `needs_review` |
| `has_api`      | Whether `/v1/models` is confirmed live |
| `engine`       | Identified OSS engine (new-api, one-api, dify, litellm, …) |
| `real_models_count` | # of models exposed when the endpoint is open |
| `uptime.uptime_pct` | 30-day rolling uptime % |
| `took_ms`      | Latency at last probe |

## Why this exists

Other AI API trackers either hand-curate Western services (missing 90% of the
Chinese 中转站 ecosystem) or compare only price (not authenticity or survival).
We probe every gateway daily and publish the raw data.

## Citation

```
@software{awesome_ai_api_2026,
  author  = {Mack Ding and contributors},
  title   = {awesome-ai-api: The Open Leaderboard of AI API Gateways},
  year    = {2026},
  url     = {https://github.com/MackDing/awesome-ai-api},
  license = {MIT}
}
```
