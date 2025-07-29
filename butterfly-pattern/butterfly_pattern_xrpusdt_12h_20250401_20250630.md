# Butterfly Pattern Strategy Comparison - XRPUSDT 12h

## Strategy Overview
- **Pattern**: Butterfly Pattern (Bullish & Bearish)
- **Entry**: At close price when pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods

- **Take Profit**: 5.0%

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 3 | 3 |
| Win Rate | 100.00% | 100.00% |
| Total Return | 7.90% | 12.97% |
| Final Capital | $1079.01 | $1129.69 |
| Total PnL | $79.01 | $129.69 |
| Average PnL per Trade | $26.34 | $43.23 |
| Best Trade | $49.47 | $53.82 |
| Worst Trade | $3.09 | $26.40 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-09 12:00 | 2025-04-12 12:00 | LONG | $2.0529 | $2.1598 | $49.47 | 5.21% | Bullish Butterfly | TP |
| 2025-04-12 12:00 | 2025-04-17 00:00 | SHORT | $2.1598 | $2.1025 | $26.45 | 2.65% | Bearish Butterfly | Time |
| 2025-06-19 00:00 | 2025-06-23 12:00 | LONG | $2.1519 | $2.1584 | $3.09 | 0.30% | Bullish Butterfly | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-09 12:00 | 2025-04-12 12:00 | LONG | $2.0529 | $2.1598 | $49.47 | 5.21% | Bullish Butterfly | TP |
| 2025-04-12 12:00 | 2025-04-20 00:00 | SHORT | $2.1598 | $2.0432 | $53.82 | 5.40% | Bearish Butterfly | TP |
| 2025-06-19 00:00 | 2025-06-29 12:00 | LONG | $2.1519 | $2.2061 | $26.40 | 2.52% | Bullish Butterfly | End |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 12.97% return vs 7.90%.

### Key Observations:
- **Trade Frequency**: 3 vs 3 trades
- **Win Rate Difference**: 100.00% vs 100.00%
- **Return Difference**: 5.07% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
