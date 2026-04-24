# Data And Methodology

Use this reference when generating `weekly-finance-trading-outlook` articles. It converts news and upstream analysis into a repeatable next-week sector and stock outlook.

## 0. Market Coverage Requirement

Cover both markets in every article:

- US equities: US-listed sectors/industries, sector ETFs where useful, and US-listed stocks.
- China A-shares: China A-share industries/themes and Shanghai/Shenzhen/Beijing-listed stocks.

Keep the two markets separate through the workflow because their liquidity, policy, investor structure, settlement calendars, and data signals differ. Do not infer A-share conclusions from US data, or US conclusions from A-share data, unless the transmission mechanism is stated and verified.

Minimum output target when evidence is sufficient:

| Market | Bullish sectors | Bearish sectors | Bullish stocks | Bearish stocks |
| --- | ---: | ---: | ---: | ---: |
| US equities | 2-4 | 2-4 | At least 2 | At least 2 |
| China A-shares | 2-4 | 2-4 | At least 2 | At least 2 |

If evidence is insufficient for any cell, write `证据不足，暂不强推` and explain the missing data.

## 1. Data Checklist

### Market Behavior

Use price and volume as the first verification layer.

- Price/volume: volume breakout, low-volume rebound, high-volume selloff, low-volume pullback.
- Relative strength: sector ETF or index vs broad market over 1 week, 1 month, and 3 months when available.
- Technical levels: support/resistance, 20/50/200-day moving averages, previous high/low, gap support.
- US baseline: S&P 500, Nasdaq Composite or Nasdaq 100, Russell 2000, S&P sector indexes/ETFs.
- A-share baseline: 上证指数、深证成指、创业板指、科创50、沪深300、中证500/1000, and relevant CSI/SW sector indexes or ETFs.

Interpretation:

- Bullish confirmation: catalyst + higher volume + breakout above key resistance + rising relative strength.
- Bearish confirmation: bad catalyst + high-volume breakdown + weak breadth + failed rebound near resistance.
- Warning: favorable news with shrinking volume or weak breadth can indicate insufficient follow-through.

### Capital Flows

Use flows to test whether larger capital is confirming the narrative.

- A-shares: northbound funds when available, main fund net inflow/outflow, margin balance.
- US/global: ETF flows, sector fund flows, institutional positioning when available.
- Company level: abnormal turnover, block trades, buybacks, insider transactions, 13F only as stale context.

Interpretation:

- Inflow after a catalyst supports continuation only if valuation/crowding is not extreme.
- Outflow on good news can mean "借利好出货".
- Inflow on bad news can mean absorption, but require price stabilization before calling bullish.

### Structure And Sentiment

Measure market temperature objectively.

- Breadth: advancers/decliners, sector participation, equal-weight vs cap-weight index.
- 52-week highs/lows: confirm or reject index strength.
- Volatility: VIX for US markets, China volatility indicators when available.
- Options: put/call ratio, skew, implied volatility term structure when available.
- A-share short-term sentiment: limit-up/limit-down count, consecutive limit-up height, broken-board rate.
- US breadth: NYSE/Nasdaq advancers-decliners, 52-week highs/lows, equal-weight vs cap-weight S&P 500.
- A-share breadth: all-market advancers-decliners, limit-up/limit-down, broken-board rate, ST/ex-ST risk where relevant.

Interpretation:

- Healthy bullish setup: broad participation, more new highs, controlled volatility, sector leadership expanding.
- Fragile bullish setup: index rises while breadth narrows, new highs shrink, volatility complacency is extreme.
- Reversal setup: panic volatility plus capitulation volume can support a rebound only after price stabilizes.

### Liquidity

Liquidity decides how much valuation expansion the market can support.

- China: 10Y government bond yield, SHIBOR, DR007, PBOC open market operations, credit impulse when available.
- US/global: Fed balance sheet, TGA balance, US Treasury yields, dollar index, financial conditions.
- Micro liquidity: margin financing balance, fund issuance, ETF creations/redemptions, money market fund flows.

Interpretation:

- Falling rates and easing liquidity usually support growth and duration assets.
- Rising yields and tighter dollar liquidity usually pressure long-duration equities and crowded risk assets.
- Liquidity signals dominate when policy or central-bank expectations change sharply.

### Expectations And Crowding

Search for expectation gaps, not just good or bad news.

- Consensus estimates: EPS/revenue revisions, earnings surprise, guidance revisions.
- Valuation: forward P/E, EV/EBITDA, P/B, percentile vs own history and peers when available.
- Positioning: fund over/underweight, ETF ownership, short interest, borrow cost, put/call skew.
- Event pricing: pre-event run-up or selloff, implied move before earnings/events.

Interpretation:

- Good news + low expectation = bullish catalyst.
- Good news + high expectation/crowding = risk of "利好出尽".
- Bad news + high expectation = bearish shock.
- Bad news + low expectation/priced-in = possible "利空出尽".

## 2. Three-Factor Model

Next-week price movement can be approximated as:

`未来一周涨跌 = 盈利预期变化 + 估值/情绪变化 + 流动性溢价变化`

Assign weights based on current regime:

- Earnings season: earnings expectation 45-60%, sentiment 20-35%, liquidity 15-25%.
- Major policy/central-bank shift: liquidity 40-60%, sentiment 20-35%, earnings 15-25%.
- Range-bound market without clear macro driver: sentiment/funds 40-55%, earnings 25-35%, liquidity 15-25%.
- Crisis or shock: liquidity and balance-sheet pressure dominate until volatility stabilizes.

Use a simple score from -2 to +2 for each factor:

| Score | Meaning |
| --- | --- |
| +2 | Strong positive, verified by multiple data types |
| +1 | Positive, but partial confirmation |
| 0 | Neutral or mixed |
| -1 | Negative, but partial confirmation |
| -2 | Strong negative, verified by multiple data types |

Overall interpretation:

- `+4` or above: high-conviction bullish candidate.
- `+2` to `+3`: medium-conviction bullish candidate.
- `-2` to `-3`: medium-conviction bearish candidate.
- `-4` or below: high-conviction bearish candidate.
- Between `-1` and `+1`: watchlist only unless event risk is unusually clear.

## 3. News-Data Verification

For each important news item:

1. Identify whether it changes earnings, valuation/sentiment, liquidity, or only narrative.
2. Check whether price and volume confirm the news.
3. Check whether breadth and sector participation confirm continuation.
4. Check whether flows confirm accumulation/distribution.
5. Check whether valuation, expectations, and crowding leave room for follow-through.
6. State the assumption and falsification signal.

Avoid this logic:

`利好新闻 -> 看涨`

Use this logic:

`新闻 -> 约束变化 -> 资金行为 -> 定价结果 -> 风险边界 -> 可验证信号`

## 4. Top-Down Selection Process

### Macro Position

Decide whether next week should be:

- Aggressive: liquidity supportive, volatility stable/falling, breadth expanding.
- Balanced: mixed macro signals, sector rotation but no broad confirmation.
- Defensive: yields rising, volatility rising, breadth weakening, liquidity tightening.

### Sector Direction

Screen sectors for:

- Verified catalyst from policy, earnings, supply/demand, rate changes, commodity prices, or currency.
- Relative strength vs broad market.
- Flows and participation.
- Valuation and crowding room.

Select only sectors where the evidence chain is complete enough to explain.

Run this screen separately for US equities and China A-shares. A sector can be bullish in one market and bearish in the other because policy exposure, earnings cycle, valuation, and positioning differ.

### Stock Selection

Within selected sectors, prefer stocks with:

- Company-specific catalyst or expectation revision.
- Volume-confirmed breakout/reversal or breakdown.
- Better relative strength than sector peers for bullish names; worse relative strength for bearish names.
- Manageable valuation and crowding.
- Clear technical invalidation level or observable condition.

For US stocks, prioritize company filings, earnings releases, guidance, analyst estimate revisions, sector ETF confirmation, options/short interest when reliable, and dollar/yield sensitivity.

For A-shares, prioritize exchange announcements, earnings previews, policy/industry data, northbound/main fund flows, margin financing, daily limit behavior, sector theme breadth, and avoid unsupported rumor-driven themes.

## 5. Trading Plan Requirements

For every stock include:

- Market: US equities or China A-shares.
- Direction: bullish, bearish, or watchlist.
- Action: buy, hold, sell, reduce, or observe.
- Entry: price zone if verified; otherwise condition-based entry.
- Position: suggested staging, for example 30% initial, 30% confirmation, 40% only after breakout.
- Exit: profit-taking zone or condition.
- Invalidation: stop-loss or thesis-break condition.
- Tracking: 2-4 observable data points to update next week.

Keep trading advice conditional:

- If the base assumption holds, state the action.
- If the falsification signal appears, state the alternative action.
- If data quality is insufficient, use `观望` instead of forced action.

## 6. Visuals

Include at least two visuals. Good choices:

- Sector score table with earnings/sentiment/liquidity sub-scores.
- Bullish vs bearish heatmap.
- Mermaid scenario tree.
- Mermaid flowchart for `触发事件 -> 资金行为 -> 定价结果`.
- Stock action table.

Use visuals to compress evidence, not to decorate.

## 7. Validation Checklist

Before saving, verify:

- Dates match the outlook horizon and upstream report date.
- Numbers have units and source links.
- Market data is labeled close, intraday, or pending.
- Actual data and expectations are not mixed.
- Bullish and bearish sections both include assumptions and invalidation.
- Stock-level advice is explicit and conditional.
- No conclusion relies on a single anecdote.
- Disclaimer is present.
