# Triangle Pattern Strategy Comparison - ETHUSDT 1h

## Strategy Overview
- **Pattern**: Triangle Pattern (Ascending & Descending)
- **Entry**: At close price when pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods

- **Take Profit**: 5.0%

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 5 | 5 |
| Win Rate | 40.00% | 80.00% |
| Total Return | 3.71% | 11.31% |
| Final Capital | $1037.15 | $1113.10 |
| Total PnL | $37.15 | $113.10 |
| Average PnL per Trade | $7.43 | $22.62 |
| Best Trade | $45.98 | $52.83 |
| Worst Trade | $-5.75 | $-28.77 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-07-13 07:00 | 2025-07-13 16:00 | LONG | $2962.9400 | $2974.5800 | $3.73 | 0.39% | Triangle UP | Time |
| 2025-07-16 08:00 | 2025-07-16 17:00 | LONG | $3164.4900 | $3317.0900 | $45.98 | 4.82% | Triangle UP | Time |
| 2025-07-30 08:00 | 2025-07-30 17:00 | LONG | $3815.6500 | $3805.1400 | $-2.75 | -0.28% | Triangle UP | Time |
| 2025-08-05 16:00 | 2025-08-06 01:00 | SHORT | $3577.6700 | $3592.3100 | $-4.07 | -0.41% | Triangle DOWN | Time |
| 2025-08-06 19:00 | 2025-08-07 04:00 | LONG | $3683.6500 | $3662.2700 | $-5.75 | -0.58% | Triangle UP | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-07-13 07:00 | 2025-07-14 09:00 | LONG | $2962.9400 | $3044.7100 | $26.22 | 2.76% | Triangle UP | Time |
| 2025-07-16 08:00 | 2025-07-16 18:00 | LONG | $3164.4900 | $3335.9800 | $52.83 | 5.42% | Triangle UP | TP |
| 2025-07-30 08:00 | 2025-07-31 10:00 | LONG | $3815.6500 | $3855.4800 | $10.70 | 1.04% | Triangle UP | Time |
| 2025-08-05 16:00 | 2025-08-06 18:00 | SHORT | $3577.6700 | $3677.0900 | $-28.77 | -2.78% | Triangle DOWN | Time |
| 2025-08-06 19:00 | 2025-08-07 20:00 | LONG | $3683.6500 | $3874.1400 | $52.12 | 5.17% | Triangle UP | TP |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 11.31% return vs 3.71%.

### Key Observations:
- **Trade Frequency**: 5 vs 5 trades
- **Win Rate Difference**: 40.00% vs 80.00%
- **Return Difference**: 7.60% gap

---
*Báo cáo được tạo tự động bởi Triangle Pattern Backtest System*
