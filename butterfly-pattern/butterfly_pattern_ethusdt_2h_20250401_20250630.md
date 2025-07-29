# Butterfly Pattern Strategy Comparison - ETHUSDT 2h

## Strategy Overview
- **Pattern**: Butterfly Pattern (Bullish & Bearish)
- **Entry**: At close price when pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods

- **Take Profit**: 5.0%

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 13 | 11 |
| Win Rate | 53.85% | 54.55% |
| Total Return | 11.87% | 13.78% |
| Final Capital | $1118.70 | $1137.80 |
| Total PnL | $118.70 | $137.80 |
| Average PnL per Trade | $9.13 | $12.53 |
| Best Trade | $66.12 | $66.94 |
| Worst Trade | $-48.86 | $-98.60 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-08 04:00 | 2025-04-08 16:00 | SHORT | $1591.8300 | $1481.0400 | $66.12 | 6.96% | Bearish Butterfly | TP |
| 2025-04-10 18:00 | 2025-04-11 12:00 | LONG | $1514.6700 | $1570.6100 | $37.41 | 3.69% | Bullish Butterfly | Time |
| 2025-04-11 18:00 | 2025-04-12 12:00 | SHORT | $1565.7900 | $1638.7600 | $-48.86 | -4.66% | Bearish Butterfly | Time |
| 2025-04-17 16:00 | 2025-04-18 10:00 | LONG | $1610.0400 | $1590.6700 | $-12.05 | -1.20% | Bullish Butterfly | Time |
| 2025-04-26 02:00 | 2025-04-26 20:00 | SHORT | $1797.4800 | $1812.0500 | $-8.03 | -0.81% | Bearish Butterfly | Time |
| 2025-05-04 22:00 | 2025-05-05 16:00 | SHORT | $1808.8600 | $1814.5100 | $-3.07 | -0.31% | Bearish Butterfly | Time |
| 2025-05-05 16:00 | 2025-05-06 10:00 | LONG | $1814.5100 | $1769.9200 | $-24.08 | -2.46% | Bullish Butterfly | Time |
| 2025-05-07 20:00 | 2025-05-08 02:00 | LONG | $1802.7300 | $1901.1000 | $52.22 | 5.46% | Bullish Butterfly | TP |
| 2025-05-24 20:00 | 2025-05-25 14:00 | SHORT | $2540.0900 | $2511.7000 | $11.25 | 1.12% | Bearish Butterfly | Time |
| 2025-05-29 00:00 | 2025-05-29 18:00 | SHORT | $2711.7600 | $2650.1200 | $23.13 | 2.27% | Bearish Butterfly | Time |
| 2025-06-19 18:00 | 2025-06-20 12:00 | LONG | $2504.8700 | $2536.2900 | $13.04 | 1.25% | Bullish Butterfly | Time |
| 2025-06-25 16:00 | 2025-06-26 10:00 | LONG | $2422.8300 | $2450.3600 | $11.95 | 1.14% | Bullish Butterfly | Time |
| 2025-06-28 08:00 | 2025-06-29 02:00 | SHORT | $2427.1200 | $2427.8600 | $-0.32 | -0.03% | Bearish Butterfly | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-08 04:00 | 2025-04-08 16:00 | SHORT | $1591.8300 | $1481.0400 | $66.12 | 6.96% | Bearish Butterfly | TP |
| 2025-04-10 18:00 | 2025-04-12 08:00 | LONG | $1514.6700 | $1597.5000 | $55.39 | 5.47% | Bullish Butterfly | TP |
| 2025-04-17 16:00 | 2025-04-19 20:00 | LONG | $1610.0400 | $1620.7700 | $7.10 | 0.67% | Bullish Butterfly | Time |
| 2025-04-26 02:00 | 2025-04-28 06:00 | SHORT | $1797.4800 | $1804.7900 | $-4.36 | -0.41% | Bearish Butterfly | Time |
| 2025-05-04 22:00 | 2025-05-07 02:00 | SHORT | $1808.8600 | $1826.4800 | $-10.40 | -0.97% | Bearish Butterfly | Time |
| 2025-05-07 20:00 | 2025-05-08 02:00 | LONG | $1802.7300 | $1901.1000 | $57.74 | 5.46% | Bullish Butterfly | TP |
| 2025-05-24 20:00 | 2025-05-27 00:00 | SHORT | $2540.0900 | $2529.6000 | $4.60 | 0.41% | Bearish Butterfly | Time |
| 2025-05-29 00:00 | 2025-05-30 16:00 | SHORT | $2711.7600 | $2549.3100 | $66.94 | 5.99% | Bearish Butterfly | TP |
| 2025-06-19 18:00 | 2025-06-21 22:00 | LONG | $2504.8700 | $2295.7300 | $-98.60 | -8.35% | Bullish Butterfly | Time |
| 2025-06-25 16:00 | 2025-06-27 20:00 | LONG | $2422.8300 | $2419.8500 | $-1.34 | -0.12% | Bullish Butterfly | Time |
| 2025-06-28 08:00 | 2025-06-29 16:00 | SHORT | $2427.1200 | $2439.1400 | $-5.38 | -0.50% | Bearish Butterfly | End |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 13.78% return vs 11.87%.

### Key Observations:
- **Trade Frequency**: 13 vs 11 trades
- **Win Rate Difference**: 53.85% vs 54.55%
- **Return Difference**: 1.91% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
