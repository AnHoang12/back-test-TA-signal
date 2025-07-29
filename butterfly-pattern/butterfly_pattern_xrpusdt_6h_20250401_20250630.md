# Butterfly Pattern Strategy Comparison - XRPUSDT 6h

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
| Total Return | 35.78% |
| Final Capital | $1102.70 | $1157.77 |
| Total PnL | $102.70 | $157.77 |
| Average PnL per Trade | $34.23 | $52.59 |
| Best Trade | $66.90 | $70.24 |
| Worst Trade | $13.33 | $36.36 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-05-02 18:00 | 2025-05-05 00:00 | SHORT | $2.2093 | $2.1783 | $13.33 | 1.40% | Bearish Butterfly | Time |
| 2025-05-21 18:00 | 2025-05-24 00:00 | SHORT | $2.3952 | $2.3393 | $22.47 | 2.33% | Bearish Butterfly | Time |
| 2025-06-15 00:00 | 2025-06-16 12:00 | LONG | $2.1606 | $2.3075 | $66.90 | 6.80% | Bullish Butterfly | TP |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-05-02 18:00 | 2025-05-06 06:00 | SHORT | $2.2093 | $2.0903 | $51.17 | 5.39% | Bearish Butterfly | TP |
| 2025-05-21 18:00 | 2025-05-28 06:00 | SHORT | $2.3952 | $2.3080 | $36.36 | 3.64% | Bearish Butterfly | Time |
| 2025-06-15 00:00 | 2025-06-16 12:00 | LONG | $2.1606 | $2.3075 | $70.24 | 6.80% | Bullish Butterfly | TP |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 15.78% return vs 10.27%.

### Key Observations:
- **Trade Frequency**: 3 vs 3 trades
- **Win Rate Difference**: 100.00% vs 100.00%
- **Return Difference**: 5.51% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
