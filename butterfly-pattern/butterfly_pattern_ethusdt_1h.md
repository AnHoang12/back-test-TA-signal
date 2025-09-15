# Butterfly Pattern Strategy Comparison - ETHUSDT 1h

## Strategy Overview
- **Pattern**: Butterfly Pattern (Bullish & Bearish)
- **Entry**: At close price when pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods

- **Take Profit**: 5.0%

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 19 | 18 |
| Win Rate | 68.42% | 50.00% |
| Total Return | 10.91% | -1.46% |
| Final Capital | $1109.10 | $985.42 |
| Total PnL | $109.10 | $-14.58 |
| Average PnL per Trade | $5.74 | $-0.81 |
| Best Trade | $26.97 | $39.61 |
| Worst Trade | $-15.86 | $-55.41 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-06-18 21:00 | 2025-06-19 06:00 | SHORT | $2528.3600 | $2519.0400 | $3.50 | 0.37% | Bearish Butterfly | Time |
| 2025-06-19 06:00 | 2025-06-19 15:00 | SHORT | $2519.0400 | $2492.9700 | $9.87 | 1.03% | Bearish Butterfly | Time |
| 2025-06-20 23:00 | 2025-06-21 08:00 | LONG | $2406.4900 | $2441.5600 | $14.03 | 1.46% | Bullish Butterfly | Time |
| 2025-06-22 13:00 | 2025-06-22 22:00 | SHORT | $2199.9300 | $2233.8100 | $-15.03 | -1.54% | Bearish Butterfly | Time |
| 2025-06-25 03:00 | 2025-06-25 12:00 | SHORT | $2444.3800 | $2428.8900 | $6.09 | 0.63% | Bearish Butterfly | Time |
| 2025-07-01 02:00 | 2025-07-01 11:00 | SHORT | $2483.5400 | $2449.0600 | $13.43 | 1.39% | Bearish Butterfly | Time |
| 2025-07-03 13:00 | 2025-07-03 22:00 | LONG | $2624.6800 | $2593.6800 | $-11.58 | -1.18% | Bullish Butterfly | Time |
| 2025-07-05 16:00 | 2025-07-06 01:00 | LONG | $2505.6500 | $2517.8500 | $4.72 | 0.49% | Bullish Butterfly | Time |
| 2025-07-08 03:00 | 2025-07-08 12:00 | LONG | $2538.3400 | $2583.0700 | $17.16 | 1.76% | Bullish Butterfly | Time |
| 2025-07-12 05:00 | 2025-07-12 14:00 | LONG | $2952.8100 | $2928.3000 | $-8.22 | -0.83% | Bullish Butterfly | Time |
| 2025-07-13 20:00 | 2025-07-14 05:00 | SHORT | $2991.9100 | $3040.2300 | $-15.86 | -1.62% | Bearish Butterfly | Time |
| 2025-07-19 05:00 | 2025-07-19 14:00 | SHORT | $3586.3100 | $3531.5700 | $14.76 | 1.53% | Bearish Butterfly | Time |
| 2025-07-29 21:00 | 2025-07-30 06:00 | LONG | $3781.1400 | $3824.9500 | $11.37 | 1.16% | Bullish Butterfly | Time |
| 2025-08-16 08:00 | 2025-08-16 17:00 | SHORT | $4442.6100 | $4404.3500 | $8.54 | 0.86% | Bearish Butterfly | Time |
| 2025-08-24 05:00 | 2025-08-24 14:00 | SHORT | $4783.8600 | $4795.0000 | $-2.33 | -0.23% | Bearish Butterfly | Time |
| 2025-08-26 13:00 | 2025-08-26 22:00 | LONG | $4480.2800 | $4601.3800 | $26.97 | 2.70% | Bullish Butterfly | Time |
| 2025-08-31 19:00 | 2025-09-01 04:00 | SHORT | $4456.0100 | $4385.6500 | $16.16 | 1.58% | Bearish Butterfly | Time |
| 2025-09-03 03:00 | 2025-09-03 12:00 | SHORT | $4335.0200 | $4353.9600 | $-4.54 | -0.44% | Bearish Butterfly | Time |
| 2025-09-05 01:00 | 2025-09-05 10:00 | LONG | $4326.1900 | $4409.9900 | $20.04 | 1.94% | Bullish Butterfly | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-06-18 21:00 | 2025-06-19 23:00 | SHORT | $2528.3600 | $2521.1200 | $2.72 | 0.29% | Bearish Butterfly | Time |
| 2025-06-20 23:00 | 2025-06-22 01:00 | LONG | $2406.4900 | $2266.5000 | $-55.41 | -5.82% | Bullish Butterfly | Time |
| 2025-06-22 13:00 | 2025-06-23 15:00 | SHORT | $2199.9300 | $2248.5400 | $-19.89 | -2.21% | Bearish Butterfly | Time |
| 2025-06-25 03:00 | 2025-06-26 05:00 | SHORT | $2444.3800 | $2475.5900 | $-11.25 | -1.28% | Bearish Butterfly | Time |
| 2025-07-01 02:00 | 2025-07-02 04:00 | SHORT | $2483.5400 | $2439.5600 | $15.41 | 1.77% | Bearish Butterfly | Time |
| 2025-07-03 13:00 | 2025-07-04 15:00 | LONG | $2624.6800 | $2500.5200 | $-41.87 | -4.73% | Bullish Butterfly | Time |
| 2025-07-05 16:00 | 2025-07-06 18:00 | LONG | $2505.6500 | $2532.0200 | $8.90 | 1.05% | Bullish Butterfly | Time |
| 2025-07-08 03:00 | 2025-07-09 05:00 | LONG | $2538.3400 | $2628.2100 | $30.22 | 3.54% | Bullish Butterfly | Time |
| 2025-07-12 05:00 | 2025-07-13 07:00 | LONG | $2952.8100 | $2962.9400 | $3.03 | 0.34% | Bullish Butterfly | Time |
| 2025-07-13 20:00 | 2025-07-14 22:00 | SHORT | $2991.9100 | $3013.6100 | $-6.42 | -0.73% | Bearish Butterfly | Time |
| 2025-07-19 05:00 | 2025-07-20 07:00 | SHORT | $3586.3100 | $3668.4900 | $-20.15 | -2.29% | Bearish Butterfly | Time |
| 2025-07-29 21:00 | 2025-07-30 23:00 | LONG | $3781.1400 | $3810.0000 | $6.56 | 0.76% | Bullish Butterfly | Time |
| 2025-08-16 08:00 | 2025-08-17 10:00 | SHORT | $4442.6100 | $4568.6300 | $-24.57 | -2.84% | Bearish Butterfly | Time |
| 2025-08-24 05:00 | 2025-08-25 07:00 | SHORT | $4783.8600 | $4591.3600 | $33.92 | 4.02% | Bearish Butterfly | Time |
| 2025-08-26 13:00 | 2025-08-27 15:00 | LONG | $4480.2800 | $4657.5700 | $34.63 | 3.96% | Bullish Butterfly | Time |
| 2025-08-31 19:00 | 2025-09-01 21:00 | SHORT | $4456.0100 | $4261.6200 | $39.61 | 4.36% | Bearish Butterfly | Time |
| 2025-09-03 03:00 | 2025-09-04 05:00 | SHORT | $4335.0200 | $4375.2900 | $-8.78 | -0.93% | Bearish Butterfly | Time |
| 2025-09-05 01:00 | 2025-09-06 03:00 | LONG | $4326.1900 | $4320.4200 | $-1.25 | -0.13% | Bullish Butterfly | Time |

## Analysis

**Winner: 9 Periods Strategy**

The 9-period exit strategy outperformed with 10.91% return vs -1.46%.

### Key Observations:
- **Trade Frequency**: 19 vs 18 trades
- **Win Rate Difference**: 68.42% vs 50.00%
- **Return Difference**: 12.37% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
