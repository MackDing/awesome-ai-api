# awesome-ai-api

> 全球最大的开源 AI API 中转站评测中心
> 社区驱动，完全透明，无付费排名

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)

**🇨🇳 中文** · [English](./README.md)

---

## 这是什么?

`awesome-ai-api` 是一个**开源的 AI API 中转站目录和评测中心**。

我们追踪、对比、评测那些能让你通过统一 API 访问 Claude、GPT、Gemini、DeepSeek、Qwen 等 200+ 模型的服务——通常价格更低、支付方式更友好、功能更丰富。

### 为什么做这个?

- 🔍 **透明** — 无付费排名，数据公开，PR 可编辑
- 🌍 **全球视野** — 中英双语，涵盖国内外中转站
- 🛠 **开发者优先** — 结构化 JSON 数据，不只是一个好看的页面
- 🤝 **社区驱动** — 价格和评测由真实用户更新

---

## 目录

- [🏆 排行榜](#-排行榜)
- [📊 分类](#-分类)
- [📝 评测](#-评测)
- [⚠️ 黑名单](#️-黑名单)
- [🧪 基准测试](#-基准测试)
- [🤝 贡献](#-贡献)
- [📜 许可证](#-许可证)

---

## 🏆 排行榜

*最后更新: 2026-04-22 · [评分方法](./reviews/methodology.md)*

| 排名 | 中转站 | 类型 | 模型数 | Claude Code | 支付 | 评分 | 评测 |
|------|--------|------|--------|-------------|------|------|------|
| 🥇 1 | [OpenRouter](./gateways/openrouter.md) | 全球 | 300+ | ✅ | 💳 卡/加密货币 | 9.4 | [查看](./gateways/openrouter.md) |
| 🥈 2 | [One API (自部署)](./gateways/one-api.md) | 自部署 | 任意 | ✅ | N/A | 9.2 | [查看](./gateways/one-api.md) |
| 🥉 3 | [Road2All](./gateways/road2all.md) | 国内 | 100+ | ✅ | 💳 支付宝/微信 | 9.0 | [查看](./gateways/road2all.md) |
| 4 | [DeepBricks](./gateways/deepbricks.md) | 国内 | 80+ | ✅ | 💳 支付宝 | 8.8 | [查看](./gateways/deepbricks.md) |
| 5 | [AiHubMix](./gateways/aihubmix.md) | 国内 | 150+ | ✅ | 💳 支付宝/微信 | 8.7 | [查看](./gateways/aihubmix.md) |
| 6 | [OhMyGPT](./gateways/ohmygpt.md) | 国内 | 100+ | ✅ | 💳 支付宝/微信 | 8.6 | [查看](./gateways/ohmygpt.md) |
| 7 | [API2D](./gateways/api2d.md) | 国内 | 60+ | ✅ | 💳 支付宝/微信 | 8.5 | [查看](./gateways/api2d.md) |
| 8 | [Together AI](./gateways/together-ai.md) | 全球 | 100+ | ❌ | 💳 信用卡 | 8.4 | [查看](./gateways/together-ai.md) |
| 9 | [Groq](./gateways/groq.md) | 全球 | 20+ | ❌ | 💳 信用卡 | 8.3 | [查看](./gateways/groq.md) |
| 10 | [Fireworks AI](./gateways/fireworks-ai.md) | 全球 | 50+ | ❌ | 💳 信用卡 | 8.2 | [查看](./gateways/fireworks-ai.md) |

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
