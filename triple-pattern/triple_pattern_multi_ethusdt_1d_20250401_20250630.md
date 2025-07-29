# Triple Pattern Strategy Comparison - Multi Position - ETHUSDT 1d

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
| Total Trades | 10 | 10 |
| Win Rate | 80.00% | 90.00% |
| Total Return | 3.53% | 8.45% |
| Final Capital | $1035.26 | $1084.48 |
| Total PnL | $35.26 | $84.48 |
| Average PnL per Trade | $3.53 | $8.45 |
| Best Trade | $14.77 | $14.77 |
| Worst Trade | $-29.01 | $-6.69 |
| Long Trades | 10 | 10 |
| Short Trades | 0 | 0 |
| Max Concurrent Positions | 3 | 3 |

## Strategy 1: Exit after 9 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-05-12 00:00 | 2025-05-13 00:00 | LONG | $2495.4700 | $2679.7100 | $14.77 | 7.38% | triple_bottom_breakout | TP | 1 |
| 3 | 2025-05-20 00:00 | 2025-05-22 00:00 | LONG | $2524.1900 | $2664.8200 | $7.24 | 5.57% | triple_bottom_breakout | TP | 2 |
| 2 | 2025-05-19 00:00 | 2025-05-22 00:00 | LONG | $2528.1400 | $2664.8200 | $8.78 | 5.41% | triple_bottom_breakout | TP | 3 |
| 1 | 2025-05-16 00:00 | 2025-05-22 00:00 | LONG | $2537.1200 | $2664.8200 | $10.22 | 5.03% | triple_bottom_breakout | TP | 6 |
| 4 | 2025-05-24 00:00 | 2025-05-27 00:00 | LONG | $2530.4000 | $2660.8100 | $10.73 | 5.15% | triple_bottom_breakout | TP | 3 |
| 5 | 2025-05-25 00:00 | 2025-05-28 00:00 | LONG | $2551.2200 | $2681.6000 | $8.51 | 5.11% | triple_bottom_breakout | TP | 3 |
| 6 | 2025-05-28 00:00 | 2025-06-06 00:00 | LONG | $2681.6000 | $2476.1000 | $-16.25 | -7.66% | triple_bottom_breakout | Time | 9 |
| 7 | 2025-06-01 00:00 | 2025-06-09 00:00 | LONG | $2539.2100 | $2680.1300 | $9.41 | 5.55% | triple_bottom_breakout | TP | 8 |
| 8 | 2025-06-04 00:00 | 2025-06-10 00:00 | LONG | $2607.6800 | $2816.4000 | $10.86 | 8.00% | triple_bottom_breakout | TP | 6 |
| 9 | 2025-06-13 00:00 | 2025-06-22 00:00 | LONG | $2579.1900 | $2227.7000 | $-29.01 | -13.63% | triple_bottom_breakout | Time | 9 |

## Strategy 2: Exit after 26 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-05-12 00:00 | 2025-05-13 00:00 | LONG | $2495.4700 | $2679.7100 | $14.77 | 7.38% | triple_bottom_breakout | TP | 1 |
| 3 | 2025-05-20 00:00 | 2025-05-22 00:00 | LONG | $2524.1900 | $2664.8200 | $7.24 | 5.57% | triple_bottom_breakout | TP | 2 |
| 2 | 2025-05-19 00:00 | 2025-05-22 00:00 | LONG | $2528.1400 | $2664.8200 | $8.78 | 5.41% | triple_bottom_breakout | TP | 3 |
| 1 | 2025-05-16 00:00 | 2025-05-22 00:00 | LONG | $2537.1200 | $2664.8200 | $10.22 | 5.03% | triple_bottom_breakout | TP | 6 |
| 4 | 2025-05-24 00:00 | 2025-05-27 00:00 | LONG | $2530.4000 | $2660.8100 | $10.73 | 5.15% | triple_bottom_breakout | TP | 3 |
| 5 | 2025-05-25 00:00 | 2025-05-28 00:00 | LONG | $2551.2200 | $2681.6000 | $8.51 | 5.11% | triple_bottom_breakout | TP | 3 |
| 7 | 2025-06-01 00:00 | 2025-06-09 00:00 | LONG | $2539.2100 | $2680.1300 | $9.41 | 5.55% | triple_bottom_breakout | TP | 8 |
| 8 | 2025-06-04 00:00 | 2025-06-10 00:00 | LONG | $2607.6800 | $2816.4000 | $10.86 | 8.00% | triple_bottom_breakout | TP | 6 |
| 6 | 2025-05-28 00:00 | 2025-06-10 00:00 | LONG | $2681.6000 | $2816.4000 | $10.66 | 5.03% | triple_bottom_breakout | TP | 13 |
| 9 | 2025-06-13 00:00 | 2025-06-29 00:00 | LONG | $2579.1900 | $2500.0900 | $-6.69 | -3.07% | triple_bottom_breakout | End | 16 |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 8.45% return vs 3.53%.

### Key Observations:
- **Trade Frequency**: 10 vs 10 trades
- **Win Rate Difference**: 80.00% vs 90.00%
- **Return Difference**: 4.92% gap
- **Position Management**: Up to 3 positions at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)
- **Position Size**: 20.0% of capital per position

---
*Báo cáo được tạo tự động bởi Triple Pattern Multi-Position Backtest System*
