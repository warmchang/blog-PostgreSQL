---
name: weekly-finance-trading-outlook
description: Generate a source-backed Chinese Markdown outlook for the next trading week from daily-finance and finance-core-analysis outputs, plus current authoritative market data. Use when the user asks to identify high-probability bullish and bearish industries/sectors and individual stocks for the coming week across both US equities and China A-shares, with explicit assumptions, falsification signals, charts/tables, validation, and concrete trading plans including buy/hold/sell, entry/exit, staged position, watchlist, and action guidance.
---

# Weekly Finance Trading Outlook

## Overview

Generate a publishable Chinese Markdown article that forecasts **未来一周美股和中国 A 股极大概率看涨和看空的行业与股票**.

Use upstream `daily-finance` for verified facts and `finance-core-analysis` for mechanism analysis. Add current authoritative market, liquidity, sentiment, positioning, and expectation data before making any sector or stock call.

The output must cover both markets:

- US equities: US-listed sectors/industries, sector ETFs when useful, and US-listed stocks.
- China A-shares: A-share industries/themes and Shanghai/Shenzhen/Beijing-listed stocks when evidence is sufficient.

If one market is closed, on holiday, or lacks reliable current data, still include that market as a separate section and mark the limitation clearly.

## Inputs

Prefer reading both files for the same report date:

- `markdown/daily-finance-YYYY-MM-DD.md`
- `markdown/finance-core-analysis-YYYY-MM-DD.md`

If the user provides files or pasted content, use those. If the report date is ambiguous and no latest pair can be inferred from `markdown/`, ask which date to use.

If only one upstream file exists:

- With only `daily-finance`: build the mechanism yourself and mark confidence lower.
- With only `finance-core-analysis`: reuse its fact base and avoid unsupported news details.

## Required External Data

Always access current external data for a current outlook. Use primary or authoritative sources first:

- Official releases, exchanges, central banks, regulators, company filings, ETF/fund issuers
- Reuters, Bloomberg, FT, WSJ
- 财新、第一财经、财经、21世纪经济报道、经济观察报
- Market data tools for prices, volume, volatility, yields, commodities, currencies, and ETFs
- US market data: major indexes, S&P 500/Nasdaq/Russell breadth, sector ETFs, VIX, Treasury yields, dollar index, ETF flows, earnings revisions.
- A-share market data: major indexes, CSI/SW sector indexes or ETFs, northbound funds, main fund flows, margin financing, limit-up/limit-down data, China 10Y yield, SHIBOR/DR007.

Read `references/data-and-methodology.md` when selecting data sources, scoring signals, and writing scenario/falsification logic.

Do not present unverified data as fact. If a key data point is inaccessible, say so and reduce confidence instead of inventing a substitute.

## Workflow

1. **Build the fact base**
   - Extract 3-5 key facts from `daily-finance`.
   - Extract the main mechanism, base case, alternative case, and watch variables from `finance-core-analysis`.
   - Re-check stale or market-moving numbers with current authoritative data.

2. **Collect confirmation data**
   - Market behavior: price/volume, relative strength, support/resistance, moving averages.
   - Capital flows: main funds, northbound funds for A-shares, ETF/fund flows for US/global markets.
   - Structure and sentiment: market breadth, 52-week highs/lows, VIX or local volatility index, put/call ratio, limit-up/limit-down data where relevant.
   - Liquidity: China 10Y yield, SHIBOR/DR007 where relevant, Fed balance sheet, TGA, US yields, margin balance, fund issuance/positioning when available.
   - Expectations and positioning: earnings estimate revisions, revenue/EPS consensus, valuation percentile, institutional crowding.

3. **Score sectors**
   - Start top-down: macro risk appetite and liquidity set the recommended overall exposure.
   - Compare sectors with the three-factor model: earnings expectation, valuation/sentiment, liquidity premium.
   - Identify bullish and bearish sectors separately for US equities and China A-shares.
   - Target 2-4 bullish sectors and 2-4 bearish sectors per market when evidence is sufficient; use fewer only when data quality does not support more.
   - For every sector call, include: catalyst, data confirmation, assumption, falsification signal, confidence.

4. **Select stocks**
   - Select stocks separately for US equities and China A-shares from the highest-conviction sectors, and include representative bearish names where evidence supports downside risk.
   - Target at least 2 bullish and 2 bearish stocks per market when evidence is sufficient; otherwise explain why a market has fewer actionable names.
   - Require company-specific evidence: earnings/news catalyst, price-volume behavior, relative strength, fund flow or positioning, valuation/expectation context.
   - Avoid using one stock as proof of a whole sector. Separate stock-specific logic from sector logic.

5. **Write explicit trading plans**
   - For each stock, provide one clear action: `买入`, `持有`, `卖出`, `观望`, or `减仓`.
   - Include entry zone, invalidation/stop-loss condition, staged position plan, profit-taking or sell zone, observation triggers, and next action.
   - Make recommendations conditional on the stated assumptions. If assumptions break, give the alternative action.
   - If exact price levels cannot be verified, use observable technical conditions instead of fabricated prices.

6. **Validate before saving**
   - Check dates, units, directions, close vs intraday status, actual vs expected.
   - Ensure every important number has a source.
   - Ensure every conclusion follows from a causal chain, not from a headline.
   - Ensure bullish and bearish calls state assumptions and falsification signals.
   - Ensure stock advice is explicit but risk-bounded.

## Required Article Structure

Save a complete Markdown article with this structure:

1. `# 标题`
2. `## 核心结论`
   - Overall stance for next week: aggressive, balanced, or defensive.
   - Separate US equity stance and China A-share stance.
   - Bullish and bearish sectors for US equities.
   - Bullish and bearish sectors for China A-shares.
   - Highest-conviction stock actions in one table, grouped by market.
3. `## 数据底座`
   - Upstream facts from daily-finance and finance-core-analysis.
   - Newly verified market, liquidity, sentiment, flow, and expectation data.
   - Separate US and China/A-share data snapshots.
4. `## 方法论：新闻-数据验证 + 三因子模型`
   - Explain weights used for earnings expectation, valuation/sentiment, and liquidity.
   - State why the current week should emphasize those weights.
5. `## 美股：下周看涨行业`
   - One subsection per sector: logic, evidence, assumptions, falsification, representative stocks.
6. `## 美股：下周看空行业`
   - Same structure as bullish sectors.
7. `## 中国 A 股：下周看涨行业`
   - One subsection per sector: logic, evidence, assumptions, falsification, representative stocks.
8. `## 中国 A 股：下周看空行业`
   - Same structure as bullish sectors.
9. `## 个股操盘计划`
   - Table plus narrative for each stock.
   - Group by `美股` and `中国 A 股`.
   - Include action, entry, position sizing, exit, stop/invalidation, tracking triggers.
10. `## 图表与可视化`
   - Include at least 2 useful visuals: Markdown tables, Mermaid charts, ASCII heatmaps, or sourced image links when available.
   - Include at least one visual comparing US and A-share sector scores or market regimes.
   - Prefer visuals that compare sector scores, scenario paths, or trading decision trees.
11. `## 反身性与失效条件`
   - Explain what would invalidate the main view and how conclusions change.
   - Include separate invalidation signals for US equities and China A-shares.
12. `## 校验记录`
    - Briefly list data checks and logic checks performed.
13. `## 来源`
14. `## 免责声明`
    - Include: `本文仅供学习和研究参考，不构成任何投资建议或收益承诺。市场有风险，交易需独立决策并自担风险。`

## Output File

Save to:

`markdown/weekly-finance-trading-outlook-YYYY-MM-DD.md`

Use the same report date as the upstream files. If running on a weekend or holiday, still use the upstream report date unless the user specifies another date.

Create `markdown/` if missing. Use UTF-8. If saving fails, output the complete Markdown in chat.

## Guardrails

- Do not use self-media, social media rumors, or unsourced screenshots as evidence.
- Do not recommend leveraged or derivative trades unless the user explicitly asks.
- Do not make a sector call from isolated anecdotes.
- Do not hide uncertainty. Use confidence labels: `高`, `中`, `低`.
- Do not overstate "极大概率": define it as evidence-weighted probability, not certainty.
- Do not omit bearish alternatives for bullish calls or bullish alternatives for bearish calls.
- Do not collapse US equities and China A-shares into one generic conclusion; keep market-specific conclusions, data, and trading plans separate.
