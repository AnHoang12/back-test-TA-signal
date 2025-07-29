# Triple Pattern Strategy Comparison - BTCUSDT 1d

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
| Total Trades | 3 | 2 |
| Win Rate | 66.67% | 100.00% |
| Total Return | 2.93% | 6.39% |
| Final Capital | $1029.32 | $1063.86 |
| Total PnL | $29.32 | $63.86 |
| Average PnL per Trade | $9.77 | $31.93 |
| Best Trade | $51.00 | $51.00 |
| Worst Trade | $-46.58 | $12.86 |
| Long Trades | 3 | 2 |
| Short Trades | 0 | 0 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-05-15 00:00 | 2025-05-21 00:00 | LONG | $103763.7100 | $109643.9900 | $51.00 | 5.67% | triple_bottom_breakout | TP | 6 |
| 2025-06-02 00:00 | 2025-06-11 00:00 | LONG | $105857.9900 | $108645.1200 | $24.90 | 2.63% | triple_bottom_breakout | Time | 9 |
| 2025-06-13 00:00 | 2025-06-22 00:00 | LONG | $106066.5900 | $100963.8700 | $-46.58 | -4.81% | triple_bottom_breakout | Time | 9 |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-05-15 00:00 | 2025-05-21 00:00 | LONG | $103763.7100 | $109643.9900 | $51.00 | 5.67% | triple_bottom_breakout | TP | 6 |
| 2025-06-02 00:00 | 2025-06-28 00:00 | LONG | $105857.9900 | $107296.7900 | $12.86 | 1.36% | triple_bottom_breakout | Time | 26 |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 6.39% return vs 2.93%.

### Key Observations:
- **Trade Frequency**: 3 vs 2 trades
- **Win Rate Difference**: 66.67% vs 100.00%
- **Return Difference**: 3.45% gap
- **Position Management**: Only 1 position at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)

---
*Báo cáo được tạo tự động bởi Triple Pattern Backtest System*
