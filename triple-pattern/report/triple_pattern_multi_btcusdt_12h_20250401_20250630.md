# Triple Pattern Strategy Comparison - Multi Position - BTCUSDT 12h

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
| Total Trades | 28 | 17 |
| Win Rate | 71.43% | 70.59% |
| Total Return | 3.28% | 6.12% |
| Final Capital | $1032.85 | $1061.25 |
| Total PnL | $32.85 | $61.25 |
| Average PnL per Trade | $1.17 | $3.60 |
| Best Trade | $11.08 | $13.39 |
| Worst Trade | $-7.89 | $-6.93 |
| Long Trades | 22 | 13 |
| Short Trades | 6 | 4 |
| Max Concurrent Positions | 3 | 3 |

## Strategy 1: Exit after 9 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-04-23 00:00 | 2025-04-27 12:00 | LONG | $93466.0100 | $93749.3000 | $0.61 | 0.30% | triple_bottom_breakout | Time | 9 |
| 1 | 2025-04-23 12:00 | 2025-04-28 00:00 | LONG | $93691.0800 | $95319.9900 | $2.78 | 1.74% | triple_bottom_breakout | Time | 9 |
| 2 | 2025-04-25 12:00 | 2025-04-30 00:00 | LONG | $94638.6800 | $95176.6600 | $0.73 | 0.57% | triple_bottom_breakout | Time | 9 |
| 3 | 2025-04-28 00:00 | 2025-05-02 12:00 | LONG | $95319.9900 | $96887.1400 | $2.88 | 1.64% | triple_bottom_breakout | Time | 9 |
| 4 | 2025-04-29 00:00 | 2025-05-03 12:00 | LONG | $95129.7400 | $95856.4200 | $1.07 | 0.76% | triple_bottom_breakout | Time | 9 |
| 5 | 2025-05-02 12:00 | 2025-05-07 00:00 | LONG | $96887.1400 | $97047.4300 | $0.29 | 0.17% | triple_bottom_breakout | Time | 9 |
| 7 | 2025-05-07 12:00 | 2025-05-08 12:00 | LONG | $97030.5000 | $103261.6000 | $10.81 | 6.42% | triple_bottom_breakout | TP | 2 |
| 6 | 2025-05-06 12:00 | 2025-05-08 12:00 | LONG | $96834.0200 | $103261.6000 | $11.08 | 6.64% | triple_bottom_breakout | TP | 4 |
| 8 | 2025-05-09 12:00 | 2025-05-14 00:00 | LONG | $102971.9900 | $103944.9300 | $1.95 | 0.94% | triple_bottom_breakout | Time | 9 |
| 9 | 2025-05-11 00:00 | 2025-05-15 12:00 | LONG | $104652.0100 | $103763.7100 | $-1.40 | -0.85% | triple_bottom_breakout | Time | 9 |
| 10 | 2025-05-12 12:00 | 2025-05-17 00:00 | LONG | $102791.3200 | $102994.1700 | $0.26 | 0.20% | triple_bottom_breakout | Time | 9 |
| 11 | 2025-05-14 00:00 | 2025-05-18 12:00 | LONG | $103944.9300 | $106454.2600 | $3.55 | 2.41% | triple_bottom_breakout | Time | 9 |
| 12 | 2025-05-16 00:00 | 2025-05-20 12:00 | LONG | $103651.7100 | $106849.9900 | $4.64 | 3.09% | triple_bottom_breakout | Time | 9 |
| 13 | 2025-05-20 12:00 | 2025-05-25 00:00 | LONG | $106849.9900 | $107260.0000 | $0.80 | 0.38% | triple_bottom_breakout | Time | 9 |
| 14 | 2025-05-21 12:00 | 2025-05-26 00:00 | LONG | $109643.9900 | $109772.7200 | $0.20 | 0.12% | triple_bottom_breakout | Time | 9 |
| 15 | 2025-05-25 12:00 | 2025-05-30 00:00 | LONG | $109004.1900 | $105880.5100 | $-5.01 | -2.87% | triple_bottom_breakout | Time | 9 |
| 16 | 2025-05-27 00:00 | 2025-05-31 12:00 | LONG | $109585.4900 | $104591.8800 | $-7.89 | -4.56% | triple_bottom_breakout | Time | 9 |
| 17 | 2025-05-28 00:00 | 2025-06-01 12:00 | LONG | $108870.3800 | $105642.9300 | $-4.11 | -2.96% | triple_bottom_breakout | Time | 9 |
| 18 | 2025-06-01 12:00 | 2025-06-06 00:00 | LONG | $105642.9300 | $103927.9900 | $-3.32 | -1.62% | triple_bottom_breakout | Time | 9 |
| 19 | 2025-06-03 12:00 | 2025-06-08 00:00 | SHORT | $105376.8900 | $105686.7100 | $-0.48 | -0.29% | triple_top_breakdown | Time | 9 |
| 20 | 2025-06-04 00:00 | 2025-06-08 12:00 | SHORT | $105084.3600 | $105734.0000 | $-0.81 | -0.62% | triple_top_breakdown | Time | 9 |
| 21 | 2025-06-08 12:00 | 2025-06-13 00:00 | SHORT | $105734.0000 | $105039.4800 | $1.34 | 0.66% | triple_top_breakdown | Time | 9 |
| 22 | 2025-06-16 12:00 | 2025-06-21 00:00 | SHORT | $106794.5300 | $103874.6400 | $5.58 | 2.73% | triple_top_breakdown | Time | 9 |
| 23 | 2025-06-18 12:00 | 2025-06-23 00:00 | SHORT | $104886.7800 | $101289.0100 | $5.60 | 3.43% | triple_top_breakdown | Time | 9 |
| 24 | 2025-06-19 00:00 | 2025-06-23 12:00 | SHORT | $104776.2300 | $105333.9300 | $-0.69 | -0.53% | triple_top_breakdown | Time | 9 |
| 25 | 2025-06-26 00:00 | 2025-06-30 00:00 | LONG | $107325.4100 | $107654.2000 | $0.63 | 0.31% | triple_bottom_breakout | End | 8 |
| 26 | 2025-06-27 00:00 | 2025-06-30 00:00 | LONG | $106983.6000 | $107654.2000 | $1.03 | 0.63% | triple_bottom_breakout | End | 6 |
| 27 | 2025-06-27 12:00 | 2025-06-30 00:00 | LONG | $107047.5900 | $107654.2000 | $0.75 | 0.57% | triple_bottom_breakout | End | 5 |

## Strategy 2: Exit after 26 periods

| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 0 | 2025-04-23 00:00 | 2025-05-06 00:00 | LONG | $93466.0100 | $93812.5400 | $0.74 | 0.37% | triple_bottom_breakout | Time | 26 |
| 1 | 2025-04-23 12:00 | 2025-05-06 12:00 | LONG | $93691.0800 | $96834.0200 | $5.37 | 3.35% | triple_bottom_breakout | Time | 26 |
| 2 | 2025-04-25 12:00 | 2025-05-08 00:00 | LONG | $94638.6800 | $99409.1400 | $6.45 | 5.04% | triple_bottom_breakout | TP | 25 |
| 4 | 2025-05-07 12:00 | 2025-05-08 12:00 | LONG | $97030.5000 | $103261.6000 | $9.02 | 6.42% | triple_bottom_breakout | TP | 2 |
| 3 | 2025-05-06 12:00 | 2025-05-08 12:00 | LONG | $96834.0200 | $103261.6000 | $11.66 | 6.64% | triple_bottom_breakout | TP | 4 |
| 7 | 2025-05-12 12:00 | 2025-05-21 12:00 | LONG | $102791.3200 | $109643.9900 | $8.82 | 6.67% | triple_bottom_breakout | TP | 18 |
| 5 | 2025-05-09 12:00 | 2025-05-21 12:00 | LONG | $102971.9900 | $109643.9900 | $13.39 | 6.48% | triple_bottom_breakout | TP | 24 |
| 6 | 2025-05-11 00:00 | 2025-05-22 00:00 | LONG | $104652.0100 | $110981.9700 | $10.00 | 6.05% | triple_bottom_breakout | TP | 22 |
| 8 | 2025-05-21 12:00 | 2025-06-03 12:00 | LONG | $109643.9900 | $105376.8900 | $-6.93 | -3.89% | triple_bottom_breakout | Time | 26 |
| 9 | 2025-05-25 12:00 | 2025-06-07 12:00 | LONG | $109004.1900 | $105552.1500 | $-5.62 | -3.17% | triple_bottom_breakout | Time | 26 |
| 10 | 2025-05-27 00:00 | 2025-06-09 00:00 | LONG | $109585.4900 | $107759.2100 | $-2.37 | -1.67% | triple_bottom_breakout | Time | 26 |
| 11 | 2025-06-03 12:00 | 2025-06-16 12:00 | SHORT | $105376.8900 | $106794.5300 | $-1.99 | -1.35% | triple_top_breakdown | Time | 26 |
| 12 | 2025-06-08 12:00 | 2025-06-21 12:00 | SHORT | $105734.0000 | $102120.0100 | $5.22 | 3.42% | triple_top_breakdown | Time | 26 |
| 13 | 2025-06-16 12:00 | 2025-06-22 12:00 | SHORT | $106794.5300 | $100963.8700 | $9.78 | 5.46% | triple_top_breakdown | TP | 12 |
| 14 | 2025-06-18 12:00 | 2025-06-30 00:00 | SHORT | $104886.7800 | $107654.2000 | $-3.78 | -2.64% | triple_top_breakdown | End | 23 |
| 15 | 2025-06-26 00:00 | 2025-06-30 00:00 | LONG | $107325.4100 | $107654.2000 | $0.56 | 0.31% | triple_bottom_breakout | End | 8 |
| 16 | 2025-06-27 00:00 | 2025-06-30 00:00 | LONG | $106983.6000 | $107654.2000 | $0.92 | 0.63% | triple_bottom_breakout | End | 6 |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 6.12% return vs 3.28%.

### Key Observations:
- **Trade Frequency**: 28 vs 17 trades
- **Win Rate Difference**: 71.43% vs 70.59%
- **Return Difference**: 2.84% gap
- **Position Management**: Up to 3 positions at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)
- **Position Size**: 20.0% of capital per position

---
*Báo cáo được tạo tự động bởi Triple Pattern Multi-Position Backtest System*
