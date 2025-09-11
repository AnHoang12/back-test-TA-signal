# Triple Pattern Strategy Comparison - Multi Position - SOLUSDT 6h

## Strategy Overview
- **Pattern**: Triple Top & Triple Bottom Pattern
- **Entry**: Breakout/breakdown with reversal candles
- **Reversal Candles**: Hammer, Engulfing, Doji patterns
- **Position Management**: Up to 3 positions at a time
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods
- **Take Profit**: 5.0%
- **Position Size**: 20.0% of capital per position

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 47 | 32 |
| Win Rate | 44.68% | 53.12% |
| Total Return | -9.31% | -8.60% |
| Final Capital | $906.87 | $913.95 |
| Total PnL | $-93.13 | $-86.05 |
| Average PnL per Trade | $-1.98 | $-2.69 |
| Best Trade | $11.57 | $11.17 |
| Worst Trade | $-23.08 | $-40.80 |
| Long Trades | 32 | 20 |
| Short Trades | 15 | 12 |
| Max Concurrent Positions | 3 | 3 |

## Strategy 1: Exit after 9 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-04-16 12:00 | 2025-04-18 18:00 | SHORT | $125.1500 | $134.0400 | $-14.21 | -7.10% | triple_top_breakdown | Time | 9 |
| 1 | 2025-04-17 06:00 | 2025-04-19 12:00 | LONG | $133.1200 | $138.9000 | $6.95 | 4.34% | triple_bottom_breakout | Time | 9 |
| 3 | 2025-04-18 18:00 | 2025-04-20 00:00 | LONG | $134.0400 | $140.7700 | $7.01 | 5.02% | triple_bottom_breakout | TP | 5 |
| 2 | 2025-04-18 06:00 | 2025-04-20 12:00 | LONG | $134.2700 | $136.3700 | $2.00 | 1.56% | triple_bottom_breakout | Time | 9 |
| 4 | 2025-04-19 12:00 | 2025-04-21 18:00 | LONG | $138.9000 | $136.5600 | $-2.44 | -1.68% | triple_bottom_breakout | Time | 9 |
| 5 | 2025-04-20 12:00 | 2025-04-22 12:00 | LONG | $136.3700 | $144.7300 | $10.50 | 6.13% | triple_bottom_breakout | TP | 8 |
| 6 | 2025-04-20 18:00 | 2025-04-22 18:00 | LONG | $137.8600 | $148.7900 | $10.87 | 7.93% | triple_bottom_breakout | TP | 8 |
| 7 | 2025-04-25 18:00 | 2025-04-28 00:00 | LONG | $150.8200 | $149.7400 | $-1.46 | -0.72% | triple_bottom_breakout | Time | 9 |
| 8 | 2025-04-26 00:00 | 2025-04-28 06:00 | LONG | $151.0000 | $151.7000 | $0.76 | 0.46% | triple_bottom_breakout | Time | 9 |
| 9 | 2025-04-26 18:00 | 2025-04-29 00:00 | LONG | $149.2100 | $146.6400 | $-2.25 | -1.72% | triple_bottom_breakout | Time | 9 |
| 10 | 2025-04-28 00:00 | 2025-04-30 06:00 | LONG | $149.7400 | $147.9400 | $-1.74 | -1.20% | triple_bottom_breakout | Time | 9 |
| 11 | 2025-04-29 06:00 | 2025-05-01 12:00 | LONG | $149.0000 | $151.2800 | $2.67 | 1.53% | triple_bottom_breakout | Time | 9 |
| 12 | 2025-04-29 12:00 | 2025-05-01 18:00 | LONG | $148.7800 | $150.8500 | $1.94 | 1.39% | triple_bottom_breakout | Time | 9 |
| 13 | 2025-05-01 18:00 | 2025-05-04 00:00 | LONG | $150.8500 | $146.2400 | $-6.24 | -3.06% | triple_bottom_breakout | Time | 9 |
| 14 | 2025-05-03 00:00 | 2025-05-05 06:00 | SHORT | $147.7400 | $144.1900 | $3.92 | 2.40% | triple_top_breakdown | Time | 9 |
| 15 | 2025-05-03 18:00 | 2025-05-06 00:00 | SHORT | $146.7100 | $144.5000 | $1.97 | 1.51% | triple_top_breakdown | Time | 9 |
| 16 | 2025-05-09 12:00 | 2025-05-11 18:00 | LONG | $171.9700 | $173.1900 | $1.45 | 0.71% | triple_bottom_breakout | Time | 9 |
| 17 | 2025-05-09 18:00 | 2025-05-12 00:00 | LONG | $172.7800 | $174.5400 | $1.66 | 1.02% | triple_bottom_breakout | Time | 9 |
| 18 | 2025-05-12 06:00 | 2025-05-13 18:00 | LONG | $174.1100 | $183.7500 | $11.33 | 5.54% | triple_bottom_breakout | TP | 6 |
| 19 | 2025-05-14 06:00 | 2025-05-16 12:00 | LONG | $181.0600 | $170.3800 | $-12.21 | -5.90% | triple_bottom_breakout | Time | 9 |
| 20 | 2025-05-15 12:00 | 2025-05-17 18:00 | LONG | $173.1100 | $165.9400 | $-6.86 | -4.14% | triple_bottom_breakout | Time | 9 |
| 21 | 2025-05-16 06:00 | 2025-05-18 12:00 | LONG | $172.8100 | $172.2500 | $-0.43 | -0.32% | triple_bottom_breakout | Time | 9 |
| 24 | 2025-05-18 12:00 | 2025-05-19 00:00 | SHORT | $172.2500 | $162.7000 | $8.01 | 5.54% | triple_top_breakdown | TP | 2 |
| 22 | 2025-05-17 00:00 | 2025-05-19 06:00 | LONG | $167.5000 | $162.1900 | $-4.59 | -3.17% | triple_bottom_breakout | Time | 9 |
| 23 | 2025-05-17 18:00 | 2025-05-20 00:00 | LONG | $165.9400 | $169.2500 | $2.95 | 1.99% | triple_bottom_breakout | Time | 9 |
| 25 | 2025-05-21 12:00 | 2025-05-23 18:00 | SHORT | $167.1300 | $174.0100 | $-8.41 | -4.12% | triple_top_breakdown | Time | 9 |
| 26 | 2025-05-22 18:00 | 2025-05-25 00:00 | LONG | $179.6800 | $174.0200 | $-5.15 | -3.15% | triple_bottom_breakout | Time | 9 |
| 27 | 2025-05-24 12:00 | 2025-05-26 18:00 | LONG | $176.8500 | $174.9100 | $-1.86 | -1.10% | triple_bottom_breakout | Time | 9 |
| 28 | 2025-05-28 06:00 | 2025-05-30 12:00 | LONG | $174.5100 | $158.5700 | $-18.38 | -9.13% | triple_bottom_breakout | Time | 9 |
| 29 | 2025-05-29 00:00 | 2025-05-31 06:00 | LONG | $172.0200 | $152.9200 | $-17.87 | -11.10% | triple_bottom_breakout | Time | 9 |
| 30 | 2025-06-02 12:00 | 2025-06-04 18:00 | SHORT | $153.6700 | $153.2600 | $0.52 | 0.27% | triple_top_breakdown | Time | 9 |
| 33 | 2025-06-05 06:00 | 2025-06-05 18:00 | SHORT | $152.3700 | $144.2900 | $7.33 | 5.30% | triple_top_breakdown | TP | 2 |
| 32 | 2025-06-04 12:00 | 2025-06-05 18:00 | SHORT | $156.0700 | $144.2900 | $9.37 | 7.55% | triple_top_breakdown | TP | 5 |
| 31 | 2025-06-04 06:00 | 2025-06-05 18:00 | SHORT | $155.9200 | $144.2900 | $11.57 | 7.46% | triple_top_breakdown | TP | 6 |
| 34 | 2025-06-06 12:00 | 2025-06-08 18:00 | SHORT | $150.1000 | $152.4500 | $-3.13 | -1.57% | triple_top_breakdown | Time | 9 |
| 35 | 2025-06-07 06:00 | 2025-06-09 12:00 | SHORT | $151.4500 | $156.3100 | $-5.13 | -3.21% | triple_top_breakdown | Time | 9 |
| 36 | 2025-06-08 18:00 | 2025-06-11 00:00 | SHORT | $152.4500 | $164.9400 | $-13.69 | -8.19% | triple_top_breakdown | Time | 9 |
| 37 | 2025-06-11 00:00 | 2025-06-13 06:00 | LONG | $164.9400 | $145.4500 | $-23.08 | -11.82% | triple_bottom_breakout | Time | 9 |
| 38 | 2025-06-14 18:00 | 2025-06-17 00:00 | SHORT | $144.6400 | $153.6100 | $-11.83 | -6.20% | triple_top_breakdown | Time | 9 |
| 39 | 2025-06-15 18:00 | 2025-06-18 00:00 | LONG | $152.9700 | $148.3000 | $-4.66 | -3.05% | triple_bottom_breakout | Time | 9 |
| 40 | 2025-06-16 06:00 | 2025-06-18 12:00 | LONG | $156.4800 | $145.5500 | $-8.53 | -6.98% | triple_bottom_breakout | Time | 9 |
| 41 | 2025-06-17 18:00 | 2025-06-20 00:00 | SHORT | $147.5700 | $145.3400 | $2.02 | 1.51% | triple_top_breakdown | Time | 9 |
| 42 | 2025-06-22 06:00 | 2025-06-24 12:00 | SHORT | $133.2500 | $144.8000 | $-16.13 | -8.67% | triple_top_breakdown | Time | 9 |
| 43 | 2025-06-24 00:00 | 2025-06-26 06:00 | LONG | $145.4900 | $143.6500 | $-1.88 | -1.26% | triple_bottom_breakout | Time | 9 |
| 44 | 2025-06-24 12:00 | 2025-06-26 18:00 | LONG | $144.8000 | $139.0600 | $-6.07 | -3.96% | triple_bottom_breakout | Time | 9 |
| 45 | 2025-06-25 18:00 | 2025-06-28 00:00 | LONG | $143.5700 | $143.9300 | $0.31 | 0.25% | triple_bottom_breakout | Time | 9 |
| 46 | 2025-06-29 12:00 | 2025-06-29 12:00 | LONG | $151.4300 | $151.4300 | $0.00 | 0.00% | triple_bottom_breakout | End | 0 |

## Strategy 2: Exit after 26 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 1 | 2025-04-17 06:00 | 2025-04-19 18:00 | LONG | $133.1200 | $139.8700 | $8.11 | 5.07% | triple_bottom_breakout | TP | 10 |
| 3 | 2025-04-20 12:00 | 2025-04-22 12:00 | LONG | $136.3700 | $144.7300 | $8.34 | 6.13% | triple_bottom_breakout | TP | 8 |
| 2 | 2025-04-18 06:00 | 2025-04-22 12:00 | LONG | $134.2700 | $144.7300 | $9.97 | 7.79% | triple_bottom_breakout | TP | 17 |
| 0 | 2025-04-16 12:00 | 2025-04-23 00:00 | SHORT | $125.1500 | $150.6800 | $-40.80 | -20.40% | triple_top_breakdown | Time | 26 |
| 4 | 2025-04-25 18:00 | 2025-05-02 06:00 | LONG | $150.8200 | $150.7300 | $-0.12 | -0.06% | triple_bottom_breakout | Time | 26 |
| 5 | 2025-04-26 00:00 | 2025-05-02 12:00 | LONG | $151.0000 | $149.8300 | $-1.22 | -0.77% | triple_bottom_breakout | Time | 26 |
| 6 | 2025-04-26 18:00 | 2025-05-03 06:00 | LONG | $149.2100 | $147.1400 | $-1.75 | -1.39% | triple_bottom_breakout | Time | 26 |
| 7 | 2025-05-03 00:00 | 2025-05-09 12:00 | SHORT | $147.7400 | $171.9700 | $-28.15 | -16.40% | triple_top_breakdown | Time | 26 |
| 8 | 2025-05-03 18:00 | 2025-05-10 06:00 | SHORT | $146.7100 | $169.0000 | $-24.64 | -15.19% | triple_top_breakdown | Time | 26 |
| 11 | 2025-05-12 06:00 | 2025-05-13 18:00 | LONG | $174.1100 | $183.7500 | $7.14 | 5.54% | triple_bottom_breakout | TP | 6 |
| 10 | 2025-05-09 18:00 | 2025-05-13 18:00 | LONG | $172.7800 | $183.7500 | $8.05 | 6.35% | triple_bottom_breakout | TP | 16 |
| 9 | 2025-05-09 12:00 | 2025-05-13 18:00 | LONG | $171.9700 | $183.7500 | $10.85 | 6.85% | triple_bottom_breakout | TP | 17 |
| 12 | 2025-05-14 06:00 | 2025-05-20 18:00 | LONG | $181.0600 | $168.5900 | $-13.17 | -6.89% | triple_bottom_breakout | Time | 26 |
| 13 | 2025-05-15 12:00 | 2025-05-22 00:00 | LONG | $173.1100 | $175.8600 | $2.43 | 1.59% | triple_bottom_breakout | Time | 26 |
| 14 | 2025-05-16 06:00 | 2025-05-22 18:00 | LONG | $172.8100 | $179.6800 | $4.86 | 3.98% | triple_bottom_breakout | Time | 26 |
| 15 | 2025-05-21 12:00 | 2025-05-28 00:00 | SHORT | $167.1300 | $174.6000 | $-5.97 | -4.47% | triple_top_breakdown | Time | 26 |
| 16 | 2025-05-22 18:00 | 2025-05-29 06:00 | LONG | $179.6800 | $172.8800 | $-6.18 | -3.78% | triple_bottom_breakout | Time | 26 |
| 17 | 2025-05-24 12:00 | 2025-05-31 00:00 | LONG | $176.8500 | $154.2300 | $-16.71 | -12.79% | triple_bottom_breakout | Time | 26 |
| 18 | 2025-05-28 06:00 | 2025-06-03 18:00 | LONG | $174.5100 | $155.1900 | $-14.39 | -11.07% | triple_bottom_breakout | Time | 26 |
| 21 | 2025-06-04 12:00 | 2025-06-05 18:00 | SHORT | $156.0700 | $144.2900 | $9.04 | 7.55% | triple_top_breakdown | TP | 5 |
| 20 | 2025-06-04 06:00 | 2025-06-05 18:00 | SHORT | $155.9200 | $144.2900 | $11.17 | 7.46% | triple_top_breakdown | TP | 6 |
| 19 | 2025-06-02 12:00 | 2025-06-05 18:00 | SHORT | $153.6700 | $144.2900 | $9.66 | 6.10% | triple_top_breakdown | TP | 13 |
| 24 | 2025-06-08 18:00 | 2025-06-13 00:00 | SHORT | $152.4500 | $143.7600 | $6.83 | 5.70% | triple_top_breakdown | TP | 17 |
| 23 | 2025-06-07 06:00 | 2025-06-13 00:00 | SHORT | $151.4500 | $143.7600 | $7.61 | 5.08% | triple_top_breakdown | TP | 23 |
| 22 | 2025-06-06 12:00 | 2025-06-13 00:00 | SHORT | $150.1000 | $143.7600 | $7.91 | 4.22% | triple_top_breakdown | Time | 26 |
| 25 | 2025-06-14 18:00 | 2025-06-21 06:00 | SHORT | $144.6400 | $142.0800 | $3.39 | 1.77% | triple_top_breakdown | Time | 26 |
| 26 | 2025-06-15 18:00 | 2025-06-22 06:00 | LONG | $152.9700 | $133.2500 | $-19.78 | -12.89% | triple_bottom_breakout | Time | 26 |
| 27 | 2025-06-16 06:00 | 2025-06-22 18:00 | LONG | $156.4800 | $131.7100 | $-19.43 | -15.83% | triple_bottom_breakout | Time | 26 |
| 30 | 2025-06-24 12:00 | 2025-06-28 12:00 | LONG | $144.8000 | $152.1700 | $6.18 | 5.09% | triple_bottom_breakout | TP | 16 |
| 28 | 2025-06-22 06:00 | 2025-06-28 18:00 | SHORT | $133.2500 | $150.7200 | $-21.50 | -13.11% | triple_top_breakdown | Time | 26 |
| 29 | 2025-06-24 00:00 | 2025-06-29 12:00 | LONG | $145.4900 | $151.4300 | $6.20 | 4.08% | triple_bottom_breakout | End | 22 |
| 31 | 2025-06-29 12:00 | 2025-06-29 12:00 | LONG | $151.4300 | $151.4300 | $0.00 | 0.00% | triple_bottom_breakout | End | 0 |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with -8.60% return vs -9.31%.

### Key Observations:
- **Trade Frequency**: 47 vs 32 trades
- **Win Rate Difference**: 44.68% vs 53.12%
- **Return Difference**: 0.71% gap
- **Position Management**: Up to 3 positions at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)
- **Position Size**: 20.0% of capital per position

---
*Báo cáo được tạo tự động bởi Triple Pattern Multi-Position Backtest System*
