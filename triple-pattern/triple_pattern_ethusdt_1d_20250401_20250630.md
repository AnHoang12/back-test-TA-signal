# Triple Pattern Strategy Comparison - ETHUSDT 1d

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
| Total Trades | 5 | 5 |
| Win Rate | 60.00% | 80.00% |
| Total Return | -4.72% | 18.56% |
| Final Capital | $952.81 | $1185.58 |
| Total PnL | $-47.19 | $185.58 |
| Average PnL per Trade | $-9.44 | $37.12 |
| Best Trade | $66.45 | $66.45 |
| Worst Trade | $-133.20 | $-33.65 |
| Long Trades | 5 | 5 |
| Short Trades | 0 | 0 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-05-12 00:00 | 2025-05-13 00:00 | LONG | $2495.4700 | $2679.7100 | $66.45 | 7.38% | triple_bottom_breakout | TP | 1 |
| 2025-05-16 00:00 | 2025-05-22 00:00 | LONG | $2537.1200 | $2664.8200 | $48.31 | 5.03% | triple_bottom_breakout | TP | 6 |
| 2025-05-24 00:00 | 2025-05-27 00:00 | LONG | $2530.4000 | $2660.8100 | $51.71 | 5.15% | triple_bottom_breakout | TP | 3 |
| 2025-05-28 00:00 | 2025-06-06 00:00 | LONG | $2681.6000 | $2476.1000 | $-80.45 | -7.66% | triple_bottom_breakout | Time | 9 |
| 2025-06-13 00:00 | 2025-06-22 00:00 | LONG | $2579.1900 | $2227.7000 | $-133.20 | -13.63% | triple_bottom_breakout | Time | 9 |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-05-12 00:00 | 2025-05-13 00:00 | LONG | $2495.4700 | $2679.7100 | $66.45 | 7.38% | triple_bottom_breakout | TP | 1 |
| 2025-05-16 00:00 | 2025-05-22 00:00 | LONG | $2537.1200 | $2664.8200 | $48.31 | 5.03% | triple_bottom_breakout | TP | 6 |
| 2025-05-24 00:00 | 2025-05-27 00:00 | LONG | $2530.4000 | $2660.8100 | $51.71 | 5.15% | triple_bottom_breakout | TP | 3 |
| 2025-05-28 00:00 | 2025-06-10 00:00 | LONG | $2681.6000 | $2816.4000 | $52.77 | 5.03% | triple_bottom_breakout | TP | 13 |
| 2025-06-13 00:00 | 2025-06-29 00:00 | LONG | $2579.1900 | $2500.0900 | $-33.65 | -3.07% | triple_bottom_breakout | End | 16 |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 18.56% return vs -4.72%.

### Key Observations:
- **Trade Frequency**: 5 vs 5 trades
- **Win Rate Difference**: 60.00% vs 80.00%
- **Return Difference**: 23.28% gap
- **Position Management**: Only 1 position at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)

---
*Báo cáo được tạo tự động bởi Triple Pattern Backtest System*
