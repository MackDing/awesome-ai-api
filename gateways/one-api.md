# One API (self-hosted)

> Open-source unified LLM gateway. Run your own reseller / internal quota system. 20k+ GitHub stars.

**[GitHub](https://github.com/songquanpeng/one-api)** · **[Docs](https://github.com/songquanpeng/one-api#readme)**

---

## Quick Facts

| Field | Value |
|-------|-------|
| **Founded** | 2023 |
| **Base Region** | Self-hosted (anywhere) |
| **Target Users** | Teams, OPCs, resellers |
| **Site Language** | English / Chinese |
| **API Compatible With** | OpenAI-compatible |
| **Claude Code Support** | ✅ (with Anthropic channel) |
| **Last Verified** | 2026-04-22 |

## Pricing

Zero cost for the software (MIT-style license). You pay:
- Upstream provider costs (pass-through)
- Your own hosting ($5/mo VPS is enough)

## Supported Models

Any model exposed via an OpenAI-compatible endpoint can be added as a "channel":
- OpenAI, Anthropic, Google, Mistral, Cohere, xAI, DeepSeek, Moonshot, Zhipu, Alibaba…
- Any upstream reseller (as a channel)
- Self-hosted LLMs (llama.cpp, vLLM, Ollama, LM Studio…)

## Payment Methods

- N/A for the gateway itself
- Upstream providers and your own billing plugin (e.g. EasyPay, Stripe)

## Features

- **Multi-channel routing** with priority and weight
- **Per-user API keys** with quotas and rate limits
- **Token-based billing** to end users
- **Admin dashboard** with usage charts
- **Logs and auditing**
- **Docker one-liner deployment**

## Pros & Cons

**Pros**
- Total ownership — your keys, your data, your margin
- Cheap to run; scales to thousands of users on a small VPS
- Huge community, forks, and themes (NewAPI, VoAPI…)
- Can wrap *any* upstream, including other resellers

**Cons**
- You handle uptime, security, abuse, and billing yourself
- UI and docs are CN-first; English polish uneven
- Upgrades occasionally break schemas — back up before updating
- No built-in observability; bring your own logging

## Review Score

| Dimension | Score (/10) | Note |
|-----------|-------------|------|
| Price | 10.0 | Free + infra cost only |
| Latency | 9.0 | Depends on your deployment |
| Stability | 8.5 | Your job to keep it up |
| Model Coverage | 9.5 | As broad as your channels |
| Support | 8.0 | Community-driven |
| Payment UX | 9.0 | Via plugins |
| **Overall** | **9.2** | |

## User Reviews

- Very popular among Chinese developers building their own reseller businesses
- Large ecosystem of forks: `NewAPI`, `VoAPI`, `songquanpeng/one-api` upstream remains the canonical base

## Changelog

- `2026-04-22` — Initial entry

---

**Conflict of interest disclosure**: None. The maintainer (Mack) runs One API internally but has no affiliation with the upstream project.
