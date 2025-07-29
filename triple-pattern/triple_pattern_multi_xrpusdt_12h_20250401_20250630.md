# Triple Pattern Strategy Comparison - Multi Position - XRPUSDT 12h

## Strategy Overview
- **Pattern**: Triple Top & Triple Bottom Pattern
- **Entry**: Breakout/breakdown with reversal candles
- **Reversal Candles**: Hammer, Engulfing, Doji patterns
- **Position Management**: Up to 3 positions at a time
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods
- **Take Profit**: 5.0%
- **Position Size**: 20.0% of capital per position

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 22 | 12 |
| Win Rate | 36.36% | 41.67% |
| Total Return | -5.93% | -4.07% |
| Final Capital | $940.66 | $959.28 |
| Total PnL | $-59.34 | $-40.72 |
| Average PnL per Trade | $-2.70 | $-3.39 |
| Best Trade | $10.31 | $12.70 |
| Worst Trade | $-15.99 | $-22.91 |
| Long Trades | 12 | 6 |
| Short Trades | 10 | 6 |
| Max Concurrent Positions | 3 | 3 |

## Strategy 1: Exit after 9 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-04-27 12:00 | 2025-05-02 00:00 | LONG | $2.2520 | $2.2151 | $-3.28 | -1.64% | triple_bottom_breakout | Time | 9 |
| 1 | 2025-04-30 00:00 | 2025-05-04 12:00 | LONG | $2.2385 | $2.1560 | $-5.90 | -3.69% | triple_bottom_breakout | Time | 9 |
| 2 | 2025-04-30 12:00 | 2025-05-05 00:00 | SHORT | $2.1908 | $2.1427 | $2.81 | 2.20% | triple_top_breakdown | Time | 9 |
| 3 | 2025-05-02 00:00 | 2025-05-06 12:00 | LONG | $2.2151 | $2.1550 | $-3.85 | -2.71% | triple_bottom_breakout | Time | 9 |
| 6 | 2025-05-08 00:00 | 2025-05-08 12:00 | LONG | $2.2082 | $2.3272 | $7.59 | 5.39% | triple_bottom_breakout | TP | 1 |
| 4 | 2025-05-04 12:00 | 2025-05-09 00:00 | SHORT | $2.1560 | $2.3950 | $-15.99 | -11.09% | triple_top_breakdown | Time | 9 |
| 5 | 2025-05-05 00:00 | 2025-05-09 12:00 | SHORT | $2.1427 | $2.3439 | $-13.29 | -9.39% | triple_top_breakdown | Time | 9 |
| 7 | 2025-05-13 00:00 | 2025-05-17 12:00 | LONG | $2.5344 | $2.3531 | $-13.85 | -7.15% | triple_bottom_breakout | Time | 9 |
| 8 | 2025-05-17 12:00 | 2025-05-22 00:00 | LONG | $2.3531 | $2.4319 | $6.39 | 3.35% | triple_bottom_breakout | Time | 9 |
| 9 | 2025-05-21 00:00 | 2025-05-25 12:00 | LONG | $2.3524 | $2.3417 | $-0.69 | -0.45% | triple_bottom_breakout | Time | 9 |
| 10 | 2025-05-21 12:00 | 2025-05-26 00:00 | LONG | $2.3952 | $2.3349 | $-3.08 | -2.52% | triple_bottom_breakout | Time | 9 |
| 11 | 2025-05-22 12:00 | 2025-05-27 00:00 | LONG | $2.4311 | $2.3197 | $-6.29 | -4.58% | triple_bottom_breakout | Time | 9 |
| 13 | 2025-05-26 00:00 | 2025-05-30 00:00 | SHORT | $2.3349 | $2.2066 | $7.47 | 5.49% | triple_top_breakdown | TP | 8 |
| 12 | 2025-05-25 12:00 | 2025-05-30 00:00 | LONG | $2.3417 | $2.2066 | $-8.08 | -5.77% | triple_bottom_breakout | Time | 9 |
| 14 | 2025-05-27 12:00 | 2025-05-30 12:00 | SHORT | $2.3168 | $2.1398 | $10.31 | 7.64% | triple_top_breakdown | TP | 6 |
| 15 | 2025-05-31 00:00 | 2025-06-04 12:00 | SHORT | $2.1394 | $2.2009 | $-5.52 | -2.87% | triple_top_breakdown | Time | 9 |
| 16 | 2025-06-06 12:00 | 2025-06-11 00:00 | SHORT | $2.1598 | $2.3146 | $-13.69 | -7.17% | triple_top_breakdown | Time | 9 |
| 19 | 2025-06-11 12:00 | 2025-06-13 00:00 | SHORT | $2.2704 | $2.1544 | $6.81 | 5.11% | triple_top_breakdown | TP | 3 |
| 17 | 2025-06-09 00:00 | 2025-06-13 00:00 | SHORT | $2.2689 | $2.1544 | $7.71 | 5.05% | triple_top_breakdown | TP | 8 |
| 18 | 2025-06-10 00:00 | 2025-06-14 12:00 | LONG | $2.3046 | $2.1394 | $-8.76 | -7.17% | triple_bottom_breakout | Time | 9 |
| 20 | 2025-06-22 12:00 | 2025-06-27 00:00 | SHORT | $2.0172 | $2.0909 | $-6.92 | -3.65% | triple_top_breakdown | Time | 9 |
| 21 | 2025-06-25 00:00 | 2025-06-29 12:00 | LONG | $2.1952 | $2.2061 | $0.75 | 0.50% | triple_bottom_breakout | Time | 9 |

## Strategy 2: Exit after 26 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 1 | 2025-04-30 00:00 | 2025-05-09 00:00 | LONG | $2.2385 | $2.3950 | $11.19 | 6.99% | triple_bottom_breakout | TP | 18 |
| 0 | 2025-04-27 12:00 | 2025-05-09 00:00 | LONG | $2.2520 | $2.3950 | $12.70 | 6.35% | triple_bottom_breakout | TP | 23 |
| 2 | 2025-04-30 12:00 | 2025-05-13 12:00 | SHORT | $2.1908 | $2.5829 | $-22.91 | -17.90% | triple_top_breakdown | Time | 26 |
| 3 | 2025-05-13 00:00 | 2025-05-26 00:00 | LONG | $2.5344 | $2.3349 | $-14.10 | -7.87% | triple_bottom_breakout | Time | 26 |
| 6 | 2025-05-26 00:00 | 2025-05-30 00:00 | SHORT | $2.3349 | $2.2066 | $7.59 | 5.49% | triple_top_breakdown | TP | 8 |
| 4 | 2025-05-17 12:00 | 2025-05-30 12:00 | LONG | $2.3531 | $2.1398 | $-14.90 | -9.06% | triple_bottom_breakout | Time | 26 |
| 5 | 2025-05-21 00:00 | 2025-06-03 00:00 | LONG | $2.3524 | $2.2149 | $-7.69 | -5.85% | triple_bottom_breakout | Time | 26 |
| 9 | 2025-06-09 00:00 | 2025-06-13 00:00 | SHORT | $2.2689 | $2.1544 | $6.48 | 5.05% | triple_top_breakdown | TP | 8 |
| 7 | 2025-05-31 00:00 | 2025-06-13 00:00 | SHORT | $2.1394 | $2.1544 | $-1.19 | -0.70% | triple_top_breakdown | Time | 26 |
| 8 | 2025-06-06 12:00 | 2025-06-19 12:00 | SHORT | $2.1598 | $2.1648 | $-0.37 | -0.23% | triple_top_breakdown | Time | 26 |
| 10 | 2025-06-22 12:00 | 2025-06-29 12:00 | SHORT | $2.0172 | $2.2061 | $-18.29 | -9.36% | triple_top_breakdown | End | 14 |
| 11 | 2025-06-25 00:00 | 2025-06-29 12:00 | LONG | $2.1952 | $2.2061 | $0.78 | 0.50% | triple_bottom_breakout | End | 9 |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with -4.07% return vs -5.93%.

### Key Observations:
- **Trade Frequency**: 22 vs 12 trades
- **Win Rate Difference**: 36.36% vs 41.67%
- **Return Difference**: 1.86% gap
- **Position Management**: Up to 3 positions at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)
- **Position Size**: 20.0% of capital per position

---
*Báo cáo được tạo tự động bởi Triple Pattern Multi-Position Backtest System*
