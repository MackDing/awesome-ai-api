# awesome-ai-api

> 全球最大的开源 AI API 中转站评测中心  
> 社区驱动 · 完全透明 · **每个站点每日实探** · 无付费排名

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="./CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"></a>
  <!-- STATS_ZH:BEGIN -->
  <img src="https://img.shields.io/badge/%E4%B8%AD%E8%BD%AC%E7%AB%99-211-blue" alt="中转站总数">
  <img src="https://img.shields.io/badge/API%E5%B7%B2%E9%AA%8C%E8%AF%81-105-success" alt="API已验证">
  <img src="https://img.shields.io/badge/%E6%9B%B4%E6%96%B0-%E6%AF%8F%E6%97%A510%3A00_SGT-orange" alt="每日更新">
  <!-- STATS_ZH:END -->
</p>

<p align="center">
  <b>🇨🇳 中文</b> · <a href="./README.md">English</a>
</p>

---

## 我们与别家不同

我们不只是列表—— **每天会真实探测每个站点的 OpenAI 兼容 `/v1/models` 端点**。主页 `200 OK` 不算数。

- 🔌 **端点级真实性验证** — 每一个 🔌 徽章 = 接口层确认可用
- 🔍 **透明** — [原始数据](./data/gateways.json) Git 全历史可追溯
- 🌍 **全球** — 中英双语，涵盖国内外
- 🛠 **开发者优先** — 结构化 JSON、每日历史快照、PR 可编辑
- 🤝 **社区驱动** — 价格与评测由真实用户更新

---

## 🎯 快速选择

200+ 个站看花了？从这里开始。

<!-- QUICKPICKS_ZH:BEGIN -->
| 使用场景 | 推荐 | 理由 |
|---|---|---|
| 🌐 **全球统一 API** | [OpenRouter](https://openrouter.ai) | 先驱者，最稳定，最贵 |
| 👨‍💻 **国内最佳 Claude Code** | [PackyAPI](https://www.packyapi.com) | Claude Code 原生支持，上游活跃，¥1 试用 |
| 🏢 **企业客户／开发票** | [柏拉图AI](https://api.bltcy.ai) · [云雾](https://yunwu.ai) | 老牌站，多节点，支持 MidJourney/DeepSeek，能开票 |
| 💰 **极致低价 Claude（接受风险）** | [Terminal.Pub](https://terminal.pub) · [XcodeBest](https://xcode.best) | ~官方 0.15%，新站少充 |
| 🆓 **免费试用** | [AnyRouter](https://anyrouter.dev) · [发现AI](https://www.findcg.com) | 注册送额度，无需绑卡 |
| 🏠 **自建自用** | [One API](https://github.com/songquanpeng/one-api) · [New API](https://github.com/Calcium-Ion/new-api) | 开源 · 国内 60% 站点的底层 |
| ⚡ **纯推理（Llama/Qwen/DeepSeek）** | [Groq](https://groq.com) · [Together](https://together.ai) · [Fireworks](https://fireworks.ai) | 非中转，自建 GPU，仅支持国外信用卡 |
| 🌯 **多模态（视频／音乐／图像）** | [神马AI](https://api.whatai.cc) · [302.AI](https://302.ai) | MidJourney、可灵、Suno、PPT生成 |
<!-- QUICKPICKS_ZH:END -->

> ⚠️ **切勿大额充值。** 这个行业每周都有跑路。先充 ¥10 试用、验证质量，再考虑大额。

---

## 目录

- [🏆 完整排行榜](#-完整排行榜)
- [📊 分类](#-分类)
- [📝 评测](#-评测)
- [⚠️ 黑名单](#️-黑名单)
- [🧪 基准测试](#-基准测试)
- [🤝 贡献](#-贡献)
- [📜 许可证](#-许可证)

---

## 🏆 完整排行榜

每日 **新加坡时间 10:00 (UTC+8)** 自动生成。查看 [评分方法](./reviews/methodology.md) · [历史存档](./data/history/) · [原始数据](./data/gateways.json)

**🔌 = 已确认的 `/v1/models` 端点（真 API，不是单纯展示页）**

<details>
<summary><b>📊 点击展开完整 211 个中转站榜单</b></summary>

<!-- LEADERBOARD_ZH:BEGIN -->
_Last updated: 2026-04-22 20:58 (SGT)_

**合计 211 个中转站** · 🔌 **105 个已确认 `/v1/models` 端点** · 🟢 已验证 131 · 🟡 疑似 8 · 🧰 开源 7 · 🔍 待复核 65

| # | 中转站 | 地区 | API | 模型 | 支付 | 评分 | 响应 | 分类 |
|---|--------|------|-----|------|------|------|------|------|
| 🥇 | [PackyAPI (PackyCode)](https://www.packyapi.com) | cn | 🔌 | claude, gpt, gemini, openai | wechat | 9.6 | 290 ms | 🟢 已验证 |
| 🥈 | [ClaudeCN](https://claudecn.top) | cn | 🔌 | claude, gpt, gemini, openai | card | 9.6 | 2459 ms | 🟢 已验证 |
| 🥉 | [V-API](https://api.vveai.com) | cn | 🔌 | claude, gpt, gemini, chatgpt | — | 9.5 | 533 ms | 🟢 已验证 |
| 4 | [OneToken](https://onetoken.one) | cn | 🔌 | claude, gpt, gemini, chatgpt | — | 9.5 | 547 ms | 🟢 已验证 |
| 5 | [V-API](https://api.v3.cm) | cn | 🔌 | claude, gpt, gemini, chatgpt | — | 9.5 | 562 ms | 🟢 已验证 |
| 6 | [V-API](https://api.gpt.ge) | cn | 🔌 | claude, gpt, gemini, chatgpt | — | 9.5 | 591 ms | 🟢 已验证 |
| 7 | [V-API](https://api.v36.cm) | cn | 🔌 | claude, gpt, gemini, chatgpt | — | 9.5 | 771 ms | 🟢 已验证 |
| 8 | [Doro AI](https://doro.lol) | cn | 🔌 | claude, gpt, gemini, chatgpt | — | 9.5 | 806 ms | 🟢 已验证 |
| 9 | [AIHubMix](https://aihubmix.com) | global | 🔌 | claude, gpt, gemini, chatgpt | — | 9.5 | 846 ms | 🟢 已验证 |
| 10 | [Flow2API](https://flow2api.com) | cn | 🔌 | claude, gpt, gemini, chatgpt | — | 9.5 | 924 ms | 🟢 已验证 |
| 11 | [jeniya.cn](https://jeniya.cn) | cn | 🔌 | claude, gpt, chatgpt, openai | — | 9.5 | 924 ms | 🟢 已验证 |
| 12 | [api.oneabc.org](https://api.oneabc.org) | cn | 🔌 | claude, gpt, gemini, chatgpt | — | 9.5 | 990 ms | 🟢 已验证 |
| 13 | [Claude Code/GPT/Gemini API 中转代理](https://ai.tokencloud.ai) | cn | 🔌 | claude, gpt, gemini | wechat | 9.5 | 1582 ms | 🟢 已验证 |
| 14 | [Yuegle API](https://api.yuegle.com) | cn | 🔌 | claude, gpt, gemini, chatgpt | — | 9.5 | 1640 ms | 🟢 已验证 |
| 15 | [毫秒API MJ gpt claude AI luma deepseek 中转 AI中转 chatgpt中转 claud](https://api.holdai.top) | cn | 🔌 | claude, gpt, chatgpt, openai | — | 9.5 | 1665 ms | 🟢 已验证 |
| 16 | [便携AI聚合API](https://api.bianxieai.com) | cn | 🔌 | claude, gemini, openai, deepseek | — | 9.5 | 1776 ms | 🟢 已验证 |
| 17 | [ePhone AI](https://api.ephone.ai) | cn | 🔌 | claude, gpt, gemini, openai | — | 9.5 | 2348 ms | 🟢 已验证 |
| 18 | [AnyRouter](https://anyrouter.dev) | global | 🔌 | claude, gpt, gemini, anthropic | — | 9.5 | 2376 ms | 🟢 已验证 |
| 19 | [apipro.maynor1024.live](https://apipro.maynor1024.live) | cn | 🔌 | claude, gpt, gemini, openai | — | 9.5 | 2834 ms | 🟢 已验证 |
| 20 | [老张API](https://api.laozhang.ai) | cn | 🔌 | claude, gpt, gemini, grok | — | 9.4 | 575 ms | 🟢 已验证 |
| 21 | [API Market](https://api.302ai.cn) | global | 🔌 | gpt, gemini, anthropic, openai | — | 9.4 | 641 ms | 🟢 已验证 |
| 22 | [api-996444-cn](https://api.996444.cn) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 108 ms | 🟢 已验证 |
| 23 | [api.aipaibox.com](https://api.aipaibox.com) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 113 ms | 🟢 已验证 |
| 24 | [xcode.best](https://xcode.best) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 332 ms | 🟢 已验证 |
| 25 | [oneapi.paintbot.top](https://oneapi.paintbot.top) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 341 ms | 🟢 已验证 |
| 26 | [terminal.pub](https://terminal.pub) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 363 ms | 🟢 已验证 |
| 27 | [api.ikuncode.cc](https://api.ikuncode.cc) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 366 ms | 🟢 已验证 |
| 28 | [chatfire.cn](https://chatfire.cn) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 487 ms | 🟢 已验证 |
| 29 | [api-chatfire-cn](https://api.chatfire.cn) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 506 ms | 🟢 已验证 |
| 30 | [api.gemai.cc](https://api.gemai.cc) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 529 ms | 🟢 已验证 |
| 31 | [aigcbest.top](https://aigcbest.top) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 540 ms | 🟢 已验证 |
| 32 | [DDS Hub](https://www.ddshub.cc) | global | 🔌 | gpt, qwen, grok | — | 9.3 | 548 ms | 🟢 已验证 |
| 33 | [35.aigcbest.top](https://35.aigcbest.top) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 576 ms | 🟢 已验证 |
| 34 | [api.dzzi.ai](https://api.dzzi.ai) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 593 ms | 🟢 已验证 |
| 35 | [api.ekan8.com](https://api.ekan8.com) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 611 ms | 🟢 已验证 |
| 36 | [zerocode.sbs](https://zerocode.sbs) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 611 ms | 🟢 已验证 |
| 37 | [api.onechats.top](https://api.onechats.top) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 640 ms | 🟢 已验证 |
| 38 | [bytecatcode.org](https://www.bytecatcode.org) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 678 ms | 🟢 已验证 |
| 39 | [api.openai-ch.top](https://api.openai-ch.top) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 699 ms | 🟢 已验证 |
| 40 | [dawclaudecode.com](https://dawclaudecode.com) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 701 ms | 🟢 已验证 |
| 41 | [new.yunai.link](https://new.yunai.link) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 716 ms | 🟢 已验证 |
| 42 | [openclaudecode.cn](https://www.openclaudecode.cn) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 731 ms | 🟢 已验证 |
| 43 | [chatapi.onechats.top](https://chatapi.onechats.top) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 757 ms | 🟢 已验证 |
| 44 | [duckcoding.com](https://duckcoding.com) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 763 ms | 🟢 已验证 |
| 45 | [duckcoding.ai](https://www.duckcoding.ai) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 805 ms | 🟢 已验证 |
| 46 | [api.ifopen.ai](https://api.ifopen.ai) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 810 ms | 🟢 已验证 |
| 47 | [BUZZ AI](https://buzzai.cc) | cn | 🔌 | claude, anthropic, openai | — | 9.3 | 876 ms | 🟢 已验证 |
| 48 | [api-gueai-com](https://api.gueai.com) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 1023 ms | 🟢 已验证 |
| 49 | [chintao.cn](https://chintao.cn) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 1140 ms | 🟢 已验证 |
| 50 | [ggwk1.online](https://www.ggwk1.online) | cn | 🔌 | claude, gemini, openai | — | 9.3 | 1156 ms | 🟢 已验证 |

> 仅展示 Top 50。完整 211 个榜单见 [`data/_leaderboard.zh.md`](data/_leaderboard.zh.md)。

<!-- LEADERBOARD_ZH:END -->

</details>

> 📌 **想上榜?** 用[中转站模板](./gateways/_template.md)提交 PR,符合[收录标准](./CONTRIBUTING.md#收录标准)即可收录。

---

## 📊 分类

### 按目标市场

- 🌍 [全球中转站](./data/by-region.md#global) — OpenRouter, Together AI, Groq, Fireworks
- 🇨🇳 [国内中转站](./data/by-region.md#china) — Road2All, DeepBricks, AiHubMix, OhMyGPT
- 🏠 [自部署方案](./data/by-region.md#self-hosted) — One API, NewAPI, LiteLLM

### 按特色

- 🤖 [Claude Code 兼容](./data/by-feature.md#claude-code) — 完整支持 Claude Code CLI
- ⚡ [低延迟](./data/by-feature.md#low-latency) — TTFT 低于 500ms
- 💰 [低价优选](./data/by-feature.md#best-price) — 相较官方有显著折扣
- 🔒 [隐私优先](./data/by-feature.md#privacy) — 无数据留存 / 可私有部署

### 按支付方式

- 💳 [支付宝/微信](./data/by-payment.md#cn) — 国内用户友好
- 💳 [信用卡](./data/by-payment.md#card) — 国际通用
- ₿ [加密货币](./data/by-payment.md#crypto) — 匿名支付

---

## 📝 评测

深度评测和基准报告:

- 📊 [2026 Q2 中转站基准测试](./reviews/2026-Q2-benchmark.md) *(即将发布)*
- 🔬 [Claude Code 中转站横评](./reviews/claude-code-shootout.md) *(即将发布)*
- 💸 [价格分析: 官方 vs 中转](./reviews/pricing-analysis.md) *(即将发布)*
- 🧪 [评分方法论](./reviews/methodology.md)

---

## ⚠️ 黑名单

被标记存在严重问题的中转站(跑路、数据泄漏、模型造假)。

详见 [blacklist.md](./data/blacklist.md),含事件证据归档。

> 如果你被某中转站坑过,请在 GitHub Discussion 提交证据。我们会公开透明地处理。

---

## 🧪 基准测试

我们定期运行基准测试,评估:

- **延迟** (TTFT, 总响应时间)
- **吞吐** (tokens/秒)
- **稳定性** (在线率 %)
- **准确度** (模型行为是否与官方一致)
- **计费一致性** (报价 vs 实际扣费)

测试脚本见 [`scripts/benchmark.py`](./scripts/benchmark.py),结果在 [`data/benchmarks/`](./data/benchmarks/)。

---

## 🤝 贡献

欢迎用户、中转站运营方、研究者提交 PR。详见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

**快速贡献:**
- ✏️ 更新某中转站的价格或模型列表
- 📝 提交新中转站(用[模板](./gateways/_template.md))
- 🚨 举报跑路或故障
- 🧪 提交基准测试数据
- 🌐 改善翻译

---

## 📜 许可证

内容基于 [MIT License](./LICENSE) 发布。鼓励署名但不强制。

---

## 🙏 致谢

灵感来源: [apicompare.best](https://apicompare.best)、[helpaio.com/transit](https://www.helpaio.com/transit)、[trustmrr.com](https://trustmrr.com) — 它们分别启发了我们的**价格数据、内容深度、可验证信任**三个维度。我们把它们融合进 GitHub 原生的开放性中。

---

<p align="center">
  <em>由 <a href="https://github.com/MackDing">Mack Ding</a> 和贡献者共建 · 献给全球 OPC 社区</em>
</p>
