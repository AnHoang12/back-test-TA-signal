# Triple Pattern Strategy Comparison - Multi Position - ETHUSDT 6h

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
| Total Trades | 39 | 29 |
| Win Rate | 58.97% | 65.52% |
| Total Return | 3.10% | 3.63% |
| Final Capital | $1031.04 | $1036.25 |
| Total PnL | $31.04 | $36.25 |
| Average PnL per Trade | $0.80 | $1.25 |
| Best Trade | $18.66 | $15.87 |
| Worst Trade | $-49.16 | $-77.07 |
| Long Trades | 26 | 18 |
| Short Trades | 13 | 11 |
| Max Concurrent Positions | 3 | 3 |

## Strategy 1: Exit after 9 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-04-12 00:00 | 2025-04-14 06:00 | SHORT | $1568.5600 | $1675.3200 | $-13.61 | -6.81% | triple_top_breakdown | Time | 9 |
| 1 | 2025-04-13 00:00 | 2025-04-15 06:00 | SHORT | $1609.2800 | $1632.0500 | $-2.26 | -1.41% | triple_top_breakdown | Time | 9 |
| 2 | 2025-04-23 06:00 | 2025-04-25 12:00 | LONG | $1797.2300 | $1785.8200 | $-1.25 | -0.63% | triple_bottom_breakout | Time | 9 |
| 3 | 2025-04-23 12:00 | 2025-04-25 18:00 | LONG | $1800.7200 | $1784.6000 | $-1.41 | -0.90% | triple_bottom_breakout | Time | 9 |
| 4 | 2025-04-24 06:00 | 2025-04-26 12:00 | LONG | $1755.1000 | $1804.5000 | $3.55 | 2.81% | triple_bottom_breakout | Time | 9 |
| 5 | 2025-04-25 12:00 | 2025-04-27 18:00 | LONG | $1785.8200 | $1791.2900 | $0.43 | 0.31% | triple_bottom_breakout | Time | 9 |
| 6 | 2025-04-25 18:00 | 2025-04-28 00:00 | LONG | $1784.6000 | $1795.8000 | $0.90 | 0.63% | triple_bottom_breakout | Time | 9 |
| 7 | 2025-04-27 12:00 | 2025-04-29 18:00 | LONG | $1798.1200 | $1797.8100 | $-0.02 | -0.02% | triple_bottom_breakout | Time | 9 |
| 8 | 2025-04-28 00:00 | 2025-04-30 06:00 | LONG | $1795.8000 | $1815.7000 | $1.87 | 1.11% | triple_bottom_breakout | Time | 9 |
| 9 | 2025-04-29 12:00 | 2025-05-01 18:00 | LONG | $1825.1900 | $1838.1100 | $0.96 | 0.71% | triple_bottom_breakout | Time | 9 |
| 10 | 2025-05-06 12:00 | 2025-05-08 18:00 | SHORT | $1768.0200 | $2207.3900 | $-49.16 | -24.85% | triple_top_breakdown | Time | 9 |
| 12 | 2025-05-09 18:00 | 2025-05-10 18:00 | LONG | $2345.0400 | $2583.2300 | $15.28 | 10.16% | triple_bottom_breakout | TP | 4 |
| 11 | 2025-05-09 12:00 | 2025-05-10 18:00 | LONG | $2350.0300 | $2583.2300 | $18.66 | 9.92% | triple_bottom_breakout | TP | 5 |
| 13 | 2025-05-11 06:00 | 2025-05-13 12:00 | LONG | $2530.6700 | $2610.5500 | $6.15 | 3.16% | triple_bottom_breakout | Time | 9 |
| 14 | 2025-05-12 18:00 | 2025-05-13 18:00 | LONG | $2495.4700 | $2679.7100 | $11.50 | 7.38% | triple_bottom_breakout | TP | 4 |
| 15 | 2025-05-14 00:00 | 2025-05-16 06:00 | LONG | $2673.3600 | $2620.8300 | $-3.90 | -1.96% | triple_bottom_breakout | Time | 9 |
| 16 | 2025-05-15 00:00 | 2025-05-17 06:00 | SHORT | $2567.7100 | $2481.6700 | $5.32 | 3.35% | triple_top_breakdown | Time | 9 |
| 17 | 2025-05-17 06:00 | 2025-05-19 12:00 | LONG | $2481.6700 | $2505.0000 | $1.87 | 0.94% | triple_bottom_breakout | Time | 9 |
| 18 | 2025-05-18 12:00 | 2025-05-20 18:00 | SHORT | $2489.9200 | $2524.1900 | $-2.19 | -1.38% | triple_top_breakdown | Time | 9 |
| 19 | 2025-05-18 18:00 | 2025-05-21 00:00 | LONG | $2497.7800 | $2593.6100 | $4.88 | 3.84% | triple_bottom_breakout | Time | 9 |
| 20 | 2025-05-20 18:00 | 2025-05-22 06:00 | LONG | $2524.1900 | $2650.7500 | $8.68 | 5.01% | triple_bottom_breakout | TP | 6 |
| 21 | 2025-05-24 12:00 | 2025-05-26 18:00 | LONG | $2557.8000 | $2563.7000 | $0.46 | 0.23% | triple_bottom_breakout | Time | 9 |
| 22 | 2025-05-26 06:00 | 2025-05-28 12:00 | LONG | $2568.0800 | $2652.8000 | $5.31 | 3.30% | triple_bottom_breakout | Time | 9 |
| 23 | 2025-05-27 00:00 | 2025-05-29 00:00 | LONG | $2569.5100 | $2722.8000 | $10.09 | 5.97% | triple_bottom_breakout | TP | 8 |
| 24 | 2025-05-28 12:00 | 2025-05-30 18:00 | LONG | $2652.8000 | $2531.3400 | $-7.72 | -4.58% | triple_bottom_breakout | Time | 9 |
| 25 | 2025-05-30 00:00 | 2025-06-01 06:00 | LONG | $2643.7100 | $2497.3500 | $-9.45 | -5.54% | triple_bottom_breakout | Time | 9 |
| 27 | 2025-06-03 18:00 | 2025-06-05 18:00 | SHORT | $2593.3600 | $2414.0100 | $11.12 | 6.92% | triple_top_breakdown | TP | 8 |
| 26 | 2025-06-03 12:00 | 2025-06-05 18:00 | SHORT | $2619.1100 | $2414.0100 | $15.74 | 7.83% | triple_top_breakdown | TP | 9 |
| 28 | 2025-06-04 06:00 | 2025-06-06 12:00 | LONG | $2624.4000 | $2499.5000 | $-6.12 | -4.76% | triple_bottom_breakout | Time | 9 |
| 29 | 2025-06-06 18:00 | 2025-06-09 00:00 | SHORT | $2476.1000 | $2480.8800 | $-0.40 | -0.19% | triple_top_breakdown | Time | 9 |
| 30 | 2025-06-07 06:00 | 2025-06-09 12:00 | SHORT | $2495.7500 | $2571.6900 | $-4.99 | -3.04% | triple_top_breakdown | Time | 9 |
| 31 | 2025-06-13 12:00 | 2025-06-15 18:00 | SHORT | $2543.1900 | $2547.6100 | $-0.35 | -0.17% | triple_top_breakdown | Time | 9 |
| 32 | 2025-06-15 18:00 | 2025-06-18 00:00 | SHORT | $2547.6100 | $2537.1000 | $0.84 | 0.41% | triple_top_breakdown | Time | 9 |
| 33 | 2025-06-19 00:00 | 2025-06-21 06:00 | SHORT | $2522.1100 | $2442.7500 | $6.42 | 3.15% | triple_top_breakdown | Time | 9 |
| 34 | 2025-06-24 00:00 | 2025-06-26 06:00 | LONG | $2420.0100 | $2450.3600 | $2.58 | 1.25% | triple_bottom_breakout | Time | 9 |
| 35 | 2025-06-24 06:00 | 2025-06-26 12:00 | SHORT | $2409.4400 | $2420.7000 | $-0.77 | -0.47% | triple_top_breakdown | Time | 9 |
| 36 | 2025-06-24 18:00 | 2025-06-27 00:00 | LONG | $2448.4500 | $2440.0000 | $-0.45 | -0.35% | triple_bottom_breakout | Time | 9 |
| 37 | 2025-06-26 18:00 | 2025-06-29 00:00 | LONG | $2415.9600 | $2433.7700 | $1.32 | 0.74% | triple_bottom_breakout | Time | 9 |
| 38 | 2025-06-28 00:00 | 2025-06-29 12:00 | LONG | $2422.2000 | $2439.1400 | $1.19 | 0.70% | triple_bottom_breakout | End | 6 |

## Strategy 2: Exit after 26 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-04-12 00:00 | 2025-04-18 12:00 | SHORT | $1568.5600 | $1591.8600 | $-2.97 | -1.49% | triple_top_breakdown | Time | 26 |
| 1 | 2025-04-13 00:00 | 2025-04-19 12:00 | SHORT | $1609.2800 | $1618.8400 | $-0.95 | -0.59% | triple_top_breakdown | Time | 26 |
| 2 | 2025-04-23 06:00 | 2025-04-29 18:00 | LONG | $1797.2300 | $1797.8100 | $0.06 | 0.03% | triple_bottom_breakout | Time | 26 |
| 3 | 2025-04-23 12:00 | 2025-04-30 00:00 | LONG | $1800.7200 | $1806.1100 | $0.48 | 0.30% | triple_bottom_breakout | Time | 26 |
| 4 | 2025-04-24 06:00 | 2025-04-30 18:00 | LONG | $1755.1000 | $1793.6100 | $2.80 | 2.19% | triple_bottom_breakout | Time | 26 |
| 7 | 2025-05-09 18:00 | 2025-05-10 18:00 | LONG | $2345.0400 | $2583.2300 | $12.99 | 10.16% | triple_bottom_breakout | TP | 4 |
| 6 | 2025-05-09 12:00 | 2025-05-10 18:00 | LONG | $2350.0300 | $2583.2300 | $15.87 | 9.92% | triple_bottom_breakout | TP | 5 |
| 5 | 2025-05-06 12:00 | 2025-05-13 00:00 | SHORT | $1768.0200 | $2449.7500 | $-77.07 | -38.56% | triple_top_breakdown | Time | 26 |
| 9 | 2025-05-12 18:00 | 2025-05-13 18:00 | LONG | $2495.4700 | $2679.7100 | $9.79 | 7.38% | triple_bottom_breakout | TP | 4 |
| 8 | 2025-05-11 06:00 | 2025-05-13 18:00 | LONG | $2530.6700 | $2679.7100 | $9.76 | 5.89% | triple_bottom_breakout | TP | 10 |
| 11 | 2025-05-15 00:00 | 2025-05-19 00:00 | SHORT | $2567.7100 | $2378.7100 | $11.43 | 7.36% | triple_top_breakdown | TP | 16 |
| 10 | 2025-05-14 00:00 | 2025-05-20 12:00 | LONG | $2673.3600 | $2497.4700 | $-12.77 | -6.58% | triple_bottom_breakout | Time | 26 |
| 12 | 2025-05-17 06:00 | 2025-05-22 00:00 | LONG | $2481.6700 | $2609.4100 | $6.40 | 5.15% | triple_bottom_breakout | TP | 19 |
| 13 | 2025-05-20 18:00 | 2025-05-22 06:00 | LONG | $2524.1900 | $2650.7500 | $8.47 | 5.01% | triple_bottom_breakout | TP | 6 |
| 14 | 2025-05-24 12:00 | 2025-05-27 12:00 | LONG | $2557.8000 | $2695.7400 | $10.62 | 5.39% | triple_bottom_breakout | TP | 12 |
| 16 | 2025-05-27 00:00 | 2025-05-29 00:00 | LONG | $2569.5100 | $2722.8000 | $7.52 | 5.97% | triple_bottom_breakout | TP | 8 |
| 15 | 2025-05-26 06:00 | 2025-05-29 00:00 | LONG | $2568.0800 | $2722.8000 | $9.49 | 6.02% | triple_bottom_breakout | TP | 11 |
| 17 | 2025-05-28 12:00 | 2025-06-04 00:00 | LONG | $2652.8000 | $2624.7000 | $-1.51 | -1.06% | triple_bottom_breakout | Time | 26 |
| 18 | 2025-05-30 00:00 | 2025-06-05 12:00 | LONG | $2643.7100 | $2570.2000 | $-4.84 | -2.78% | triple_bottom_breakout | Time | 26 |
| 19 | 2025-06-03 12:00 | 2025-06-05 18:00 | SHORT | $2619.1100 | $2414.0100 | $10.90 | 7.83% | triple_top_breakdown | TP | 9 |
| 20 | 2025-06-04 06:00 | 2025-06-10 06:00 | LONG | $2624.4000 | $2773.6400 | $7.93 | 5.69% | triple_bottom_breakout | TP | 24 |
| 21 | 2025-06-06 18:00 | 2025-06-13 06:00 | SHORT | $2476.1000 | $2545.4000 | $-4.91 | -2.80% | triple_top_breakdown | Time | 26 |
| 22 | 2025-06-07 06:00 | 2025-06-13 18:00 | SHORT | $2495.7500 | $2579.1900 | $-4.69 | -3.34% | triple_top_breakdown | Time | 26 |
| 23 | 2025-06-13 12:00 | 2025-06-20 00:00 | SHORT | $2543.1900 | $2515.8800 | $1.89 | 1.07% | triple_top_breakdown | Time | 26 |
| 24 | 2025-06-15 18:00 | 2025-06-20 12:00 | SHORT | $2547.6100 | $2419.4100 | $8.44 | 5.03% | triple_top_breakdown | TP | 19 |
| 25 | 2025-06-19 00:00 | 2025-06-21 18:00 | SHORT | $2522.1100 | $2295.7300 | $12.05 | 8.98% | triple_top_breakdown | TP | 11 |
| 26 | 2025-06-24 00:00 | 2025-06-29 12:00 | LONG | $2420.0100 | $2439.1400 | $1.64 | 0.79% | triple_bottom_breakout | End | 22 |
| 27 | 2025-06-24 06:00 | 2025-06-29 12:00 | SHORT | $2409.4400 | $2439.1400 | $-2.05 | -1.23% | triple_top_breakdown | End | 21 |
| 28 | 2025-06-24 18:00 | 2025-06-29 12:00 | LONG | $2448.4500 | $2439.1400 | $-0.50 | -0.38% | triple_bottom_breakout | End | 19 |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 3.63% return vs 3.10%.

### Key Observations:
- **Trade Frequency**: 39 vs 29 trades
- **Win Rate Difference**: 58.97% vs 65.52%
- **Return Difference**: 0.52% gap
- **Position Management**: Up to 3 positions at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)
- **Position Size**: 20.0% of capital per position

---
*Báo cáo được tạo tự động bởi Triple Pattern Multi-Position Backtest System*
