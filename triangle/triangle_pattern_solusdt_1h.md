# Triangle Pattern Strategy Comparison - SOLUSDT 1h

## Strategy Overview
- **Pattern**: Triangle Pattern (Ascending & Descending)
- **Entry**: At close price when pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods

- **Take Profit**: 5.0%

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 2 | 2 |
| Win Rate | 0.00% | 50.00% |
| Total Return | -3.27% | 0.32% |
| Final Capital | $967.26 | $1003.17 |
| Total PnL | $-32.74 | $3.17 |
| Average PnL per Trade | $-16.37 | $1.58 |
| Best Trade | $-11.29 | $26.99 |
| Worst Trade | $-21.45 | $-23.82 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-07-03 16:00 | 2025-07-04 01:00 | SHORT | $150.6600 | $152.4500 | $-11.29 | -1.19% | Triangle DOWN | Time |
| 2025-08-15 19:00 | 2025-08-16 04:00 | SHORT | $183.8900 | $188.0900 | $-21.45 | -2.28% | Triangle DOWN | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-07-03 16:00 | 2025-07-04 18:00 | SHORT | $150.6600 | $146.3800 | $26.99 | 2.84% | Triangle DOWN | Time |
| 2025-08-15 19:00 | 2025-08-16 21:00 | SHORT | $183.8900 | $188.3800 | $-23.82 | -2.44% | Triangle DOWN | Time |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 0.32% return vs -3.27%.

### Key Observations:
- **Trade Frequency**: 2 vs 2 trades
- **Win Rate Difference**: 0.00% vs 50.00%
- **Return Difference**: 3.59% gap

---
*Báo cáo được tạo tự động bởi Triangle Pattern Backtest System*
