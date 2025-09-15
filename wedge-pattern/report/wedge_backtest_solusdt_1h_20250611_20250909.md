# Wedge Pattern Strategy Comparison - SOLUSDT 1h

## Strategy Overview
- **Pattern**: Rising/Falling Wedge (pivot-based)
- **Entry**: Breakout after last pivot in wedge
- **Position Management**: Only 1 position at a time
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods
- **Take Profit**: 3.0%
- **Pivot window**: 3
- **Pattern max length**: 35
- **Num Highs/Lows**: 3/3

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 5 | 5 |
| Win Rate | 0.00% | 40.00% |
| Total Return | -7.47% | -3.30% |
| Final Capital | $9252.73 | $9669.80 |
| Total PnL | $-747.27 | $-330.20 |
| Average PnL per Trade | $-149.45 | $-66.04 |
| Best Trade | $-41.33 | $298.88 |
| Worst Trade | $-238.86 | $-468.58 |
| Long Trades | 2 | 2 |
| Short Trades | 3 | 3 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-06-27 09:00:00 | 2025-06-27 18:00:00 | LONG | $142.1000 | $140.6400 | $-92.47 | -1.03% | FALLING | Time | 9 |
| 2025-07-22 20:00:00 | 2025-07-23 05:00:00 | SHORT | $200.6500 | $201.5800 | $-41.33 | -0.46% | RISING | Time | 9 |
| 2025-08-01 13:00:00 | 2025-08-01 22:00:00 | LONG | $165.6700 | $161.2800 | $-235.30 | -2.65% | FALLING | Time | 9 |
| 2025-08-08 02:00:00 | 2025-08-08 11:00:00 | SHORT | $174.8400 | $177.6500 | $-139.31 | -1.61% | RISING | Time | 9 |
| 2025-08-27 08:00:00 | 2025-08-27 17:00:00 | SHORT | $203.4900 | $209.1800 | $-238.86 | -2.80% | RISING | Time | 9 |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-06-27 09:00:00 | 2025-06-28 07:00:00 | LONG | $142.1000 | $146.5700 | $283.11 | 3.15% | FALLING | TP | 22 |
| 2025-07-22 20:00:00 | 2025-07-23 12:00:00 | SHORT | $200.6500 | $194.1700 | $298.88 | 3.23% | RISING | TP | 16 |
| 2025-08-01 13:00:00 | 2025-08-02 15:00:00 | LONG | $165.6700 | $161.5000 | $-239.72 | -2.52% | FALLING | Time | 26 |
| 2025-08-08 02:00:00 | 2025-08-09 04:00:00 | SHORT | $174.8400 | $178.6700 | $-203.90 | -2.19% | RISING | Time | 26 |
| 2025-08-27 08:00:00 | 2025-08-28 10:00:00 | SHORT | $203.4900 | $213.9400 | $-468.58 | -5.14% | RISING | Time | 26 |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with -3.30% return vs -7.47%.

---
*Báo cáo được tạo tự động bởi Wedge Pattern Backtest System*
