# Triple Pattern Strategy Comparison - Multi Position - BNBUSDT 4h

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
| Total Trades | 70 | 46 |
| Win Rate | 45.71% | 47.83% |
| Total Return | -1.47% | -1.35% |
| Final Capital | $985.26 | $986.54 |
| Total PnL | $-14.74 | $-13.46 |
| Average PnL per Trade | $-0.21 | $-0.29 |
| Best Trade | $8.37 | $15.60 |
| Worst Trade | $-9.25 | $-12.43 |
| Long Trades | 45 | 28 |
| Short Trades | 25 | 18 |
| Max Concurrent Positions | 3 | 3 |

## Strategy 1: Exit after 9 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-04-07 20:00 | 2025-04-09 08:00 | SHORT | $554.6000 | $550.3400 | $1.54 | 0.77% | triple_top_breakdown | Time | 9 |
| 1 | 2025-04-12 00:00 | 2025-04-13 12:00 | SHORT | $585.0500 | $584.2200 | $0.28 | 0.14% | triple_top_breakdown | Time | 9 |
| 2 | 2025-04-12 04:00 | 2025-04-13 16:00 | LONG | $588.8900 | $582.7600 | $-1.67 | -1.04% | triple_bottom_breakout | Time | 9 |
| 3 | 2025-04-15 00:00 | 2025-04-16 12:00 | LONG | $587.6100 | $583.4400 | $-1.42 | -0.71% | triple_bottom_breakout | Time | 9 |
| 4 | 2025-04-17 20:00 | 2025-04-19 08:00 | LONG | $590.4900 | $591.0400 | $0.19 | 0.09% | triple_bottom_breakout | Time | 9 |
| 5 | 2025-04-18 00:00 | 2025-04-19 12:00 | LONG | $590.5000 | $589.4100 | $-0.29 | -0.18% | triple_bottom_breakout | Time | 9 |
| 6 | 2025-04-19 00:00 | 2025-04-20 12:00 | LONG | $593.3500 | $588.2000 | $-1.11 | -0.87% | triple_bottom_breakout | Time | 9 |
| 7 | 2025-04-21 20:00 | 2025-04-23 08:00 | LONG | $597.3400 | $611.1900 | $4.63 | 2.32% | triple_bottom_breakout | Time | 9 |
| 8 | 2025-04-22 00:00 | 2025-04-23 12:00 | LONG | $599.9800 | $606.6200 | $1.77 | 1.11% | triple_bottom_breakout | Time | 9 |
| 9 | 2025-04-22 20:00 | 2025-04-24 08:00 | LONG | $618.5100 | $597.6900 | $-4.30 | -3.37% | triple_bottom_breakout | Time | 9 |
| 10 | 2025-04-24 16:00 | 2025-04-26 04:00 | LONG | $598.9400 | $602.3200 | $1.13 | 0.56% | triple_bottom_breakout | Time | 9 |
| 11 | 2025-04-25 08:00 | 2025-04-26 20:00 | LONG | $605.8900 | $607.2300 | $0.35 | 0.22% | triple_bottom_breakout | Time | 9 |
| 12 | 2025-04-25 12:00 | 2025-04-27 00:00 | LONG | $605.5300 | $602.7700 | $-0.58 | -0.46% | triple_bottom_breakout | Time | 9 |
| 13 | 2025-04-26 04:00 | 2025-04-27 16:00 | LONG | $602.3200 | $605.4500 | $0.74 | 0.52% | triple_bottom_breakout | Time | 9 |
| 14 | 2025-04-28 00:00 | 2025-04-29 12:00 | SHORT | $603.8300 | $601.6100 | $0.74 | 0.37% | triple_top_breakdown | Time | 9 |
| 15 | 2025-04-28 12:00 | 2025-04-30 00:00 | SHORT | $600.9100 | $603.8700 | $-0.79 | -0.49% | triple_top_breakdown | Time | 9 |
| 16 | 2025-04-29 00:00 | 2025-04-30 12:00 | LONG | $606.5200 | $597.0900 | $-1.99 | -1.55% | triple_bottom_breakout | Time | 9 |
| 17 | 2025-05-06 04:00 | 2025-05-07 16:00 | LONG | $599.0400 | $599.0400 | $0.00 | 0.00% | triple_bottom_breakout | Time | 9 |
| 18 | 2025-05-07 04:00 | 2025-05-08 16:00 | LONG | $606.6000 | $619.4000 | $3.37 | 2.11% | triple_bottom_breakout | Time | 9 |
| 19 | 2025-05-07 08:00 | 2025-05-08 20:00 | LONG | $606.4900 | $629.1700 | $4.78 | 3.74% | triple_bottom_breakout | Time | 9 |
| 20 | 2025-05-09 12:00 | 2025-05-11 00:00 | LONG | $635.9000 | $662.3100 | $8.37 | 4.15% | triple_bottom_breakout | Time | 9 |
| 21 | 2025-05-10 04:00 | 2025-05-11 16:00 | LONG | $661.8600 | $653.4300 | $-2.05 | -1.27% | triple_bottom_breakout | Time | 9 |
| 22 | 2025-05-12 20:00 | 2025-05-14 08:00 | LONG | $660.0700 | $659.7000 | $-0.11 | -0.06% | triple_bottom_breakout | Time | 9 |
| 23 | 2025-05-13 00:00 | 2025-05-14 12:00 | SHORT | $641.9300 | $651.9200 | $-2.52 | -1.56% | triple_top_breakdown | Time | 9 |
| 24 | 2025-05-14 08:00 | 2025-05-15 20:00 | LONG | $659.7000 | $651.8800 | $-2.02 | -1.19% | triple_bottom_breakout | Time | 9 |
| 25 | 2025-05-14 16:00 | 2025-05-16 04:00 | LONG | $652.6200 | $655.4800 | $0.74 | 0.44% | triple_bottom_breakout | Time | 9 |
| 26 | 2025-05-14 20:00 | 2025-05-16 08:00 | LONG | $652.4700 | $654.3700 | $0.39 | 0.29% | triple_bottom_breakout | Time | 9 |
| 27 | 2025-05-15 20:00 | 2025-05-17 08:00 | LONG | $651.8800 | $641.5200 | $-2.25 | -1.59% | triple_bottom_breakout | Time | 9 |
| 28 | 2025-05-17 16:00 | 2025-05-19 04:00 | SHORT | $640.4200 | $638.6200 | $0.57 | 0.28% | triple_top_breakdown | Time | 9 |
| 29 | 2025-05-19 04:00 | 2025-05-20 16:00 | SHORT | $638.6200 | $648.0500 | $-2.98 | -1.48% | triple_top_breakdown | Time | 9 |
| 30 | 2025-05-19 20:00 | 2025-05-21 08:00 | SHORT | $649.6200 | $654.8600 | $-1.30 | -0.81% | triple_top_breakdown | Time | 9 |
| 31 | 2025-05-22 08:00 | 2025-05-23 20:00 | LONG | $687.1100 | $656.9800 | $-8.81 | -4.39% | triple_bottom_breakout | Time | 9 |
| 32 | 2025-05-23 12:00 | 2025-05-25 00:00 | LONG | $670.5600 | $665.9100 | $-1.11 | -0.69% | triple_bottom_breakout | Time | 9 |
| 33 | 2025-05-25 00:00 | 2025-05-26 12:00 | LONG | $665.9100 | $675.4100 | $2.84 | 1.43% | triple_bottom_breakout | Time | 9 |
| 34 | 2025-05-25 08:00 | 2025-05-26 20:00 | LONG | $661.8800 | $674.2900 | $2.98 | 1.87% | triple_bottom_breakout | Time | 9 |
| 35 | 2025-05-25 12:00 | 2025-05-27 00:00 | SHORT | $663.2000 | $674.1300 | $-2.10 | -1.65% | triple_top_breakdown | Time | 9 |
| 36 | 2025-05-26 12:00 | 2025-05-28 00:00 | LONG | $675.4100 | $684.3400 | $1.88 | 1.32% | triple_bottom_breakout | Time | 9 |
| 37 | 2025-05-27 00:00 | 2025-05-28 12:00 | LONG | $674.1300 | $681.8800 | $1.97 | 1.15% | triple_bottom_breakout | Time | 9 |
| 38 | 2025-05-29 04:00 | 2025-05-30 16:00 | LONG | $685.2900 | $666.3200 | $-5.55 | -2.77% | triple_bottom_breakout | Time | 9 |
| 39 | 2025-05-29 08:00 | 2025-05-30 20:00 | LONG | $685.7900 | $655.3600 | $-7.11 | -4.44% | triple_bottom_breakout | Time | 9 |
| 40 | 2025-05-29 20:00 | 2025-05-31 08:00 | LONG | $675.0200 | $654.0600 | $-3.98 | -3.11% | triple_bottom_breakout | Time | 9 |
| 41 | 2025-05-31 08:00 | 2025-06-01 20:00 | SHORT | $654.0600 | $660.7700 | $-2.02 | -1.03% | triple_top_breakdown | Time | 9 |
| 42 | 2025-05-31 20:00 | 2025-06-02 08:00 | SHORT | $658.0100 | $651.3200 | $1.60 | 1.02% | triple_top_breakdown | Time | 9 |
| 43 | 2025-06-01 16:00 | 2025-06-03 04:00 | SHORT | $655.0400 | $665.1000 | $-1.94 | -1.54% | triple_top_breakdown | Time | 9 |
| 44 | 2025-06-03 00:00 | 2025-06-04 12:00 | SHORT | $667.6500 | $669.4700 | $-0.47 | -0.27% | triple_top_breakdown | Time | 9 |
| 45 | 2025-06-03 08:00 | 2025-06-04 20:00 | LONG | $665.2000 | $663.2300 | $-0.48 | -0.30% | triple_bottom_breakout | Time | 9 |
| 46 | 2025-06-05 08:00 | 2025-06-06 20:00 | SHORT | $661.9900 | $642.7000 | $5.72 | 2.91% | triple_top_breakdown | Time | 9 |
| 47 | 2025-06-06 04:00 | 2025-06-07 16:00 | SHORT | $641.4600 | $652.0400 | $-2.59 | -1.65% | triple_top_breakdown | Time | 9 |
| 48 | 2025-06-06 12:00 | 2025-06-08 00:00 | SHORT | $647.6100 | $649.3500 | $-0.34 | -0.27% | triple_top_breakdown | Time | 9 |
| 49 | 2025-06-07 08:00 | 2025-06-08 20:00 | LONG | $648.3500 | $652.0000 | $0.79 | 0.56% | triple_bottom_breakout | Time | 9 |
| 50 | 2025-06-08 04:00 | 2025-06-09 16:00 | LONG | $649.2700 | $659.7000 | $2.71 | 1.61% | triple_bottom_breakout | Time | 9 |
| 51 | 2025-06-08 08:00 | 2025-06-09 20:00 | LONG | $650.4700 | $665.5800 | $3.14 | 2.32% | triple_bottom_breakout | Time | 9 |
| 52 | 2025-06-09 00:00 | 2025-06-10 12:00 | LONG | $651.5900 | $661.3000 | $2.03 | 1.49% | triple_bottom_breakout | Time | 9 |
| 53 | 2025-06-10 16:00 | 2025-06-12 04:00 | LONG | $667.5400 | $667.0500 | $-0.15 | -0.07% | triple_bottom_breakout | Time | 9 |
| 54 | 2025-06-11 04:00 | 2025-06-12 16:00 | LONG | $670.3900 | $658.4600 | $-2.83 | -1.78% | triple_bottom_breakout | Time | 9 |
| 55 | 2025-06-11 20:00 | 2025-06-13 08:00 | LONG | $667.4300 | $654.5100 | $-2.46 | -1.94% | triple_bottom_breakout | Time | 9 |
| 56 | 2025-06-12 16:00 | 2025-06-14 04:00 | SHORT | $658.4600 | $651.8400 | $1.74 | 1.01% | triple_top_breakdown | Time | 9 |
| 57 | 2025-06-13 08:00 | 2025-06-14 20:00 | SHORT | $654.5100 | $645.6100 | $2.22 | 1.36% | triple_top_breakdown | Time | 9 |
| 58 | 2025-06-15 04:00 | 2025-06-16 16:00 | SHORT | $649.0200 | $659.0300 | $-3.06 | -1.54% | triple_top_breakdown | Time | 9 |
| 59 | 2025-06-20 00:00 | 2025-06-21 12:00 | SHORT | $644.8100 | $636.8500 | $2.44 | 1.23% | triple_top_breakdown | Time | 9 |
| 60 | 2025-06-21 04:00 | 2025-06-22 12:00 | SHORT | $641.3800 | $607.6200 | $8.33 | 5.26% | triple_top_breakdown | TP | 8 |
| 61 | 2025-06-22 00:00 | 2025-06-23 12:00 | SHORT | $629.5000 | $622.9900 | $1.72 | 1.03% | triple_top_breakdown | Time | 9 |
| 62 | 2025-06-22 16:00 | 2025-06-24 04:00 | SHORT | $605.5300 | $639.1500 | $-9.25 | -5.55% | triple_top_breakdown | Time | 9 |
| 63 | 2025-06-23 08:00 | 2025-06-24 20:00 | SHORT | $617.2800 | $643.5300 | $-5.67 | -4.25% | triple_top_breakdown | Time | 9 |
| 64 | 2025-06-24 04:00 | 2025-06-25 16:00 | SHORT | $639.1500 | $647.6000 | $-2.27 | -1.32% | triple_top_breakdown | Time | 9 |
| 65 | 2025-06-24 12:00 | 2025-06-26 00:00 | LONG | $639.5800 | $648.5900 | $1.94 | 1.41% | triple_bottom_breakout | Time | 9 |
| 66 | 2025-06-26 00:00 | 2025-06-27 12:00 | LONG | $648.5900 | $646.6100 | $-0.60 | -0.31% | triple_bottom_breakout | Time | 9 |
| 67 | 2025-06-26 04:00 | 2025-06-27 16:00 | LONG | $647.5300 | $645.3000 | $-0.54 | -0.34% | triple_bottom_breakout | Time | 9 |
| 68 | 2025-06-26 16:00 | 2025-06-28 04:00 | LONG | $645.1900 | $647.0100 | $0.36 | 0.28% | triple_bottom_breakout | Time | 9 |
| 69 | 2025-06-29 00:00 | 2025-06-29 16:00 | LONG | $648.6700 | $648.6500 | $-0.01 | -0.00% | triple_bottom_breakout | End | 4 |

## Strategy 2: Exit after 26 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-04-07 20:00 | 2025-04-12 04:00 | SHORT | $554.6000 | $588.8900 | $-12.37 | -6.18% | triple_top_breakdown | Time | 26 |
| 1 | 2025-04-12 00:00 | 2025-04-16 08:00 | SHORT | $585.0500 | $582.0900 | $0.81 | 0.51% | triple_top_breakdown | Time | 26 |
| 2 | 2025-04-12 04:00 | 2025-04-16 12:00 | LONG | $588.8900 | $583.4400 | $-1.53 | -0.93% | triple_bottom_breakout | Time | 26 |
| 3 | 2025-04-15 00:00 | 2025-04-19 08:00 | LONG | $587.6100 | $591.0400 | $0.77 | 0.58% | triple_bottom_breakout | Time | 26 |
| 4 | 2025-04-17 20:00 | 2025-04-22 04:00 | LONG | $590.4900 | $604.3100 | $4.00 | 2.34% | triple_bottom_breakout | Time | 26 |
| 5 | 2025-04-18 00:00 | 2025-04-22 08:00 | LONG | $590.5000 | $605.8800 | $3.56 | 2.60% | triple_bottom_breakout | Time | 26 |
| 6 | 2025-04-21 20:00 | 2025-04-26 04:00 | LONG | $597.3400 | $602.3200 | $1.13 | 0.83% | triple_bottom_breakout | Time | 26 |
| 7 | 2025-04-22 20:00 | 2025-04-27 04:00 | LONG | $618.5100 | $599.9600 | $-5.15 | -3.00% | triple_bottom_breakout | Time | 26 |
| 8 | 2025-04-24 16:00 | 2025-04-29 00:00 | LONG | $598.9400 | $606.5200 | $1.74 | 1.27% | triple_bottom_breakout | Time | 26 |
| 9 | 2025-04-26 04:00 | 2025-04-30 12:00 | LONG | $602.3200 | $597.0900 | $-1.19 | -0.87% | triple_bottom_breakout | Time | 26 |
| 10 | 2025-04-28 00:00 | 2025-05-02 08:00 | SHORT | $603.8300 | $597.8500 | $1.42 | 0.99% | triple_top_breakdown | Time | 26 |
| 11 | 2025-04-29 00:00 | 2025-05-03 08:00 | LONG | $606.5200 | $596.3400 | $-2.39 | -1.68% | triple_bottom_breakout | Time | 26 |
| 12 | 2025-05-06 04:00 | 2025-05-08 20:00 | LONG | $599.0400 | $629.1700 | $9.97 | 5.03% | triple_bottom_breakout | TP | 16 |
| 14 | 2025-05-07 08:00 | 2025-05-09 20:00 | LONG | $606.4900 | $666.2900 | $12.50 | 9.86% | triple_bottom_breakout | TP | 15 |
| 13 | 2025-05-07 04:00 | 2025-05-09 20:00 | LONG | $606.6000 | $666.2900 | $15.60 | 9.84% | triple_bottom_breakout | TP | 16 |
| 15 | 2025-05-09 12:00 | 2025-05-12 08:00 | LONG | $635.9000 | $678.1000 | $9.50 | 6.64% | triple_bottom_breakout | TP | 17 |
| 16 | 2025-05-10 04:00 | 2025-05-14 12:00 | LONG | $661.8600 | $651.9200 | $-2.66 | -1.50% | triple_bottom_breakout | Time | 26 |
| 17 | 2025-05-12 20:00 | 2025-05-17 04:00 | LONG | $660.0700 | $643.0500 | $-4.44 | -2.58% | triple_bottom_breakout | Time | 26 |
| 18 | 2025-05-13 00:00 | 2025-05-17 08:00 | SHORT | $641.9300 | $641.5200 | $0.09 | 0.06% | triple_top_breakdown | Time | 26 |
| 19 | 2025-05-14 16:00 | 2025-05-19 00:00 | LONG | $652.6200 | $638.9300 | $-3.04 | -2.10% | triple_bottom_breakout | Time | 26 |
| 20 | 2025-05-17 16:00 | 2025-05-22 00:00 | SHORT | $640.4200 | $685.3400 | $-12.43 | -7.01% | triple_top_breakdown | Time | 26 |
| 21 | 2025-05-19 04:00 | 2025-05-23 12:00 | SHORT | $638.6200 | $670.5600 | $-8.51 | -5.00% | triple_top_breakdown | Time | 26 |
| 22 | 2025-05-19 20:00 | 2025-05-24 04:00 | SHORT | $649.6200 | $668.1700 | $-3.89 | -2.86% | triple_top_breakdown | Time | 26 |
| 23 | 2025-05-22 08:00 | 2025-05-26 16:00 | LONG | $687.1100 | $672.3200 | $-3.05 | -2.15% | triple_bottom_breakout | Time | 26 |
| 24 | 2025-05-23 12:00 | 2025-05-27 20:00 | LONG | $670.5600 | $686.9100 | $3.56 | 2.44% | triple_bottom_breakout | Time | 26 |
| 25 | 2025-05-25 00:00 | 2025-05-29 08:00 | LONG | $665.9100 | $685.7900 | $4.27 | 2.99% | triple_bottom_breakout | Time | 26 |
| 26 | 2025-05-27 00:00 | 2025-05-31 08:00 | LONG | $674.1300 | $654.0600 | $-4.24 | -2.98% | triple_bottom_breakout | Time | 26 |
| 27 | 2025-05-29 04:00 | 2025-06-02 12:00 | LONG | $685.2900 | $657.2300 | $-5.88 | -4.09% | triple_bottom_breakout | Time | 26 |
| 28 | 2025-05-29 08:00 | 2025-06-02 16:00 | LONG | $685.7900 | $661.1000 | $-5.20 | -3.60% | triple_bottom_breakout | Time | 26 |
| 29 | 2025-05-31 08:00 | 2025-06-04 16:00 | SHORT | $654.0600 | $667.4200 | $-2.92 | -2.04% | triple_top_breakdown | Time | 26 |
| 30 | 2025-06-03 00:00 | 2025-06-05 20:00 | SHORT | $667.6500 | $633.3200 | $8.74 | 5.14% | triple_top_breakdown | TP | 17 |
| 31 | 2025-06-03 08:00 | 2025-06-07 16:00 | LONG | $665.2000 | $652.0400 | $-2.69 | -1.98% | triple_bottom_breakout | Time | 26 |
| 32 | 2025-06-05 08:00 | 2025-06-09 16:00 | SHORT | $661.9900 | $659.7000 | $0.47 | 0.35% | triple_top_breakdown | Time | 26 |
| 33 | 2025-06-06 04:00 | 2025-06-10 12:00 | SHORT | $641.4600 | $661.3000 | $-4.49 | -3.09% | triple_top_breakdown | Time | 26 |
| 34 | 2025-06-08 04:00 | 2025-06-12 12:00 | LONG | $649.2700 | $660.2100 | $2.41 | 1.68% | triple_bottom_breakout | Time | 26 |
| 35 | 2025-06-10 16:00 | 2025-06-15 00:00 | LONG | $667.5400 | $647.5400 | $-5.09 | -3.00% | triple_bottom_breakout | Time | 26 |
| 36 | 2025-06-11 04:00 | 2025-06-15 12:00 | LONG | $670.3900 | $647.6900 | $-4.60 | -3.39% | triple_bottom_breakout | Time | 26 |
| 37 | 2025-06-12 16:00 | 2025-06-17 00:00 | SHORT | $658.4600 | $656.4000 | $0.43 | 0.31% | triple_top_breakdown | Time | 26 |
| 38 | 2025-06-15 04:00 | 2025-06-19 12:00 | SHORT | $649.0200 | $639.6600 | $2.06 | 1.44% | triple_top_breakdown | Time | 26 |
| 40 | 2025-06-21 04:00 | 2025-06-22 12:00 | SHORT | $641.3800 | $607.6200 | $8.31 | 5.26% | triple_top_breakdown | TP | 8 |
| 39 | 2025-06-20 00:00 | 2025-06-22 12:00 | SHORT | $644.8100 | $607.6200 | $11.39 | 5.77% | triple_top_breakdown | TP | 15 |
| 41 | 2025-06-22 00:00 | 2025-06-26 08:00 | SHORT | $629.5000 | $644.4800 | $-3.01 | -2.38% | triple_top_breakdown | Time | 26 |
| 42 | 2025-06-22 16:00 | 2025-06-27 00:00 | SHORT | $605.5300 | $645.8800 | $-11.74 | -6.66% | triple_top_breakdown | Time | 26 |
| 43 | 2025-06-23 08:00 | 2025-06-27 16:00 | SHORT | $617.2800 | $645.3000 | $-6.40 | -4.54% | triple_top_breakdown | Time | 26 |
| 44 | 2025-06-26 16:00 | 2025-06-29 16:00 | LONG | $645.1900 | $648.6500 | $0.74 | 0.54% | triple_bottom_breakout | End | 18 |
| 45 | 2025-06-29 00:00 | 2025-06-29 16:00 | LONG | $648.6700 | $648.6500 | $-0.01 | -0.00% | triple_bottom_breakout | End | 4 |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with -1.35% return vs -1.47%.

### Key Observations:
- **Trade Frequency**: 70 vs 46 trades
- **Win Rate Difference**: 45.71% vs 47.83%
- **Return Difference**: 0.13% gap
- **Position Management**: Up to 3 positions at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)
- **Position Size**: 20.0% of capital per position

---
*Báo cáo được tạo tự động bởi Triple Pattern Multi-Position Backtest System*
