# Triple Pattern Strategy Comparison - Multi Position - XRPUSDT 6h

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
| Total Trades | 38 | 24 |
| Win Rate | 42.11% | 58.33% |
| Total Return | -4.08% | -2.37% |
| Final Capital | $959.18 | $976.35 |
| Total PnL | $-40.82 | $-23.65 |
| Average PnL per Trade | $-1.07 | $-0.99 |
| Best Trade | $12.15 | $12.98 |
| Worst Trade | $-13.91 | $-45.13 |
| Long Trades | 17 | 11 |
| Short Trades | 21 | 13 |
| Max Concurrent Positions | 3 | 3 |

## Strategy 1: Exit after 9 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-04-25 18:00 | 2025-04-28 00:00 | SHORT | $2.1812 | $2.2727 | $-8.39 | -4.19% | triple_top_breakdown | Time | 9 |
| 1 | 2025-04-26 06:00 | 2025-04-28 06:00 | LONG | $2.1938 | $2.3189 | $9.12 | 5.70% | triple_bottom_breakout | TP | 8 |
| 2 | 2025-04-30 06:00 | 2025-05-02 12:00 | LONG | $2.2385 | $2.2147 | $-2.13 | -1.06% | triple_bottom_breakout | Time | 9 |
| 3 | 2025-04-30 18:00 | 2025-05-03 00:00 | SHORT | $2.1908 | $2.2118 | $-1.53 | -0.96% | triple_top_breakdown | Time | 9 |
| 4 | 2025-05-01 12:00 | 2025-05-03 18:00 | LONG | $2.2346 | $2.1872 | $-2.72 | -2.12% | triple_bottom_breakout | Time | 9 |
| 5 | 2025-05-02 12:00 | 2025-05-04 18:00 | SHORT | $2.2147 | $2.1560 | $3.77 | 2.65% | triple_top_breakdown | Time | 9 |
| 6 | 2025-05-03 06:00 | 2025-05-05 12:00 | SHORT | $2.1881 | $2.1443 | $2.91 | 2.00% | triple_top_breakdown | Time | 9 |
| 7 | 2025-05-05 12:00 | 2025-05-07 18:00 | SHORT | $2.1443 | $2.1265 | $1.66 | 0.83% | triple_top_breakdown | Time | 9 |
| 8 | 2025-05-05 18:00 | 2025-05-08 00:00 | SHORT | $2.1306 | $2.1749 | $-3.33 | -2.08% | triple_top_breakdown | Time | 9 |
| 9 | 2025-05-07 12:00 | 2025-05-09 18:00 | SHORT | $2.1144 | $2.3439 | $-13.91 | -10.85% | triple_top_breakdown | Time | 9 |
| 10 | 2025-05-10 00:00 | 2025-05-12 06:00 | LONG | $2.3729 | $2.4490 | $6.32 | 3.21% | triple_bottom_breakout | Time | 9 |
| 12 | 2025-05-11 06:00 | 2025-05-12 12:00 | LONG | $2.3863 | $2.5633 | $9.36 | 7.42% | triple_bottom_breakout | TP | 5 |
| 11 | 2025-05-10 06:00 | 2025-05-12 12:00 | LONG | $2.3799 | $2.5633 | $12.15 | 7.71% | triple_bottom_breakout | TP | 9 |
| 13 | 2025-05-12 18:00 | 2025-05-15 00:00 | LONG | $2.5439 | $2.4980 | $-3.66 | -1.80% | triple_bottom_breakout | Time | 9 |
| 14 | 2025-05-14 00:00 | 2025-05-16 06:00 | LONG | $2.5864 | $2.4254 | $-10.09 | -6.22% | triple_bottom_breakout | Time | 9 |
| 15 | 2025-05-14 18:00 | 2025-05-17 00:00 | LONG | $2.5503 | $2.3642 | $-9.46 | -7.30% | triple_bottom_breakout | Time | 9 |
| 16 | 2025-05-15 12:00 | 2025-05-17 18:00 | LONG | $2.4827 | $2.3531 | $-7.49 | -5.22% | triple_bottom_breakout | Time | 9 |
| 17 | 2025-05-16 06:00 | 2025-05-18 12:00 | LONG | $2.4254 | $2.3972 | $-1.69 | -1.16% | triple_bottom_breakout | Time | 9 |
| 18 | 2025-05-17 00:00 | 2025-05-19 06:00 | LONG | $2.3642 | $2.3243 | $-2.37 | -1.69% | triple_bottom_breakout | Time | 9 |
| 19 | 2025-05-18 12:00 | 2025-05-20 18:00 | SHORT | $2.3972 | $2.3565 | $2.85 | 1.70% | triple_top_breakdown | Time | 9 |
| 20 | 2025-05-20 00:00 | 2025-05-22 06:00 | SHORT | $2.3759 | $2.4319 | $-3.82 | -2.36% | triple_top_breakdown | Time | 9 |
| 21 | 2025-05-20 12:00 | 2025-05-22 18:00 | SHORT | $2.3492 | $2.4311 | $-4.52 | -3.49% | triple_top_breakdown | Time | 9 |
| 22 | 2025-05-21 06:00 | 2025-05-23 12:00 | SHORT | $2.3524 | $2.3669 | $-0.85 | -0.62% | triple_top_breakdown | Time | 9 |
| 23 | 2025-05-22 18:00 | 2025-05-23 18:00 | SHORT | $2.4311 | $2.2966 | $9.24 | 5.53% | triple_top_breakdown | TP | 4 |
| 24 | 2025-05-23 12:00 | 2025-05-25 18:00 | SHORT | $2.3669 | $2.3417 | $1.71 | 1.06% | triple_top_breakdown | Time | 9 |
| 25 | 2025-05-23 18:00 | 2025-05-26 00:00 | SHORT | $2.2966 | $2.3447 | $-3.44 | -2.09% | triple_top_breakdown | Time | 9 |
| 26 | 2025-05-31 18:00 | 2025-06-03 00:00 | SHORT | $2.1738 | $2.2037 | $-2.70 | -1.38% | triple_top_breakdown | Time | 9 |
| 27 | 2025-06-01 00:00 | 2025-06-03 06:00 | SHORT | $2.1711 | $2.2149 | $-3.16 | -2.02% | triple_top_breakdown | Time | 9 |
| 28 | 2025-06-03 18:00 | 2025-06-06 00:00 | LONG | $2.2446 | $2.1320 | $-9.77 | -5.02% | triple_bottom_breakout | Time | 9 |
| 29 | 2025-06-05 00:00 | 2025-06-07 06:00 | SHORT | $2.1996 | $2.1829 | $1.18 | 0.76% | triple_top_breakdown | Time | 9 |
| 30 | 2025-06-07 18:00 | 2025-06-10 00:00 | SHORT | $2.1769 | $2.2844 | $-9.53 | -4.94% | triple_top_breakdown | Time | 9 |
| 31 | 2025-06-12 18:00 | 2025-06-15 00:00 | SHORT | $2.1899 | $2.1606 | $2.56 | 1.34% | triple_top_breakdown | Time | 9 |
| 32 | 2025-06-13 18:00 | 2025-06-16 00:00 | SHORT | $2.1472 | $2.1814 | $-2.44 | -1.59% | triple_top_breakdown | Time | 9 |
| 33 | 2025-06-15 06:00 | 2025-06-17 12:00 | SHORT | $2.1590 | $2.1474 | $0.87 | 0.54% | triple_top_breakdown | Time | 9 |
| 34 | 2025-06-17 00:00 | 2025-06-19 06:00 | LONG | $2.2362 | $2.1519 | $-5.99 | -3.77% | triple_bottom_breakout | Time | 9 |
| 35 | 2025-06-26 00:00 | 2025-06-28 06:00 | LONG | $2.1889 | $2.1927 | $0.33 | 0.17% | triple_bottom_breakout | Time | 9 |
| 36 | 2025-06-27 12:00 | 2025-06-28 12:00 | LONG | $2.0920 | $2.1996 | $7.82 | 5.14% | triple_bottom_breakout | TP | 4 |
| 37 | 2025-06-29 00:00 | 2025-06-29 12:00 | LONG | $2.1862 | $2.1897 | $0.31 | 0.16% | triple_bottom_breakout | End | 2 |

## Strategy 2: Exit after 26 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 1 | 2025-04-26 06:00 | 2025-04-28 06:00 | LONG | $2.1938 | $2.3189 | $9.12 | 5.70% | triple_bottom_breakout | TP | 8 |
| 0 | 2025-04-25 18:00 | 2025-05-02 06:00 | SHORT | $2.1812 | $2.2151 | $-3.11 | -1.55% | triple_top_breakdown | Time | 26 |
| 4 | 2025-05-02 12:00 | 2025-05-06 06:00 | SHORT | $2.2147 | $2.0903 | $8.03 | 5.62% | triple_top_breakdown | TP | 15 |
| 2 | 2025-04-30 06:00 | 2025-05-06 18:00 | LONG | $2.2385 | $2.1550 | $-6.04 | -3.73% | triple_bottom_breakout | Time | 26 |
| 3 | 2025-04-30 18:00 | 2025-05-07 06:00 | SHORT | $2.1908 | $2.1428 | $2.84 | 2.19% | triple_top_breakdown | Time | 26 |
| 7 | 2025-05-10 06:00 | 2025-05-12 12:00 | LONG | $2.3799 | $2.5633 | $9.97 | 7.71% | triple_bottom_breakout | TP | 9 |
| 6 | 2025-05-10 00:00 | 2025-05-12 12:00 | LONG | $2.3729 | $2.5633 | $12.98 | 8.02% | triple_bottom_breakout | TP | 10 |
| 5 | 2025-05-07 12:00 | 2025-05-14 00:00 | SHORT | $2.1144 | $2.5864 | $-45.13 | -22.32% | triple_top_breakdown | Time | 26 |
| 8 | 2025-05-12 18:00 | 2025-05-19 06:00 | LONG | $2.5439 | $2.3243 | $-14.36 | -8.63% | triple_bottom_breakout | Time | 26 |
| 9 | 2025-05-14 00:00 | 2025-05-20 12:00 | LONG | $2.5864 | $2.3492 | $-15.08 | -9.17% | triple_bottom_breakout | Time | 26 |
| 10 | 2025-05-14 18:00 | 2025-05-21 06:00 | LONG | $2.5503 | $2.3524 | $-10.21 | -7.76% | triple_bottom_breakout | Time | 26 |
| 11 | 2025-05-20 00:00 | 2025-05-26 12:00 | SHORT | $2.3759 | $2.3004 | $4.31 | 3.18% | triple_top_breakdown | Time | 26 |
| 12 | 2025-05-20 12:00 | 2025-05-27 00:00 | SHORT | $2.3492 | $2.2964 | $3.11 | 2.25% | triple_top_breakdown | Time | 26 |
| 13 | 2025-05-21 06:00 | 2025-05-27 18:00 | SHORT | $2.3524 | $2.3168 | $2.04 | 1.51% | triple_top_breakdown | Time | 26 |
| 14 | 2025-05-31 18:00 | 2025-06-07 06:00 | SHORT | $2.1738 | $2.1829 | $-0.80 | -0.42% | triple_top_breakdown | Time | 26 |
| 15 | 2025-06-01 00:00 | 2025-06-07 12:00 | SHORT | $2.1711 | $2.1731 | $-0.14 | -0.09% | triple_top_breakdown | Time | 26 |
| 16 | 2025-06-03 18:00 | 2025-06-10 06:00 | LONG | $2.2446 | $2.3046 | $3.28 | 2.67% | triple_bottom_breakout | Time | 26 |
| 17 | 2025-06-07 18:00 | 2025-06-14 06:00 | SHORT | $2.1769 | $2.1769 | $0.00 | 0.00% | triple_top_breakdown | Time | 26 |
| 18 | 2025-06-12 18:00 | 2025-06-19 06:00 | SHORT | $2.1899 | $2.1519 | $2.76 | 1.74% | triple_top_breakdown | Time | 26 |
| 19 | 2025-06-13 18:00 | 2025-06-20 06:00 | SHORT | $2.1472 | $2.1725 | $-1.50 | -1.18% | triple_top_breakdown | Time | 26 |
| 20 | 2025-06-15 06:00 | 2025-06-21 18:00 | SHORT | $2.1590 | $2.0632 | $5.99 | 4.44% | triple_top_breakdown | Time | 26 |
| 22 | 2025-06-27 12:00 | 2025-06-28 12:00 | LONG | $2.0920 | $2.1996 | $7.97 | 5.14% | triple_bottom_breakout | TP | 4 |
| 21 | 2025-06-26 00:00 | 2025-06-29 12:00 | LONG | $2.1889 | $2.1897 | $0.07 | 0.04% | triple_bottom_breakout | End | 14 |
| 23 | 2025-06-29 00:00 | 2025-06-29 12:00 | LONG | $2.1862 | $2.1897 | $0.25 | 0.16% | triple_bottom_breakout | End | 2 |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with -2.37% return vs -4.08%.

### Key Observations:
- **Trade Frequency**: 38 vs 24 trades
- **Win Rate Difference**: 42.11% vs 58.33%
- **Return Difference**: 1.72% gap
- **Position Management**: Up to 3 positions at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)
- **Position Size**: 20.0% of capital per position

---
*Báo cáo được tạo tự động bởi Triple Pattern Multi-Position Backtest System*
