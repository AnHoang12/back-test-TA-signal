# Triple Pattern Strategy Comparison - BTCUSDT 12h

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
| Win Rate | 83.33% | 71.43% |
| Total Return | 10.58% | 12.85% |
| Final Capital | $1105.84 | $1128.53 |
| Total PnL | $105.84 | $128.53 |
| Average PnL per Trade | $8.82 | $18.36 |
| Best Trade | $58.90 | $62.00 |
| Worst Trade | $-28.75 | $-39.41 |
| Long Trades | 10 | 5 |
| Short Trades | 2 | 2 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-04-23 00:00 | 2025-04-27 12:00 | LONG | $93466.0100 | $93749.3000 | $2.73 | 0.30% | triple_bottom_breakout | Time | 9 |
| 2025-04-28 00:00 | 2025-05-02 12:00 | LONG | $95319.9900 | $96887.1400 | $14.84 | 1.64% | triple_bottom_breakout | Time | 9 |
| 2025-05-02 12:00 | 2025-05-07 00:00 | LONG | $96887.1400 | $97047.4300 | $1.52 | 0.17% | triple_bottom_breakout | Time | 9 |
| 2025-05-07 12:00 | 2025-05-08 12:00 | LONG | $97030.5000 | $103261.6000 | $58.90 | 6.42% | triple_bottom_breakout | TP | 2 |
| 2025-05-09 12:00 | 2025-05-14 00:00 | LONG | $102971.9900 | $103944.9300 | $9.17 | 0.94% | triple_bottom_breakout | Time | 9 |
| 2025-05-14 00:00 | 2025-05-18 12:00 | LONG | $103944.9300 | $106454.2600 | $23.62 | 2.41% | triple_bottom_breakout | Time | 9 |
| 2025-05-20 12:00 | 2025-05-25 00:00 | LONG | $106849.9900 | $107260.0000 | $3.84 | 0.38% | triple_bottom_breakout | Time | 9 |
| 2025-05-25 12:00 | 2025-05-30 00:00 | LONG | $109004.1900 | $105880.5100 | $-28.75 | -2.87% | triple_bottom_breakout | Time | 9 |
| 2025-06-01 12:00 | 2025-06-06 00:00 | LONG | $105642.9300 | $103927.9900 | $-15.86 | -1.62% | triple_bottom_breakout | Time | 9 |
| 2025-06-08 12:00 | 2025-06-13 00:00 | SHORT | $105734.0000 | $105039.4800 | $6.33 | 0.66% | triple_top_breakdown | Time | 9 |
| 2025-06-16 12:00 | 2025-06-21 00:00 | SHORT | $106794.5300 | $103874.6400 | $26.49 | 2.73% | triple_top_breakdown | Time | 9 |
| 2025-06-26 00:00 | 2025-06-30 00:00 | LONG | $107325.4100 | $107654.2000 | $3.04 | 0.31% | triple_bottom_breakout | End | 8 |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-04-23 00:00 | 2025-05-06 00:00 | LONG | $93466.0100 | $93812.5400 | $3.34 | 0.37% | triple_bottom_breakout | Time | 26 |
| 2025-05-06 12:00 | 2025-05-08 12:00 | LONG | $96834.0200 | $103261.6000 | $59.94 | 6.64% | triple_bottom_breakout | TP | 4 |
| 2025-05-09 12:00 | 2025-05-21 12:00 | LONG | $102971.9900 | $109643.9900 | $62.00 | 6.48% | triple_bottom_breakout | TP | 24 |
| 2025-05-21 12:00 | 2025-06-03 12:00 | LONG | $109643.9900 | $105376.8900 | $-39.41 | -3.89% | triple_bottom_breakout | Time | 26 |
| 2025-06-03 12:00 | 2025-06-16 12:00 | SHORT | $105376.8900 | $106794.5300 | $-13.15 | -1.35% | triple_top_breakdown | Time | 26 |
| 2025-06-16 12:00 | 2025-06-22 12:00 | SHORT | $106794.5300 | $100963.8700 | $52.71 | 5.46% | triple_top_breakdown | TP | 12 |
| 2025-06-26 00:00 | 2025-06-30 00:00 | LONG | $107325.4100 | $107654.2000 | $3.10 | 0.31% | triple_bottom_breakout | End | 8 |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 12.85% return vs 10.58%.

### Key Observations:
- **Trade Frequency**: 12 vs 7 trades
- **Win Rate Difference**: 83.33% vs 71.43%
- **Return Difference**: 2.27% gap
- **Position Management**: Only 1 position at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)

---
*Báo cáo được tạo tự động bởi Triple Pattern Backtest System*
