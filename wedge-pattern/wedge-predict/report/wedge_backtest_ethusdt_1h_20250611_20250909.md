# Wedge Pattern Strategy Comparison - ETHUSDT 1h

## Strategy Overview
- **Pattern**: Rising/Falling Wedge (pivot-based)
- **Entry**: Breakout after last pivot in wedge
- **Position Management**: Only 1 position at a time
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods
- **Take Profit**: 3.0%
- **Pivot window**: 3
- **Pattern max length**: 48
- **Num Highs/Lows**: 3/3

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 11 | 10 |
| Win Rate | 54.55% | 60.00% |
| Total Return | 1.10% | -1.47% |
| Final Capital | $10109.72 | $9853.10 |
| Total PnL | $109.72 | $-146.90 |
| Average PnL per Trade | $9.97 | $-14.69 |
| Best Trade | $194.24 | $284.54 |
| Worst Trade | $-187.15 | $-528.02 |
| Long Trades | 6 | 6 |
| Short Trades | 5 | 4 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-06-13 08:00:00 | 2025-06-13 17:00:00 | LONG | $2517.8200 | $2543.1900 | $90.69 | 1.01% | FALLING | Time | 9 |
| 2025-06-28 14:00:00 | 2025-06-28 23:00:00 | SHORT | $2425.5700 | $2435.6200 | $-37.63 | -0.41% | RISING | Time | 9 |
| 2025-07-19 05:00:00 | 2025-07-19 14:00:00 | LONG | $3586.3100 | $3531.5700 | $-138.10 | -1.53% | FALLING | Time | 9 |
| 2025-07-22 12:00:00 | 2025-07-22 21:00:00 | LONG | $3701.5500 | $3705.7700 | $10.17 | 0.11% | FALLING | Time | 9 |
| 2025-08-03 23:00:00 | 2025-08-04 08:00:00 | SHORT | $3496.7400 | $3550.5000 | $-137.33 | -1.54% | RISING | Time | 9 |
| 2025-08-08 03:00:00 | 2025-08-08 12:00:00 | SHORT | $3939.1800 | $3892.3700 | $104.68 | 1.19% | RISING | Time | 9 |
| 2025-08-20 09:00:00 | 2025-08-20 18:00:00 | LONG | $4222.7400 | $4291.6700 | $145.33 | 1.63% | FALLING | Time | 9 |
| 2025-08-26 03:00:00 | 2025-08-26 12:00:00 | LONG | $4402.5800 | $4497.2400 | $194.24 | 2.15% | FALLING | Time | 9 |
| 2025-08-29 22:00:00 | 2025-08-30 07:00:00 | LONG | $4366.3900 | $4402.3900 | $75.93 | 0.82% | FALLING | Time | 9 |
| 2025-08-30 21:00:00 | 2025-08-31 06:00:00 | SHORT | $4346.9100 | $4434.6000 | $-187.15 | -2.02% | RISING | Time | 9 |
| 2025-08-31 08:00:00 | 2025-08-31 17:00:00 | SHORT | $4471.8500 | $4477.3000 | $-11.10 | -0.12% | RISING | Time | 9 |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-06-13 08:00:00 | 2025-06-14 10:00:00 | LONG | $2517.8200 | $2531.1000 | $47.47 | 0.53% | FALLING | Time | 26 |
| 2025-06-28 14:00:00 | 2025-06-29 16:00:00 | SHORT | $2425.5700 | $2439.0600 | $-50.29 | -0.56% | RISING | Time | 26 |
| 2025-07-19 05:00:00 | 2025-07-20 07:00:00 | LONG | $3586.3100 | $3668.4900 | $206.18 | 2.29% | FALLING | Time | 26 |
| 2025-07-22 12:00:00 | 2025-07-23 14:00:00 | LONG | $3701.5500 | $3616.4400 | $-211.15 | -2.30% | FALLING | Time | 26 |
| 2025-08-03 23:00:00 | 2025-08-05 01:00:00 | SHORT | $3496.7400 | $3680.3800 | $-472.29 | -5.25% | RISING | Time | 26 |
| 2025-08-08 03:00:00 | 2025-08-09 05:00:00 | SHORT | $3939.1800 | $4181.9400 | $-528.02 | -6.16% | RISING | Time | 26 |
| 2025-08-20 09:00:00 | 2025-08-20 20:00:00 | LONG | $4222.7400 | $4355.4000 | $254.24 | 3.14% | FALLING | TP | 11 |
| 2025-08-26 03:00:00 | 2025-08-26 14:00:00 | LONG | $4402.5800 | $4553.1200 | $284.54 | 3.42% | FALLING | TP | 11 |
| 2025-08-29 22:00:00 | 2025-08-31 00:00:00 | LONG | $4366.3900 | $4467.3700 | $198.37 | 2.31% | FALLING | Time | 26 |
| 2025-08-31 08:00:00 | 2025-09-01 10:00:00 | SHORT | $4471.8500 | $4408.5000 | $124.04 | 1.42% | RISING | Time | 26 |

## Analysis

**Winner: 9 Periods Strategy**

The 9-period exit strategy outperformed with 1.10% return vs -1.47%.

---
*Báo cáo được tạo tự động bởi Wedge Pattern Backtest System*
