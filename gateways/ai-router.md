# AI-ROUTER

> Independent ChatGPT and Claude API relay with an OpenAI-compatible developer endpoint.

**[Official Website](https://ai-router.dev/)** · **[Public catalog](https://api.ai-router.dev/api/v1/payment/public/catalog)** · **[Register](https://ai-router.dev/register)**

---

## Quick Facts | 基本信息

| Field | Value |
|-------|-------|
| **Founded** | 2025-12 (project origin) |
| **Base Region** | Global |
| **Target Users** | Developers, coding-agent users, and small teams |
| **Site Language** | English, Chinese, Russian, Japanese, German, and additional locales |
| **API Compatible With** | OpenAI-compatible; account/group dependent model access |
| **Claude Code Support** | ⚠️ Verify the account-visible model and tool-call contract |
| **Last Verified** | 2026-09-02 |

## Pricing | 定价

The public catalog exposes model-level values for the OpenCode dedicated-credit
product. Values below are USD per 1M tokens and are not a universal quote for
every account or group:

| Model | Input | Output | Official | Diff |
|-------|-------|--------|----------|------|
| GPT-5.6 Sol | $5.00 | $30.00 | — | Not compared |
| GPT-5.6 Terra | $2.00 | $12.00 | — | Not compared |
| GPT-5.6 Luna | $0.20 | $1.20 | — | Not compared |
| GPT-5.5 | $5.00 | $30.00 | — | Not compared |
| GPT-5.4 | $2.50 | $15.00 | — | Not compared |

See the live [public catalog](https://api.ai-router.dev/api/v1/payment/public/catalog)
for current package, payment, and model information. Do not infer a discount
by comparing unlike subscription, balance, and token units.

## Supported Models | 支持模型

- **OpenAI-compatible catalog**: GPT-5.6 Sol, GPT-5.6 Terra, GPT-5.6 Luna, GPT-5.5, and GPT-5.4 are present in the public OpenCode catalog as of the verification date.
- **Claude**: access and model IDs are account/group dependent; verify the authenticated model list before production use.

## Payment Methods | 支付方式

- 💳 Fiat/card rails where enabled for the account
- 💳 Alipay where enabled
- ₿ Crypto where enabled

## Features | 特色功能

- OpenAI-compatible `/v1` endpoint for supported account models
- Per-user API keys with usage and balance visibility
- Package, balance, and subscription controls
- Localized public homepages, including Russian, Japanese, and German routes

## Pros & Cons | 优缺点

**Pros | 优势**
- Public machine-readable catalog and registration flow
- Usage and balance controls are visible to the account owner
- Multiple payment rails are exposed in the current public catalog

**Cons | 局限**
- `GET /v1/models` requires an authenticated key
- Model availability, limits, and effective rates can vary by account or group
- Independent relay; not OpenAI or Anthropic and not endorsed by either provider

## Review Score | 评分

No independent score or uptime claim is submitted. Community benchmarks and
reviews should be added only when they include reproducible dates, endpoints,
and account context.

## User Reviews | 用户评价

*No independent review links submitted with this operator entry.*

## Changelog | 更新日志

- `2026-09-02` — Initial operator-submitted entry with public catalog evidence

---

**Conflict of interest disclosure** | **利益相关声明**: This is an operator
self-submission by AI-ROUTER. The entry intentionally avoids unverified price
comparisons, uptime guarantees, and provider endorsement claims.
