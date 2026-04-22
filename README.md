# awesome-ai-api

> The world's largest open-source hub for AI API gateways & reseller reviews.
> Curated, community-driven, fully transparent.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)
[![Discussions](https://img.shields.io/github/discussions/MackDing/awesome-ai-api)](https://github.com/MackDing/awesome-ai-api/discussions)

[🇨🇳 中文](./README.zh-CN.md) · **English**

---

## What is this?

`awesome-ai-api` is a **curated, open-source directory and review hub** for AI API gateways (also known as "resellers", "relay stations", "中转站").

We track, compare, and review services that let you access Claude, GPT, Gemini, DeepSeek, Qwen, and 200+ other models through unified APIs — often at lower prices, with better payment options, or additional features.

### Why we exist

- 🔍 **Transparency** — No paid placement. Data is public, PR-editable.
- 🌍 **Global** — Bilingual (EN/中文), covers both Western and Chinese gateways.
- 🛠 **Developer-first** — Structured JSON data, not just a pretty page.
- 🤝 **Community-driven** — Pricing and reviews updated by the people who actually use these services.

---

## Table of Contents

- [🏆 Leaderboard](#-leaderboard)
- [📊 Categories](#-categories)
- [📝 Reviews](#-reviews)
- [⚠️ Blacklist](#-blacklist)
- [🧪 Benchmark](#-benchmark)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

---

## 🏆 Leaderboard

*Last updated: 2026-04-22 · [See methodology](./reviews/methodology.md)*

| Rank | Gateway | Type | Models | Claude Code | Pay | Score | Review |
|------|---------|------|--------|-------------|-----|-------|--------|
| 🥇 1 | [OpenRouter](./gateways/openrouter.md) | Global | 300+ | ✅ | 💳 Card/Crypto | 9.4 | [Link](./gateways/openrouter.md) |
| 🥈 2 | [One API (self-host)](./gateways/one-api.md) | Self-host | Any | ✅ | N/A | 9.2 | [Link](./gateways/one-api.md) |
| 🥉 3 | [Road2All](./gateways/road2all.md) | CN | 100+ | ✅ | 💳 Alipay/WeChat | 9.0 | [Link](./gateways/road2all.md) |
| 4 | [DeepBricks](./gateways/deepbricks.md) | CN | 80+ | ✅ | 💳 Alipay | 8.8 | [Link](./gateways/deepbricks.md) |
| 5 | [AiHubMix](./gateways/aihubmix.md) | CN | 150+ | ✅ | 💳 Alipay/WeChat | 8.7 | [Link](./gateways/aihubmix.md) |
| 6 | [OhMyGPT](./gateways/ohmygpt.md) | CN | 100+ | ✅ | 💳 Alipay/WeChat | 8.6 | [Link](./gateways/ohmygpt.md) |
| 7 | [API2D](./gateways/api2d.md) | CN | 60+ | ✅ | 💳 Alipay/WeChat | 8.5 | [Link](./gateways/api2d.md) |
| 8 | [Together AI](./gateways/together-ai.md) | Global | 100+ | ❌ | 💳 Card | 8.4 | [Link](./gateways/together-ai.md) |
| 9 | [Groq](./gateways/groq.md) | Global | 20+ | ❌ | 💳 Card | 8.3 | [Link](./gateways/groq.md) |
| 10 | [Fireworks AI](./gateways/fireworks-ai.md) | Global | 50+ | ❌ | 💳 Card | 8.2 | [Link](./gateways/fireworks-ai.md) |

> 📌 **Want your gateway listed?** Open a PR with a filled [gateway template](./gateways/_template.md). We accept any provider that meets our [listing criteria](./CONTRIBUTING.md#listing-criteria).

---

## 📊 Categories

### By Target Market

- 🌍 [Global Gateways](./data/by-region.md#global) — OpenRouter, Together AI, Groq, Fireworks
- 🇨🇳 [China Gateways](./data/by-region.md#china) — Road2All, DeepBricks, AiHubMix, OhMyGPT
- 🏠 [Self-Hosted](./data/by-region.md#self-hosted) — One API, NewAPI, LiteLLM

### By Specialty

- 🤖 [Claude Code Compatible](./data/by-feature.md#claude-code) — Services fully supporting Claude Code CLI
- ⚡ [Low-Latency](./data/by-feature.md#low-latency) — Sub-500ms TTFT
- 💰 [Best-Price](./data/by-feature.md#best-price) — Discounted vs. official rates
- 🔒 [Privacy-First](./data/by-feature.md#privacy) — No data retention / on-prem

### By Payment

- 💳 [Alipay/WeChat](./data/by-payment.md#cn) — For Chinese users
- 💳 [Credit Card](./data/by-payment.md#card) — International
- ₿ [Crypto](./data/by-payment.md#crypto) — Anonymous payment support

---

## 📝 Reviews

Deep-dive reviews and benchmark reports:

- 📊 [2026 Q2 Gateway Benchmark](./reviews/2026-Q2-benchmark.md) *(coming soon)*
- 🔬 [Claude Code Gateway Shootout](./reviews/claude-code-shootout.md) *(coming soon)*
- 💸 [Price Analysis: Official vs Gateway](./reviews/pricing-analysis.md) *(coming soon)*
- 🧪 [Methodology](./reviews/methodology.md)

---

## ⚠️ Blacklist

Gateways that have been flagged for serious issues (rug-pulls, data leaks, fake models).

See [blacklist.md](./data/blacklist.md) for the current list and evidence archive.

> If you've been affected, please open a GitHub Discussion with evidence. We review reports transparently.

---

## 🧪 Benchmark

We run periodic benchmarks testing:

- **Latency** (TTFT, total response time)
- **Throughput** (tokens/sec)
- **Reliability** (uptime %)
- **Accuracy** (model behavior matches official?)
- **Pricing consistency** (quoted vs. billed)

See [`scripts/benchmark.py`](./scripts/benchmark.py) for the test harness. Results in [`data/benchmarks/`](./data/benchmarks/).

---

## 🤝 Contributing

We welcome PRs from users, gateway operators, and researchers. See [CONTRIBUTING.md](./CONTRIBUTING.md).

**Quick ways to help:**
- ✏️ Update a gateway's pricing or model list
- 📝 Submit a new gateway (use the [template](./gateways/_template.md))
- 🚨 Report a scam or outage
- 🧪 Submit benchmark data
- 🌐 Improve translations

---

## 📜 License

Content is released under the [MIT License](./LICENSE). Attribution appreciated but not required.

---

## 🙏 Acknowledgments

Inspired by [apicompare.best](https://apicompare.best), [helpaio.com/transit](https://www.helpaio.com/transit), and [trustmrr.com](https://trustmrr.com) — each taught us one piece of the puzzle: **price data, content depth, and verified trust**. We combine them with GitHub-native openness.

---

<p align="center">
  <em>Built by <a href="https://github.com/MackDing">Mack Ding</a> and contributors · Made for the global OPC community</em>
</p>
