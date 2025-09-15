# Wedge Pattern Strategy Comparison - BNBUSDT 1h

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
| Total Trades | 5 | 4 |
| Win Rate | 20.00% | 0.00% |
| Total Return | -4.26% | -5.06% |
| Final Capital | $9573.92 | $9494.13 |
| Total PnL | $-426.08 | $-505.87 |
| Average PnL per Trade | $-85.22 | $-126.47 |
| Best Trade | $76.68 | $-56.76 |
| Worst Trade | $-211.06 | $-207.53 |
| Long Trades | 4 | 3 |
| Short Trades | 1 | 1 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-06-13 09:00:00 | 2025-06-13 18:00:00 | LONG | $654.8400 | $651.0200 | $-52.50 | -0.58% | FALLING | Time | 9 |
| 2025-07-17 00:00:00 | 2025-07-17 09:00:00 | SHORT | $717.1900 | $720.6200 | $-42.82 | -0.48% | RISING | Time | 9 |
| 2025-08-02 05:00:00 | 2025-08-02 14:00:00 | LONG | $766.1600 | $748.0200 | $-211.06 | -2.37% | FALLING | Time | 9 |
| 2025-08-24 01:00:00 | 2025-08-24 10:00:00 | LONG | $882.2700 | $862.4100 | $-196.38 | -2.25% | FALLING | Time | 9 |
| 2025-08-24 19:00:00 | 2025-08-25 04:00:00 | LONG | $869.5200 | $877.3200 | $76.68 | 0.90% | FALLING | Time | 9 |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-06-13 09:00:00 | 2025-06-14 11:00:00 | LONG | $654.8400 | $650.7100 | $-56.76 | -0.63% | FALLING | Time | 26 |
| 2025-07-17 00:00:00 | 2025-07-18 02:00:00 | SHORT | $717.1900 | $731.8100 | $-182.42 | -2.04% | RISING | Time | 26 |
| 2025-08-02 05:00:00 | 2025-08-03 07:00:00 | LONG | $766.1600 | $748.0600 | $-207.53 | -2.36% | FALLING | Time | 26 |
| 2025-08-24 01:00:00 | 2025-08-25 03:00:00 | LONG | $882.2700 | $876.2000 | $-59.15 | -0.69% | FALLING | Time | 26 |

## Analysis

**Winner: 9 Periods Strategy**

The 9-period exit strategy outperformed with -4.26% return vs -5.06%.

---
*Báo cáo được tạo tự động bởi Wedge Pattern Backtest System*
