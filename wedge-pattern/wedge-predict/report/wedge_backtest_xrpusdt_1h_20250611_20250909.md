# Wedge Pattern Strategy Comparison - XRPUSDT 1h

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
| Total Trades | 5 | 5 |
| Win Rate | 60.00% | 100.00% |
| Total Return | 1.75% | 12.78% |
| Final Capital | $10175.09 | $11278.21 |
| Total PnL | $175.09 | $1278.21 |
| Average PnL per Trade | $35.02 | $255.64 |
| Best Trade | $202.42 | $356.66 |
| Worst Trade | $-42.76 | $108.12 |
| Long Trades | 4 | 4 |
| Short Trades | 1 | 1 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-06-13 09:00:00 | 2025-06-13 18:00:00 | LONG | $2.1326 | $2.1329 | $1.27 | 0.01% | FALLING | Time | 9 |
| 2025-07-15 14:00:00 | 2025-07-15 23:00:00 | LONG | $2.8548 | $2.9190 | $202.42 | 2.25% | FALLING | Time | 9 |
| 2025-08-17 13:00:00 | 2025-08-17 22:00:00 | SHORT | $3.1281 | $3.1107 | $51.08 | 0.56% | RISING | Time | 9 |
| 2025-08-20 05:00:00 | 2025-08-20 14:00:00 | LONG | $2.9003 | $2.8887 | $-36.91 | -0.40% | FALLING | Time | 9 |
| 2025-08-30 00:00:00 | 2025-08-30 09:00:00 | LONG | $2.8172 | $2.8041 | $-42.76 | -0.47% | FALLING | Time | 9 |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-06-13 09:00:00 | 2025-06-14 11:00:00 | LONG | $2.1326 | $2.1769 | $186.95 | 2.08% | FALLING | Time | 26 |
| 2025-07-15 14:00:00 | 2025-07-16 08:00:00 | LONG | $2.8548 | $2.9567 | $327.25 | 3.57% | FALLING | TP | 18 |
| 2025-08-17 13:00:00 | 2025-08-18 02:00:00 | SHORT | $3.1281 | $3.0102 | $356.66 | 3.77% | RISING | TP | 13 |
| 2025-08-20 05:00:00 | 2025-08-20 19:00:00 | LONG | $2.9003 | $2.9890 | $299.22 | 3.06% | FALLING | TP | 14 |
| 2025-08-30 00:00:00 | 2025-08-31 02:00:00 | LONG | $2.8172 | $2.8475 | $108.12 | 1.08% | FALLING | Time | 26 |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 12.78% return vs 1.75%.

---
*Báo cáo được tạo tự động bởi Wedge Pattern Backtest System*
