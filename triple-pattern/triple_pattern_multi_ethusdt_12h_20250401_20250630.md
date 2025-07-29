# Triple Pattern Strategy Comparison - Multi Position - ETHUSDT 12h

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
| Total Trades | 20 | 17 |
| Win Rate | 60.00% | 82.35% |
| Total Return | 5.14% | 11.40% |
| Final Capital | $1051.37 | $1113.95 |
| Total PnL | $51.37 | $113.95 |
| Average PnL per Trade | $2.57 | $6.70 |
| Best Trade | $20.80 | $20.93 |
| Worst Trade | $-15.59 | $-26.31 |
| Long Trades | 16 | 13 |
| Short Trades | 4 | 4 |
| Max Concurrent Positions | 3 | 3 |

## Strategy 1: Exit after 9 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-04-23 12:00 | 2025-04-28 00:00 | LONG | $1795.0700 | $1816.2000 | $2.35 | 1.18% | triple_bottom_breakout | Time | 9 |
| 1 | 2025-04-25 12:00 | 2025-04-30 00:00 | LONG | $1784.6000 | $1815.7000 | $2.79 | 1.74% | triple_bottom_breakout | Time | 9 |
| 2 | 2025-04-26 00:00 | 2025-04-30 12:00 | LONG | $1785.8500 | $1793.6100 | $0.56 | 0.43% | triple_bottom_breakout | Time | 9 |
| 3 | 2025-04-30 12:00 | 2025-05-05 00:00 | LONG | $1793.6100 | $1804.6300 | $1.24 | 0.61% | triple_bottom_breakout | Time | 9 |
| 4 | 2025-05-05 00:00 | 2025-05-08 00:00 | LONG | $1804.6300 | $1957.6300 | $17.07 | 8.48% | triple_bottom_breakout | TP | 6 |
| 5 | 2025-05-09 12:00 | 2025-05-10 12:00 | LONG | $2345.0400 | $2583.2300 | $20.80 | 10.16% | triple_bottom_breakout | TP | 2 |
| 6 | 2025-05-13 00:00 | 2025-05-13 12:00 | LONG | $2513.3900 | $2679.7100 | $13.83 | 6.62% | triple_bottom_breakout | TP | 1 |
| 7 | 2025-05-14 12:00 | 2025-05-19 00:00 | LONG | $2609.7400 | $2417.5800 | $-15.59 | -7.36% | triple_bottom_breakout | Time | 9 |
| 8 | 2025-05-15 12:00 | 2025-05-20 00:00 | LONG | $2548.6900 | $2514.2000 | $-2.29 | -1.35% | triple_bottom_breakout | Time | 9 |
| 9 | 2025-05-18 12:00 | 2025-05-22 00:00 | LONG | $2497.7800 | $2650.7500 | $8.30 | 6.12% | triple_bottom_breakout | TP | 7 |
| 10 | 2025-05-21 12:00 | 2025-05-26 00:00 | LONG | $2550.9900 | $2568.0800 | $1.21 | 0.67% | triple_bottom_breakout | Time | 9 |
| 11 | 2025-05-26 12:00 | 2025-05-29 00:00 | LONG | $2563.7000 | $2715.8300 | $12.46 | 5.93% | triple_bottom_breakout | TP | 5 |
| 12 | 2025-06-02 12:00 | 2025-06-07 00:00 | LONG | $2607.4100 | $2495.7500 | $-9.10 | -4.28% | triple_bottom_breakout | Time | 9 |
| 13 | 2025-06-03 00:00 | 2025-06-07 12:00 | LONG | $2601.7800 | $2524.6300 | $-5.04 | -2.97% | triple_bottom_breakout | Time | 9 |
| 14 | 2025-06-04 00:00 | 2025-06-08 12:00 | LONG | $2624.4000 | $2509.8300 | $-5.94 | -4.37% | triple_bottom_breakout | Time | 9 |
| 15 | 2025-06-11 12:00 | 2025-06-16 00:00 | LONG | $2771.6100 | $2617.0100 | $-11.63 | -5.58% | triple_bottom_breakout | Time | 9 |
| 16 | 2025-06-17 00:00 | 2025-06-20 12:00 | SHORT | $2552.1900 | $2406.4900 | $11.77 | 5.71% | triple_top_breakdown | TP | 7 |
| 17 | 2025-06-18 00:00 | 2025-06-21 12:00 | SHORT | $2513.8600 | $2295.7300 | $14.31 | 8.68% | triple_top_breakdown | TP | 7 |
| 18 | 2025-06-24 00:00 | 2025-06-28 12:00 | SHORT | $2409.4400 | $2435.6200 | $-2.30 | -1.09% | triple_top_breakdown | Time | 9 |
| 19 | 2025-06-26 00:00 | 2025-06-29 12:00 | SHORT | $2450.3600 | $2500.0900 | $-3.43 | -2.03% | triple_top_breakdown | End | 7 |

## Strategy 2: Exit after 26 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-04-23 12:00 | 2025-05-06 12:00 | LONG | $1795.0700 | $1817.0000 | $2.44 | 1.22% | triple_bottom_breakout | Time | 26 |
| 2 | 2025-04-26 00:00 | 2025-05-08 00:00 | LONG | $1785.8500 | $1957.6300 | $12.31 | 9.62% | triple_bottom_breakout | TP | 24 |
| 1 | 2025-04-25 12:00 | 2025-05-08 00:00 | LONG | $1784.6000 | $1957.6300 | $15.51 | 9.70% | triple_bottom_breakout | TP | 25 |
| 3 | 2025-05-09 12:00 | 2025-05-10 12:00 | LONG | $2345.0400 | $2583.2300 | $20.93 | 10.16% | triple_bottom_breakout | TP | 2 |
| 4 | 2025-05-13 00:00 | 2025-05-13 12:00 | LONG | $2513.3900 | $2679.7100 | $13.91 | 6.62% | triple_bottom_breakout | TP | 1 |
| 7 | 2025-05-18 12:00 | 2025-05-22 00:00 | LONG | $2497.7800 | $2650.7500 | $8.35 | 6.12% | triple_bottom_breakout | TP | 7 |
| 5 | 2025-05-14 12:00 | 2025-05-27 12:00 | LONG | $2609.7400 | $2660.8100 | $4.17 | 1.96% | triple_bottom_breakout | Time | 26 |
| 6 | 2025-05-15 12:00 | 2025-05-28 12:00 | LONG | $2548.6900 | $2681.6000 | $8.89 | 5.21% | triple_bottom_breakout | TP | 26 |
| 8 | 2025-05-26 12:00 | 2025-05-29 00:00 | LONG | $2563.7000 | $2715.8300 | $8.19 | 5.93% | triple_bottom_breakout | TP | 5 |
| 11 | 2025-06-04 00:00 | 2025-06-10 00:00 | LONG | $2624.4000 | $2773.6400 | $7.97 | 5.69% | triple_bottom_breakout | TP | 12 |
| 10 | 2025-06-03 00:00 | 2025-06-10 00:00 | LONG | $2601.7800 | $2773.6400 | $11.57 | 6.61% | triple_bottom_breakout | TP | 14 |
| 9 | 2025-06-02 12:00 | 2025-06-10 00:00 | LONG | $2607.4100 | $2773.6400 | $13.96 | 6.38% | triple_bottom_breakout | TP | 15 |
| 13 | 2025-06-17 00:00 | 2025-06-20 12:00 | SHORT | $2552.1900 | $2406.4900 | $10.31 | 5.71% | triple_top_breakdown | TP | 7 |
| 14 | 2025-06-18 00:00 | 2025-06-21 12:00 | SHORT | $2513.8600 | $2295.7300 | $12.53 | 8.68% | triple_top_breakdown | TP | 7 |
| 12 | 2025-06-11 12:00 | 2025-06-24 12:00 | LONG | $2771.6100 | $2448.4500 | $-26.31 | -11.66% | triple_bottom_breakout | Time | 26 |
| 15 | 2025-06-24 00:00 | 2025-06-29 12:00 | SHORT | $2409.4400 | $2500.0900 | $-6.96 | -3.76% | triple_top_breakdown | End | 11 |
| 16 | 2025-06-26 00:00 | 2025-06-29 12:00 | SHORT | $2450.3600 | $2500.0900 | $-3.81 | -2.03% | triple_top_breakdown | End | 7 |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 11.40% return vs 5.14%.

### Key Observations:
- **Trade Frequency**: 20 vs 17 trades
- **Win Rate Difference**: 60.00% vs 82.35%
- **Return Difference**: 6.26% gap
- **Position Management**: Up to 3 positions at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)
- **Position Size**: 20.0% of capital per position

---
*Báo cáo được tạo tự động bởi Triple Pattern Multi-Position Backtest System*
