# Triple Pattern Strategy Comparison - Multi Position - BNBUSDT 6h

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
| Total Trades | 51 | 31 |
| Win Rate | 43.14% | 41.94% |
| Total Return | -0.60% | 3.22% |
| Final Capital | $993.99 | $1032.23 |
| Total PnL | $-6.01 | $32.23 |
| Average PnL per Trade | $-0.12 | $1.04 |
| Best Trade | $12.42 | $12.51 |
| Worst Trade | $-7.22 | $-6.84 |
| Long Trades | 32 | 19 |
| Short Trades | 19 | 12 |
| Max Concurrent Positions | 3 | 3 |

## Strategy 1: Exit after 9 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-04-13 12:00 | 2025-04-15 18:00 | LONG | $588.5300 | $579.5200 | $-3.06 | -1.53% | triple_bottom_breakout | Time | 9 |
| 1 | 2025-04-15 00:00 | 2025-04-17 06:00 | LONG | $589.2000 | $586.2000 | $-0.81 | -0.51% | triple_bottom_breakout | Time | 9 |
| 2 | 2025-04-16 06:00 | 2025-04-18 12:00 | LONG | $582.0900 | $595.7200 | $3.92 | 2.34% | triple_bottom_breakout | Time | 9 |
| 3 | 2025-04-17 00:00 | 2025-04-19 06:00 | LONG | $582.4900 | $591.0400 | $1.97 | 1.47% | triple_bottom_breakout | Time | 9 |
| 4 | 2025-04-18 06:00 | 2025-04-20 12:00 | LONG | $591.8600 | $589.4000 | $-0.58 | -0.42% | triple_bottom_breakout | Time | 9 |
| 5 | 2025-04-19 12:00 | 2025-04-21 18:00 | LONG | $590.2000 | $597.3400 | $2.09 | 1.21% | triple_bottom_breakout | Time | 9 |
| 6 | 2025-04-23 00:00 | 2025-04-25 06:00 | LONG | $616.5400 | $605.8900 | $-3.47 | -1.73% | triple_bottom_breakout | Time | 9 |
| 7 | 2025-04-23 18:00 | 2025-04-26 00:00 | LONG | $605.7100 | $602.1500 | $-0.94 | -0.59% | triple_bottom_breakout | Time | 9 |
| 8 | 2025-04-24 12:00 | 2025-04-26 18:00 | SHORT | $596.4100 | $607.2300 | $-2.33 | -1.81% | triple_top_breakdown | Time | 9 |
| 9 | 2025-04-25 06:00 | 2025-04-27 12:00 | LONG | $605.8900 | $601.4000 | $-1.05 | -0.74% | triple_bottom_breakout | Time | 9 |
| 10 | 2025-04-26 00:00 | 2025-04-28 06:00 | SHORT | $602.1500 | $607.4900 | $-1.29 | -0.89% | triple_top_breakdown | Time | 9 |
| 11 | 2025-04-26 18:00 | 2025-04-29 00:00 | LONG | $607.2300 | $607.5300 | $0.07 | 0.05% | triple_bottom_breakout | Time | 9 |
| 12 | 2025-04-27 12:00 | 2025-04-29 18:00 | LONG | $601.4000 | $601.0000 | $-0.09 | -0.07% | triple_bottom_breakout | Time | 9 |
| 13 | 2025-04-28 12:00 | 2025-04-30 18:00 | SHORT | $602.3200 | $599.8800 | $0.58 | 0.41% | triple_top_breakdown | Time | 9 |
| 14 | 2025-04-29 12:00 | 2025-05-01 18:00 | LONG | $603.6400 | $599.6300 | $-0.94 | -0.66% | triple_bottom_breakout | Time | 9 |
| 15 | 2025-04-30 06:00 | 2025-05-02 12:00 | SHORT | $602.4300 | $600.2100 | $0.52 | 0.37% | triple_top_breakdown | Time | 9 |
| 16 | 2025-05-02 00:00 | 2025-05-04 06:00 | SHORT | $598.8100 | $594.1400 | $1.33 | 0.78% | triple_top_breakdown | Time | 9 |
| 17 | 2025-05-06 00:00 | 2025-05-08 06:00 | LONG | $597.9100 | $613.6200 | $5.23 | 2.63% | triple_bottom_breakout | Time | 9 |
| 18 | 2025-05-09 00:00 | 2025-05-09 18:00 | LONG | $627.3600 | $666.2900 | $12.42 | 6.21% | triple_bottom_breakout | TP | 3 |
| 19 | 2025-05-09 12:00 | 2025-05-11 18:00 | LONG | $635.9000 | $651.1500 | $3.84 | 2.40% | triple_bottom_breakout | Time | 9 |
| 20 | 2025-05-11 00:00 | 2025-05-13 06:00 | LONG | $664.1600 | $653.1200 | $-2.84 | -1.66% | triple_bottom_breakout | Time | 9 |
| 21 | 2025-05-14 00:00 | 2025-05-16 06:00 | LONG | $663.4800 | $654.3700 | $-2.79 | -1.37% | triple_bottom_breakout | Time | 9 |
| 22 | 2025-05-14 06:00 | 2025-05-16 12:00 | LONG | $659.7000 | $648.9500 | $-2.65 | -1.63% | triple_bottom_breakout | Time | 9 |
| 23 | 2025-05-15 06:00 | 2025-05-17 12:00 | LONG | $653.3800 | $640.4500 | $-2.57 | -1.98% | triple_bottom_breakout | Time | 9 |
| 24 | 2025-05-18 00:00 | 2025-05-20 06:00 | LONG | $645.8600 | $643.8200 | $-0.64 | -0.32% | triple_bottom_breakout | Time | 9 |
| 25 | 2025-05-18 18:00 | 2025-05-21 00:00 | LONG | $651.5300 | $660.9200 | $2.32 | 1.44% | triple_bottom_breakout | Time | 9 |
| 26 | 2025-05-19 00:00 | 2025-05-21 06:00 | SHORT | $638.5700 | $654.8600 | $-3.29 | -2.55% | triple_top_breakdown | Time | 9 |
| 27 | 2025-05-24 12:00 | 2025-05-26 18:00 | LONG | $675.6300 | $674.2900 | $-0.40 | -0.20% | triple_bottom_breakout | Time | 9 |
| 28 | 2025-05-26 06:00 | 2025-05-28 12:00 | LONG | $674.1700 | $686.0800 | $2.84 | 1.77% | triple_bottom_breakout | Time | 9 |
| 29 | 2025-05-27 00:00 | 2025-05-29 06:00 | LONG | $675.0300 | $685.7900 | $2.69 | 1.59% | triple_bottom_breakout | Time | 9 |
| 30 | 2025-05-28 06:00 | 2025-05-30 12:00 | LONG | $687.4400 | $662.2000 | $-4.96 | -3.67% | triple_bottom_breakout | Time | 9 |
| 31 | 2025-05-30 00:00 | 2025-06-01 06:00 | LONG | $674.0600 | $650.5000 | $-6.12 | -3.50% | triple_bottom_breakout | Time | 9 |
| 32 | 2025-06-03 00:00 | 2025-06-05 06:00 | SHORT | $667.3400 | $661.9900 | $1.60 | 0.80% | triple_top_breakdown | Time | 9 |
| 33 | 2025-06-04 06:00 | 2025-06-05 18:00 | SHORT | $667.8000 | $633.3200 | $8.25 | 5.16% | triple_top_breakdown | TP | 6 |
| 34 | 2025-06-04 12:00 | 2025-06-06 18:00 | LONG | $667.5000 | $642.7000 | $-4.75 | -3.72% | triple_bottom_breakout | Time | 9 |
| 35 | 2025-06-05 06:00 | 2025-06-07 12:00 | SHORT | $661.9900 | $649.4600 | $2.70 | 1.89% | triple_top_breakdown | Time | 9 |
| 36 | 2025-06-06 12:00 | 2025-06-08 18:00 | SHORT | $646.9100 | $652.0000 | $-1.16 | -0.79% | triple_top_breakdown | Time | 9 |
| 37 | 2025-06-07 12:00 | 2025-06-09 18:00 | SHORT | $649.4600 | $665.5800 | $-4.26 | -2.48% | triple_top_breakdown | Time | 9 |
| 38 | 2025-06-07 18:00 | 2025-06-10 00:00 | SHORT | $650.8200 | $662.1800 | $-2.40 | -1.75% | triple_top_breakdown | Time | 9 |
| 39 | 2025-06-10 12:00 | 2025-06-12 18:00 | LONG | $664.4900 | $654.7500 | $-2.93 | -1.47% | triple_bottom_breakout | Time | 9 |
| 40 | 2025-06-12 00:00 | 2025-06-14 06:00 | LONG | $667.1800 | $650.7100 | $-3.95 | -2.47% | triple_bottom_breakout | Time | 9 |
| 41 | 2025-06-12 18:00 | 2025-06-15 00:00 | SHORT | $654.7500 | $649.9600 | $1.22 | 0.73% | triple_top_breakdown | Time | 9 |
| 42 | 2025-06-15 12:00 | 2025-06-17 18:00 | SHORT | $648.4300 | $648.0800 | $0.11 | 0.05% | triple_top_breakdown | Time | 9 |
| 43 | 2025-06-15 18:00 | 2025-06-18 00:00 | SHORT | $648.1900 | $652.7900 | $-1.13 | -0.71% | triple_top_breakdown | Time | 9 |
| 44 | 2025-06-16 06:00 | 2025-06-18 12:00 | SHORT | $654.4300 | $641.6500 | $2.48 | 1.95% | triple_top_breakdown | Time | 9 |
| 45 | 2025-06-19 12:00 | 2025-06-21 18:00 | SHORT | $642.2500 | $628.9700 | $4.11 | 2.07% | triple_top_breakdown | Time | 9 |
| 46 | 2025-06-20 00:00 | 2025-06-22 06:00 | SHORT | $644.3100 | $630.3900 | $3.44 | 2.16% | triple_top_breakdown | Time | 9 |
| 47 | 2025-06-20 06:00 | 2025-06-22 12:00 | LONG | $647.3400 | $610.6200 | $-7.22 | -5.67% | triple_bottom_breakout | Time | 9 |
| 48 | 2025-06-24 00:00 | 2025-06-26 06:00 | LONG | $642.2300 | $644.4800 | $0.70 | 0.35% | triple_bottom_breakout | Time | 9 |
| 49 | 2025-06-24 06:00 | 2025-06-26 12:00 | SHORT | $638.5000 | $645.2000 | $-1.67 | -1.05% | triple_top_breakdown | Time | 9 |
| 50 | 2025-06-24 12:00 | 2025-06-26 18:00 | LONG | $643.1200 | $642.3000 | $-0.16 | -0.13% | triple_bottom_breakout | Time | 9 |

## Strategy 2: Exit after 26 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-04-13 12:00 | 2025-04-20 00:00 | LONG | $588.5300 | $594.4900 | $2.03 | 1.01% | triple_bottom_breakout | Time | 26 |
| 1 | 2025-04-15 00:00 | 2025-04-21 12:00 | LONG | $589.2000 | $596.2500 | $1.91 | 1.20% | triple_bottom_breakout | Time | 26 |
| 2 | 2025-04-16 06:00 | 2025-04-22 18:00 | LONG | $582.0900 | $618.5100 | $8.01 | 6.26% | triple_bottom_breakout | TP | 26 |
| 3 | 2025-04-23 00:00 | 2025-04-29 12:00 | LONG | $616.5400 | $603.6400 | $-4.23 | -2.09% | triple_bottom_breakout | Time | 26 |
| 4 | 2025-04-23 18:00 | 2025-04-30 06:00 | LONG | $605.7100 | $602.4300 | $-0.88 | -0.54% | triple_bottom_breakout | Time | 26 |
| 5 | 2025-04-24 12:00 | 2025-05-01 00:00 | SHORT | $596.4100 | $600.8100 | $-0.96 | -0.74% | triple_top_breakdown | Time | 26 |
| 6 | 2025-04-29 12:00 | 2025-05-06 00:00 | LONG | $603.6400 | $597.9100 | $-1.36 | -0.95% | triple_bottom_breakout | Time | 26 |
| 7 | 2025-04-30 06:00 | 2025-05-06 18:00 | SHORT | $602.4300 | $602.5700 | $-0.03 | -0.02% | triple_top_breakdown | Time | 26 |
| 8 | 2025-05-02 00:00 | 2025-05-08 12:00 | SHORT | $598.8100 | $616.6000 | $-4.25 | -2.97% | triple_top_breakdown | Time | 26 |
| 9 | 2025-05-06 00:00 | 2025-05-08 18:00 | LONG | $597.9100 | $629.1700 | $7.47 | 5.23% | triple_bottom_breakout | TP | 11 |
| 10 | 2025-05-09 00:00 | 2025-05-09 18:00 | LONG | $627.3600 | $666.2900 | $12.51 | 6.21% | triple_bottom_breakout | TP | 3 |
| 11 | 2025-05-09 12:00 | 2025-05-12 06:00 | LONG | $635.9000 | $678.1000 | $10.70 | 6.64% | triple_bottom_breakout | TP | 11 |
| 12 | 2025-05-11 00:00 | 2025-05-17 12:00 | LONG | $664.1600 | $640.4500 | $-6.13 | -3.57% | triple_bottom_breakout | Time | 26 |
| 13 | 2025-05-14 00:00 | 2025-05-20 12:00 | LONG | $663.4800 | $646.7400 | $-4.34 | -2.52% | triple_bottom_breakout | Time | 26 |
| 14 | 2025-05-14 06:00 | 2025-05-20 18:00 | LONG | $659.7000 | $650.0000 | $-2.02 | -1.47% | triple_bottom_breakout | Time | 26 |
| 15 | 2025-05-18 00:00 | 2025-05-22 00:00 | LONG | $645.8600 | $681.3600 | $7.87 | 5.50% | triple_bottom_breakout | TP | 16 |
| 16 | 2025-05-24 12:00 | 2025-05-31 00:00 | LONG | $675.6300 | $653.1100 | $-6.84 | -3.33% | triple_bottom_breakout | Time | 26 |
| 17 | 2025-05-26 06:00 | 2025-06-01 18:00 | LONG | $674.1700 | $660.7700 | $-3.26 | -1.99% | triple_bottom_breakout | Time | 26 |
| 18 | 2025-05-27 00:00 | 2025-06-02 12:00 | LONG | $675.0300 | $660.8100 | $-2.77 | -2.11% | triple_bottom_breakout | Time | 26 |
| 20 | 2025-06-04 06:00 | 2025-06-05 18:00 | SHORT | $667.8000 | $633.3200 | $8.37 | 5.16% | triple_top_breakdown | TP | 6 |
| 19 | 2025-06-03 00:00 | 2025-06-05 18:00 | SHORT | $667.3400 | $633.3200 | $10.33 | 5.10% | triple_top_breakdown | TP | 11 |
| 21 | 2025-06-04 12:00 | 2025-06-11 00:00 | LONG | $667.5000 | $669.2500 | $0.34 | 0.26% | triple_bottom_breakout | Time | 26 |
| 22 | 2025-06-06 12:00 | 2025-06-13 00:00 | SHORT | $646.9100 | $647.7600 | $-0.24 | -0.13% | triple_top_breakdown | Time | 26 |
| 23 | 2025-06-07 12:00 | 2025-06-14 00:00 | SHORT | $649.4600 | $652.4800 | $-0.67 | -0.47% | triple_top_breakdown | Time | 26 |
| 24 | 2025-06-12 00:00 | 2025-06-18 12:00 | LONG | $667.1800 | $641.6500 | $-5.42 | -3.83% | triple_bottom_breakout | Time | 26 |
| 25 | 2025-06-15 12:00 | 2025-06-22 00:00 | SHORT | $648.4300 | $633.5200 | $4.09 | 2.30% | triple_top_breakdown | Time | 26 |
| 26 | 2025-06-15 18:00 | 2025-06-22 06:00 | SHORT | $648.1900 | $630.3900 | $3.91 | 2.75% | triple_top_breakdown | Time | 26 |
| 27 | 2025-06-19 12:00 | 2025-06-26 00:00 | SHORT | $642.2500 | $647.0000 | $-1.04 | -0.74% | triple_top_breakdown | Time | 26 |
| 28 | 2025-06-24 00:00 | 2025-06-29 12:00 | LONG | $642.2300 | $648.7600 | $1.82 | 1.02% | triple_bottom_breakout | End | 22 |
| 29 | 2025-06-24 06:00 | 2025-06-29 12:00 | SHORT | $638.5000 | $648.7600 | $-2.30 | -1.61% | triple_top_breakdown | End | 21 |
| 30 | 2025-06-26 00:00 | 2025-06-29 12:00 | SHORT | $647.0000 | $648.7600 | $-0.39 | -0.27% | triple_top_breakdown | End | 14 |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 3.22% return vs -0.60%.

### Key Observations:
- **Trade Frequency**: 51 vs 31 trades
- **Win Rate Difference**: 43.14% vs 41.94%
- **Return Difference**: 3.82% gap
- **Position Management**: Up to 3 positions at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)
- **Position Size**: 20.0% of capital per position

---
*Báo cáo được tạo tự động bởi Triple Pattern Multi-Position Backtest System*
