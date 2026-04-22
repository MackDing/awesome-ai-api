# awesome-ai-api

> The world's largest open-source hub for AI API gateways & reseller reviews.  
> Curated · community-driven · fully transparent · **every gateway probed daily**.

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="./CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"></a>
  <!-- STATS:BEGIN -->
  <img src="https://img.shields.io/badge/Gateways-206-blue" alt="Total">
  <img src="https://img.shields.io/badge/API_verified-101-success" alt="API verified">
  <img src="https://img.shields.io/badge/Updated-daily_10:00_SGT-orange" alt="Updated">
  <!-- STATS:END -->
</p>

<p align="center">
  <a href="./README.zh-CN.md">🇨🇳 中文</a> · <b>English</b>
</p>

---

## What makes us different

We don't just list gateways — **we probe every one of them daily** for a real OpenAI-compatible `/v1/models` endpoint. No `200 OK on the homepage` inflation.

- 🔌 **Ground-truth API detection** — every 🔌 badge = endpoint confirmed live
- 🔍 **Transparency** — no paid placement; [raw data](./data/gateways.json) is Git-history-tracked
- 🌏 **Global** — bilingual (EN/中文), covers Western + Chinese markets
- 🛠 **Developer-first** — structured JSON, daily history snapshots, PR-editable
- 🤝 **Community-driven** — pricing & reviews by people who actually pay for these services

---

## 🎯 Quick Picks

Confused by 200+ gateways? Start here.

<!-- QUICKPICKS:BEGIN -->
| Use case | Recommendation | Why |
|---|---|---|
| 🌐 **Global, one API for all models** | [OpenRouter](https://openrouter.ai) | Pioneer of the pattern; most stable, highest fees |
| 👨‍💻 **Best Claude Code in China** | [PackyAPI](https://www.packyapi.com) | Claude-Code native, active upstream, ¥1/sample |
| 🏢 **Enterprise / invoices** | [柏拉图AI](https://api.bltcy.ai) · [云雾](https://yunwu.ai) | Long-running, multi-region, invoices, DeepSeek/MidJourney too |
| 💰 **Cheap Claude (accept risk)** | [Terminal.Pub](https://terminal.pub) · [XcodeBest](https://xcode.best) | ~0.15% of official; new = verify before topping up |
| 🆓 **Free trial credit** | [AnyRouter](https://anyrouter.dev) · [发现AI](https://www.findcg.com) | Credits on signup, no card |
| 🏠 **Self-hosted** | [One API](https://github.com/songquanpeng/one-api) · [New API](https://github.com/Calcium-Ion/new-api) | OSS; the engine 60% of the CN list runs on |
| ⚡ **Inference-only (Llama/Qwen/DeepSeek)** | [Groq](https://groq.com) · [Together](https://together.ai) · [Fireworks](https://fireworks.ai) | Not resellers; own GPUs; US cards only |
| 🌯 **Multi-modal (video/music/image)** | [神马AI](https://api.whatai.cc) · [302.AI](https://302.ai) | MidJourney, Kling, Suno, PPT generators |
<!-- QUICKPICKS:END -->

> ⚠️ **Never pre-pay large amounts.** This industry has weekly rug-pulls. Top up ¥10 first, validate quality, then consider going up.

---

## 💚 Support this project

This repo is free, ad-free, and has no paid placement. If the leaderboard saved you from topping up a rug-pull, consider chipping in:

- **USDT (any EVM chain — ERC20 / BSC / Polygon / Arbitrum / Base / Optimism):**  
  `0xa5c74e7D3f0c8f1c0d7A395A6B7861Ab0A64cA7F`
- ⭐ **Star the repo** — also helps a lot; boosts us in GitHub trending.
- 📝 **Open a PR** with a gateway report — the most valuable contribution.

> 💡 **Double-check the chain before sending.** Sending from an exchange? Withdraw on **ERC20 / BSC / Polygon / Arbitrum / Base / Optimism**. **Do NOT use TRC20** (TRON) — that address doesn't exist on Tron.

---

## Table of Contents

- [🏆 Full Leaderboard](#-full-leaderboard)
- [📊 Categories](#-categories)
- [📝 Reviews](#-reviews)
- [⚠️ Blacklist](#️-blacklist)
- [🧪 Benchmark](#-benchmark)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

---

## 🏆 Full Leaderboard

Auto-generated daily at **10:00 SGT (UTC+8)** from live probes. See [methodology](./reviews/methodology.md) · [history](./data/history/) · [raw data](./data/gateways.json).

**🔌 = confirmed `/v1/models` endpoint (real API, not just a marketing page).**

<details>
<summary><b>📊 Click to expand the full leaderboard</b></summary>

<!-- LEADERBOARD:BEGIN -->
_Last updated: 2026-04-22 22:51 (SGT)_

**Total: 206 gateways** · 🔌 **101 with confirmed `/v1/models` endpoint** · 🟢 126 Verified · 🟡 8 Probable · 🧰 7 OSS · 🔍 65 Needs review

**Top engines detected:** `new-api` × 35 · `one-api` × 12 · `dify` × 8 · `litellm` × 4 · `openrouter` × 2

| # | Gateway | Region | API | Models | Engine | Payment | Score | Latency | Tier |
|---|---------|--------|-----|--------|--------|---------|-------|---------|------|
| 🥇 | [AIHubMix](https://aihubmix.com) | global | 🔌 | **225 models** | openrouter | — | 9.9 | 545 ms | 🟢 Verified |
| 🥈 | [PackyAPI (PackyCode)](https://www.packyapi.com) | cn | 🔌 | claude, gpt, gemini | — | wechat | 9.6 | 268 ms | 🟢 Verified |
| 🥉 | [ClaudeCN](https://claudecn.top) | cn | 🔌 | claude, gpt, gemini | — | card | 9.6 | 2597 ms | 🟢 Verified |
| 4 | [V-API](https://api.v3.cm) | cn | 🔌 | claude, gpt, gemini | — | — | 9.5 | 560 ms | 🟢 Verified |
| 5 | [api.oneabc.org](https://api.oneabc.org) | cn | 🔌 | claude, gpt, gemini | — | — | 9.5 | 563 ms | 🟢 Verified |
| 6 | [V-API](https://api.vveai.com) | cn | 🔌 | claude, gpt, gemini | — | — | 9.5 | 738 ms | 🟢 Verified |
| 7 | [V-API](https://api.gpt.ge) | cn | 🔌 | claude, gpt, gemini | — | — | 9.5 | 742 ms | 🟢 Verified |
| 8 | [Doro AI](https://doro.lol) | cn | 🔌 | claude, gpt, gemini | new-api | — | 9.5 | 922 ms | 🟢 Verified |
| 9 | [Yuegle API](https://api.yuegle.com) | cn | 🔌 | claude, gpt, gemini | — | — | 9.5 | 1130 ms | 🟢 Verified |
| 10 | [V-API](https://api.v36.cm) | cn | 🔌 | claude, gpt, gemini | — | — | 9.5 | 1383 ms | 🟢 Verified |
| 11 | [Claude Code/GPT/Gemini API 中转代理](https://ai.tokencloud.ai) | cn | 🔌 | claude, gpt, gemini | — | wechat | 9.5 | 1410 ms | 🟢 Verified |
| 12 | [jeniya.cn](https://jeniya.cn) | cn | 🔌 | claude, gpt, chatgpt | — | — | 9.5 | 1482 ms | 🟢 Verified |
| 13 | [便携AI聚合API](https://api.bianxieai.com) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.5 | 1574 ms | 🟢 Verified |
| 14 | [毫秒API MJ gpt claude AI luma deepseek 中转 AI中转 chatgpt中转 claud](https://api.holdai.top) | cn | 🔌 | claude, gpt, chatgpt | — | — | 9.5 | 1590 ms | 🟢 Verified |
| 15 | [apipro.maynor1024.live](https://apipro.maynor1024.live) | cn | 🔌 | claude, gpt, gemini | — | — | 9.5 | 1613 ms | 🟢 Verified |
| 16 | [OneToken](https://onetoken.one) | cn | 🔌 | claude, gpt, gemini | new-api | — | 9.5 | 1869 ms | 🟢 Verified |
| 17 | [Avian](https://avian.io) | global | 🔌 | **6 models** | — | — | 9.5 | 2256 ms | 🟢 Verified |
| 18 | [Flow2API](https://flow2api.com) | cn | 🔌 | claude, gpt, gemini | new-api | — | 9.5 | 2277 ms | 🟢 Verified |
| 19 | [老张API](https://api.laozhang.ai) | cn | 🔌 | claude, gpt, gemini | — | — | 9.4 | 617 ms | 🟢 Verified |
| 20 | [API Market](https://api.302ai.cn) | global | 🔌 | gpt, gemini, anthropic | — | — | 9.4 | 759 ms | 🟢 Verified |
| 21 | [api-996444-cn](https://api.996444.cn) | cn | 🔌 | claude, gemini, openai | — | — | 9.3 | 109 ms | 🟢 Verified |
| 22 | [api.aipaibox.com](https://api.aipaibox.com) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 171 ms | 🟢 Verified |
| 23 | [DDS Hub](https://www.ddshub.cc) | global | 🔌 | gpt, qwen, grok | — | — | 9.3 | 214 ms | 🟢 Verified |
| 24 | [oneapi.paintbot.top](https://oneapi.paintbot.top) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 222 ms | 🟢 Verified |
| 25 | [api.ikuncode.cc](https://api.ikuncode.cc) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 348 ms | 🟢 Verified |
| 26 | [BUZZ AI](https://buzzai.cc) | cn | 🔌 | claude, anthropic, openai | — | — | 9.3 | 351 ms | 🟢 Verified |
| 27 | [chatfire.cn](https://chatfire.cn) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 360 ms | 🟢 Verified |
| 28 | [duckcoding.com](https://duckcoding.com) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 440 ms | 🟢 Verified |
| 29 | [xcode.best](https://xcode.best) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 541 ms | 🟢 Verified |
| 30 | [aigcbest.top](https://aigcbest.top) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 575 ms | 🟢 Verified |
| 31 | [api.dzzi.ai](https://api.dzzi.ai) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 576 ms | 🟢 Verified |
| 32 | [35.aigcbest.top](https://35.aigcbest.top) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 594 ms | 🟢 Verified |
| 33 | [api-chatfire-cn](https://api.chatfire.cn) | cn | 🔌 | claude, gemini, openai | — | — | 9.3 | 614 ms | 🟢 Verified |
| 34 | [api.ekan8.com](https://api.ekan8.com) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 645 ms | 🟢 Verified |
| 35 | [api.gemai.cc](https://api.gemai.cc) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 667 ms | 🟢 Verified |
| 36 | [api.ifopen.ai](https://api.ifopen.ai) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 707 ms | 🟢 Verified |
| 37 | [terminal.pub](https://terminal.pub) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 750 ms | 🟢 Verified |
| 38 | [new.yunai.link](https://new.yunai.link) | cn | 🔌 | claude, gemini, openai | — | — | 9.3 | 863 ms | 🟢 Verified |
| 39 | [azapi-com-cn](https://azapi.com.cn) | cn | 🔌 | claude, gemini, openai | — | — | 9.3 | 933 ms | 🟢 Verified |
| 40 | [zerocode.sbs](https://zerocode.sbs) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 1021 ms | 🟢 Verified |
| 41 | [openclaudecode.cn](https://www.openclaudecode.cn) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 1028 ms | 🟢 Verified |
| 42 | [api-gueai-com](https://api.gueai.com) | cn | 🔌 | claude, gemini, openai | — | — | 9.3 | 1059 ms | 🟢 Verified |
| 43 | [duckcoding.ai](https://www.duckcoding.ai) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 1192 ms | 🟢 Verified |
| 44 | [KKSJ AI模型中转API](https://cnapi.kksj.org) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 1197 ms | 🟢 Verified |
| 45 | [神马中转API_低价稳定的代理API](https://api.whatai.cc) | cn | 🔌 | claude, gpt, gemini | — | — | 9.3 | 1198 ms | 🟢 Verified |
| 46 | [apirouter.ai](https://apirouter.ai) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 1317 ms | 🟢 Verified |
| 47 | [dawclaudecode.com](https://dawclaudecode.com) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 1364 ms | 🟢 Verified |
| 48 | [api-deerapi-com](https://api.deerapi.com) | cn | 🔌 | claude, gemini, openai | — | — | 9.3 | 1408 ms | 🟢 Verified |
| 49 | [api.openai-ch.top](https://api.openai-ch.top) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 1511 ms | 🟢 Verified |
| 50 | [api.soruxgpt.com](https://api.soruxgpt.com) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 1584 ms | 🟢 Verified |

> Top 50 shown. See [`data/_leaderboard.md`](data/_leaderboard.md) for the full list of 206 gateways.

<!-- LEADERBOARD:END -->

</details>

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
