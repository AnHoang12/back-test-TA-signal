# Triple Pattern Strategy Comparison - ETHUSDT 4h

## Strategy Overview
- **Pattern**: Triple Top & Triple Bottom Pattern
- **Entry**: Breakout/breakdown with reversal candles
- **Reversal Candles**: Hammer, Engulfing, Doji patterns
- **Position Management**: Only 1 position at a time
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods
- **Take Profit**: 5.0%
- **Position Size**: 90.0% of capital

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 37 | 18 |
| Win Rate | 45.95% | 44.44% |
| Total Return | 7.99% | -45.89% |
| Final Capital | $1079.87 | $541.12 |
| Total PnL | $79.87 | $-458.88 |
| Average PnL per Trade | $2.16 | $-25.49 |
| Best Trade | $68.43 | $58.56 |
| Worst Trade | $-103.31 | $-396.03 |
| Long Trades | 21 | 9 |
| Short Trades | 16 | 9 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-04-07 20:00 | 2025-04-08 16:00 | SHORT | $1553.0400 | $1466.6700 | $50.05 | 5.56% | triple_top_breakdown | TP | 5 |
| 2025-04-10 08:00 | 2025-04-10 12:00 | SHORT | $1594.8100 | $1495.9800 | $58.56 | 6.20% | triple_top_breakdown | TP | 1 |
| 2025-04-11 16:00 | 2025-04-13 04:00 | SHORT | $1565.7900 | $1613.5000 | $-30.40 | -3.05% | triple_top_breakdown | Time | 9 |
| 2025-04-20 12:00 | 2025-04-22 00:00 | SHORT | $1573.5000 | $1579.2200 | $-3.53 | -0.36% | triple_top_breakdown | Time | 9 |
| 2025-04-23 04:00 | 2025-04-24 16:00 | LONG | $1792.1100 | $1763.1000 | $-15.66 | -1.62% | triple_bottom_breakout | Time | 9 |
| 2025-04-24 16:00 | 2025-04-26 04:00 | LONG | $1763.1000 | $1800.4900 | $20.21 | 2.12% | triple_bottom_breakout | Time | 9 |
| 2025-04-27 04:00 | 2025-04-28 16:00 | LONG | $1803.7600 | $1797.1700 | $-3.55 | -0.37% | triple_bottom_breakout | Time | 9 |
| 2025-04-29 00:00 | 2025-04-30 12:00 | LONG | $1802.0800 | $1764.7400 | $-20.06 | -2.07% | triple_bottom_breakout | Time | 9 |
| 2025-05-02 00:00 | 2025-05-03 12:00 | LONG | $1847.7400 | $1834.5300 | $-6.79 | -0.71% | triple_bottom_breakout | Time | 9 |
| 2025-05-06 04:00 | 2025-05-07 16:00 | SHORT | $1806.0300 | $1795.8200 | $5.34 | 0.57% | triple_top_breakdown | Time | 9 |
| 2025-05-09 00:00 | 2025-05-09 04:00 | LONG | $2205.0600 | $2364.0900 | $68.43 | 7.21% | triple_bottom_breakout | TP | 1 |
| 2025-05-09 08:00 | 2025-05-10 16:00 | LONG | $2351.2900 | $2499.4800 | $63.68 | 6.30% | triple_bottom_breakout | TP | 8 |
| 2025-05-12 00:00 | 2025-05-13 12:00 | LONG | $2520.0000 | $2566.2100 | $19.58 | 1.83% | triple_bottom_breakout | Time | 9 |
| 2025-05-15 12:00 | 2025-05-17 00:00 | LONG | $2563.7600 | $2496.9800 | $-28.27 | -2.60% | triple_bottom_breakout | Time | 9 |
| 2025-05-18 08:00 | 2025-05-19 20:00 | SHORT | $2501.7500 | $2528.1400 | $-11.18 | -1.05% | triple_top_breakdown | Time | 9 |
| 2025-05-19 20:00 | 2025-05-21 08:00 | LONG | $2528.1400 | $2536.6500 | $3.53 | 0.34% | triple_bottom_breakout | Time | 9 |
| 2025-05-21 12:00 | 2025-05-23 00:00 | LONG | $2567.0100 | $2722.0000 | $63.57 | 6.04% | triple_bottom_breakout | TP | 9 |
| 2025-05-23 12:00 | 2025-05-25 00:00 | LONG | $2568.5300 | $2512.7800 | $-24.10 | -2.17% | triple_bottom_breakout | Time | 9 |
| 2025-05-25 08:00 | 2025-05-26 20:00 | SHORT | $2497.9100 | $2563.7000 | $-28.67 | -2.63% | triple_top_breakdown | Time | 9 |
| 2025-05-30 00:00 | 2025-05-31 12:00 | LONG | $2631.1900 | $2536.3000 | $-38.32 | -3.61% | triple_bottom_breakout | Time | 9 |
| 2025-05-31 16:00 | 2025-06-02 04:00 | SHORT | $2537.4000 | $2506.9400 | $12.34 | 1.20% | triple_top_breakdown | Time | 9 |
| 2025-06-03 00:00 | 2025-06-04 12:00 | LONG | $2603.3900 | $2667.9300 | $25.76 | 2.48% | triple_bottom_breakout | Time | 9 |
| 2025-06-06 04:00 | 2025-06-07 16:00 | SHORT | $2455.6400 | $2517.3100 | $-26.68 | -2.51% | triple_top_breakdown | Time | 9 |
| 2025-06-07 20:00 | 2025-06-09 08:00 | SHORT | $2524.6300 | $2541.7900 | $-7.06 | -0.68% | triple_top_breakdown | Time | 9 |
| 2025-06-11 04:00 | 2025-06-12 16:00 | LONG | $2791.5900 | $2695.0000 | $-35.71 | -3.46% | triple_bottom_breakout | Time | 9 |
| 2025-06-12 16:00 | 2025-06-13 00:00 | SHORT | $2695.0000 | $2514.3300 | $67.04 | 6.70% | triple_top_breakdown | TP | 2 |
| 2025-06-13 12:00 | 2025-06-15 00:00 | SHORT | $2551.2700 | $2530.1000 | $8.80 | 0.83% | triple_top_breakdown | Time | 9 |
| 2025-06-15 00:00 | 2025-06-16 12:00 | SHORT | $2530.1000 | $2632.2500 | $-43.13 | -4.04% | triple_top_breakdown | Time | 9 |
| 2025-06-16 20:00 | 2025-06-18 08:00 | SHORT | $2544.1700 | $2513.8600 | $12.26 | 1.19% | triple_top_breakdown | Time | 9 |
| 2025-06-18 12:00 | 2025-06-20 00:00 | SHORT | $2508.9600 | $2517.1900 | $-3.41 | -0.33% | triple_top_breakdown | Time | 9 |
| 2025-06-20 08:00 | 2025-06-21 20:00 | LONG | $2549.6500 | $2295.7300 | $-103.31 | -9.96% | triple_bottom_breakout | Time | 9 |
| 2025-06-22 04:00 | 2025-06-23 16:00 | SHORT | $2270.6800 | $2312.7700 | $-17.51 | -1.85% | triple_top_breakdown | Time | 9 |
| 2025-06-23 16:00 | 2025-06-24 12:00 | LONG | $2312.7700 | $2438.1000 | $50.32 | 5.42% | triple_bottom_breakout | TP | 5 |
| 2025-06-24 16:00 | 2025-06-26 04:00 | LONG | $2434.2400 | $2489.8900 | $22.27 | 2.29% | triple_bottom_breakout | Time | 9 |
| 2025-06-26 04:00 | 2025-06-27 16:00 | LONG | $2489.8900 | $2412.6700 | $-30.83 | -3.10% | triple_bottom_breakout | Time | 9 |
| 2025-06-28 00:00 | 2025-06-29 12:00 | LONG | $2420.9300 | $2436.6800 | $6.29 | 0.65% | triple_bottom_breakout | Time | 9 |
| 2025-06-29 16:00 | 2025-06-29 16:00 | LONG | $2437.9600 | $2437.9600 | $0.00 | 0.00% | triple_bottom_breakout | End | 0 |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-04-07 20:00 | 2025-04-08 16:00 | SHORT | $1553.0400 | $1466.6700 | $50.05 | 5.56% | triple_top_breakdown | TP | 5 |
| 2025-04-10 08:00 | 2025-04-10 12:00 | SHORT | $1594.8100 | $1495.9800 | $58.56 | 6.20% | triple_top_breakdown | TP | 1 |
| 2025-04-11 16:00 | 2025-04-16 00:00 | SHORT | $1565.7900 | $1591.0400 | $-16.09 | -1.61% | triple_top_breakdown | Time | 26 |
| 2025-04-20 12:00 | 2025-04-24 20:00 | SHORT | $1573.5000 | $1769.6500 | $-122.57 | -12.47% | triple_top_breakdown | Time | 26 |
| 2025-04-24 20:00 | 2025-04-29 04:00 | LONG | $1769.6500 | $1821.7100 | $25.68 | 2.94% | triple_bottom_breakout | Time | 26 |
| 2025-05-02 00:00 | 2025-05-06 08:00 | LONG | $1847.7400 | $1769.9200 | $-37.74 | -4.21% | triple_bottom_breakout | Time | 26 |
| 2025-05-06 12:00 | 2025-05-10 20:00 | SHORT | $1770.0900 | $2583.2300 | $-396.03 | -45.94% | triple_top_breakdown | Time | 26 |
| 2025-05-12 00:00 | 2025-05-13 16:00 | LONG | $2520.0000 | $2690.9400 | $34.30 | 6.78% | triple_bottom_breakout | TP | 10 |
| 2025-05-15 12:00 | 2025-05-19 20:00 | LONG | $2563.7600 | $2528.1400 | $-7.45 | -1.39% | triple_bottom_breakout | Time | 26 |
| 2025-05-19 20:00 | 2025-05-22 12:00 | LONG | $2528.1400 | $2664.4800 | $28.57 | 5.39% | triple_bottom_breakout | TP | 16 |
| 2025-05-23 12:00 | 2025-05-27 20:00 | LONG | $2568.5300 | $2660.8100 | $19.96 | 3.59% | triple_bottom_breakout | Time | 26 |
| 2025-05-30 00:00 | 2025-06-03 08:00 | LONG | $2631.1900 | $2601.7800 | $-6.41 | -1.12% | triple_bottom_breakout | Time | 26 |
| 2025-06-03 08:00 | 2025-06-05 20:00 | SHORT | $2601.7800 | $2414.0100 | $40.97 | 7.22% | triple_top_breakdown | TP | 15 |
| 2025-06-06 04:00 | 2025-06-10 12:00 | SHORT | $2455.6400 | $2732.9500 | $-68.28 | -11.29% | triple_top_breakdown | Time | 26 |
| 2025-06-11 04:00 | 2025-06-15 12:00 | LONG | $2791.5900 | $2541.8100 | $-48.60 | -8.95% | triple_bottom_breakout | Time | 26 |
| 2025-06-16 20:00 | 2025-06-20 16:00 | SHORT | $2544.1700 | $2414.8500 | $25.39 | 5.08% | triple_top_breakdown | TP | 23 |
| 2025-06-22 04:00 | 2025-06-26 12:00 | SHORT | $2270.6800 | $2433.0300 | $-37.34 | -7.15% | triple_top_breakdown | Time | 26 |
| 2025-06-27 08:00 | 2025-06-29 16:00 | LONG | $2447.2500 | $2437.9600 | $-1.86 | -0.38% | triple_bottom_breakout | End | 14 |

## Analysis

**Winner: 9 Periods Strategy**

The 9-period exit strategy outperformed with 7.99% return vs -45.89%.

### Key Observations:
- **Trade Frequency**: 37 vs 18 trades
- **Win Rate Difference**: 45.95% vs 44.44%
- **Return Difference**: 53.88% gap
- **Position Management**: Only 1 position at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)

---
*Báo cáo được tạo tự động bởi Triple Pattern Backtest System*
