# Butterfly Pattern Strategy Comparison - XRPUSDT 4h

## Strategy Overview
- **Pattern**: Butterfly Pattern (Bullish & Bearish)
- **Entry**: At close price when pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods

- **Take Profit**: 5.0%

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 6 | 6 |
| Win Rate | 66.67% | 83.33% |
| Total Return | 14.83% | 29.02% |
| Final Capital | $1148.27 | $1290.18 |
| Total PnL | $148.27 | $290.18 |
| Average PnL per Trade | $24.71 | $48.36 |
| Best Trade | $109.12 | $113.85 |
| Worst Trade | $-43.62 | $-60.61 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-04 16:00 | 2025-04-06 04:00 | SHORT | $2.1285 | $2.0940 | $15.40 | 1.62% | Bearish Butterfly | Time |
| 2025-04-09 04:00 | 2025-04-09 16:00 | LONG | $1.8317 | $2.0389 | $109.12 | 11.31% | Bullish Butterfly | TP |
| 2025-04-18 04:00 | 2025-04-19 16:00 | LONG | $2.0692 | $2.0839 | $7.59 | 0.71% | Bullish Butterfly | Time |
| 2025-05-02 16:00 | 2025-05-04 04:00 | SHORT | $2.2093 | $2.2112 | $-0.92 | -0.09% | Bearish Butterfly | Time |
| 2025-06-02 12:00 | 2025-06-03 16:00 | LONG | $2.1594 | $2.2814 | $60.71 | 5.65% | Bullish Butterfly | TP |
| 2025-06-07 08:00 | 2025-06-08 20:00 | SHORT | $2.1829 | $2.2670 | $-43.62 | -3.85% | Bearish Butterfly | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-04 16:00 | 2025-04-06 16:00 | SHORT | $2.1285 | $1.9953 | $59.45 | 6.26% | Bearish Butterfly | TP |
| 2025-04-09 04:00 | 2025-04-09 16:00 | LONG | $1.8317 | $2.0389 | $113.85 | 11.31% | Bullish Butterfly | TP |
| 2025-04-18 04:00 | 2025-04-22 12:00 | LONG | $2.0692 | $2.1551 | $46.27 | 4.15% | Bullish Butterfly | Time |
| 2025-05-02 16:00 | 2025-05-06 08:00 | SHORT | $2.2093 | $2.0903 | $62.41 | 5.39% | Bearish Butterfly | TP |
| 2025-06-02 12:00 | 2025-06-03 16:00 | LONG | $2.1594 | $2.2814 | $68.81 | 5.65% | Bullish Butterfly | TP |
| 2025-06-07 08:00 | 2025-06-11 16:00 | SHORT | $2.1829 | $2.2860 | $-60.61 | -4.72% | Bearish Butterfly | Time |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 29.02% return vs 14.83%.

### Key Observations:
- **Trade Frequency**: 6 vs 6 trades
- **Win Rate Difference**: 66.67% vs 83.33%
- **Return Difference**: 14.19% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
