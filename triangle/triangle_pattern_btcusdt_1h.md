# Triangle Pattern Strategy Comparison - BTCUSDT 1h

## Strategy Overview
- **Pattern**: Triangle Pattern (Ascending & Descending)
- **Entry**: At close price when pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods

- **Take Profit**: 5.0%

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 4 | 4 |
| Win Rate | 100.00% | 75.00% |
| Total Return | 2.50% | 6.76% |
| Final Capital | $1024.97 | $1067.63 |
| Total PnL | $24.97 | $67.63 |
| Average PnL per Trade | $6.24 | $16.91 |
| Best Trade | $9.33 | $33.33 |
| Worst Trade | $3.51 | $-4.15 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-06-23 08:00 | 2025-06-23 17:00 | LONG | $101881.3700 | $102484.0200 | $5.62 | 0.59% | Triangle UP | Time |
| 2025-07-13 08:00 | 2025-07-13 17:00 | LONG | $117895.7800 | $118699.6000 | $6.51 | 0.68% | Triangle UP | Time |
| 2025-07-16 11:00 | 2025-07-16 20:00 | LONG | $118769.0600 | $119921.9600 | $9.33 | 0.97% | Triangle UP | Time |
| 2025-07-26 03:00 | 2025-07-26 12:00 | LONG | $117489.6200 | $117914.1700 | $3.51 | 0.36% | Triangle UP | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-06-23 08:00 | 2025-06-24 10:00 | LONG | $101881.3700 | $105281.9900 | $31.71 | 3.34% | Triangle UP | Time |
| 2025-07-13 08:00 | 2025-07-14 10:00 | LONG | $117895.7800 | $121905.4800 | $33.33 | 3.40% | Triangle UP | Time |
| 2025-07-16 11:00 | 2025-07-17 13:00 | LONG | $118769.0600 | $118281.9900 | $-4.15 | -0.41% | Triangle UP | Time |
| 2025-07-26 03:00 | 2025-07-27 05:00 | LONG | $117489.6200 | $118274.7300 | $6.73 | 0.67% | Triangle UP | Time |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 6.76% return vs 2.50%.

### Key Observations:
- **Trade Frequency**: 4 vs 4 trades
- **Win Rate Difference**: 100.00% vs 75.00%
- **Return Difference**: 4.27% gap

---
*Báo cáo được tạo tự động bởi Triangle Pattern Backtest System*
