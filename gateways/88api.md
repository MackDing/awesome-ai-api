# 88API

> Hong Kong-operated multi-provider AI API gateway with public model-level pricing and OpenAI-, Anthropic-, and Gemini-compatible routes.

**[Official Website](https://88api.ai/)** · **[Pricing](https://88api.ai/pricing)** · **[Docs](https://88api.ai/zh/docs/)**

---

## Quick Facts | 基本信息

| Field | Value |
|-------|-------|
| **Service launched** | 2026-05 ([domain registration: 2026-05-07](https://rdap.org/domain/88api.ai)) |
| **Current operator** | 88 DIGITAL TECHNOLOGY LIMITED, incorporated in Hong Kong on 2026-07-17 |
| **Base Region** | Hong Kong / Global |
| **Target Users** | Developers, AI coding users, OPC, and enterprise teams |
| **Site Language** | Chinese, English, Japanese, French, Russian, Vietnamese, and Traditional Chinese |
| **API Compatible With** | OpenAI Chat/Responses, Anthropic Messages, and Gemini |
| **Claude Code Support** | ✅ [Documented](https://88api.ai/zh/docs/apps/claude-code/); model and channel dependent |
| **Last Verified** | 2026-09-09 |

## Pricing | 定价

The values below are displayed by the public model marketplace in its default
"Standard" view. Text-model prices are CNY per 1M tokens. Group selection,
dynamic time tiers, context length, and model availability can change the final
billed price. Check the live [model marketplace](https://88api.ai/pricing) or
machine-readable [pricing catalog](https://88api.ai/api/pricing) before use.

| Model | Input | Output | Billing note |
|-------|-------|--------|--------------|
| GPT-6 Astra | ¥3.50 | ¥17.50 | Dynamic token pricing |
| Claude Sonnet 4.6 | ¥1.05 | ¥5.25 | Cache: ¥0.105 / 1M |
| Claude Opus 4.6 | ¥1.75 | ¥8.75 | Cache: ¥0.175 / 1M |
| Gemini 3.1 Pro Preview | ¥4.20 | ¥25.20 | Dynamic token pricing |
| DeepSeek V4 Pro | ¥4.50 | ¥13.50 | Dynamic time- and group-based pricing |
| Gemini 3.1 Flash Image | — | — | ¥0.15 per request |
| Seedance 2.5 720p Official | — | — | ¥1.20 per second |

Prices observed on 2026-09-09. The live catalog is authoritative.

## Supported Models | 支持模型

The public catalog exposed 77 enabled models on the verification date:

- **OpenAI**: 13 models, including GPT and Codex-oriented routes
- **Anthropic**: 8 Claude models
- **Google**: 17 Gemini models, including text, image, speech, and multimodal routes
- **DeepSeek**: official-API and self-hosted open-weight route groups
- **Video**: 8 Seedance models plus other video-generation providers
- **Other providers**: Qwen, Kimi, MiniMax, GLM, Hunyuan, Grok, Kling, and Xiaomi MiMo

Catalog counts and availability change over time; use the live pricing catalog
for current model IDs.

## Engine and Upstream Disclosure | 引擎与上游说明

- The managed service uses [New API](https://github.com/QuantumNous/new-api) as its gateway engine; it is not represented as a fully proprietary gateway.
- 88API maintains a public [New API fork](https://github.com/blackdm666/new-api) and submits fixes and provider work upstream, including [Gemini Interactions video support](https://github.com/QuantumNous/new-api/pull/7020), [asynchronous performance-metric fixes](https://github.com/QuantumNous/new-api/pull/7073), and [Responses billing safeguards](https://github.com/QuantumNous/new-api/pull/7195).
- The Sub2API adapter used for subscription-pool routing is now available in upstream New API ([upstream commit](https://github.com/QuantumNous/new-api/commit/2d23cdf2915432632e37637198a72c752d642bcf)).
- OpenAI and Claude low-cost groups can use subscription-account pools rather than direct official API routes.
- DeepSeek is offered through separate official-API and self-hosted open-weight groups.
- Seedance is offered through separate Volcano Engine official and third-party groups.

Upstream type, price, and availability are group dependent. Users should select
the route appropriate to their reliability and provenance requirements.

## Payment and Support | 支付与支持

- Prepaid virtual-credit wallet; available payment rails depend on account and region
- Corporate transfer and invoicing support for enterprise customers
- Consumed virtual credits are not eligible for no-reason refunds; see the published [User Agreement](https://88api.ai/user-agreement)
- [Privacy Policy](https://88api.ai/privacy-policy) is publicly available
- Human support daily from 10:00 to 24:00 (UTC+8) through in-console live chat
- Public Telegram group: [88API Token 聚合站](https://t.me/apitoken88)

## Features | 特色功能

- One account and API key across OpenAI-, Anthropic-, and Gemini-compatible routes
- Public pricing catalog with per-model billing type, enabled groups, and endpoint types
- Rolling 24-hour per-model success rate, latency, and throughput displayed in the model marketplace
- OpenAI Chat Completions and Responses, Anthropic Messages, Gemini, image, speech, and video endpoints
- Detailed integration guides for Claude Code, Codex, Cline, Continue, Cherry Studio, Chatbox, Open WebUI, and other clients
- Multi-provider route groups with automatic routing and channel health handling

## Pros & Cons | 优缺点

**Pros | 优势**

- Public model-level pricing and machine-readable catalog without login
- Multi-protocol and multimodal coverage under one account
- Public 24-hour model performance indicators and broad client documentation
- Identified Hong Kong corporate operator and daily human support window

**Cons | 局限**

- Some low-cost frontier-model routes use subscription pools rather than official provider APIs
- Effective prices and availability vary by group, dynamic tier, and account configuration
- Built on New API; independent long-term benchmark data remains limited
- Model-level 24-hour metrics are operator-generated and are not a platform-wide SLA

## Review Score | 评分

*Operator self-submission. No self-authored score is provided; the repository's
independent probes should determine reachability, endpoint status, latency,
uptime, and leaderboard score.*

## Benchmark Data | 基准数据

The public model marketplace displays rolling 24-hour model success rate,
latency, and throughput. No static benchmark claim is submitted because these
values change continuously.

## User Reviews | 用户评价

*No independent user-review score submitted with this operator entry.*

## Changelog | 更新日志

- `2026-09-09` — Initial operator-submitted entry

---

**Conflict of interest disclosure** | **利益相关声明**: This is an operator
self-submission by 88API. The entry discloses its New API base, mixed upstream
route types, dynamic pricing limitations, and operator relationship.
