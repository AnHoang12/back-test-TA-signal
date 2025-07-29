# Triple Pattern Strategy Comparison - Multi Position - SOLUSDT 4h

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
| Total Trades | 73 | 51 |
| Win Rate | 56.16% | 56.86% |
| Total Return | 2.14% | 0.14% |
| Final Capital | $1021.36 | $1001.38 |
| Total PnL | $21.36 | $1.38 |
| Average PnL per Trade | $0.29 | $0.03 |
| Best Trade | $13.37 | $19.19 |
| Worst Trade | $-21.67 | $-36.44 |
| Long Trades | 38 | 24 |
| Short Trades | 35 | 27 |
| Max Concurrent Positions | 3 | 3 |

## Strategy 1: Exit after 9 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-04-09 20:00 | 2025-04-11 08:00 | LONG | $119.0500 | $118.0200 | $-1.73 | -0.87% | triple_bottom_breakout | Time | 9 |
| 1 | 2025-04-12 16:00 | 2025-04-14 04:00 | LONG | $130.7100 | $132.3000 | $2.43 | 1.22% | triple_bottom_breakout | Time | 9 |
| 2 | 2025-04-13 16:00 | 2025-04-15 04:00 | LONG | $128.2100 | $131.5500 | $4.16 | 2.61% | triple_bottom_breakout | Time | 9 |
| 3 | 2025-04-13 20:00 | 2025-04-15 08:00 | LONG | $128.3800 | $132.1500 | $3.75 | 2.94% | triple_bottom_breakout | Time | 9 |
| 4 | 2025-04-16 04:00 | 2025-04-17 16:00 | SHORT | $124.7800 | $132.9100 | $-13.14 | -6.52% | triple_top_breakdown | Time | 9 |
| 5 | 2025-04-17 12:00 | 2025-04-19 00:00 | LONG | $133.4500 | $138.8200 | $6.49 | 4.02% | triple_bottom_breakout | Time | 9 |
| 6 | 2025-04-18 04:00 | 2025-04-19 16:00 | LONG | $134.9100 | $138.7100 | $4.70 | 2.82% | triple_bottom_breakout | Time | 9 |
| 7 | 2025-04-19 04:00 | 2025-04-20 16:00 | LONG | $138.7600 | $137.2000 | $-1.88 | -1.12% | triple_bottom_breakout | Time | 9 |
| 8 | 2025-04-19 08:00 | 2025-04-20 20:00 | LONG | $138.7700 | $137.8600 | $-0.88 | -0.66% | triple_bottom_breakout | Time | 9 |
| 9 | 2025-04-19 20:00 | 2025-04-21 08:00 | LONG | $139.8700 | $138.9900 | $-0.89 | -0.63% | triple_bottom_breakout | Time | 9 |
| 10 | 2025-04-21 16:00 | 2025-04-22 12:00 | LONG | $136.9400 | $145.3200 | $12.28 | 6.12% | triple_bottom_breakout | TP | 5 |
| 11 | 2025-04-23 00:00 | 2025-04-24 12:00 | LONG | $149.2400 | $149.3400 | $0.14 | 0.07% | triple_bottom_breakout | Time | 9 |
| 12 | 2025-04-24 04:00 | 2025-04-25 16:00 | SHORT | $147.1700 | $151.4000 | $-4.67 | -2.87% | triple_top_breakdown | Time | 9 |
| 13 | 2025-04-24 08:00 | 2025-04-25 20:00 | LONG | $147.7000 | $150.8200 | $2.75 | 2.11% | triple_bottom_breakout | Time | 9 |
| 14 | 2025-04-25 04:00 | 2025-04-26 16:00 | LONG | $154.8600 | $149.2500 | $-5.24 | -3.62% | triple_bottom_breakout | Time | 9 |
| 15 | 2025-04-26 04:00 | 2025-04-27 16:00 | LONG | $151.3600 | $150.0300 | $-1.53 | -0.88% | triple_bottom_breakout | Time | 9 |
| 16 | 2025-04-26 16:00 | 2025-04-28 04:00 | LONG | $149.2500 | $151.0900 | $2.06 | 1.23% | triple_bottom_breakout | Time | 9 |
| 17 | 2025-04-26 20:00 | 2025-04-28 08:00 | LONG | $149.2100 | $151.7000 | $2.23 | 1.67% | triple_bottom_breakout | Time | 9 |
| 18 | 2025-04-28 00:00 | 2025-04-29 12:00 | LONG | $148.3900 | $148.0200 | $-0.35 | -0.25% | triple_bottom_breakout | Time | 9 |
| 19 | 2025-04-29 08:00 | 2025-04-30 20:00 | SHORT | $149.0000 | $147.5400 | $1.70 | 0.98% | triple_top_breakdown | Time | 9 |
| 20 | 2025-05-05 20:00 | 2025-05-07 08:00 | SHORT | $146.7200 | $147.5900 | $-1.20 | -0.59% | triple_top_breakdown | Time | 9 |
| 22 | 2025-05-07 16:00 | 2025-05-08 08:00 | LONG | $145.7700 | $154.5700 | $9.77 | 6.04% | triple_bottom_breakout | TP | 4 |
| 21 | 2025-05-07 12:00 | 2025-05-09 00:00 | SHORT | $145.7500 | $161.3700 | $-21.67 | -10.72% | triple_top_breakdown | Time | 9 |
| 23 | 2025-05-09 12:00 | 2025-05-11 00:00 | LONG | $170.7500 | $175.8600 | $5.98 | 2.99% | triple_bottom_breakout | Time | 9 |
| 24 | 2025-05-10 04:00 | 2025-05-11 16:00 | LONG | $172.3200 | $172.7300 | $0.38 | 0.24% | triple_bottom_breakout | Time | 9 |
| 25 | 2025-05-12 12:00 | 2025-05-13 20:00 | LONG | $174.4000 | $183.7500 | $10.78 | 5.36% | triple_bottom_breakout | TP | 8 |
| 26 | 2025-05-14 16:00 | 2025-05-16 04:00 | LONG | $177.0600 | $172.1300 | $-5.66 | -2.78% | triple_bottom_breakout | Time | 9 |
| 27 | 2025-05-16 12:00 | 2025-05-18 00:00 | SHORT | $172.0800 | $166.9000 | $6.09 | 3.01% | triple_top_breakdown | Time | 9 |
| 28 | 2025-05-17 04:00 | 2025-05-18 16:00 | SHORT | $168.5500 | $166.6500 | $1.82 | 1.13% | triple_top_breakdown | Time | 9 |
| 29 | 2025-05-18 08:00 | 2025-05-19 20:00 | LONG | $170.7900 | $166.8600 | $-3.94 | -2.30% | triple_bottom_breakout | Time | 9 |
| 30 | 2025-05-19 20:00 | 2025-05-21 08:00 | LONG | $166.8600 | $169.3400 | $3.02 | 1.49% | triple_bottom_breakout | Time | 9 |
| 31 | 2025-05-20 12:00 | 2025-05-22 00:00 | SHORT | $166.6400 | $176.8200 | $-9.92 | -6.11% | triple_top_breakdown | Time | 9 |
| 32 | 2025-05-21 08:00 | 2025-05-22 04:00 | LONG | $169.3400 | $178.4900 | $9.24 | 5.40% | triple_bottom_breakout | TP | 5 |
| 33 | 2025-05-22 12:00 | 2025-05-24 00:00 | LONG | $179.0200 | $175.1100 | $-4.44 | -2.18% | triple_bottom_breakout | Time | 9 |
| 34 | 2025-05-24 12:00 | 2025-05-26 00:00 | LONG | $176.3100 | $177.0100 | $0.80 | 0.40% | triple_bottom_breakout | Time | 9 |
| 35 | 2025-05-25 08:00 | 2025-05-26 20:00 | LONG | $171.9800 | $174.9100 | $2.76 | 1.70% | triple_bottom_breakout | Time | 9 |
| 36 | 2025-05-26 08:00 | 2025-05-27 20:00 | LONG | $177.9100 | $176.7100 | $-1.15 | -0.67% | triple_bottom_breakout | Time | 9 |
| 37 | 2025-05-27 00:00 | 2025-05-28 12:00 | SHORT | $173.5100 | $169.7000 | $3.71 | 2.20% | triple_top_breakdown | Time | 9 |
| 38 | 2025-05-27 04:00 | 2025-05-28 16:00 | LONG | $175.4600 | $169.4200 | $-4.66 | -3.44% | triple_bottom_breakout | Time | 9 |
| 39 | 2025-05-28 12:00 | 2025-05-30 00:00 | SHORT | $169.7000 | $165.1600 | $4.73 | 2.68% | triple_top_breakdown | Time | 9 |
| 40 | 2025-05-28 16:00 | 2025-05-30 04:00 | SHORT | $169.4200 | $162.6800 | $6.66 | 3.98% | triple_top_breakdown | Time | 9 |
| 41 | 2025-05-29 20:00 | 2025-05-30 20:00 | SHORT | $166.7100 | $156.2000 | $8.45 | 6.30% | triple_top_breakdown | TP | 6 |
| 42 | 2025-05-30 16:00 | 2025-06-01 04:00 | SHORT | $160.8100 | $154.4500 | $7.05 | 3.95% | triple_top_breakdown | Time | 9 |
| 43 | 2025-05-31 08:00 | 2025-06-01 20:00 | SHORT | $152.9200 | $157.6800 | $-5.33 | -3.11% | triple_top_breakdown | Time | 9 |
| 44 | 2025-06-02 04:00 | 2025-06-03 16:00 | SHORT | $155.5500 | $160.5600 | $-6.67 | -3.22% | triple_top_breakdown | Time | 9 |
| 45 | 2025-06-02 12:00 | 2025-06-04 00:00 | SHORT | $153.1600 | $156.5600 | $-3.68 | -2.22% | triple_top_breakdown | Time | 9 |
| 46 | 2025-06-02 16:00 | 2025-06-04 04:00 | SHORT | $152.9500 | $156.4200 | $-3.01 | -2.27% | triple_top_breakdown | Time | 9 |
| 47 | 2025-06-04 08:00 | 2025-06-05 16:00 | SHORT | $155.9200 | $146.2000 | $12.75 | 6.23% | triple_top_breakdown | TP | 8 |
| 49 | 2025-06-05 08:00 | 2025-06-05 20:00 | SHORT | $152.3700 | $144.2900 | $6.94 | 5.30% | triple_top_breakdown | TP | 3 |
| 48 | 2025-06-05 04:00 | 2025-06-05 20:00 | SHORT | $152.4400 | $144.2900 | $8.74 | 5.35% | triple_top_breakdown | TP | 4 |
| 50 | 2025-06-06 16:00 | 2025-06-08 04:00 | SHORT | $149.0900 | $149.3100 | $-0.31 | -0.15% | triple_top_breakdown | Time | 9 |
| 51 | 2025-06-07 12:00 | 2025-06-09 00:00 | SHORT | $150.9900 | $151.5400 | $-0.61 | -0.36% | triple_top_breakdown | Time | 9 |
| 53 | 2025-06-09 12:00 | 2025-06-10 16:00 | LONG | $155.0200 | $163.6100 | $9.31 | 5.54% | triple_bottom_breakout | TP | 7 |
| 52 | 2025-06-09 08:00 | 2025-06-10 16:00 | LONG | $155.6200 | $163.6100 | $10.78 | 5.13% | triple_bottom_breakout | TP | 8 |
| 54 | 2025-06-11 04:00 | 2025-06-12 16:00 | LONG | $166.6500 | $154.8400 | $-15.16 | -7.09% | triple_bottom_breakout | Time | 9 |
| 55 | 2025-06-12 12:00 | 2025-06-13 00:00 | SHORT | $157.0200 | $144.7600 | $13.37 | 7.81% | triple_top_breakdown | TP | 3 |
| 56 | 2025-06-13 04:00 | 2025-06-14 16:00 | SHORT | $145.0200 | $143.5000 | $2.24 | 1.05% | triple_top_breakdown | Time | 9 |
| 57 | 2025-06-15 04:00 | 2025-06-16 16:00 | SHORT | $145.8700 | $157.7900 | $-17.49 | -8.17% | triple_top_breakdown | Time | 9 |
| 58 | 2025-06-15 20:00 | 2025-06-17 08:00 | LONG | $152.9700 | $150.5300 | $-2.73 | -1.60% | triple_bottom_breakout | Time | 9 |
| 59 | 2025-06-16 08:00 | 2025-06-17 20:00 | LONG | $156.4800 | $147.5700 | $-7.80 | -5.69% | triple_bottom_breakout | Time | 9 |
| 60 | 2025-06-16 20:00 | 2025-06-18 08:00 | SHORT | $150.7200 | $146.5200 | $4.15 | 2.79% | triple_top_breakdown | Time | 9 |
| 61 | 2025-06-19 08:00 | 2025-06-20 20:00 | SHORT | $145.0900 | $140.1100 | $7.18 | 3.43% | triple_top_breakdown | Time | 9 |
| 62 | 2025-06-19 12:00 | 2025-06-21 00:00 | SHORT | $143.1600 | $140.7600 | $2.81 | 1.68% | triple_top_breakdown | Time | 9 |
| 64 | 2025-06-21 04:00 | 2025-06-22 08:00 | SHORT | $140.6400 | $133.2500 | $9.24 | 5.25% | triple_top_breakdown | TP | 7 |
| 63 | 2025-06-20 20:00 | 2025-06-22 08:00 | SHORT | $140.1100 | $133.2500 | $8.68 | 4.90% | triple_top_breakdown | Time | 9 |
| 65 | 2025-06-22 00:00 | 2025-06-23 12:00 | SHORT | $135.1100 | $133.4300 | $1.75 | 1.24% | triple_top_breakdown | Time | 9 |
| 66 | 2025-06-22 16:00 | 2025-06-24 04:00 | SHORT | $129.0600 | $144.0100 | $-21.63 | -11.58% | triple_top_breakdown | Time | 9 |
| 67 | 2025-06-23 12:00 | 2025-06-25 00:00 | SHORT | $133.4300 | $145.5200 | $-16.12 | -9.06% | triple_top_breakdown | Time | 9 |
| 68 | 2025-06-24 04:00 | 2025-06-25 16:00 | SHORT | $144.0100 | $144.7400 | $-0.89 | -0.51% | triple_top_breakdown | Time | 9 |
| 69 | 2025-06-25 04:00 | 2025-06-26 16:00 | LONG | $147.0100 | $142.2900 | $-5.54 | -3.21% | triple_bottom_breakout | Time | 9 |
| 70 | 2025-06-26 12:00 | 2025-06-28 00:00 | LONG | $143.0000 | $143.4000 | $0.48 | 0.28% | triple_bottom_breakout | Time | 9 |
| 71 | 2025-06-27 20:00 | 2025-06-29 08:00 | SHORT | $142.0900 | $151.6800 | $-11.59 | -6.75% | triple_top_breakdown | Time | 9 |
| 72 | 2025-06-28 20:00 | 2025-06-29 16:00 | LONG | $150.7200 | $151.1800 | $0.53 | 0.31% | triple_bottom_breakout | End | 5 |

## Strategy 2: Exit after 26 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-04-09 20:00 | 2025-04-12 12:00 | LONG | $119.0500 | $130.4700 | $19.19 | 9.59% | triple_bottom_breakout | TP | 16 |
| 1 | 2025-04-12 16:00 | 2025-04-17 00:00 | LONG | $130.7100 | $129.7900 | $-1.43 | -0.70% | triple_bottom_breakout | Time | 26 |
| 3 | 2025-04-13 20:00 | 2025-04-17 20:00 | LONG | $128.3800 | $134.8300 | $6.55 | 5.02% | triple_bottom_breakout | TP | 24 |
| 2 | 2025-04-13 16:00 | 2025-04-17 20:00 | LONG | $128.2100 | $134.8300 | $8.42 | 5.16% | triple_bottom_breakout | TP | 25 |
| 4 | 2025-04-17 12:00 | 2025-04-20 00:00 | LONG | $133.4500 | $140.9600 | $8.15 | 5.63% | triple_bottom_breakout | TP | 15 |
| 5 | 2025-04-18 04:00 | 2025-04-22 12:00 | LONG | $134.9100 | $145.3200 | $13.70 | 7.72% | triple_bottom_breakout | TP | 26 |
| 6 | 2025-04-19 04:00 | 2025-04-22 20:00 | LONG | $138.7600 | $148.7900 | $10.27 | 7.23% | triple_bottom_breakout | TP | 22 |
| 7 | 2025-04-20 12:00 | 2025-04-24 20:00 | SHORT | $135.9400 | $152.5500 | $-17.63 | -12.22% | triple_top_breakdown | Time | 26 |
| 8 | 2025-04-23 00:00 | 2025-04-27 08:00 | LONG | $149.2400 | $147.9500 | $-1.59 | -0.86% | triple_bottom_breakout | Time | 26 |
| 9 | 2025-04-24 04:00 | 2025-04-28 12:00 | SHORT | $147.1700 | $146.3400 | $0.83 | 0.56% | triple_top_breakdown | Time | 26 |
| 10 | 2025-04-25 04:00 | 2025-04-29 12:00 | LONG | $154.8600 | $148.0200 | $-6.32 | -4.42% | triple_bottom_breakout | Time | 26 |
| 11 | 2025-04-28 00:00 | 2025-05-02 08:00 | LONG | $148.3900 | $150.7300 | $2.38 | 1.58% | triple_bottom_breakout | Time | 26 |
| 12 | 2025-04-29 08:00 | 2025-05-03 16:00 | SHORT | $149.0000 | $147.4200 | $1.60 | 1.06% | triple_top_breakdown | Time | 26 |
| 15 | 2025-05-07 16:00 | 2025-05-08 08:00 | LONG | $145.7700 | $154.5700 | $8.07 | 6.04% | triple_bottom_breakout | TP | 4 |
| 13 | 2025-05-05 20:00 | 2025-05-10 04:00 | SHORT | $146.7200 | $172.3200 | $-36.44 | -17.45% | triple_top_breakdown | Time | 26 |
| 14 | 2025-05-07 12:00 | 2025-05-11 20:00 | SHORT | $145.7500 | $173.1900 | $-31.45 | -18.83% | triple_top_breakdown | Time | 26 |
| 17 | 2025-05-10 04:00 | 2025-05-13 16:00 | LONG | $172.3200 | $182.0500 | $8.06 | 5.65% | triple_bottom_breakout | TP | 21 |
| 16 | 2025-05-09 12:00 | 2025-05-13 16:00 | LONG | $170.7500 | $182.0500 | $8.95 | 6.62% | triple_bottom_breakout | TP | 25 |
| 18 | 2025-05-12 12:00 | 2025-05-13 20:00 | LONG | $174.4000 | $183.7500 | $7.57 | 5.36% | triple_bottom_breakout | TP | 8 |
| 19 | 2025-05-14 16:00 | 2025-05-19 00:00 | LONG | $177.0600 | $165.3500 | $-13.34 | -6.61% | triple_bottom_breakout | Time | 26 |
| 20 | 2025-05-16 12:00 | 2025-05-19 04:00 | SHORT | $172.0800 | $161.8900 | $9.56 | 5.92% | triple_top_breakdown | TP | 16 |
| 21 | 2025-05-17 04:00 | 2025-05-21 12:00 | SHORT | $168.5500 | $172.1700 | $-2.77 | -2.15% | triple_top_breakdown | Time | 26 |
| 22 | 2025-05-19 20:00 | 2025-05-22 00:00 | LONG | $166.8600 | $176.8200 | $10.46 | 5.97% | triple_bottom_breakout | TP | 13 |
| 23 | 2025-05-20 12:00 | 2025-05-24 20:00 | SHORT | $166.6400 | $175.8700 | $-7.76 | -5.54% | triple_top_breakdown | Time | 26 |
| 24 | 2025-05-22 12:00 | 2025-05-26 20:00 | LONG | $179.0200 | $174.9100 | $-4.01 | -2.30% | triple_bottom_breakout | Time | 26 |
| 25 | 2025-05-24 12:00 | 2025-05-28 20:00 | LONG | $176.3100 | $172.2100 | $-3.25 | -2.33% | triple_bottom_breakout | Time | 26 |
| 26 | 2025-05-25 08:00 | 2025-05-29 16:00 | LONG | $171.9800 | $166.8400 | $-4.13 | -2.99% | triple_bottom_breakout | Time | 26 |
| 27 | 2025-05-27 00:00 | 2025-05-30 04:00 | SHORT | $173.5100 | $162.6800 | $9.03 | 6.24% | triple_top_breakdown | TP | 19 |
| 28 | 2025-05-29 20:00 | 2025-05-30 20:00 | SHORT | $166.7100 | $156.2000 | $10.70 | 6.30% | triple_top_breakdown | TP | 6 |
| 29 | 2025-05-30 16:00 | 2025-06-01 08:00 | SHORT | $160.8100 | $152.0500 | $9.07 | 5.45% | triple_top_breakdown | TP | 10 |
| 30 | 2025-05-31 08:00 | 2025-06-04 16:00 | SHORT | $152.9200 | $155.3700 | $-2.71 | -1.60% | triple_top_breakdown | Time | 26 |
| 31 | 2025-06-02 04:00 | 2025-06-05 16:00 | SHORT | $155.5500 | $146.2000 | $10.26 | 6.01% | triple_top_breakdown | TP | 21 |
| 33 | 2025-06-05 04:00 | 2025-06-05 20:00 | SHORT | $152.4400 | $144.2900 | $7.62 | 5.35% | triple_top_breakdown | TP | 4 |
| 32 | 2025-06-02 12:00 | 2025-06-05 20:00 | SHORT | $153.1600 | $144.2900 | $7.90 | 5.79% | triple_top_breakdown | TP | 20 |
| 36 | 2025-06-09 08:00 | 2025-06-10 16:00 | LONG | $155.6200 | $163.6100 | $6.87 | 5.13% | triple_bottom_breakout | TP | 8 |
| 34 | 2025-06-06 16:00 | 2025-06-11 00:00 | SHORT | $149.0900 | $166.6700 | $-24.66 | -11.79% | triple_top_breakdown | Time | 26 |
| 35 | 2025-06-07 12:00 | 2025-06-11 20:00 | SHORT | $150.9900 | $160.9700 | $-11.06 | -6.61% | triple_top_breakdown | Time | 26 |
| 38 | 2025-06-12 12:00 | 2025-06-13 00:00 | SHORT | $157.0200 | $144.7600 | $13.19 | 7.81% | triple_top_breakdown | TP | 3 |
| 37 | 2025-06-11 04:00 | 2025-06-15 12:00 | LONG | $166.6500 | $150.8400 | $-16.33 | -9.49% | triple_bottom_breakout | Time | 26 |
| 39 | 2025-06-13 04:00 | 2025-06-17 12:00 | SHORT | $145.0200 | $147.6200 | $-3.08 | -1.79% | triple_top_breakdown | Time | 26 |
| 40 | 2025-06-15 04:00 | 2025-06-19 12:00 | SHORT | $145.8700 | $143.1600 | $2.55 | 1.86% | triple_top_breakdown | Time | 26 |
| 41 | 2025-06-15 20:00 | 2025-06-20 04:00 | LONG | $152.9700 | $147.4700 | $-5.07 | -3.60% | triple_bottom_breakout | Time | 26 |
| 42 | 2025-06-19 08:00 | 2025-06-21 16:00 | SHORT | $145.0900 | $137.2800 | $7.88 | 5.38% | triple_top_breakdown | TP | 14 |
| 43 | 2025-06-19 12:00 | 2025-06-21 20:00 | SHORT | $143.1600 | $135.4300 | $7.84 | 5.40% | triple_top_breakdown | TP | 14 |
| 44 | 2025-06-20 20:00 | 2025-06-22 12:00 | SHORT | $140.1100 | $128.5500 | $11.82 | 8.25% | triple_top_breakdown | TP | 10 |
| 45 | 2025-06-22 00:00 | 2025-06-26 08:00 | SHORT | $135.1100 | $143.6500 | $-11.13 | -6.32% | triple_top_breakdown | Time | 26 |
| 46 | 2025-06-22 04:00 | 2025-06-26 12:00 | SHORT | $134.8200 | $143.0000 | $-8.55 | -6.07% | triple_top_breakdown | Time | 26 |
| 47 | 2025-06-22 16:00 | 2025-06-27 00:00 | SHORT | $129.0600 | $141.3600 | $-13.70 | -9.53% | triple_top_breakdown | Time | 26 |
| 48 | 2025-06-26 12:00 | 2025-06-28 16:00 | LONG | $143.0000 | $150.6700 | $9.36 | 5.36% | triple_bottom_breakout | TP | 13 |
| 49 | 2025-06-27 20:00 | 2025-06-29 16:00 | SHORT | $142.0900 | $151.1800 | $-10.59 | -6.40% | triple_top_breakdown | End | 11 |
| 50 | 2025-06-28 20:00 | 2025-06-29 16:00 | LONG | $150.7200 | $151.1800 | $0.52 | 0.31% | triple_bottom_breakout | End | 5 |

## Analysis

**Winner: 9 Periods Strategy**

The 9-period exit strategy outperformed with 2.14% return vs 0.14%.

### Key Observations:
- **Trade Frequency**: 73 vs 51 trades
- **Win Rate Difference**: 56.16% vs 56.86%
- **Return Difference**: 2.00% gap
- **Position Management**: Up to 3 positions at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)
- **Position Size**: 20.0% of capital per position

---
*Báo cáo được tạo tự động bởi Triple Pattern Multi-Position Backtest System*
