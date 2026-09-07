# AIgateway

> Unified OpenAI-compatible API for 1,000+ models from 85+ labs — text, image, video, audio, embeddings — at pass-through provider pricing plus a flat 5% on top-ups.

**[aigateway.sh](https://aigateway.sh)** · **[Pricing](https://aigateway.sh/models)** · **[Docs](https://aigateway.sh/docs)**

---

## Quick Facts | 基本信息

| Field | Value |
|-------|-------|
| **Founded** | 2026-04 |
| **Base Region** | Global (edge-native, Cloudflare Workers) |
| **Target Users** | Developers, agent builders, multi-tenant SaaS |
| **Site Language** | EN |
| **API Compatible With** | OpenAI-compatible + native Anthropic Messages (`/v1/messages`) |
| **Claude Code Support** | ✅ (set `ANTHROPIC_BASE_URL=https://api.aigateway.sh`) |
| **Last Verified** | 2026-09-07 |

## Pricing | 定价

*Prices in USD per 1M tokens.*

| Model | Input | Output | Official | Diff |
|-------|-------|--------|----------|------|
| Claude Opus 4.7 | $5.00 | $25.00 | $5 / $25 | 0% (pass-through + 5% on top-up) |
| Claude Sonnet 4.6 | $3.00 | $15.00 | $3 / $15 | 0% |
| GPT-5.4 | $2.50 | $15.00 | $2.50 / $15 | 0% |
| Gemini 3.7 Flash | $0.75 | $3.75 | $0.75 / $3.75 | 0% |
| Kimi K2.7 Code | $0.95 | $4.00 | $0.95 / $4 | 0% |
| GLM-5.3 Flash | $0.15 | $0.50 | — | hosted-dispatch price |
| DeepSeek V4 Pro (0813) | $1.32 | $3.96 | — | hosted-dispatch price |

Pass-through provider pricing: the listed price is what you pay per token; the only fee is a flat 5% added when purchasing credit top-ups. Cache hits bill at a discount. New accounts get $1 credit on a trial catalog after adding a card (no charge).

## Supported Models | 支持模型

- **Anthropic**: Claude Opus/Sonnet/Haiku 4.x
- **OpenAI**: GPT-5.4 family, gpt-oss, o-series
- **Google**: Gemini 3.x Pro/Flash, Imagen
- **DeepSeek**: V4 Pro/Flash
- **Moonshot**: Kimi K3, K2.7 Code
- **Z.ai**: GLM-5.3, GLM-5.3 Flash, GLM-5.2
- **Meta**: Llama 4
- **Alibaba**: Qwen 3.8 Max
- **Others**: 1,000+ total across 85+ labs, every modality (text, image, video, audio, embeddings)

## Payment Methods | 支付方式

- 💳 Credit card (Stripe)
- ❌ No Alipay/WeChat
- ❌ No crypto

## Features | 特色功能

- **OpenAI-compatible + Anthropic Messages** — drop-in for both SDKs; Claude Code works via `ANTHROPIC_BASE_URL`
- **Sub-accounts API** — mint scoped per-customer keys with spend caps and isolated analytics; a billing layer for multi-tenant AI apps
- **Eval-driven routing** — POST a dataset plus candidate models, get back an alias that routes to the eval winner
- **Three-tier response cache** — exact (KV), semantic (Vectorize), prompt-prefix; cache hits bill at a discount
- **MCP server** — `api.aigateway.sh/mcp` with model-discovery tools
- **Open-source CLI** (`aig`), Python + JS SDKs, `aig migrate` from 8 gateways

## Pros & Cons | 优缺点

**Pros | 优势**
- Largest catalog of any gateway here (1,000+ models, every modality)
- Transparent pricing: pass-through, single flat 5% fee on top-ups, no per-request markup
- Independent infrastructure (own gateway code, not a one-api/new-api re-skin)
- Native Claude Code support

**Cons | 劣势**
- No Alipay/WeChat — hard for Chinese users without a card
- Young service (founded 2026-04)
- No published SLA yet

## Review Score | 评分

| Dimension | Score (/10) | Note |
|-----------|-------------|------|
| **Price** | 9 | Pass-through + flat 5% on top-ups only |
| **Latency** | 9 | Edge-native on Cloudflare Workers; p50 overhead <50ms |
| **Stability** | 7 | Young service; /status page live |
| **Model Coverage** | 10 | 1,000+ models, 85+ labs, all modalities |
| **Support** | 7 | Founder-run support, Discord |
| **Payment UX** | 6 | Card only (Stripe) |
| **Overall** | **8** | |

## Benchmark Data | 基准数据

Last run: 2026-09-07 (operator self-reported)

| Endpoint | Status | Latency |
|----------|--------|---------|
| `GET https://api.aigateway.sh/v1/models` | 200 | ~350 ms (1,065 models returned) |
| `GET /v1/balance` | 200 | — |

## User Reviews | 用户评价

*None yet — new listing.*

## Changelog | 更新日志

- `2026-09-07` — Initial entry

---

**Conflict of interest disclosure** | **利益相关声明**: Entry submitted by the founder of AIgateway. All prices verified against the live `/v1/models` endpoint on 2026-09-07; review scores are self-assessed and flagged as such.
