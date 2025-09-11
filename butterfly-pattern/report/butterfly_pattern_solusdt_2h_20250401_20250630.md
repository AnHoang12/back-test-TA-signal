# Butterfly Pattern Strategy Comparison - SOLUSDT 2h

## Strategy Overview
- **Pattern**: Butterfly Pattern (Bullish & Bearish)
- **Entry**: At close price when pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods

- **Take Profit**: 5.0%

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 5 | 5 |
| Win Rate | 40.00% | 80.00% |
| Total Return | -6.49% | -6.71% |
| Final Capital | $935.11 | $932.92 |
| Total PnL | $-64.89 | $-67.08 |
| Average PnL per Trade | $-12.98 | $-13.42 |
| Best Trade | $25.44 | $19.19 |
| Worst Trade | $-47.59 | $-111.21 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-14 18:00 | 2025-04-15 12:00 | LONG | $131.0800 | $132.0800 | $7.25 | 0.76% | Bullish Butterfly | Time |
| 2025-05-05 16:00 | 2025-05-06 10:00 | LONG | $145.8000 | $142.5700 | $-21.20 | -2.22% | Bullish Butterfly | Time |
| 2025-05-16 10:00 | 2025-05-17 04:00 | LONG | $172.8100 | $167.5000 | $-28.78 | -3.07% | Bullish Butterfly | Time |
| 2025-05-24 22:00 | 2025-05-25 16:00 | SHORT | $175.8700 | $170.9500 | $25.44 | 2.80% | Bearish Butterfly | Time |
| 2025-05-29 06:00 | 2025-05-30 00:00 | LONG | $172.2300 | $163.4500 | $-47.59 | -5.10% | Bullish Butterfly | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-14 18:00 | 2025-04-16 22:00 | LONG | $131.0800 | $131.3300 | $1.81 | 0.19% | Bullish Butterfly | Time |
| 2025-05-05 16:00 | 2025-05-07 20:00 | LONG | $145.8000 | $147.3300 | $9.99 | 1.05% | Bullish Butterfly | Time |
| 2025-05-16 10:00 | 2025-05-18 14:00 | LONG | $172.8100 | $176.2600 | $19.19 | 2.00% | Bullish Butterfly | Time |
| 2025-05-24 22:00 | 2025-05-27 02:00 | SHORT | $175.8700 | $173.5100 | $13.14 | 1.34% | Bearish Butterfly | Time |
| 2025-05-29 06:00 | 2025-05-31 10:00 | LONG | $172.2300 | $152.9200 | $-111.21 | -11.21% | Bullish Butterfly | Time |

## Analysis

**Winner: 9 Periods Strategy**

The 9-period exit strategy outperformed with -6.49% return vs -6.71%.

### Key Observations:
- **Trade Frequency**: 5 vs 5 trades
- **Win Rate Difference**: 40.00% vs 80.00%
- **Return Difference**: 0.22% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
