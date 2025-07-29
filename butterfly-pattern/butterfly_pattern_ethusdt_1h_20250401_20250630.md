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
| Total Trades | 21 | 19 |
| Win Rate | 57.14% | 47.37% |
| Total Return | -4.07% | -9.43% |
| Final Capital | $959.25 | $905.66 |
| Total PnL | $-40.75 | $-94.34 |
| Average PnL per Trade | $-1.94 | $-4.97 |
| Best Trade | $46.05 | $56.57 |
| Worst Trade | $-93.79 | $-172.59 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-01 22:00 | 2025-04-02 07:00 | SHORT | $1911.9000 | $1865.0600 | $23.27 | 2.45% | Bearish Butterfly | Time |
| 2025-04-06 09:00 | 2025-04-06 18:00 | LONG | $1791.0800 | $1618.2800 | $-93.79 | -9.65% | Bullish Butterfly | Time |
| 2025-04-08 13:00 | 2025-04-08 16:00 | SHORT | $1568.5900 | $1486.7900 | $46.05 | 5.21% | Bearish Butterfly | TP |
| 2025-04-11 22:00 | 2025-04-12 07:00 | SHORT | $1566.3800 | $1582.0500 | $-9.27 | -1.00% | Bearish Butterfly | Time |
| 2025-04-24 00:00 | 2025-04-24 09:00 | SHORT | $1789.8900 | $1743.5000 | $23.79 | 2.59% | Bearish Butterfly | Time |
| 2025-04-30 08:00 | 2025-04-30 17:00 | LONG | $1795.2400 | $1775.5300 | $-10.33 | -1.10% | Bullish Butterfly | Time |
| 2025-05-04 21:00 | 2025-05-05 06:00 | SHORT | $1835.4100 | $1820.3600 | $7.63 | 0.82% | Bearish Butterfly | Time |
| 2025-05-05 21:00 | 2025-05-06 06:00 | LONG | $1816.7500 | $1806.3800 | $-5.35 | -0.57% | Bullish Butterfly | Time |
| 2025-05-12 14:00 | 2025-05-12 23:00 | SHORT | $2505.9400 | $2495.4700 | $3.90 | 0.42% | Bearish Butterfly | Time |
| 2025-05-23 01:00 | 2025-05-23 10:00 | SHORT | $2675.6200 | $2671.5500 | $1.42 | 0.15% | Bearish Butterfly | Time |
| 2025-05-24 19:00 | 2025-05-25 04:00 | SHORT | $2554.4700 | $2517.5000 | $13.57 | 1.45% | Bearish Butterfly | Time |
| 2025-05-28 18:00 | 2025-05-29 03:00 | SHORT | $2636.1700 | $2762.5000 | $-45.57 | -4.79% | Bearish Butterfly | Time |
| 2025-06-01 01:00 | 2025-06-01 10:00 | LONG | $2507.2900 | $2493.6000 | $-4.96 | -0.55% | Bullish Butterfly | Time |
| 2025-06-02 04:00 | 2025-06-02 13:00 | LONG | $2492.5900 | $2504.6700 | $4.38 | 0.48% | Bullish Butterfly | Time |
| 2025-06-03 08:00 | 2025-06-03 17:00 | SHORT | $2607.2900 | $2619.1100 | $-4.11 | -0.45% | Bearish Butterfly | Time |
| 2025-06-07 12:00 | 2025-06-07 21:00 | SHORT | $2497.8500 | $2522.1300 | $-8.78 | -0.97% | Bearish Butterfly | Time |
| 2025-06-18 21:00 | 2025-06-19 06:00 | SHORT | $2528.3600 | $2519.0400 | $3.30 | 0.37% | Bearish Butterfly | Time |
| 2025-06-19 06:00 | 2025-06-19 15:00 | SHORT | $2519.0400 | $2492.9700 | $9.29 | 1.03% | Bearish Butterfly | Time |
| 2025-06-20 23:00 | 2025-06-21 08:00 | LONG | $2406.4900 | $2441.5600 | $13.21 | 1.46% | Bullish Butterfly | Time |
| 2025-06-22 13:00 | 2025-06-22 22:00 | SHORT | $2199.9300 | $2233.8100 | $-14.16 | -1.54% | Bearish Butterfly | Time |
| 2025-06-25 03:00 | 2025-06-25 12:00 | SHORT | $2444.3800 | $2428.8900 | $5.74 | 0.63% | Bearish Butterfly | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-01 22:00 | 2025-04-02 22:00 | SHORT | $1911.9000 | $1798.0500 | $56.57 | 5.95% | Bearish Butterfly | TP |
| 2025-04-06 09:00 | 2025-04-07 11:00 | LONG | $1791.0800 | $1483.1100 | $-172.59 | -17.19% | Bullish Butterfly | Time |
| 2025-04-08 13:00 | 2025-04-08 16:00 | SHORT | $1568.5900 | $1486.7900 | $43.79 | 5.21% | Bearish Butterfly | TP |
| 2025-04-11 22:00 | 2025-04-13 00:00 | SHORT | $1566.3800 | $1642.1000 | $-42.61 | -4.83% | Bearish Butterfly | Time |
| 2025-04-24 00:00 | 2025-04-25 02:00 | SHORT | $1789.8900 | $1744.6100 | $21.27 | 2.53% | Bearish Butterfly | Time |
| 2025-04-30 08:00 | 2025-05-01 10:00 | LONG | $1795.2400 | $1847.6100 | $25.12 | 2.92% | Bullish Butterfly | Time |
| 2025-05-04 21:00 | 2025-05-05 23:00 | SHORT | $1835.4100 | $1820.1900 | $7.34 | 0.83% | Bearish Butterfly | Time |
| 2025-05-12 14:00 | 2025-05-13 16:00 | SHORT | $2505.9400 | $2597.5000 | $-32.59 | -3.65% | Bearish Butterfly | Time |
| 2025-05-23 01:00 | 2025-05-23 21:00 | SHORT | $2675.6200 | $2534.3000 | $45.48 | 5.28% | Bearish Butterfly | TP |
| 2025-05-24 19:00 | 2025-05-25 21:00 | SHORT | $2554.4700 | $2515.1900 | $13.90 | 1.54% | Bearish Butterfly | Time |
| 2025-05-28 18:00 | 2025-05-29 20:00 | SHORT | $2636.1700 | $2643.9800 | $-2.72 | -0.30% | Bearish Butterfly | Time |
| 2025-06-01 01:00 | 2025-06-02 03:00 | LONG | $2507.2900 | $2496.3100 | $-4.01 | -0.44% | Bullish Butterfly | Time |
| 2025-06-02 04:00 | 2025-06-03 00:00 | LONG | $2492.5900 | $2621.9100 | $47.27 | 5.19% | Bullish Butterfly | TP |
| 2025-06-03 08:00 | 2025-06-04 10:00 | SHORT | $2607.2900 | $2638.4500 | $-11.42 | -1.20% | Bearish Butterfly | Time |
| 2025-06-07 12:00 | 2025-06-08 14:00 | SHORT | $2497.8500 | $2514.4500 | $-6.28 | -0.66% | Bearish Butterfly | Time |
| 2025-06-18 21:00 | 2025-06-19 23:00 | SHORT | $2528.3600 | $2521.1200 | $2.69 | 0.29% | Bearish Butterfly | Time |
| 2025-06-20 23:00 | 2025-06-22 01:00 | LONG | $2406.4900 | $2266.5000 | $-54.78 | -5.82% | Bullish Butterfly | Time |
| 2025-06-22 13:00 | 2025-06-23 15:00 | SHORT | $2199.9300 | $2248.5400 | $-19.66 | -2.21% | Bearish Butterfly | Time |
| 2025-06-25 03:00 | 2025-06-26 05:00 | SHORT | $2444.3800 | $2475.5900 | $-11.12 | -1.28% | Bearish Butterfly | Time |

## Analysis

**Winner: 9 Periods Strategy**

The 9-period exit strategy outperformed with -4.07% return vs -9.43%.

### Key Observations:
- **Trade Frequency**: 21 vs 19 trades
- **Win Rate Difference**: 57.14% vs 47.37%
- **Return Difference**: 5.36% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
