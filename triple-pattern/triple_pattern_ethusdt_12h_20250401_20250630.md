# Triple Pattern Strategy Comparison - ETHUSDT 12h

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
| Total Trades | 12 | 7 |
| Win Rate | 66.67% | 71.43% |
| Total Return | 18.99% | 10.54% |
| Final Capital | $1189.88 | $1105.41 |
| Total PnL | $189.88 | $105.41 |
| Average PnL per Trade | $15.82 | $15.06 |
| Best Trade | $99.98 | $92.42 |
| Worst Trade | $-83.82 | $-132.01 |
| Long Trades | 10 | 6 |
| Short Trades | 2 | 1 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-04-23 12:00 | 2025-04-28 00:00 | LONG | $1795.0700 | $1816.2000 | $10.59 | 1.18% | triple_bottom_breakout | Time | 9 |
| 2025-04-30 12:00 | 2025-05-05 00:00 | LONG | $1793.6100 | $1804.6300 | $5.59 | 0.61% | triple_bottom_breakout | Time | 9 |
| 2025-05-05 00:00 | 2025-05-08 00:00 | LONG | $1804.6300 | $1957.6300 | $77.54 | 8.48% | triple_bottom_breakout | TP | 6 |
| 2025-05-09 12:00 | 2025-05-10 12:00 | LONG | $2345.0400 | $2583.2300 | $99.98 | 10.16% | triple_bottom_breakout | TP | 2 |
| 2025-05-13 00:00 | 2025-05-13 12:00 | LONG | $2513.3900 | $2679.7100 | $71.09 | 6.62% | triple_bottom_breakout | TP | 1 |
| 2025-05-14 12:00 | 2025-05-19 00:00 | LONG | $2609.7400 | $2417.5800 | $-83.82 | -7.36% | triple_bottom_breakout | Time | 9 |
| 2025-05-21 12:00 | 2025-05-26 00:00 | LONG | $2550.9900 | $2568.0800 | $7.12 | 0.67% | triple_bottom_breakout | Time | 9 |
| 2025-05-26 12:00 | 2025-05-29 00:00 | LONG | $2563.7000 | $2715.8300 | $63.45 | 5.93% | triple_bottom_breakout | TP | 5 |
| 2025-06-02 12:00 | 2025-06-07 00:00 | LONG | $2607.4100 | $2495.7500 | $-48.24 | -4.28% | triple_bottom_breakout | Time | 9 |
| 2025-06-11 12:00 | 2025-06-16 00:00 | LONG | $2771.6100 | $2617.0100 | $-60.41 | -5.58% | triple_bottom_breakout | Time | 9 |
| 2025-06-17 00:00 | 2025-06-20 12:00 | SHORT | $2552.1900 | $2406.4900 | $58.72 | 5.71% | triple_top_breakdown | TP | 7 |
| 2025-06-24 00:00 | 2025-06-28 12:00 | SHORT | $2409.4400 | $2435.6200 | $-11.75 | -1.09% | triple_top_breakdown | Time | 9 |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-04-23 12:00 | 2025-05-06 12:00 | LONG | $1795.0700 | $1817.0000 | $11.00 | 1.22% | triple_bottom_breakout | Time | 26 |
| 2025-05-09 12:00 | 2025-05-10 12:00 | LONG | $2345.0400 | $2583.2300 | $92.42 | 10.16% | triple_bottom_breakout | TP | 2 |
| 2025-05-13 00:00 | 2025-05-13 12:00 | LONG | $2513.3900 | $2679.7100 | $65.72 | 6.62% | triple_bottom_breakout | TP | 1 |
| 2025-05-14 12:00 | 2025-05-27 12:00 | LONG | $2609.7400 | $2660.8100 | $20.59 | 1.96% | triple_bottom_breakout | Time | 26 |
| 2025-06-02 12:00 | 2025-06-10 00:00 | LONG | $2607.4100 | $2773.6400 | $68.26 | 6.38% | triple_bottom_breakout | TP | 15 |
| 2025-06-11 12:00 | 2025-06-24 12:00 | LONG | $2771.6100 | $2448.4500 | $-132.01 | -11.66% | triple_bottom_breakout | Time | 26 |
| 2025-06-26 00:00 | 2025-06-29 12:00 | SHORT | $2450.3600 | $2500.0900 | $-20.57 | -2.03% | triple_top_breakdown | End | 7 |

## Analysis

**Winner: 9 Periods Strategy**

The 9-period exit strategy outperformed with 18.99% return vs 10.54%.

### Key Observations:
- **Trade Frequency**: 12 vs 7 trades
- **Win Rate Difference**: 66.67% vs 71.43%
- **Return Difference**: 8.45% gap
- **Position Management**: Only 1 position at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)

---
*Báo cáo được tạo tự động bởi Triple Pattern Backtest System*
