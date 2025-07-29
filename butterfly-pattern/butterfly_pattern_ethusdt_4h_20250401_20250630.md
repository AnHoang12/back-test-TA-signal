# Butterfly Pattern Strategy Comparison - ETHUSDT 4h

## Strategy Overview
- **Pattern**: Butterfly Pattern (Bullish & Bearish)
- **Entry**: At close price when pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods

- **Take Profit**: 5.0%

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 6 | 6 |
| Win Rate | 50.00% | 33.33% |
| Total Return | 10.66% | 7.96% |
| Final Capital | $1106.63 | $1079.62 |
| Total PnL | $106.63 | $79.62 |
| Average PnL per Trade | $17.77 | $13.27 |
| Best Trade | $90.60 | $90.60 |
| Worst Trade | $-33.71 | $-54.68 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-06 04:00 | 2025-04-06 16:00 | SHORT | $1797.6900 | $1626.2400 | $90.60 | 9.54% | Bearish Butterfly | TP |
| 2025-04-25 16:00 | 2025-04-27 04:00 | SHORT | $1802.1600 | $1803.7600 | $-0.92 | -0.09% | Bearish Butterfly | Time |
| 2025-06-02 12:00 | 2025-06-04 00:00 | LONG | $2544.3900 | $2627.9000 | $33.98 | 3.28% | Bullish Butterfly | Time |
| 2025-06-07 04:00 | 2025-06-08 16:00 | LONG | $2491.2800 | $2532.5600 | $17.69 | 1.66% | Bullish Butterfly | Time |
| 2025-06-19 20:00 | 2025-06-21 08:00 | LONG | $2521.1200 | $2442.7500 | $-33.71 | -3.11% | Bullish Butterfly | Time |
| 2025-06-28 20:00 | 2025-06-29 16:00 | SHORT | $2435.6200 | $2437.9600 | $-1.01 | -0.10% | Bearish Butterfly | End |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-06 04:00 | 2025-04-06 16:00 | SHORT | $1797.6900 | $1626.2400 | $90.60 | 9.54% | Bearish Butterfly | TP |
| 2025-04-25 16:00 | 2025-04-30 00:00 | SHORT | $1802.1600 | $1808.9100 | $-3.88 | -0.37% | Bearish Butterfly | Time |
| 2025-06-02 12:00 | 2025-06-06 20:00 | LONG | $2544.3900 | $2476.1000 | $-27.71 | -2.68% | Bullish Butterfly | Time |
| 2025-06-07 04:00 | 2025-06-09 20:00 | LONG | $2491.2800 | $2680.1300 | $76.26 | 7.58% | Bullish Butterfly | TP |
| 2025-06-19 20:00 | 2025-06-24 04:00 | LONG | $2521.1200 | $2393.3100 | $-54.68 | -5.07% | Bullish Butterfly | Time |
| 2025-06-28 20:00 | 2025-06-29 16:00 | SHORT | $2435.6200 | $2437.9600 | $-0.99 | -0.10% | Bearish Butterfly | End |

## Analysis

**Winner: 9 Periods Strategy**

The 9-period exit strategy outperformed with 10.66% return vs 7.96%.

### Key Observations:
- **Trade Frequency**: 6 vs 6 trades
- **Win Rate Difference**: 50.00% vs 33.33%
- **Return Difference**: 2.70% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
