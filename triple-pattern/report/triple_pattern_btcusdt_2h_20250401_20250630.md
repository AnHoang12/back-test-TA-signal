# Triple Pattern Strategy Comparison - BTCUSDT 2h

## Strategy Overview
- **Pattern**: Triple Top & Triple Bottom Pattern
- **Entry**: Breakout/breakdown with reversal candles
- **Reversal Candles**: Hammer, Engulfing, Doji patterns
- **Position Management**: Only 1 position at a time
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods
- **Take Profit**: 5.0%
- **Position Size**: 90.0% of capital

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 70 | 32 |
| Win Rate | 51.43% | 53.12% |
| Total Return | -4.67% | 12.38% |
| Final Capital | $953.32 | $1123.75 |
| Total PnL | $-46.68 | $123.75 |
| Average PnL per Trade | $-0.67 | $3.87 |
| Best Trade | $41.70 | $56.13 |
| Worst Trade | $-47.69 | $-37.48 |
| Long Trades | 48 | 24 |
| Short Trades | 22 | 8 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-04-04 14:00 | 2025-04-05 08:00 | LONG | $82860.0000 | $83843.2900 | $10.68 | 1.19% | triple_bottom_breakout | Time | 9 |
| 2025-04-05 08:00 | 2025-04-06 02:00 | LONG | $83843.2900 | $83344.1400 | $-5.42 | -0.60% | triple_bottom_breakout | Time | 9 |
| 2025-04-06 02:00 | 2025-04-06 20:00 | LONG | $83344.1400 | $78950.6100 | $-47.69 | -5.27% | triple_bottom_breakout | Time | 9 |
| 2025-04-07 10:00 | 2025-04-08 04:00 | SHORT | $76685.6200 | $79872.2500 | $-35.81 | -4.16% | triple_top_breakdown | Time | 9 |
| 2025-04-08 04:00 | 2025-04-08 22:00 | LONG | $79872.2500 | $76322.4200 | $-36.87 | -4.44% | triple_bottom_breakout | Time | 9 |
| 2025-04-09 18:00 | 2025-04-10 12:00 | LONG | $82332.0800 | $80874.3600 | $-14.10 | -1.77% | triple_bottom_breakout | Time | 9 |
| 2025-04-11 04:00 | 2025-04-11 22:00 | LONG | $80816.0000 | $83423.8400 | $25.29 | 3.23% | triple_bottom_breakout | Time | 9 |
| 2025-04-12 10:00 | 2025-04-13 04:00 | LONG | $83528.3000 | $84515.5800 | $9.53 | 1.18% | triple_bottom_breakout | Time | 9 |
| 2025-04-13 06:00 | 2025-04-14 00:00 | SHORT | $84413.1000 | $84228.0000 | $1.79 | 0.22% | triple_top_breakdown | Time | 9 |
| 2025-04-14 02:00 | 2025-04-14 20:00 | SHORT | $84566.0300 | $84706.1000 | $-1.35 | -0.17% | triple_top_breakdown | Time | 9 |
| 2025-04-15 12:00 | 2025-04-16 06:00 | LONG | $85589.4400 | $83363.1700 | $-21.21 | -2.60% | triple_bottom_breakout | Time | 9 |
| 2025-04-16 08:00 | 2025-04-17 02:00 | SHORT | $83600.0100 | $83994.2300 | $-3.76 | -0.47% | triple_top_breakdown | Time | 9 |
| 2025-04-17 14:00 | 2025-04-18 08:00 | LONG | $84531.7100 | $84548.9000 | $0.16 | 0.02% | triple_bottom_breakout | Time | 9 |
| 2025-04-18 10:00 | 2025-04-19 04:00 | LONG | $84669.1100 | $85079.9900 | $3.85 | 0.49% | triple_bottom_breakout | Time | 9 |
| 2025-04-21 12:00 | 2025-04-22 06:00 | LONG | $87028.0900 | $88476.8300 | $13.26 | 1.66% | triple_bottom_breakout | Time | 9 |
| 2025-04-22 06:00 | 2025-04-22 20:00 | LONG | $88476.8300 | $93039.9900 | $41.70 | 5.16% | triple_bottom_breakout | TP | 7 |
| 2025-04-23 20:00 | 2025-04-24 14:00 | LONG | $93485.5000 | $93202.5100 | $-2.56 | -0.30% | triple_bottom_breakout | Time | 9 |
| 2025-04-25 22:00 | 2025-04-26 16:00 | LONG | $94638.6800 | $94316.7900 | $-2.87 | -0.34% | triple_bottom_breakout | Time | 9 |
| 2025-04-26 16:00 | 2025-04-27 10:00 | LONG | $94316.7900 | $93920.0100 | $-3.54 | -0.42% | triple_bottom_breakout | Time | 9 |
| 2025-04-27 12:00 | 2025-04-28 06:00 | LONG | $94060.0900 | $94692.4900 | $5.63 | 0.67% | triple_bottom_breakout | Time | 9 |
| 2025-05-01 16:00 | 2025-05-02 10:00 | LONG | $96794.1700 | $96928.9700 | $1.17 | 0.14% | triple_bottom_breakout | Time | 9 |
| 2025-05-02 16:00 | 2025-05-03 10:00 | LONG | $97402.5500 | $95942.0200 | $-12.66 | -1.50% | triple_bottom_breakout | Time | 9 |
| 2025-05-03 12:00 | 2025-05-04 06:00 | LONG | $96330.0000 | $95879.9900 | $-3.89 | -0.47% | triple_bottom_breakout | Time | 9 |
| 2025-05-04 14:00 | 2025-05-05 08:00 | SHORT | $95467.6000 | $94550.6300 | $7.96 | 0.96% | triple_top_breakdown | Time | 9 |
| 2025-05-05 18:00 | 2025-05-06 12:00 | SHORT | $94347.1700 | $93616.9200 | $6.47 | 0.77% | triple_top_breakdown | Time | 9 |
| 2025-05-06 16:00 | 2025-05-07 10:00 | SHORT | $94535.9300 | $97047.4300 | $-22.37 | -2.66% | triple_top_breakdown | Time | 9 |
| 2025-05-07 10:00 | 2025-05-08 04:00 | LONG | $97047.4300 | $98740.6100 | $14.34 | 1.74% | triple_bottom_breakout | Time | 9 |
| 2025-05-08 06:00 | 2025-05-09 00:00 | LONG | $99252.3400 | $103098.3400 | $32.35 | 3.87% | triple_bottom_breakout | Time | 9 |
| 2025-05-09 00:00 | 2025-05-09 18:00 | LONG | $103098.3400 | $103189.1700 | $0.76 | 0.09% | triple_bottom_breakout | Time | 9 |
| 2025-05-09 18:00 | 2025-05-10 12:00 | LONG | $103189.1700 | $103628.8600 | $3.68 | 0.43% | triple_bottom_breakout | Time | 9 |
| 2025-05-10 16:00 | 2025-05-11 10:00 | LONG | $103176.8800 | $104652.0100 | $12.41 | 1.43% | triple_bottom_breakout | Time | 9 |
| 2025-05-11 16:00 | 2025-05-12 10:00 | LONG | $104036.7000 | $103762.9000 | $-2.31 | -0.26% | triple_bottom_breakout | Time | 9 |
| 2025-05-12 14:00 | 2025-05-13 08:00 | SHORT | $102527.2600 | $103457.0300 | $-7.95 | -0.91% | triple_top_breakdown | Time | 9 |
| 2025-05-13 12:00 | 2025-05-14 06:00 | LONG | $103715.8700 | $103716.5500 | $0.01 | 0.00% | triple_bottom_breakout | Time | 9 |
| 2025-05-14 08:00 | 2025-05-15 02:00 | LONG | $103485.7300 | $102753.6300 | $-6.15 | -0.71% | triple_bottom_breakout | Time | 9 |
| 2025-05-16 14:00 | 2025-05-17 08:00 | LONG | $104183.3300 | $102896.5900 | $-10.68 | -1.24% | triple_bottom_breakout | Time | 9 |
| 2025-05-19 18:00 | 2025-05-20 12:00 | LONG | $105517.7000 | $104448.0400 | $-8.67 | -1.01% | triple_bottom_breakout | Time | 9 |
| 2025-05-21 20:00 | 2025-05-22 14:00 | LONG | $108414.6400 | $111290.8600 | $22.47 | 2.65% | triple_bottom_breakout | Time | 9 |
| 2025-05-23 06:00 | 2025-05-24 00:00 | LONG | $110715.4200 | $107479.2400 | $-25.35 | -2.92% | triple_bottom_breakout | Time | 9 |
| 2025-05-24 16:00 | 2025-05-25 10:00 | SHORT | $108920.0300 | $107260.0000 | $12.87 | 1.52% | triple_top_breakdown | Time | 9 |
| 2025-05-25 22:00 | 2025-05-26 16:00 | LONG | $109004.1900 | $109171.9100 | $1.32 | 0.15% | triple_bottom_breakout | Time | 9 |
| 2025-05-26 18:00 | 2025-05-27 12:00 | LONG | $109130.4400 | $109837.2600 | $5.55 | 0.65% | triple_bottom_breakout | Time | 9 |
| 2025-05-27 14:00 | 2025-05-28 08:00 | LONG | $110140.1100 | $108789.1700 | $-10.58 | -1.23% | triple_bottom_breakout | Time | 9 |
| 2025-05-28 08:00 | 2025-05-29 02:00 | LONG | $108789.1700 | $108044.8800 | $-5.83 | -0.68% | triple_bottom_breakout | Time | 9 |
| 2025-05-29 22:00 | 2025-05-30 16:00 | SHORT | $105589.7500 | $104183.1500 | $11.29 | 1.33% | triple_top_breakdown | Time | 9 |
| 2025-05-30 20:00 | 2025-05-31 14:00 | SHORT | $104631.5900 | $104556.0800 | $0.62 | 0.07% | triple_top_breakdown | Time | 9 |
| 2025-06-01 18:00 | 2025-06-02 12:00 | LONG | $105121.9400 | $103800.0000 | $-10.79 | -1.26% | triple_bottom_breakout | Time | 9 |
| 2025-06-02 12:00 | 2025-06-03 06:00 | SHORT | $103800.0000 | $105170.7500 | $-11.20 | -1.32% | triple_top_breakdown | Time | 9 |
| 2025-06-03 08:00 | 2025-06-04 02:00 | LONG | $105198.1100 | $105519.2700 | $2.56 | 0.31% | triple_bottom_breakout | Time | 9 |
| 2025-06-04 20:00 | 2025-06-05 14:00 | LONG | $104930.6100 | $104531.4900 | $-3.20 | -0.38% | triple_bottom_breakout | Time | 9 |
| 2025-06-05 14:00 | 2025-06-06 08:00 | SHORT | $104531.4900 | $103643.9800 | $7.11 | 0.85% | triple_top_breakdown | Time | 9 |
| 2025-06-07 00:00 | 2025-06-07 18:00 | LONG | $104453.5600 | $105725.9100 | $10.28 | 1.22% | triple_bottom_breakout | Time | 9 |
| 2025-06-08 06:00 | 2025-06-09 00:00 | LONG | $105426.4500 | $105527.7100 | $0.82 | 0.10% | triple_bottom_breakout | Time | 9 |
| 2025-06-09 04:00 | 2025-06-09 22:00 | SHORT | $105379.1100 | $110263.0200 | $-39.59 | -4.63% | triple_top_breakdown | Time | 9 |
| 2025-06-10 10:00 | 2025-06-11 04:00 | LONG | $109541.2800 | $109468.0300 | $-0.55 | -0.07% | triple_bottom_breakout | Time | 9 |
| 2025-06-11 06:00 | 2025-06-12 00:00 | LONG | $109446.7400 | $108515.9900 | $-6.96 | -0.85% | triple_bottom_breakout | Time | 9 |
| 2025-06-12 04:00 | 2025-06-12 22:00 | LONG | $107746.9100 | $105671.7300 | $-15.64 | -1.93% | triple_bottom_breakout | Time | 9 |
| 2025-06-13 08:00 | 2025-06-14 02:00 | SHORT | $104830.3600 | $105228.8200 | $-3.03 | -0.38% | triple_top_breakdown | Time | 9 |
| 2025-06-14 18:00 | 2025-06-15 12:00 | SHORT | $104645.6700 | $105515.9700 | $-6.61 | -0.83% | triple_top_breakdown | Time | 9 |
| 2025-06-15 14:00 | 2025-06-16 08:00 | SHORT | $105564.0000 | $106945.8600 | $-10.33 | -1.31% | triple_top_breakdown | Time | 9 |
| 2025-06-17 22:00 | 2025-06-18 16:00 | SHORT | $104551.1700 | $104331.8300 | $1.64 | 0.21% | triple_top_breakdown | Time | 9 |
| 2025-06-19 14:00 | 2025-06-20 08:00 | SHORT | $104096.9300 | $105940.5800 | $-13.84 | -1.77% | triple_top_breakdown | Time | 9 |
| 2025-06-20 08:00 | 2025-06-21 02:00 | SHORT | $105940.5800 | $103495.8700 | $17.74 | 2.31% | triple_top_breakdown | Time | 9 |
| 2025-06-21 02:00 | 2025-06-21 20:00 | SHORT | $103495.8700 | $101455.6100 | $15.47 | 1.97% | triple_top_breakdown | Time | 9 |
| 2025-06-22 02:00 | 2025-06-22 20:00 | SHORT | $102375.4000 | $99173.8300 | $24.98 | 3.13% | triple_top_breakdown | Time | 9 |
| 2025-06-23 12:00 | 2025-06-24 06:00 | LONG | $102354.1400 | $104933.7400 | $20.70 | 2.52% | triple_bottom_breakout | Time | 9 |
| 2025-06-24 10:00 | 2025-06-25 04:00 | LONG | $105170.0000 | $106213.7200 | $8.33 | 0.99% | triple_bottom_breakout | Time | 9 |
| 2025-06-25 04:00 | 2025-06-25 22:00 | LONG | $106213.7200 | $107340.5800 | $8.99 | 1.06% | triple_bottom_breakout | Time | 9 |
| 2025-06-26 10:00 | 2025-06-27 04:00 | LONG | $107325.4100 | $107267.7400 | $-0.46 | -0.05% | triple_bottom_breakout | Time | 9 |
| 2025-06-27 22:00 | 2025-06-28 16:00 | LONG | $107047.5900 | $107465.1200 | $3.33 | 0.39% | triple_bottom_breakout | Time | 9 |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-04-04 14:00 | 2025-04-06 18:00 | LONG | $82860.0000 | $79614.3500 | $-35.25 | -3.92% | triple_bottom_breakout | Time | 26 |
| 2025-04-07 10:00 | 2025-04-09 14:00 | SHORT | $76685.6200 | $77258.0000 | $-6.48 | -0.75% | triple_top_breakdown | Time | 26 |
| 2025-04-09 18:00 | 2025-04-11 22:00 | LONG | $82332.0800 | $83423.8400 | $11.44 | 1.33% | triple_bottom_breakout | Time | 26 |
| 2025-04-12 10:00 | 2025-04-14 14:00 | LONG | $83528.3000 | $84101.1600 | $5.99 | 0.69% | triple_bottom_breakout | Time | 26 |
| 2025-04-15 12:00 | 2025-04-17 16:00 | LONG | $85589.4400 | $85108.6600 | $-4.93 | -0.56% | triple_bottom_breakout | Time | 26 |
| 2025-04-18 00:00 | 2025-04-20 04:00 | LONG | $84925.5800 | $85088.5400 | $1.68 | 0.19% | triple_bottom_breakout | Time | 26 |
| 2025-04-21 12:00 | 2025-04-22 16:00 | LONG | $87028.0900 | $91396.1400 | $43.93 | 5.02% | triple_bottom_breakout | TP | 14 |
| 2025-04-22 18:00 | 2025-04-24 22:00 | LONG | $91414.7900 | $93980.4700 | $25.67 | 2.81% | triple_bottom_breakout | Time | 26 |
| 2025-04-25 22:00 | 2025-04-28 02:00 | LONG | $94638.6800 | $93849.9300 | $-7.82 | -0.83% | triple_bottom_breakout | Time | 26 |
| 2025-05-01 16:00 | 2025-05-03 20:00 | LONG | $96794.1700 | $96266.1700 | $-5.08 | -0.55% | triple_bottom_breakout | Time | 26 |
| 2025-05-04 14:00 | 2025-05-06 18:00 | SHORT | $95467.6000 | $94963.5000 | $4.89 | 0.53% | triple_top_breakdown | Time | 26 |
| 2025-05-07 08:00 | 2025-05-08 20:00 | LONG | $96978.4000 | $102828.0300 | $56.13 | 6.03% | triple_bottom_breakout | TP | 18 |
| 2025-05-09 00:00 | 2025-05-11 04:00 | LONG | $103098.3400 | $103840.0000 | $7.06 | 0.72% | triple_bottom_breakout | Time | 26 |
| 2025-05-11 08:00 | 2025-05-13 12:00 | LONG | $104347.9400 | $103715.8700 | $-5.98 | -0.61% | triple_bottom_breakout | Time | 26 |
| 2025-05-13 12:00 | 2025-05-15 16:00 | LONG | $103715.8700 | $103968.2400 | $2.39 | 0.24% | triple_bottom_breakout | Time | 26 |
| 2025-05-16 14:00 | 2025-05-18 18:00 | LONG | $104183.3300 | $103883.9700 | $-2.83 | -0.29% | triple_bottom_breakout | Time | 26 |
| 2025-05-19 18:00 | 2025-05-21 22:00 | LONG | $105517.7000 | $109643.9900 | $38.39 | 3.91% | triple_bottom_breakout | Time | 26 |
| 2025-05-21 22:00 | 2025-05-24 02:00 | LONG | $109643.9900 | $108366.3000 | $-11.84 | -1.17% | triple_bottom_breakout | Time | 26 |
| 2025-05-24 16:00 | 2025-05-26 20:00 | SHORT | $108920.0300 | $109346.6800 | $-3.94 | -0.39% | triple_top_breakdown | Time | 26 |
| 2025-05-27 04:00 | 2025-05-29 08:00 | LONG | $108923.3600 | $108520.0100 | $-3.71 | -0.37% | triple_bottom_breakout | Time | 26 |
| 2025-05-29 22:00 | 2025-06-01 02:00 | SHORT | $105589.7500 | $104381.0300 | $11.43 | 1.14% | triple_top_breakdown | Time | 26 |
| 2025-06-01 18:00 | 2025-06-03 22:00 | LONG | $105121.9400 | $105376.8900 | $2.45 | 0.24% | triple_bottom_breakout | Time | 26 |
| 2025-06-04 20:00 | 2025-06-07 00:00 | LONG | $104930.6100 | $104453.5600 | $-4.60 | -0.45% | triple_bottom_breakout | Time | 26 |
| 2025-06-07 00:00 | 2025-06-09 04:00 | LONG | $104453.5600 | $105379.1100 | $8.92 | 0.89% | triple_bottom_breakout | Time | 26 |
| 2025-06-09 04:00 | 2025-06-11 08:00 | SHORT | $105379.1100 | $109269.8300 | $-37.48 | -3.69% | triple_top_breakdown | Time | 26 |
| 2025-06-11 10:00 | 2025-06-13 14:00 | LONG | $109252.0900 | $105436.8700 | $-34.27 | -3.49% | triple_bottom_breakout | Time | 26 |
| 2025-06-13 16:00 | 2025-06-15 20:00 | SHORT | $105390.9400 | $104807.7500 | $5.26 | 0.55% | triple_top_breakdown | Time | 26 |
| 2025-06-16 00:00 | 2025-06-18 04:00 | LONG | $105815.0800 | $105423.5000 | $-3.54 | -0.37% | triple_bottom_breakout | Time | 26 |
| 2025-06-18 06:00 | 2025-06-20 10:00 | SHORT | $104973.2400 | $105977.8200 | $-9.11 | -0.96% | triple_top_breakdown | Time | 26 |
| 2025-06-20 18:00 | 2025-06-22 22:00 | SHORT | $103307.2200 | $100963.8700 | $21.41 | 2.27% | triple_top_breakdown | Time | 26 |
| 2025-06-23 12:00 | 2025-06-25 12:00 | LONG | $102354.1400 | $107923.2100 | $52.41 | 5.44% | triple_bottom_breakout | TP | 24 |
| 2025-06-26 10:00 | 2025-06-28 14:00 | LONG | $107325.4100 | $107449.2800 | $1.17 | 0.12% | triple_bottom_breakout | Time | 26 |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 12.38% return vs -4.67%.

### Key Observations:
- **Trade Frequency**: 70 vs 32 trades
- **Win Rate Difference**: 51.43% vs 53.12%
- **Return Difference**: 17.04% gap
- **Position Management**: Only 1 position at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)

---
*Báo cáo được tạo tự động bởi Triple Pattern Backtest System*
