# awesome-ai-api

> The world's largest open-source hub for AI API gateways & reseller reviews.  
> Curated · community-driven · fully transparent · **every gateway probed daily**.

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="./CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"></a>
  <!-- STATS:BEGIN -->
  <img src="https://img.shields.io/badge/Gateways-201-blue" alt="Total">
  <img src="https://img.shields.io/badge/API_verified-101-success" alt="API verified">
  <img src="https://img.shields.io/badge/Updated-daily_10:00_SGT-orange" alt="Updated">
  <!-- STATS:END -->
</p>

<p align="center">
  <a href="./README.zh-CN.md">🇨🇳 中文</a> · <b>English</b> · <a href="https://mackding.github.io/awesome-ai-api/">🌐 Live site</a>
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
- [❓ FAQ](#-faq)
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
_Last updated: 2026-04-23 21:57 (SGT)_

**Total: 201 gateways** · 🔌 **101 with confirmed `/v1/models` endpoint** · 🟢 127 Verified · 🟡 8 Probable · 🧰 7 OSS · 🔍 59 Needs review

**Top engines detected:** `new-api` × 38 · `one-api` × 11 · `dify` × 8 · `litellm` × 4 · `openrouter` × 2

| # | Gateway | Region | API | Models | Engine | Payment | Score | Latency | Tier |
|---|---------|--------|-----|--------|--------|---------|-------|---------|------|
| 🥇 | [AIHubMix](https://aihubmix.com) | global | 🔌 | **224 models** | openrouter | — | 9.9 | 384 ms | 🟢 Verified |
| 🥈 | [AnyRouter](https://anyrouter.dev) | global | 🔌 | **25 models** | one-api | — | 9.7 | 1176 ms | 🟢 Verified |
| 🥉 | [PackyAPI (PackyCode)](https://www.packyapi.com) | cn | 🔌 | claude, gpt, gemini | — | wechat | 9.6 | 190 ms | 🟢 Verified |
| 4 | [ClaudeCN](https://claudecn.top) | cn | 🔌 | claude, gpt, gemini | — | card | 9.6 | 202 ms | 🟢 Verified |
| 5 | [api.v36.cm](https://api.v36.cm) | cn | 🔌 | claude, gpt, gemini | — | — | 9.5 | 133 ms | 🟢 Verified |
| 6 | [OneToken](https://onetoken.one) | cn | 🔌 | claude, gpt, gemini | new-api | — | 9.5 | 140 ms | 🟢 Verified |
| 7 | [api.oneabc.org](https://api.oneabc.org) | cn | 🔌 | claude, gpt, gemini | — | — | 9.5 | 159 ms | 🟢 Verified |
| 8 | [api.vveai.com](https://api.vveai.com) | cn | 🔌 | claude, gpt, gemini | — | — | 9.5 | 160 ms | 🟢 Verified |
| 9 | [Flow2API](https://flow2api.com) | cn | 🔌 | claude, gpt, gemini | new-api | — | 9.5 | 191 ms | 🟢 Verified |
| 10 | [apipro.maynor1024.live](https://apipro.maynor1024.live) | cn | 🔌 | claude, gpt, gemini | — | — | 9.5 | 200 ms | 🟢 Verified |
| 11 | [api.v3.cm](https://api.v3.cm) | cn | 🔌 | claude, gpt, gemini | — | — | 9.5 | 209 ms | 🟢 Verified |
| 12 | [ePhone AI](https://api.ephone.ai) | cn | 🔌 | claude, gpt, gemini | — | — | 9.5 | 224 ms | 🟢 Verified |
| 13 | [api.gpt.ge](https://api.gpt.ge) | cn | 🔌 | claude, gpt, gemini | — | — | 9.5 | 312 ms | 🟢 Verified |
| 14 | [Yuegle API](https://api.yuegle.com) | cn | 🔌 | claude, gpt, gemini | — | — | 9.5 | 362 ms | 🟢 Verified |
| 15 | [Avian](https://avian.io) | global | 🔌 | **6 models** | — | — | 9.5 | 407 ms | 🟢 Verified |
| 16 | [毫秒API MJ gpt claude AI luma deepseek 中转 AI中转 chatgpt中转 claud](https://api.holdai.top) | cn | 🔌 | claude, gpt, chatgpt | — | — | 9.5 | 553 ms | 🟢 Verified |
| 17 | [jeniya.cn](https://jeniya.cn) | cn | 🔌 | claude, gpt, chatgpt | — | — | 9.5 | 577 ms | 🟢 Verified |
| 18 | [Claude Code/GPT/Gemini API 中转代理](https://ai.tokencloud.ai) | cn | 🔌 | claude, gpt, gemini | — | wechat | 9.5 | 1541 ms | 🟢 Verified |
| 19 | [Doro AI](https://doro.lol) | cn | 🔌 | claude, gpt, gemini | new-api | — | 9.5 | 1880 ms | 🟢 Verified |
| 20 | [便携AI聚合API](https://api.bianxieai.com) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.5 | 2015 ms | 🟢 Verified |
| 21 | [老张API](https://api.laozhang.ai) | cn | 🔌 | claude, gpt, gemini | — | — | 9.4 | 138 ms | 🟢 Verified |
| 22 | [api-gptgod-work](https://api.gptgod.work) | global | 🔌 | **342 models** | — | — | 9.4 | 690 ms | 🟢 Verified |
| 23 | [api-gueai-com](https://api.gueai.com) | cn | 🔌 | claude, gemini, openai | — | — | 9.3 | 100 ms | 🟢 Verified |
| 24 | [new.yunai.link](https://new.yunai.link) | cn | 🔌 | claude, gemini, openai | — | — | 9.3 | 105 ms | 🟢 Verified |
| 25 | [35.aigcbest.top](https://35.aigcbest.top) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 116 ms | 🟢 Verified |
| 26 | [chatapi.onechats.top](https://chatapi.onechats.top) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 116 ms | 🟢 Verified |
| 27 | [api.ifopen.ai](https://api.ifopen.ai) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 117 ms | 🟢 Verified |
| 28 | [aigcbest.top](https://aigcbest.top) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 126 ms | 🟢 Verified |
| 29 | [api.dzzi.ai](https://api.dzzi.ai) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 131 ms | 🟢 Verified |
| 30 | [api.ekan8.com](https://api.ekan8.com) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 162 ms | 🟢 Verified |
| 31 | [api.onechats.top](https://api.onechats.top) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 167 ms | 🟢 Verified |
| 32 | [api.aigcbest.top](https://api.aigcbest.top) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 181 ms | 🟢 Verified |
| 33 | [KKSJ AI模型中转API](https://cnapi.kksj.org) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 196 ms | 🟢 Verified |
| 34 | [api-mnapi-com](https://api.mnapi.com) | cn | 🔌 | claude, gemini, openai | — | — | 9.3 | 209 ms | 🟢 Verified |
| 35 | [api.gemai.cc](https://api.gemai.cc) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 212 ms | 🟢 Verified |
| 36 | [api.openai-ch.top](https://api.openai-ch.top) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 216 ms | 🟢 Verified |
| 37 | [api.soruxgpt.com](https://api.soruxgpt.com) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 242 ms | 🟢 Verified |
| 38 | [api-deerapi-com](https://api.deerapi.com) | cn | 🔌 | claude, gemini, openai | — | — | 9.3 | 262 ms | 🟢 Verified |
| 39 | [openclaudecode.cn](https://www.openclaudecode.cn) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 288 ms | 🟢 Verified |
| 40 | [Aiberm](https://aiberm.com) | global | 🔌 | claude, gemini, openai | — | — | 9.3 | 289 ms | 🟢 Verified |
| 41 | [柏拉图AI_API中转站 (api.bltcy.ai)](https://api.bltcy.ai) | cn | 🔌 | claude, gpt, openai | — | — | 9.3 | 289 ms | 🟢 Verified |
| 42 | [柏拉图AI_API中转站 (api.bltcy.top)](https://api.bltcy.top) | cn | 🔌 | claude, gpt, openai | — | — | 9.3 | 315 ms | 🟢 Verified |
| 43 | [api.ikuncode.cc](https://api.ikuncode.cc) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 335 ms | 🟢 Verified |
| 44 | [apirouter.ai](https://apirouter.ai) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 383 ms | 🟢 Verified |
| 45 | [ggwk1.online](https://www.ggwk1.online) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 386 ms | 🟢 Verified |
| 46 | [dawclaudecode.com](https://dawclaudecode.com) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 429 ms | 🟢 Verified |
| 47 | [azapi-com-cn](https://azapi.com.cn) | cn | 🔌 | claude, gemini, openai | — | — | 9.3 | 467 ms | 🟢 Verified |
| 48 | [神马中转API_低价稳定的代理API](https://api.whatai.cc) | cn | 🔌 | claude, gpt, gemini | — | — | 9.3 | 493 ms | 🟢 Verified |
| 49 | [zerocode.sbs](https://zerocode.sbs) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 504 ms | 🟢 Verified |
| 50 | [xcode.best](https://xcode.best) | cn | 🔌 | claude, gemini, openai | new-api | — | 9.3 | 541 ms | 🟢 Verified |

> Top 50 shown. See [`data/_leaderboard.md`](data/_leaderboard.md) for the full list of 201 gateways.

<!-- LEADERBOARD:END -->

</details>

> 📌 **Want your gateway listed?** Open a PR with a filled [gateway template](./gateways/_template.md). We accept any provider that meets our [listing criteria](./CONTRIBUTING.md#listing-criteria).

---

## ❓ FAQ

<details>
<summary><b>What exactly is an "AI API gateway" or "中转站"?</b></summary>

A third-party service that exposes Claude, GPT, Gemini, DeepSeek, Qwen, and other frontier LLMs through a **single OpenAI-compatible HTTP API**. Most of them sit in front of the official providers and resell capacity, often at discounted prices, with friendlier payment options (WeChat/Alipay), or with extra features (rate-limit pooling, routing, logging, invoices).
</details>

<details>
<summary><b>How is this different from OpenRouter's /models page, helpaio.com, or apicompare.best?</b></summary>

- **OpenRouter** only lists gateways running inside OpenRouter's own routing graph. We list **every relay we can find**, including the dozens of small CN players.
- **helpaio.com** is a blog with human-written reviews. We publish **machine-verified data** (live `/v1/models` probes, engine fingerprints, uptime) alongside reviews.
- **apicompare.best** compares prices. We compare **reachability, authenticity, and stability** — cheaper doesn't help if the gateway disappears next week.
</details>

<details>
<summary><b>How do you decide the leaderboard score?</b></summary>

We combine: reachability (HTTP 2xx), confirmed `/v1/models` endpoint, real-model count, model-keyword density on the landing page, latency, and 30-day uptime from our daily snapshots. The formula lives in [`scripts/generate_leaderboard.py`](./scripts/generate_leaderboard.py) — no black box.
</details>

<details>
<summary><b>Is this a paid directory? Who pays you to be listed?</b></summary>

**No one.** There is zero paid placement. Listings are either auto-discovered or PR'd by the community. The repo is MIT-licensed and ad-free. If the leaderboard helped you, consider [supporting the project](#-support-this-project).
</details>

<details>
<summary><b>Can I trust the top-ranked gateways with large amounts of money?</b></summary>

**No.** This industry sees weekly rug-pulls. A high score means a gateway is *currently* reachable, has a real API, and has been stable for 30 days — **not** that it is solvent or will still be online next month. Always top up small amounts first (≤ US$2), validate model quality, and scale slowly.
</details>

<details>
<summary><b>I got scammed by a gateway. How do I report it?</b></summary>

Open a [GitHub Discussion](https://github.com/MackDing/awesome-ai-api/discussions) under the `Reports` category with public evidence (screenshots, transaction IDs, Telegram group links). Two independent reports + a 14-day operator response window = the gateway lands on [`data/blacklist.json`](./data/blacklist.json).
</details>

<details>
<summary><b>How do I add my gateway?</b></summary>

Add the URL to [`data/candidates.txt`](./data/candidates.txt), then (optionally) add a human-curated `name`, `region`, and `verdict` to [`data/sites.yaml`](./data/sites.yaml). Open a PR. The daily cron will pick it up.
</details>

<details>
<summary><b>Do you support non-OpenAI-compatible APIs (raw Anthropic, raw Gemini)?</b></summary>

We primarily probe `/v1/models` (OpenAI-compatible), because it's the lingua franca. Gateways that only expose raw Anthropic or Gemini endpoints can still be listed via `data/sites.yaml` with a `verdict: likely_relay` override and a `note` explaining the protocol.
</details>

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


---

## 🦞 OPC Ecosystem

> Built by [@MackDing](https://github.com/MackDing) — One-Person Company infrastructure powered by AI agents.

| Project | What it does |
|---------|-------------|
| [**opc.ren**](https://opc.ren) | OPC founder hub — tools, signals, community |
| [**CodexClaw**](https://github.com/MackDing/CodexClaw) | Telegram bot for remote Codex access with MCP + subagent routing |
| [**awesome-ai-api**](https://github.com/MackDing/awesome-ai-api) | Leaderboard of 200+ AI API gateways & relays |
| [**claude-context-health**](https://github.com/MackDing/claude-context-health) | Diagnose & fix Claude Code session degradation |
| [**opc-daily-signal**](https://github.com/MackDing/opc-daily-signal) | AI-powered daily decision intelligence for OPC founders |
| [**doc-preprocess-hub**](https://github.com/MackDing/doc-preprocess-hub) | Enterprise document preprocessing — MinerU + docling |
