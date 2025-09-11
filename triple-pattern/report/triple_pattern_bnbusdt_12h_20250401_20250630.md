# Triple Pattern Strategy Comparison - BNBUSDT 12h

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
| Total Trades | 9 | 5 |
| Win Rate | 33.33% | 40.00% |
| Total Return | -10.17% | -3.42% |
| Final Capital | $898.35 | $965.83 |
| Total PnL | $-101.65 | $-34.17 |
| Average PnL per Trade | $-11.29 | $-6.83 |
| Best Trade | $11.36 | $30.13 |
| Worst Trade | $-38.36 | $-31.66 |
| Long Trades | 5 | 5 |
| Short Trades | 4 | 0 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-04-22 00:00 | 2025-04-26 12:00 | LONG | $605.8800 | $607.2300 | $2.01 | 0.22% | triple_bottom_breakout | Time | 9 |
| 2025-05-14 00:00 | 2025-05-18 12:00 | LONG | $659.7000 | $651.5300 | $-11.17 | -1.24% | triple_bottom_breakout | Time | 9 |
| 2025-05-19 00:00 | 2025-05-23 12:00 | SHORT | $639.9600 | $656.9800 | $-23.72 | -2.66% | triple_top_breakdown | Time | 9 |
| 2025-05-26 12:00 | 2025-05-31 00:00 | LONG | $674.2900 | $654.0600 | $-26.11 | -3.00% | triple_bottom_breakout | Time | 9 |
| 2025-06-03 00:00 | 2025-06-07 12:00 | LONG | $665.2000 | $650.8200 | $-18.31 | -2.16% | triple_bottom_breakout | Time | 9 |
| 2025-06-08 00:00 | 2025-06-12 12:00 | SHORT | $650.4700 | $654.7500 | $-5.46 | -0.66% | triple_top_breakdown | Time | 9 |
| 2025-06-13 00:00 | 2025-06-17 12:00 | SHORT | $654.5100 | $648.0800 | $8.11 | 0.98% | triple_top_breakdown | Time | 9 |
| 2025-06-23 00:00 | 2025-06-27 12:00 | SHORT | $617.2800 | $645.7100 | $-38.36 | -4.61% | triple_top_breakdown | Time | 9 |
| 2025-06-27 12:00 | 2025-06-29 12:00 | LONG | $645.7100 | $654.9000 | $11.36 | 1.42% | triple_bottom_breakout | End | 4 |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-04-22 00:00 | 2025-05-05 00:00 | LONG | $605.8800 | $593.5700 | $-18.29 | -2.03% | triple_bottom_breakout | Time | 26 |
| 2025-05-14 00:00 | 2025-05-27 00:00 | LONG | $659.7000 | $682.2000 | $30.13 | 3.41% | triple_bottom_breakout | Time | 26 |
| 2025-05-28 00:00 | 2025-06-10 00:00 | LONG | $687.4400 | $665.1900 | $-29.47 | -3.24% | triple_bottom_breakout | Time | 26 |
| 2025-06-11 12:00 | 2025-06-24 12:00 | LONG | $667.4300 | $643.5300 | $-31.66 | -3.58% | triple_bottom_breakout | Time | 26 |
| 2025-06-24 12:00 | 2025-06-29 12:00 | LONG | $643.5300 | $654.9000 | $15.12 | 1.77% | triple_bottom_breakout | End | 10 |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with -3.42% return vs -10.17%.

### Key Observations:
- **Trade Frequency**: 9 vs 5 trades
- **Win Rate Difference**: 33.33% vs 40.00%
- **Return Difference**: 6.75% gap
- **Position Management**: Only 1 position at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)

---
*Báo cáo được tạo tự động bởi Triple Pattern Backtest System*
