# Butterfly Pattern Strategy Comparison - SOLUSDT 4h

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
| Win Rate | 0.00% | 66.67% |
| Total Return | -9.67% | -8.31% |
| Final Capital | $903.35 | $916.90 |
| Total PnL | $-96.65 | $-83.10 |
| Average PnL per Trade | $-32.22 | $-27.70 |
| Best Trade | $-15.61 | $10.02 |
| Worst Trade | $-47.40 | $-97.17 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-15 16:00 | 2025-04-17 04:00 | SHORT | $127.8800 | $134.2600 | $-47.40 | -4.99% | Bearish Butterfly | Time |
| 2025-04-29 20:00 | 2025-05-01 08:00 | SHORT | $146.3100 | $151.7500 | $-33.65 | -3.72% | Bearish Butterfly | Time |
| 2025-06-05 00:00 | 2025-06-06 12:00 | LONG | $153.8300 | $151.0800 | $-15.61 | -1.79% | Bullish Butterfly | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-15 16:00 | 2025-04-20 00:00 | SHORT | $127.8800 | $140.9600 | $-97.17 | -10.23% | Bearish Butterfly | Time |
| 2025-04-29 20:00 | 2025-05-04 04:00 | SHORT | $146.3100 | $145.6200 | $4.04 | 0.47% | Bearish Butterfly | Time |
| 2025-06-05 00:00 | 2025-06-09 08:00 | LONG | $153.8300 | $155.6200 | $10.02 | 1.16% | Bullish Butterfly | Time |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with -8.31% return vs -9.67%.

### Key Observations:
- **Trade Frequency**: 3 vs 3 trades
- **Win Rate Difference**: 0.00% vs 66.67%
- **Return Difference**: 1.36% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
