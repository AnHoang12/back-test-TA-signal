# Triple Pattern Strategy Comparison - Multi Position - BTCUSDT 6h

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
| Total Trades | 55 | 31 |
| Win Rate | 60.00% | 77.42% |
| Total Return | 4.46% | 8.04% |
| Final Capital | $1044.65 | $1080.41 |
| Total PnL | $44.65 | $80.41 |
| Average PnL per Trade | $0.81 | $2.59 |
| Best Trade | $9.89 | $10.58 |
| Worst Trade | $-7.35 | $-14.77 |
| Long Trades | 42 | 23 |
| Short Trades | 13 | 8 |
| Max Concurrent Positions | 3 | 3 |

## Strategy 1: Exit after 9 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-04-13 06:00 | 2025-04-15 12:00 | LONG | $84528.6600 | $84483.2300 | $-0.11 | -0.05% | triple_bottom_breakout | Time | 9 |
| 1 | 2025-04-14 12:00 | 2025-04-16 18:00 | LONG | $84859.7300 | $84030.3800 | $-1.56 | -0.98% | triple_bottom_breakout | Time | 9 |
| 2 | 2025-04-15 06:00 | 2025-04-17 12:00 | LONG | $85589.2300 | $85108.6600 | $-0.72 | -0.56% | triple_bottom_breakout | Time | 9 |
| 3 | 2025-04-16 06:00 | 2025-04-18 12:00 | LONG | $84048.1100 | $84571.9200 | $0.89 | 0.62% | triple_bottom_breakout | Time | 9 |
| 4 | 2025-04-18 06:00 | 2025-04-20 12:00 | LONG | $84669.1100 | $84581.9800 | $-0.18 | -0.10% | triple_bottom_breakout | Time | 9 |
| 5 | 2025-04-19 12:00 | 2025-04-21 18:00 | LONG | $85239.9200 | $87516.2300 | $4.42 | 2.67% | triple_bottom_breakout | Time | 9 |
| 6 | 2025-04-20 00:00 | 2025-04-22 06:00 | LONG | $85088.5400 | $88614.1000 | $5.49 | 4.14% | triple_bottom_breakout | Time | 9 |
| 7 | 2025-04-21 12:00 | 2025-04-22 12:00 | LONG | $86847.3900 | $91396.1400 | $7.34 | 5.24% | triple_bottom_breakout | TP | 4 |
| 8 | 2025-04-21 18:00 | 2025-04-22 18:00 | LONG | $87516.2300 | $93442.9900 | $9.89 | 6.77% | triple_bottom_breakout | TP | 4 |
| 9 | 2025-04-23 00:00 | 2025-04-25 06:00 | LONG | $93478.4200 | $94635.6700 | $2.54 | 1.24% | triple_bottom_breakout | Time | 9 |
| 10 | 2025-04-23 06:00 | 2025-04-25 12:00 | LONG | $93466.0100 | $94527.7900 | $1.86 | 1.14% | triple_bottom_breakout | Time | 9 |
| 11 | 2025-04-24 06:00 | 2025-04-26 12:00 | LONG | $92619.9400 | $94316.7900 | $2.40 | 1.83% | triple_bottom_breakout | Time | 9 |
| 12 | 2025-04-25 12:00 | 2025-04-27 18:00 | LONG | $94527.7900 | $93749.3000 | $-1.48 | -0.82% | triple_bottom_breakout | Time | 9 |
| 13 | 2025-04-26 00:00 | 2025-04-28 06:00 | LONG | $94626.4700 | $95319.9900 | $1.05 | 0.73% | triple_bottom_breakout | Time | 9 |
| 14 | 2025-04-27 06:00 | 2025-04-29 12:00 | LONG | $93920.0100 | $95231.3700 | $1.98 | 1.40% | triple_bottom_breakout | Time | 9 |
| 15 | 2025-04-28 00:00 | 2025-04-30 06:00 | LONG | $94224.2800 | $95176.6600 | $1.51 | 1.01% | triple_bottom_breakout | Time | 9 |
| 16 | 2025-04-30 18:00 | 2025-05-03 00:00 | LONG | $94172.0000 | $96417.1400 | $4.94 | 2.38% | triple_bottom_breakout | Time | 9 |
| 17 | 2025-05-04 12:00 | 2025-05-06 18:00 | SHORT | $95410.0800 | $96834.0200 | $-3.11 | -1.49% | triple_top_breakdown | Time | 9 |
| 18 | 2025-05-09 00:00 | 2025-05-11 06:00 | LONG | $102979.3500 | $104652.0100 | $3.37 | 1.62% | triple_bottom_breakout | Time | 9 |
| 19 | 2025-05-09 06:00 | 2025-05-11 12:00 | LONG | $102958.3100 | $104036.7000 | $1.74 | 1.05% | triple_bottom_breakout | Time | 9 |
| 20 | 2025-05-10 06:00 | 2025-05-12 12:00 | LONG | $103434.9400 | $102556.1900 | $-1.13 | -0.85% | triple_bottom_breakout | Time | 9 |
| 21 | 2025-05-11 18:00 | 2025-05-14 00:00 | LONG | $104118.0000 | $103896.7100 | $-0.39 | -0.21% | triple_bottom_breakout | Time | 9 |
| 22 | 2025-05-12 06:00 | 2025-05-14 12:00 | LONG | $103762.9000 | $103246.7900 | $-0.72 | -0.50% | triple_bottom_breakout | Time | 9 |
| 23 | 2025-05-12 18:00 | 2025-05-15 00:00 | LONG | $102791.3200 | $102375.3100 | $-0.58 | -0.40% | triple_bottom_breakout | Time | 9 |
| 24 | 2025-05-14 00:00 | 2025-05-16 06:00 | LONG | $103896.7100 | $103651.7100 | $-0.35 | -0.24% | triple_bottom_breakout | Time | 9 |
| 25 | 2025-05-15 00:00 | 2025-05-17 06:00 | SHORT | $102375.3100 | $102994.1700 | $-1.07 | -0.60% | triple_top_breakdown | Time | 9 |
| 26 | 2025-05-15 06:00 | 2025-05-17 12:00 | LONG | $102371.6100 | $103130.4300 | $1.05 | 0.74% | triple_bottom_breakout | Time | 9 |
| 27 | 2025-05-17 18:00 | 2025-05-20 00:00 | LONG | $103126.6500 | $106105.2600 | $6.00 | 2.89% | triple_bottom_breakout | Time | 9 |
| 28 | 2025-05-19 12:00 | 2025-05-21 18:00 | LONG | $105380.9500 | $109643.9900 | $6.73 | 4.05% | triple_bottom_breakout | Time | 9 |
| 29 | 2025-05-20 12:00 | 2025-05-22 18:00 | LONG | $106200.3100 | $111696.2100 | $9.10 | 5.18% | triple_bottom_breakout | TP | 9 |
| 30 | 2025-05-21 12:00 | 2025-05-23 18:00 | LONG | $106592.7900 | $107318.3000 | $0.96 | 0.68% | triple_bottom_breakout | Time | 9 |
| 31 | 2025-05-22 06:00 | 2025-05-24 12:00 | LONG | $110981.9700 | $108920.0300 | $-2.73 | -1.86% | triple_bottom_breakout | Time | 9 |
| 32 | 2025-05-25 06:00 | 2025-05-27 12:00 | SHORT | $107260.0000 | $110232.4600 | $-5.87 | -2.77% | triple_top_breakdown | Time | 9 |
| 33 | 2025-05-25 12:00 | 2025-05-27 18:00 | LONG | $107363.3700 | $108938.1700 | $2.49 | 1.47% | triple_bottom_breakout | Time | 9 |
| 34 | 2025-05-26 12:00 | 2025-05-28 18:00 | SHORT | $109171.9100 | $107781.7800 | $1.73 | 1.27% | triple_top_breakdown | Time | 9 |
| 35 | 2025-05-28 00:00 | 2025-05-30 06:00 | LONG | $109000.0000 | $105880.5100 | $-5.27 | -2.86% | triple_bottom_breakout | Time | 9 |
| 36 | 2025-05-28 18:00 | 2025-05-31 00:00 | LONG | $107781.7800 | $103538.9400 | $-6.88 | -3.94% | triple_bottom_breakout | Time | 9 |
| 37 | 2025-05-29 00:00 | 2025-05-31 06:00 | LONG | $107681.8100 | $103498.1800 | $-5.43 | -3.89% | triple_bottom_breakout | Time | 9 |
| 38 | 2025-05-31 06:00 | 2025-06-02 12:00 | SHORT | $103498.1800 | $104399.8900 | $-1.81 | -0.87% | triple_top_breakdown | Time | 9 |
| 39 | 2025-06-01 00:00 | 2025-06-03 06:00 | SHORT | $104536.5700 | $105287.2400 | $-1.19 | -0.72% | triple_top_breakdown | Time | 9 |
| 40 | 2025-06-01 12:00 | 2025-06-03 18:00 | LONG | $105066.3300 | $105376.8900 | $0.39 | 0.30% | triple_bottom_breakout | Time | 9 |
| 41 | 2025-06-03 06:00 | 2025-06-05 12:00 | LONG | $105287.2400 | $103240.0400 | $-3.51 | -1.94% | triple_bottom_breakout | Time | 9 |
| 42 | 2025-06-04 00:00 | 2025-06-06 06:00 | LONG | $105354.1400 | $103927.9900 | $-2.32 | -1.35% | triple_bottom_breakout | Time | 9 |
| 43 | 2025-06-04 06:00 | 2025-06-06 12:00 | SHORT | $105084.3600 | $104922.1400 | $0.21 | 0.15% | triple_top_breakdown | Time | 9 |
| 44 | 2025-06-07 18:00 | 2025-06-10 00:00 | SHORT | $105552.1500 | $109310.4900 | $-7.35 | -3.56% | triple_top_breakdown | Time | 9 |
| 45 | 2025-06-15 06:00 | 2025-06-17 12:00 | SHORT | $104970.5100 | $103814.0100 | $2.26 | 1.10% | triple_top_breakdown | Time | 9 |
| 46 | 2025-06-15 18:00 | 2025-06-18 00:00 | SHORT | $105594.0100 | $105423.5000 | $0.26 | 0.16% | triple_top_breakdown | Time | 9 |
| 47 | 2025-06-16 18:00 | 2025-06-19 00:00 | SHORT | $106794.5300 | $104892.8600 | $2.33 | 1.78% | triple_top_breakdown | Time | 9 |
| 48 | 2025-06-19 00:00 | 2025-06-21 06:00 | SHORT | $104892.8600 | $103874.6400 | $2.00 | 0.97% | triple_top_breakdown | Time | 9 |
| 49 | 2025-06-20 18:00 | 2025-06-23 00:00 | SHORT | $103297.9900 | $101771.0200 | $2.43 | 1.48% | triple_top_breakdown | Time | 9 |
| 50 | 2025-06-24 00:00 | 2025-06-26 06:00 | LONG | $105396.5400 | $107325.4100 | $3.78 | 1.83% | triple_bottom_breakout | Time | 9 |
| 51 | 2025-06-24 12:00 | 2025-06-26 18:00 | LONG | $106046.6900 | $106947.0600 | $1.40 | 0.85% | triple_bottom_breakout | Time | 9 |
| 52 | 2025-06-24 18:00 | 2025-06-27 00:00 | LONG | $106083.0000 | $107267.7400 | $1.48 | 1.12% | triple_bottom_breakout | Time | 9 |
| 53 | 2025-06-27 12:00 | 2025-06-29 18:00 | LONG | $106875.7500 | $108356.9300 | $2.88 | 1.39% | triple_bottom_breakout | Time | 9 |
| 54 | 2025-06-29 00:00 | 2025-06-30 00:00 | LONG | $107309.9900 | $108280.6500 | $1.51 | 0.90% | triple_bottom_breakout | End | 4 |

## Strategy 2: Exit after 26 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-04-13 06:00 | 2025-04-19 18:00 | LONG | $84528.6600 | $85077.0100 | $1.30 | 0.65% | triple_bottom_breakout | Time | 26 |
| 1 | 2025-04-14 12:00 | 2025-04-21 00:00 | LONG | $84859.7300 | $87550.0000 | $5.07 | 3.17% | triple_bottom_breakout | Time | 26 |
| 2 | 2025-04-15 06:00 | 2025-04-21 18:00 | LONG | $85589.2300 | $87516.2300 | $2.88 | 2.25% | triple_bottom_breakout | Time | 26 |
| 4 | 2025-04-21 12:00 | 2025-04-22 12:00 | LONG | $86847.3900 | $91396.1400 | $7.71 | 5.24% | triple_bottom_breakout | TP | 4 |
| 3 | 2025-04-20 00:00 | 2025-04-22 12:00 | LONG | $85088.5400 | $91396.1400 | $10.58 | 7.41% | triple_bottom_breakout | TP | 10 |
| 5 | 2025-04-21 18:00 | 2025-04-22 18:00 | LONG | $87516.2300 | $93442.9900 | $9.74 | 6.77% | triple_bottom_breakout | TP | 4 |
| 6 | 2025-04-23 00:00 | 2025-04-29 12:00 | LONG | $93478.4200 | $95231.3700 | $3.89 | 1.88% | triple_bottom_breakout | Time | 26 |
| 7 | 2025-04-23 06:00 | 2025-04-29 18:00 | LONG | $93466.0100 | $94256.8200 | $1.40 | 0.85% | triple_bottom_breakout | Time | 26 |
| 8 | 2025-04-24 06:00 | 2025-04-30 18:00 | LONG | $92619.9400 | $94172.0000 | $2.22 | 1.68% | triple_bottom_breakout | Time | 26 |
| 9 | 2025-04-30 18:00 | 2025-05-07 06:00 | LONG | $94172.0000 | $97047.4300 | $6.38 | 3.05% | triple_bottom_breakout | Time | 26 |
| 10 | 2025-05-04 12:00 | 2025-05-11 00:00 | SHORT | $95410.0800 | $103840.0000 | $-14.77 | -8.84% | triple_top_breakdown | Time | 26 |
| 11 | 2025-05-09 00:00 | 2025-05-15 12:00 | LONG | $102979.3500 | $103968.2400 | $1.70 | 0.96% | triple_bottom_breakout | Time | 26 |
| 12 | 2025-05-09 06:00 | 2025-05-15 18:00 | LONG | $102958.3100 | $103763.7100 | $1.11 | 0.78% | triple_bottom_breakout | Time | 26 |
| 13 | 2025-05-11 18:00 | 2025-05-18 06:00 | LONG | $104118.0000 | $103800.5400 | $-0.44 | -0.30% | triple_bottom_breakout | Time | 26 |
| 15 | 2025-05-17 18:00 | 2025-05-21 18:00 | LONG | $103126.6500 | $109643.9900 | $9.06 | 6.32% | triple_bottom_breakout | TP | 16 |
| 14 | 2025-05-15 18:00 | 2025-05-21 18:00 | LONG | $103763.7100 | $109643.9900 | $10.15 | 5.67% | triple_bottom_breakout | TP | 24 |
| 16 | 2025-05-19 12:00 | 2025-05-22 00:00 | LONG | $105380.9500 | $110879.9900 | $7.48 | 5.22% | triple_bottom_breakout | TP | 10 |
| 17 | 2025-05-22 06:00 | 2025-05-28 18:00 | LONG | $110981.9700 | $107781.7800 | $-6.14 | -2.88% | triple_bottom_breakout | Time | 26 |
| 18 | 2025-05-25 06:00 | 2025-05-31 18:00 | SHORT | $107260.0000 | $104591.8800 | $4.24 | 2.49% | triple_top_breakdown | Time | 26 |
| 19 | 2025-05-25 12:00 | 2025-06-01 00:00 | LONG | $107363.3700 | $104536.5700 | $-3.59 | -2.63% | triple_bottom_breakout | Time | 26 |
| 20 | 2025-05-28 18:00 | 2025-06-04 06:00 | LONG | $107781.7800 | $105084.3600 | $-3.77 | -2.50% | triple_bottom_breakout | Time | 26 |
| 21 | 2025-06-01 00:00 | 2025-06-07 12:00 | SHORT | $104536.5700 | $105393.2100 | $-1.49 | -0.82% | triple_top_breakdown | Time | 26 |
| 22 | 2025-06-01 12:00 | 2025-06-08 00:00 | LONG | $105066.3300 | $105438.3400 | $0.52 | 0.35% | triple_bottom_breakout | Time | 26 |
| 23 | 2025-06-04 06:00 | 2025-06-10 18:00 | SHORT | $105084.3600 | $110274.3900 | $-7.20 | -4.94% | triple_top_breakdown | Time | 26 |
| 24 | 2025-06-07 18:00 | 2025-06-14 06:00 | SHORT | $105552.1500 | $105082.0100 | $0.68 | 0.45% | triple_top_breakdown | Time | 26 |
| 25 | 2025-06-15 06:00 | 2025-06-21 18:00 | SHORT | $104970.5100 | $102120.0100 | $5.70 | 2.72% | triple_top_breakdown | Time | 26 |
| 26 | 2025-06-15 18:00 | 2025-06-22 06:00 | SHORT | $105594.0100 | $102739.4800 | $4.54 | 2.70% | triple_top_breakdown | Time | 26 |
| 27 | 2025-06-16 18:00 | 2025-06-22 12:00 | SHORT | $106794.5300 | $99480.0000 | $9.19 | 6.85% | triple_top_breakdown | TP | 23 |
| 28 | 2025-06-24 00:00 | 2025-06-30 00:00 | LONG | $105396.5400 | $108280.6500 | $5.85 | 2.74% | triple_bottom_breakout | End | 24 |
| 29 | 2025-06-24 12:00 | 2025-06-30 00:00 | LONG | $106046.6900 | $108280.6500 | $3.60 | 2.11% | triple_bottom_breakout | End | 22 |
| 30 | 2025-06-24 18:00 | 2025-06-30 00:00 | LONG | $106083.0000 | $108280.6500 | $2.83 | 2.07% | triple_bottom_breakout | End | 21 |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 8.04% return vs 4.46%.

### Key Observations:
- **Trade Frequency**: 55 vs 31 trades
- **Win Rate Difference**: 60.00% vs 77.42%
- **Return Difference**: 3.58% gap
- **Position Management**: Up to 3 positions at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)
- **Position Size**: 20.0% of capital per position

---
*Báo cáo được tạo tự động bởi Triple Pattern Multi-Position Backtest System*
