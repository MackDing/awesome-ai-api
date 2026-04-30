# Contributing | 贡献指南

Thanks for helping make `awesome-ai-api` better! | 感谢你为 awesome-ai-api 做贡献!

## Quick Start | 快速开始

```bash
# 1. Fork this repo
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/awesome-ai-api.git
cd awesome-ai-api

# 3. Create a branch
git checkout -b add-new-gateway

# 4. Make changes (see below)

# 5. Commit and push
git commit -m "Add: NewGatewayName"
git push origin add-new-gateway

# 6. Open a PR
```

## Listing Criteria | 收录标准

A gateway must meet **all** of the following | 中转站必须满足以下**全部**条件:

- ✅ **Active** — Running for at least 30 days, responding to support requests | 运营至少 30 天,有响应的客服
- ✅ **Transparent pricing** — Public price list, no hidden fees | 公开价格表,无隐藏费用
- ✅ **No blatant fraud** — Not flagged as scam/rug-pull/fake-model | 未被举报跑路/假模型/欺诈
- ✅ **Accessible** — A working sign-up page and API endpoint | 可正常注册和调用
- ✅ **Independent operation** — Not a thin re-skin of an open-source aggregator (e.g. `new-api` / `one-api` / `oneapi`) without meaningful operational track record, original infrastructure, or differentiated value | 非开源聚合器（如 `new-api` / `one-api`）的简单换皮，需有独立运营记录、自有基础设施或差异化价值
- ✅ **Verifiable pricing table** — A concrete per-model price list in the entry or linked official page; vague claims like "X% cheaper than Y" alone are not sufficient | 条目内或官方页面提供具体逐模型定价表，仅写"比 X 便宜 Y%"不够

**Red flags that will block listing** | 直接拒收的红旗:
- Brand-new domain (< 30 days) submitting self-PR on day one | 域名启用不足 30 天即自荐
- Model catalog claims full Claude/GPT/Gemini frontier coverage with no upstream disclosure | 声称全量覆盖前沿模型但不披露上游来源
- Marketing copy in place of operational data (SLA numbers without status page, etc.) | 用营销话术代替运营数据（无 status page 的 SLA 承诺等）

**Not required** | 非必需条件:
- Any specific country / 不限国家
- Minimum revenue / 无收入门槛
- English-only site / 无需英文站点

## Adding a New Gateway | 添加新中转站

1. Copy `gateways/_template.md` to `gateways/<slug>.md` where `<slug>` is kebab-case (e.g. `my-new-gateway.md`)
1. 复制 `gateways/_template.md` 为 `gateways/<slug>.md`,`<slug>` 用小写短横连接 (例如 `my-new-gateway.md`)

2. Fill in all required fields | 填写所有必需字段
3. Add an entry to `data/gateways.json` | 在 `data/gateways.json` 添加记录
4. Add a row to the leaderboard tables in both READMEs | 在两个 README 的排行榜加一行
5. Open a PR with title `Add: <GatewayName>` | 提 PR,标题为 `Add: <中转站名>`

## Updating Pricing | 更新价格

Pricing changes frequently. PRs for price updates are auto-approved if:
价格变动频繁。价格更新 PR 会被快速合并,前提是:

- You provide a link to the official pricing page | 提供中转站官方价格页链接
- You update the `last_verified` date | 更新 `last_verified` 日期
- Only pricing fields are changed | 仅修改价格字段

## Reporting a Scam | 举报跑路

**Do not** add to blacklist directly in a PR.
**请勿**直接在 PR 中加入黑名单。

1. Open a [GitHub Discussion](https://github.com/MackDing/awesome-ai-api/discussions) under category `Reports` | 在 GitHub Discussion 开帖,分类选 `Reports`
2. Provide evidence: screenshots, timestamps, transaction records | 提供证据: 截图、时间戳、交易记录
3. Maintainers will verify before blacklisting | 维护者验证后才会加入黑名单

## Code of Conduct | 行为准则

- Be respectful | 保持尊重
- No promotional spam | 禁止推广灌水
- No AstroTurfing (fake reviews) | 禁止刷评/水军
- Gateway operators **may** contribute to their own entry but **must** disclose affiliation | 中转站运营方**可以**贡献自己的条目,但**必须**声明关联关系

## Questions? | 问题?

Open an [Issue](https://github.com/MackDing/awesome-ai-api/issues) or start a [Discussion](https://github.com/MackDing/awesome-ai-api/discussions).
提 [Issue](https://github.com/MackDing/awesome-ai-api/issues) 或开 [Discussion](https://github.com/MackDing/awesome-ai-api/discussions)。
