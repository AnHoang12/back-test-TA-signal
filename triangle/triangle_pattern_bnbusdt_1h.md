# Triangle Pattern Strategy Comparison - BNBUSDT 1h

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
| Win Rate | 100.00% | 100.00% |
| Total Return | 1.46% | 2.92% |
| Final Capital | $1014.57 | $1029.17 |
| Total PnL | $14.57 | $29.17 |
| Average PnL per Trade | $7.28 | $14.59 |
| Best Trade | $10.22 | $14.61 |
| Worst Trade | $4.35 | $14.56 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-08-01 09:00 | 2025-08-01 18:00 | SHORT | $768.1000 | $759.8400 | $10.22 | 1.08% | Triangle DOWN | Time |
| 2025-08-03 12:00 | 2025-08-03 21:00 | LONG | $749.8100 | $753.2100 | $4.35 | 0.45% | Triangle UP | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-08-01 09:00 | 2025-08-02 11:00 | SHORT | $768.1000 | $756.2900 | $14.61 | 1.54% | Triangle DOWN | Time |
| 2025-08-03 12:00 | 2025-08-04 14:00 | LONG | $749.8100 | $761.1400 | $14.56 | 1.51% | Triangle UP | Time |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 2.92% return vs 1.46%.

### Key Observations:
- **Trade Frequency**: 2 vs 2 trades
- **Win Rate Difference**: 100.00% vs 100.00%
- **Return Difference**: 1.46% gap

---
*Báo cáo được tạo tự động bởi Triangle Pattern Backtest System*
