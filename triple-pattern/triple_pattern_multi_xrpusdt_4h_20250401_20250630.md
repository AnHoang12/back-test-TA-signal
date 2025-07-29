# Triple Pattern Strategy Comparison - Multi Position - XRPUSDT 4h

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
| Total Trades | 88 | 53 |
| Win Rate | 39.77% | 39.62% |
| Total Return | -15.14% | -10.49% |
| Final Capital | $848.63 | $895.08 |
| Total PnL | $-151.37 | $-104.92 |
| Average PnL per Trade | $-1.72 | $-1.98 |
| Best Trade | $10.79 | $15.47 |
| Worst Trade | $-15.51 | $-19.29 |
| Long Trades | 41 | 22 |
| Short Trades | 47 | 31 |
| Max Concurrent Positions | 3 | 3 |

## Strategy 1: Exit after 9 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 1 | 2025-04-08 00:00 | 2025-04-08 20:00 | SHORT | $1.9043 | $1.7963 | $9.07 | 5.67% | triple_top_breakdown | TP | 5 |
| 0 | 2025-04-07 20:00 | 2025-04-08 20:00 | SHORT | $1.8987 | $1.7963 | $10.79 | 5.39% | triple_top_breakdown | TP | 6 |
| 2 | 2025-04-10 20:00 | 2025-04-12 08:00 | SHORT | $1.9658 | $2.0619 | $-9.97 | -4.89% | triple_top_breakdown | Time | 9 |
| 3 | 2025-04-11 12:00 | 2025-04-13 00:00 | SHORT | $2.0015 | $2.1563 | $-12.62 | -7.73% | triple_top_breakdown | Time | 9 |
| 4 | 2025-04-13 20:00 | 2025-04-15 08:00 | LONG | $2.1196 | $2.1515 | $3.00 | 1.51% | triple_bottom_breakout | Time | 9 |
| 5 | 2025-04-15 04:00 | 2025-04-16 16:00 | LONG | $2.1517 | $2.1066 | $-3.34 | -2.10% | triple_bottom_breakout | Time | 9 |
| 6 | 2025-04-15 08:00 | 2025-04-16 20:00 | LONG | $2.1515 | $2.0834 | $-5.32 | -3.17% | triple_bottom_breakout | Time | 9 |
| 7 | 2025-04-16 12:00 | 2025-04-18 00:00 | LONG | $2.0938 | $2.0559 | $-2.43 | -1.81% | triple_bottom_breakout | Time | 9 |
| 8 | 2025-04-17 16:00 | 2025-04-19 04:00 | LONG | $2.0659 | $2.0891 | $1.93 | 1.12% | triple_bottom_breakout | Time | 9 |
| 9 | 2025-04-17 20:00 | 2025-04-19 08:00 | LONG | $2.0673 | $2.0814 | $0.94 | 0.68% | triple_bottom_breakout | Time | 9 |
| 10 | 2025-04-19 12:00 | 2025-04-21 00:00 | SHORT | $2.0773 | $2.1093 | $-3.06 | -1.54% | triple_top_breakdown | Time | 9 |
| 11 | 2025-04-20 12:00 | 2025-04-22 00:00 | SHORT | $2.0488 | $2.0830 | $-2.65 | -1.67% | triple_top_breakdown | Time | 9 |
| 12 | 2025-04-20 20:00 | 2025-04-22 08:00 | SHORT | $2.0787 | $2.0993 | $-1.26 | -0.99% | triple_top_breakdown | Time | 9 |
| 13 | 2025-04-21 12:00 | 2025-04-23 00:00 | SHORT | $2.1148 | $2.2350 | $-7.99 | -5.68% | triple_top_breakdown | Time | 9 |
| 14 | 2025-04-22 16:00 | 2025-04-24 04:00 | LONG | $2.1541 | $2.1493 | $-0.38 | -0.22% | triple_bottom_breakout | Time | 9 |
| 15 | 2025-04-23 08:00 | 2025-04-24 20:00 | LONG | $2.2599 | $2.2049 | $-3.93 | -2.43% | triple_bottom_breakout | Time | 9 |
| 16 | 2025-04-23 20:00 | 2025-04-25 08:00 | LONG | $2.2184 | $2.2044 | $-0.82 | -0.63% | triple_bottom_breakout | Time | 9 |
| 17 | 2025-04-24 08:00 | 2025-04-25 20:00 | LONG | $2.1555 | $2.1812 | $1.64 | 1.19% | triple_bottom_breakout | Time | 9 |
| 18 | 2025-04-24 20:00 | 2025-04-26 08:00 | LONG | $2.2049 | $2.1938 | $-0.71 | -0.50% | triple_bottom_breakout | Time | 9 |
| 19 | 2025-04-25 12:00 | 2025-04-27 00:00 | LONG | $2.2005 | $2.1758 | $-1.56 | -1.12% | triple_bottom_breakout | Time | 9 |
| 21 | 2025-04-27 04:00 | 2025-04-27 16:00 | LONG | $2.1723 | $2.2841 | $8.28 | 5.15% | triple_bottom_breakout | TP | 3 |
| 20 | 2025-04-26 16:00 | 2025-04-28 04:00 | LONG | $2.1991 | $2.3355 | $10.35 | 6.20% | triple_bottom_breakout | TP | 9 |
| 22 | 2025-04-28 00:00 | 2025-04-29 12:00 | LONG | $2.2589 | $2.2927 | $2.43 | 1.50% | triple_bottom_breakout | Time | 9 |
| 23 | 2025-04-29 12:00 | 2025-05-01 00:00 | LONG | $2.2927 | $2.2040 | $-7.68 | -3.87% | triple_bottom_breakout | Time | 9 |
| 24 | 2025-04-29 16:00 | 2025-05-01 04:00 | LONG | $2.2923 | $2.2001 | $-6.39 | -4.02% | triple_bottom_breakout | Time | 9 |
| 25 | 2025-04-30 12:00 | 2025-05-02 00:00 | SHORT | $2.1581 | $2.2244 | $-3.90 | -3.07% | triple_top_breakdown | Time | 9 |
| 26 | 2025-05-01 12:00 | 2025-05-03 00:00 | SHORT | $2.2364 | $2.2123 | $1.83 | 1.08% | triple_top_breakdown | Time | 9 |
| 27 | 2025-05-02 04:00 | 2025-05-03 16:00 | SHORT | $2.1945 | $2.1936 | $0.07 | 0.04% | triple_top_breakdown | Time | 9 |
| 28 | 2025-05-02 12:00 | 2025-05-04 00:00 | SHORT | $2.2163 | $2.1984 | $1.04 | 0.81% | triple_top_breakdown | Time | 9 |
| 29 | 2025-05-04 16:00 | 2025-05-06 04:00 | SHORT | $2.1758 | $2.0990 | $6.90 | 3.53% | triple_top_breakdown | Time | 9 |
| 30 | 2025-05-05 08:00 | 2025-05-06 20:00 | SHORT | $2.1427 | $2.1550 | $-0.90 | -0.57% | triple_top_breakdown | Time | 9 |
| 32 | 2025-05-08 04:00 | 2025-05-08 20:00 | LONG | $2.1889 | $2.3272 | $9.94 | 6.32% | triple_bottom_breakout | TP | 4 |
| 31 | 2025-05-07 12:00 | 2025-05-09 00:00 | SHORT | $2.1268 | $2.2945 | $-15.51 | -7.89% | triple_top_breakdown | Time | 9 |
| 33 | 2025-05-10 00:00 | 2025-05-11 12:00 | LONG | $2.3672 | $2.3473 | $-1.64 | -0.84% | triple_bottom_breakout | Time | 9 |
| 34 | 2025-05-10 12:00 | 2025-05-12 00:00 | LONG | $2.3973 | $2.3961 | $-0.08 | -0.05% | triple_bottom_breakout | Time | 9 |
| 35 | 2025-05-11 12:00 | 2025-05-13 00:00 | SHORT | $2.3473 | $2.4300 | $-5.78 | -3.52% | triple_top_breakdown | Time | 9 |
| 36 | 2025-05-13 20:00 | 2025-05-15 08:00 | LONG | $2.5829 | $2.4778 | $-7.90 | -4.07% | triple_bottom_breakout | Time | 9 |
| 37 | 2025-05-14 04:00 | 2025-05-15 16:00 | LONG | $2.6191 | $2.4487 | $-10.10 | -6.51% | triple_bottom_breakout | Time | 9 |
| 38 | 2025-05-14 08:00 | 2025-05-15 20:00 | LONG | $2.6142 | $2.3856 | $-10.86 | -8.74% | triple_bottom_breakout | Time | 9 |
| 39 | 2025-05-17 16:00 | 2025-05-19 04:00 | SHORT | $2.3347 | $2.3055 | $2.35 | 1.25% | triple_top_breakdown | Time | 9 |
| 40 | 2025-05-18 16:00 | 2025-05-20 04:00 | SHORT | $2.3694 | $2.3464 | $1.46 | 0.97% | triple_top_breakdown | Time | 9 |
| 41 | 2025-05-20 00:00 | 2025-05-21 12:00 | LONG | $2.3824 | $2.3993 | $1.13 | 0.71% | triple_bottom_breakout | Time | 9 |
| 42 | 2025-05-20 08:00 | 2025-05-21 20:00 | SHORT | $2.3465 | $2.3952 | $-3.27 | -2.08% | triple_top_breakdown | Time | 9 |
| 43 | 2025-05-20 20:00 | 2025-05-22 08:00 | SHORT | $2.3565 | $2.4319 | $-4.03 | -3.20% | triple_top_breakdown | Time | 9 |
| 44 | 2025-05-22 12:00 | 2025-05-24 00:00 | LONG | $2.4328 | $2.3341 | $-7.62 | -4.06% | triple_bottom_breakout | Time | 9 |
| 45 | 2025-05-22 20:00 | 2025-05-24 08:00 | LONG | $2.4311 | $2.3517 | $-4.91 | -3.27% | triple_bottom_breakout | Time | 9 |
| 46 | 2025-05-23 12:00 | 2025-05-25 00:00 | SHORT | $2.3617 | $2.3228 | $1.98 | 1.65% | triple_top_breakdown | Time | 9 |
| 47 | 2025-05-24 04:00 | 2025-05-25 16:00 | SHORT | $2.3360 | $2.3055 | $1.73 | 1.31% | triple_top_breakdown | Time | 9 |
| 48 | 2025-05-24 12:00 | 2025-05-26 00:00 | SHORT | $2.3523 | $2.3425 | $0.56 | 0.42% | triple_top_breakdown | Time | 9 |
| 49 | 2025-05-26 00:00 | 2025-05-27 12:00 | LONG | $2.3425 | $2.3378 | $-0.37 | -0.20% | triple_bottom_breakout | Time | 9 |
| 50 | 2025-05-26 08:00 | 2025-05-27 20:00 | SHORT | $2.3349 | $2.3168 | $1.15 | 0.78% | triple_top_breakdown | Time | 9 |
| 51 | 2025-05-26 12:00 | 2025-05-28 00:00 | LONG | $2.3328 | $2.3126 | $-1.03 | -0.87% | triple_bottom_breakout | Time | 9 |
| 52 | 2025-05-30 12:00 | 2025-06-01 00:00 | SHORT | $2.1836 | $2.1637 | $1.70 | 0.91% | triple_top_breakdown | Time | 9 |
| 53 | 2025-05-30 16:00 | 2025-06-01 04:00 | SHORT | $2.1860 | $2.1594 | $1.81 | 1.22% | triple_top_breakdown | Time | 9 |
| 54 | 2025-05-30 20:00 | 2025-06-01 08:00 | SHORT | $2.1398 | $2.1411 | $-0.07 | -0.06% | triple_top_breakdown | Time | 9 |
| 55 | 2025-06-02 04:00 | 2025-06-03 16:00 | SHORT | $2.1633 | $2.2814 | $-10.20 | -5.46% | triple_top_breakdown | Time | 9 |
| 56 | 2025-06-03 00:00 | 2025-06-04 12:00 | SHORT | $2.1958 | $2.2492 | $-3.63 | -2.43% | triple_top_breakdown | Time | 9 |
| 59 | 2025-06-05 00:00 | 2025-06-05 20:00 | SHORT | $2.2054 | $2.0936 | $6.21 | 5.07% | triple_top_breakdown | TP | 5 |
| 57 | 2025-06-04 08:00 | 2025-06-05 20:00 | LONG | $2.2530 | $2.0936 | $-10.96 | -7.08% | triple_bottom_breakout | Time | 9 |
| 58 | 2025-06-04 12:00 | 2025-06-06 00:00 | LONG | $2.2492 | $2.1295 | $-8.15 | -5.32% | triple_bottom_breakout | Time | 9 |
| 60 | 2025-06-06 04:00 | 2025-06-07 16:00 | SHORT | $2.1303 | $2.1759 | $-3.88 | -2.14% | triple_top_breakdown | Time | 9 |
| 61 | 2025-06-07 08:00 | 2025-06-08 20:00 | SHORT | $2.1829 | $2.2670 | $-5.59 | -3.85% | triple_top_breakdown | Time | 9 |
| 62 | 2025-06-07 12:00 | 2025-06-09 00:00 | SHORT | $2.1829 | $2.2425 | $-3.17 | -2.73% | triple_top_breakdown | Time | 9 |
| 63 | 2025-06-07 20:00 | 2025-06-09 08:00 | SHORT | $2.1769 | $2.2689 | $-5.43 | -4.23% | triple_top_breakdown | Time | 9 |
| 64 | 2025-06-09 12:00 | 2025-06-11 00:00 | LONG | $2.2632 | $2.2979 | $2.73 | 1.53% | triple_bottom_breakout | Time | 9 |
| 65 | 2025-06-11 00:00 | 2025-06-12 12:00 | LONG | $2.2979 | $2.2284 | $-5.40 | -3.02% | triple_bottom_breakout | Time | 9 |
| 66 | 2025-06-11 04:00 | 2025-06-12 16:00 | LONG | $2.2931 | $2.2037 | $-5.56 | -3.90% | triple_bottom_breakout | Time | 9 |
| 67 | 2025-06-11 08:00 | 2025-06-12 20:00 | LONG | $2.3146 | $2.1899 | $-6.15 | -5.39% | triple_bottom_breakout | Time | 9 |
| 68 | 2025-06-12 12:00 | 2025-06-14 00:00 | LONG | $2.2284 | $2.1589 | $-3.93 | -3.12% | triple_bottom_breakout | Time | 9 |
| 69 | 2025-06-12 16:00 | 2025-06-14 04:00 | SHORT | $2.2037 | $2.1651 | $2.25 | 1.75% | triple_top_breakdown | Time | 9 |
| 70 | 2025-06-15 12:00 | 2025-06-17 00:00 | SHORT | $2.1645 | $2.2493 | $-6.84 | -3.92% | triple_top_breakdown | Time | 9 |
| 71 | 2025-06-15 16:00 | 2025-06-17 04:00 | SHORT | $2.1641 | $2.2356 | $-4.62 | -3.30% | triple_top_breakdown | Time | 9 |
| 72 | 2025-06-15 20:00 | 2025-06-17 08:00 | SHORT | $2.1655 | $2.1939 | $-1.47 | -1.31% | triple_top_breakdown | Time | 9 |
| 73 | 2025-06-17 00:00 | 2025-06-18 12:00 | LONG | $2.2493 | $2.1510 | $-5.37 | -4.37% | triple_bottom_breakout | Time | 9 |
| 74 | 2025-06-19 08:00 | 2025-06-20 20:00 | SHORT | $2.1519 | $2.1194 | $2.58 | 1.51% | triple_top_breakdown | Time | 9 |
| 75 | 2025-06-20 12:00 | 2025-06-22 00:00 | SHORT | $2.1338 | $2.0594 | $4.77 | 3.49% | triple_top_breakdown | Time | 9 |
| 76 | 2025-06-21 08:00 | 2025-06-22 08:00 | SHORT | $2.1371 | $2.0252 | $7.55 | 5.24% | triple_top_breakdown | TP | 6 |
| 78 | 2025-06-22 00:00 | 2025-06-22 12:00 | SHORT | $2.0594 | $1.9343 | $7.32 | 6.07% | triple_top_breakdown | TP | 3 |
| 77 | 2025-06-21 20:00 | 2025-06-22 12:00 | SHORT | $2.0632 | $1.9343 | $7.20 | 6.25% | triple_top_breakdown | TP | 4 |
| 79 | 2025-06-22 08:00 | 2025-06-23 20:00 | SHORT | $2.0252 | $2.1584 | $-8.34 | -6.58% | triple_top_breakdown | Time | 9 |
| 80 | 2025-06-23 00:00 | 2025-06-24 12:00 | SHORT | $2.0180 | $2.1882 | $-12.78 | -8.43% | triple_top_breakdown | Time | 9 |
| 81 | 2025-06-23 08:00 | 2025-06-24 20:00 | SHORT | $2.0013 | $2.1898 | $-11.42 | -9.42% | triple_top_breakdown | Time | 9 |
| 82 | 2025-06-25 16:00 | 2025-06-27 04:00 | LONG | $2.2057 | $2.0851 | $-9.31 | -5.47% | triple_bottom_breakout | Time | 9 |
| 85 | 2025-06-27 12:00 | 2025-06-28 12:00 | LONG | $2.0979 | $2.2038 | $5.70 | 5.05% | triple_bottom_breakout | TP | 6 |
| 83 | 2025-06-27 00:00 | 2025-06-28 12:00 | LONG | $2.1053 | $2.2038 | $6.38 | 4.68% | triple_bottom_breakout | Time | 9 |
| 84 | 2025-06-27 08:00 | 2025-06-28 20:00 | SHORT | $2.0909 | $2.1854 | $-6.38 | -4.52% | triple_top_breakdown | Time | 9 |
| 86 | 2025-06-28 20:00 | 2025-06-29 16:00 | LONG | $2.1854 | $2.1886 | $0.25 | 0.15% | triple_bottom_breakout | End | 5 |
| 87 | 2025-06-29 04:00 | 2025-06-29 16:00 | LONG | $2.1843 | $2.1886 | $0.27 | 0.20% | triple_bottom_breakout | End | 3 |

## Strategy 2: Exit after 26 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 1 | 2025-04-08 00:00 | 2025-04-08 20:00 | SHORT | $1.9043 | $1.7963 | $9.07 | 5.67% | triple_top_breakdown | TP | 5 |
| 0 | 2025-04-07 20:00 | 2025-04-08 20:00 | SHORT | $1.8987 | $1.7963 | $10.79 | 5.39% | triple_top_breakdown | TP | 6 |
| 2 | 2025-04-10 20:00 | 2025-04-15 04:00 | SHORT | $1.9658 | $2.1517 | $-19.29 | -9.46% | triple_top_breakdown | Time | 26 |
| 3 | 2025-04-11 12:00 | 2025-04-15 20:00 | SHORT | $2.0015 | $2.0842 | $-6.74 | -4.13% | triple_top_breakdown | Time | 26 |
| 4 | 2025-04-13 20:00 | 2025-04-18 04:00 | LONG | $2.1196 | $2.0692 | $-3.10 | -2.38% | triple_bottom_breakout | Time | 26 |
| 5 | 2025-04-15 04:00 | 2025-04-19 12:00 | LONG | $2.1517 | $2.0773 | $-4.89 | -3.46% | triple_bottom_breakout | Time | 26 |
| 6 | 2025-04-16 12:00 | 2025-04-20 20:00 | LONG | $2.0938 | $2.0787 | $-1.04 | -0.72% | triple_bottom_breakout | Time | 26 |
| 7 | 2025-04-19 12:00 | 2025-04-23 20:00 | SHORT | $2.0773 | $2.2184 | $-11.43 | -6.79% | triple_top_breakdown | Time | 26 |
| 8 | 2025-04-20 12:00 | 2025-04-24 20:00 | SHORT | $2.0488 | $2.2049 | $-10.26 | -7.62% | triple_top_breakdown | Time | 26 |
| 9 | 2025-04-20 20:00 | 2025-04-25 04:00 | SHORT | $2.0787 | $2.1947 | $-7.61 | -5.58% | triple_top_breakdown | Time | 26 |
| 12 | 2025-04-25 12:00 | 2025-04-28 04:00 | LONG | $2.2005 | $2.3355 | $8.32 | 6.13% | triple_bottom_breakout | TP | 16 |
| 11 | 2025-04-24 20:00 | 2025-04-28 04:00 | LONG | $2.2049 | $2.3355 | $8.13 | 5.92% | triple_bottom_breakout | TP | 20 |
| 10 | 2025-04-23 20:00 | 2025-04-28 04:00 | LONG | $2.2184 | $2.3355 | $7.41 | 5.28% | triple_bottom_breakout | TP | 26 |
| 13 | 2025-04-29 12:00 | 2025-05-03 20:00 | LONG | $2.2927 | $2.1872 | $-9.01 | -4.60% | triple_bottom_breakout | Time | 26 |
| 14 | 2025-04-29 16:00 | 2025-05-04 00:00 | LONG | $2.2923 | $2.1984 | $-6.42 | -4.10% | triple_bottom_breakout | Time | 26 |
| 15 | 2025-04-30 12:00 | 2025-05-04 20:00 | SHORT | $2.1581 | $2.1560 | $0.12 | 0.10% | triple_top_breakdown | Time | 26 |
| 16 | 2025-05-04 16:00 | 2025-05-09 00:00 | SHORT | $2.1758 | $2.2945 | $-9.15 | -5.46% | triple_top_breakdown | Time | 26 |
| 17 | 2025-05-05 08:00 | 2025-05-09 16:00 | SHORT | $2.1427 | $2.3580 | $-16.00 | -10.05% | triple_top_breakdown | Time | 26 |
| 18 | 2025-05-07 12:00 | 2025-05-11 20:00 | SHORT | $2.1268 | $2.3670 | $-14.39 | -11.29% | triple_top_breakdown | Time | 26 |
| 20 | 2025-05-10 12:00 | 2025-05-12 12:00 | LONG | $2.3973 | $2.5929 | $10.59 | 8.16% | triple_bottom_breakout | TP | 12 |
| 19 | 2025-05-10 00:00 | 2025-05-12 12:00 | LONG | $2.3672 | $2.5929 | $15.47 | 9.53% | triple_bottom_breakout | TP | 15 |
| 21 | 2025-05-13 20:00 | 2025-05-18 04:00 | LONG | $2.5829 | $2.3968 | $-13.70 | -7.21% | triple_bottom_breakout | Time | 26 |
| 22 | 2025-05-14 04:00 | 2025-05-18 12:00 | LONG | $2.6191 | $2.4378 | $-10.53 | -6.92% | triple_bottom_breakout | Time | 26 |
| 23 | 2025-05-14 08:00 | 2025-05-18 16:00 | LONG | $2.6142 | $2.3694 | $-11.39 | -9.36% | triple_bottom_breakout | Time | 26 |
| 24 | 2025-05-18 16:00 | 2025-05-23 00:00 | SHORT | $2.3694 | $2.4734 | $-8.03 | -4.39% | triple_top_breakdown | Time | 26 |
| 25 | 2025-05-20 00:00 | 2025-05-24 08:00 | LONG | $2.3824 | $2.3517 | $-1.89 | -1.29% | triple_bottom_breakout | Time | 26 |
| 26 | 2025-05-20 08:00 | 2025-05-24 16:00 | SHORT | $2.3465 | $2.3487 | $-0.11 | -0.09% | triple_top_breakdown | Time | 26 |
| 27 | 2025-05-23 12:00 | 2025-05-27 20:00 | SHORT | $2.3617 | $2.3168 | $2.45 | 1.90% | triple_top_breakdown | Time | 26 |
| 29 | 2025-05-24 16:00 | 2025-05-28 16:00 | SHORT | $2.3487 | $2.2275 | $6.65 | 5.16% | triple_top_breakdown | TP | 24 |
| 28 | 2025-05-24 12:00 | 2025-05-28 16:00 | SHORT | $2.3523 | $2.2275 | $7.00 | 5.31% | triple_top_breakdown | TP | 25 |
| 30 | 2025-05-30 12:00 | 2025-06-03 20:00 | SHORT | $2.1836 | $2.2446 | $-5.15 | -2.79% | triple_top_breakdown | Time | 26 |
| 31 | 2025-05-30 16:00 | 2025-06-04 00:00 | SHORT | $2.1860 | $2.2528 | $-4.50 | -3.06% | triple_top_breakdown | Time | 26 |
| 32 | 2025-05-30 20:00 | 2025-06-04 04:00 | SHORT | $2.1398 | $2.2340 | $-5.19 | -4.40% | triple_top_breakdown | Time | 26 |
| 35 | 2025-06-05 00:00 | 2025-06-05 20:00 | SHORT | $2.2054 | $2.0936 | $5.88 | 5.07% | triple_top_breakdown | TP | 5 |
| 33 | 2025-06-04 08:00 | 2025-06-08 16:00 | LONG | $2.2530 | $2.2884 | $2.85 | 1.57% | triple_bottom_breakout | Time | 26 |
| 34 | 2025-06-04 12:00 | 2025-06-08 20:00 | LONG | $2.2492 | $2.2670 | $1.15 | 0.79% | triple_bottom_breakout | Time | 26 |
| 36 | 2025-06-06 04:00 | 2025-06-10 12:00 | SHORT | $2.1303 | $2.2762 | $-8.02 | -6.85% | triple_top_breakdown | Time | 26 |
| 37 | 2025-06-09 12:00 | 2025-06-13 20:00 | LONG | $2.2632 | $2.1472 | $-8.19 | -5.13% | triple_bottom_breakout | Time | 26 |
| 38 | 2025-06-11 00:00 | 2025-06-15 08:00 | LONG | $2.2979 | $2.1590 | $-9.05 | -6.04% | triple_bottom_breakout | Time | 26 |
| 39 | 2025-06-11 04:00 | 2025-06-15 12:00 | LONG | $2.2931 | $2.1645 | $-6.71 | -5.61% | triple_bottom_breakout | Time | 26 |
| 40 | 2025-06-15 12:00 | 2025-06-19 20:00 | SHORT | $2.1645 | $2.1648 | $-0.02 | -0.01% | triple_top_breakdown | Time | 26 |
| 41 | 2025-06-15 16:00 | 2025-06-20 00:00 | SHORT | $2.1641 | $2.1550 | $0.59 | 0.42% | triple_top_breakdown | Time | 26 |
| 42 | 2025-06-15 20:00 | 2025-06-20 04:00 | SHORT | $2.1655 | $2.1667 | $-0.06 | -0.06% | triple_top_breakdown | Time | 26 |
| 44 | 2025-06-21 08:00 | 2025-06-22 08:00 | SHORT | $2.1371 | $2.0252 | $7.41 | 5.24% | triple_top_breakdown | TP | 6 |
| 43 | 2025-06-20 12:00 | 2025-06-22 08:00 | SHORT | $2.1338 | $2.0252 | $9.00 | 5.09% | triple_top_breakdown | TP | 11 |
| 45 | 2025-06-21 20:00 | 2025-06-22 12:00 | SHORT | $2.0632 | $1.9343 | $7.07 | 6.25% | triple_top_breakdown | TP | 4 |
| 46 | 2025-06-22 08:00 | 2025-06-26 16:00 | SHORT | $2.0252 | $2.1252 | $-7.78 | -4.94% | triple_top_breakdown | Time | 26 |
| 47 | 2025-06-23 00:00 | 2025-06-27 08:00 | SHORT | $2.0180 | $2.0909 | $-5.42 | -3.61% | triple_top_breakdown | Time | 26 |
| 48 | 2025-06-23 08:00 | 2025-06-27 16:00 | SHORT | $2.0013 | $2.0939 | $-5.56 | -4.63% | triple_top_breakdown | Time | 26 |
| 51 | 2025-06-27 16:00 | 2025-06-28 12:00 | LONG | $2.0939 | $2.2038 | $6.65 | 5.25% | triple_bottom_breakout | TP | 5 |
| 49 | 2025-06-27 00:00 | 2025-06-29 16:00 | LONG | $2.1053 | $2.1886 | $4.99 | 3.96% | triple_bottom_breakout | End | 16 |
| 50 | 2025-06-27 08:00 | 2025-06-29 16:00 | SHORT | $2.0909 | $2.1886 | $-6.06 | -4.67% | triple_top_breakdown | End | 14 |
| 52 | 2025-06-28 20:00 | 2025-06-29 16:00 | LONG | $2.1854 | $2.1886 | $0.19 | 0.15% | triple_bottom_breakout | End | 5 |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with -10.49% return vs -15.14%.

### Key Observations:
- **Trade Frequency**: 88 vs 53 trades
- **Win Rate Difference**: 39.77% vs 39.62%
- **Return Difference**: 4.65% gap
- **Position Management**: Up to 3 positions at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)
- **Position Size**: 20.0% of capital per position

---
*Báo cáo được tạo tự động bởi Triple Pattern Multi-Position Backtest System*
