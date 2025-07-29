# Triple Pattern Strategy Comparison - Multi Position - BNBUSDT 12h

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
| Total Trades | 19 | 13 |
| Win Rate | 36.84% | 53.85% |
| Total Return | -2.14% | -0.07% |
| Final Capital | $978.61 | $999.29 |
| Total PnL | $-21.39 | $-0.71 |
| Average PnL per Trade | $-1.13 | $-0.05 |
| Best Trade | $9.75 | $8.23 |
| Worst Trade | $-9.05 | $-10.58 |
| Long Trades | 13 | 10 |
| Short Trades | 6 | 3 |
| Max Concurrent Positions | 3 | 3 |

## Strategy 1: Exit after 9 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-04-22 00:00 | 2025-04-26 12:00 | LONG | $605.8800 | $607.2300 | $0.45 | 0.22% | triple_bottom_breakout | Time | 9 |
| 1 | 2025-05-14 00:00 | 2025-05-18 12:00 | LONG | $659.7000 | $651.5300 | $-2.48 | -1.24% | triple_bottom_breakout | Time | 9 |
| 2 | 2025-05-15 00:00 | 2025-05-19 12:00 | LONG | $653.3800 | $649.6200 | $-0.92 | -0.58% | triple_bottom_breakout | Time | 9 |
| 3 | 2025-05-15 12:00 | 2025-05-20 00:00 | LONG | $651.8800 | $643.8200 | $-1.58 | -1.24% | triple_bottom_breakout | Time | 9 |
| 5 | 2025-05-20 12:00 | 2025-05-22 00:00 | LONG | $650.0000 | $687.1100 | $9.75 | 5.71% | triple_bottom_breakout | TP | 3 |
| 4 | 2025-05-19 00:00 | 2025-05-23 12:00 | SHORT | $639.9600 | $656.9800 | $-3.78 | -2.66% | triple_top_breakdown | Time | 9 |
| 6 | 2025-05-22 12:00 | 2025-05-27 00:00 | LONG | $686.5700 | $682.2000 | $-1.10 | -0.64% | triple_bottom_breakout | Time | 9 |
| 7 | 2025-05-26 12:00 | 2025-05-31 00:00 | LONG | $674.2900 | $654.0600 | $-4.97 | -3.00% | triple_bottom_breakout | Time | 9 |
| 8 | 2025-05-28 00:00 | 2025-06-01 12:00 | LONG | $687.4400 | $660.7700 | $-6.48 | -3.88% | triple_bottom_breakout | Time | 9 |
| 9 | 2025-06-03 00:00 | 2025-06-07 12:00 | LONG | $665.2000 | $650.8200 | $-4.28 | -2.16% | triple_bottom_breakout | Time | 9 |
| 10 | 2025-06-08 00:00 | 2025-06-12 12:00 | SHORT | $650.4700 | $654.7500 | $-1.30 | -0.66% | triple_top_breakdown | Time | 9 |
| 11 | 2025-06-08 12:00 | 2025-06-13 00:00 | SHORT | $652.0000 | $654.5100 | $-0.61 | -0.38% | triple_top_breakdown | Time | 9 |
| 12 | 2025-06-11 12:00 | 2025-06-16 00:00 | LONG | $667.4300 | $654.4300 | $-2.45 | -1.95% | triple_bottom_breakout | Time | 9 |
| 13 | 2025-06-13 00:00 | 2025-06-17 12:00 | SHORT | $654.5100 | $648.0800 | $1.68 | 0.98% | triple_top_breakdown | Time | 9 |
| 14 | 2025-06-15 12:00 | 2025-06-20 00:00 | SHORT | $648.1900 | $647.3400 | $0.18 | 0.13% | triple_top_breakdown | Time | 9 |
| 15 | 2025-06-23 00:00 | 2025-06-27 12:00 | SHORT | $617.2800 | $645.7100 | $-9.05 | -4.61% | triple_top_breakdown | Time | 9 |
| 16 | 2025-06-24 12:00 | 2025-06-29 00:00 | LONG | $643.5300 | $651.1200 | $1.85 | 1.18% | triple_bottom_breakout | Time | 9 |
| 17 | 2025-06-25 12:00 | 2025-06-29 12:00 | LONG | $646.0700 | $654.9000 | $1.72 | 1.37% | triple_bottom_breakout | End | 8 |
| 18 | 2025-06-27 12:00 | 2025-06-29 12:00 | LONG | $645.7100 | $654.9000 | $1.96 | 1.42% | triple_bottom_breakout | End | 4 |

## Strategy 2: Exit after 26 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-04-22 00:00 | 2025-05-05 00:00 | LONG | $605.8800 | $593.5700 | $-4.06 | -2.03% | triple_bottom_breakout | Time | 26 |
| 3 | 2025-05-15 12:00 | 2025-05-22 00:00 | LONG | $651.8800 | $687.1100 | $6.89 | 5.40% | triple_bottom_breakout | TP | 13 |
| 2 | 2025-05-15 00:00 | 2025-05-22 00:00 | LONG | $653.3800 | $687.1100 | $8.23 | 5.16% | triple_bottom_breakout | TP | 14 |
| 1 | 2025-05-14 00:00 | 2025-05-27 00:00 | LONG | $659.7000 | $682.2000 | $6.79 | 3.41% | triple_bottom_breakout | Time | 26 |
| 4 | 2025-05-22 12:00 | 2025-06-04 12:00 | LONG | $686.5700 | $663.2300 | $-5.52 | -3.40% | triple_bottom_breakout | Time | 26 |
| 5 | 2025-05-26 12:00 | 2025-06-08 12:00 | LONG | $674.2900 | $652.0000 | $-4.29 | -3.31% | triple_bottom_breakout | Time | 26 |
| 6 | 2025-05-28 00:00 | 2025-06-10 00:00 | LONG | $687.4400 | $665.1900 | $-4.70 | -3.24% | triple_bottom_breakout | Time | 26 |
| 7 | 2025-06-08 00:00 | 2025-06-21 00:00 | SHORT | $650.4700 | $642.4400 | $1.82 | 1.23% | triple_top_breakdown | Time | 26 |
| 8 | 2025-06-08 12:00 | 2025-06-21 12:00 | SHORT | $652.0000 | $628.9700 | $5.05 | 3.53% | triple_top_breakdown | Time | 26 |
| 9 | 2025-06-11 12:00 | 2025-06-24 12:00 | LONG | $667.4300 | $643.5300 | $-5.10 | -3.58% | triple_bottom_breakout | Time | 26 |
| 10 | 2025-06-23 00:00 | 2025-06-29 12:00 | SHORT | $617.2800 | $654.9000 | $-10.58 | -6.09% | triple_top_breakdown | End | 13 |
| 11 | 2025-06-24 12:00 | 2025-06-29 12:00 | LONG | $643.5300 | $654.9000 | $2.94 | 1.77% | triple_bottom_breakout | End | 10 |
| 12 | 2025-06-25 12:00 | 2025-06-29 12:00 | LONG | $646.0700 | $654.9000 | $1.82 | 1.37% | triple_bottom_breakout | End | 8 |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with -0.07% return vs -2.14%.

### Key Observations:
- **Trade Frequency**: 19 vs 13 trades
- **Win Rate Difference**: 36.84% vs 53.85%
- **Return Difference**: 2.07% gap
- **Position Management**: Up to 3 positions at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)
- **Position Size**: 20.0% of capital per position

---
*Báo cáo được tạo tự động bởi Triple Pattern Multi-Position Backtest System*
