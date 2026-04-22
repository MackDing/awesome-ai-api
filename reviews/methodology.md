# Scoring Methodology | 评分方法论

## Overview

Each gateway receives a score from 0 to 10 based on six weighted dimensions. All scores are verifiable from public data or community-contributed benchmarks.

每个中转站基于六个加权维度评分(0-10)。所有评分基于公开数据或社区贡献的基准测试。

## Dimensions | 维度

| Dimension | Weight | How we measure |
|-----------|--------|----------------|
| **Price** / 价格 | 25% | Discount vs. official prices across top 10 models |
| **Latency** / 延迟 | 15% | Median TTFT and total response time, measured from CN and US probes |
| **Stability** / 稳定性 | 20% | 30-day uptime, error rate, quota consistency |
| **Model Coverage** / 模型覆盖 | 15% | Number of supported latest-gen models (Claude 4.x, GPT-5, Gemini 2.5+) |
| **Support** / 客服 | 10% | Response time, refund policy, incident transparency |
| **Payment UX** / 支付体验 | 15% | Payment methods, invoicing, top-up friction |

**Overall score** = weighted average, rounded to 0.1

## Scoring Anchors | 评分锚点

- **10** — Industry-leading, no known weaknesses
- **9** — Excellent, minor quirks only
- **8** — Solid, a few rough edges
- **7** — Acceptable, has trade-offs
- **6** — Use with caution
- **≤5** — Significant issues; consider alternatives

## Data Sources | 数据来源

- **Public pricing pages** (cited per gateway)
- **Community benchmarks** submitted via PR with raw request logs
- **Uptime probes** (to be added: public status pages)
- **User reports** via GitHub Discussions (validated by multiple reporters)

## Conflict of Interest | 利益相关

- Gateway operators may contribute to their own entries but **must disclose** in the entry footer.
- Maintainers do not accept payment or gifts for placement.
- All scoring changes go through pull requests with visible diffs.

中转站运营方可以贡献自己的条目,但必须在页尾声明关系。维护者不接受付费排名。所有评分变动都通过可见的 PR diff 完成。

## Revision History | 版本历史

- `v0.1` (2026-04-22) — Initial methodology.
