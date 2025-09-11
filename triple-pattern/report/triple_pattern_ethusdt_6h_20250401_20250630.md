# Triple Pattern Strategy Comparison - ETHUSDT 6h

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
| Total Trades | 20 | 10 |
| Win Rate | 65.00% | 60.00% |
| Total Return | -4.27% | -29.66% |
| Final Capital | $957.32 | $703.38 |
| Total PnL | $-42.68 | $-296.62 |
| Average PnL per Trade | $-2.13 | $-29.66 |
| Best Trade | $65.54 | $33.68 |
| Worst Trade | $-211.42 | $-342.49 |
| Long Trades | 13 | 7 |
| Short Trades | 7 | 3 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-04-12 00:00 | 2025-04-14 06:00 | SHORT | $1568.5600 | $1675.3200 | $-61.26 | -6.81% | triple_top_breakdown | Time | 9 |
| 2025-04-23 06:00 | 2025-04-25 12:00 | LONG | $1797.2300 | $1785.8200 | $-5.36 | -0.63% | triple_bottom_breakout | Time | 9 |
| 2025-04-25 12:00 | 2025-04-27 18:00 | LONG | $1785.8200 | $1791.2900 | $2.57 | 0.31% | triple_bottom_breakout | Time | 9 |
| 2025-04-28 00:00 | 2025-04-30 06:00 | LONG | $1795.8000 | $1815.7000 | $9.33 | 1.11% | triple_bottom_breakout | Time | 9 |
| 2025-05-06 12:00 | 2025-05-08 18:00 | SHORT | $1768.0200 | $2207.3900 | $-211.42 | -24.85% | triple_top_breakdown | Time | 9 |
| 2025-05-09 12:00 | 2025-05-10 18:00 | LONG | $2350.0300 | $2583.2300 | $65.54 | 9.92% | triple_bottom_breakout | TP | 5 |
| 2025-05-11 06:00 | 2025-05-13 12:00 | LONG | $2530.6700 | $2610.5500 | $22.71 | 3.16% | triple_bottom_breakout | Time | 9 |
| 2025-05-14 00:00 | 2025-05-16 06:00 | LONG | $2673.3600 | $2620.8300 | $-14.54 | -1.96% | triple_bottom_breakout | Time | 9 |
| 2025-05-17 06:00 | 2025-05-19 12:00 | LONG | $2481.6700 | $2505.0000 | $6.83 | 0.94% | triple_bottom_breakout | Time | 9 |
| 2025-05-20 18:00 | 2025-05-22 06:00 | LONG | $2524.1900 | $2650.7500 | $36.75 | 5.01% | triple_bottom_breakout | TP | 6 |
| 2025-05-24 12:00 | 2025-05-26 18:00 | LONG | $2557.8000 | $2563.7000 | $1.77 | 0.23% | triple_bottom_breakout | Time | 9 |
| 2025-05-27 00:00 | 2025-05-29 00:00 | LONG | $2569.5100 | $2722.8000 | $45.80 | 5.97% | triple_bottom_breakout | TP | 8 |
| 2025-05-30 00:00 | 2025-06-01 06:00 | LONG | $2643.7100 | $2497.3500 | $-44.78 | -5.54% | triple_bottom_breakout | Time | 9 |
| 2025-06-03 12:00 | 2025-06-05 18:00 | SHORT | $2619.1100 | $2414.0100 | $60.18 | 7.83% | triple_top_breakdown | TP | 9 |
| 2025-06-06 18:00 | 2025-06-09 00:00 | SHORT | $2476.1000 | $2480.8800 | $-1.59 | -0.19% | triple_top_breakdown | Time | 9 |
| 2025-06-13 12:00 | 2025-06-15 18:00 | SHORT | $2543.1900 | $2547.6100 | $-1.43 | -0.17% | triple_top_breakdown | Time | 9 |
| 2025-06-15 18:00 | 2025-06-18 00:00 | SHORT | $2547.6100 | $2537.1000 | $3.38 | 0.41% | triple_top_breakdown | Time | 9 |
| 2025-06-19 00:00 | 2025-06-21 06:00 | SHORT | $2522.1100 | $2442.7500 | $25.90 | 3.15% | triple_top_breakdown | Time | 9 |
| 2025-06-24 00:00 | 2025-06-26 06:00 | LONG | $2420.0100 | $2450.3600 | $10.61 | 1.25% | triple_bottom_breakout | Time | 9 |
| 2025-06-26 18:00 | 2025-06-29 00:00 | LONG | $2415.9600 | $2433.7700 | $6.31 | 0.74% | triple_bottom_breakout | Time | 9 |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-04-12 00:00 | 2025-04-18 12:00 | SHORT | $1568.5600 | $1591.8600 | $-13.37 | -1.49% | triple_top_breakdown | Time | 26 |
| 2025-04-23 06:00 | 2025-04-29 18:00 | LONG | $1797.2300 | $1797.8100 | $0.29 | 0.03% | triple_bottom_breakout | Time | 26 |
| 2025-05-06 12:00 | 2025-05-13 00:00 | SHORT | $1768.0200 | $2449.7500 | $-342.49 | -38.56% | triple_top_breakdown | Time | 26 |
| 2025-05-14 00:00 | 2025-05-20 12:00 | LONG | $2673.3600 | $2497.4700 | $-38.16 | -6.58% | triple_bottom_breakout | Time | 26 |
| 2025-05-20 18:00 | 2025-05-22 06:00 | LONG | $2524.1900 | $2650.7500 | $27.36 | 5.01% | triple_bottom_breakout | TP | 6 |
| 2025-05-24 12:00 | 2025-05-27 12:00 | LONG | $2557.8000 | $2695.7400 | $30.75 | 5.39% | triple_bottom_breakout | TP | 12 |
| 2025-05-28 12:00 | 2025-06-04 00:00 | LONG | $2652.8000 | $2624.7000 | $-6.33 | -1.06% | triple_bottom_breakout | Time | 26 |
| 2025-06-04 06:00 | 2025-06-10 06:00 | LONG | $2624.4000 | $2773.6400 | $33.68 | 5.69% | triple_bottom_breakout | TP | 24 |
| 2025-06-13 12:00 | 2025-06-20 00:00 | SHORT | $2543.1900 | $2515.8800 | $6.69 | 1.07% | triple_top_breakdown | Time | 26 |
| 2025-06-24 00:00 | 2025-06-29 12:00 | LONG | $2420.0100 | $2439.1400 | $4.97 | 0.79% | triple_bottom_breakout | End | 22 |

## Analysis

**Winner: 9 Periods Strategy**

The 9-period exit strategy outperformed with -4.27% return vs -29.66%.

### Key Observations:
- **Trade Frequency**: 20 vs 10 trades
- **Win Rate Difference**: 65.00% vs 60.00%
- **Return Difference**: 25.39% gap
- **Position Management**: Only 1 position at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)

---
*Báo cáo được tạo tự động bởi Triple Pattern Backtest System*
