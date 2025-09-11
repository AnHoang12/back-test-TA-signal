# Triple Pattern Strategy Comparison - SOLUSDT 6h

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
| Total Trades | 23 | 12 |
| Win Rate | 30.43% | 33.33% |
| Total Return | -38.80% | -40.59% |
| Final Capital | $611.99 | $594.08 |
| Total PnL | $-388.01 | $-405.92 |
| Average PnL per Trade | $-16.87 | $-33.83 |
| Best Trade | $53.98 | $42.88 |
| Worst Trade | $-85.59 | $-183.60 |
| Long Trades | 14 | 5 |
| Short Trades | 9 | 7 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-04-16 12:00 | 2025-04-18 18:00 | SHORT | $125.1500 | $134.0400 | $-63.93 | -7.10% | triple_top_breakdown | Time | 9 |
| 2025-04-18 18:00 | 2025-04-20 00:00 | LONG | $134.0400 | $140.7700 | $42.30 | 5.02% | triple_bottom_breakout | TP | 5 |
| 2025-04-20 12:00 | 2025-04-22 12:00 | LONG | $136.3700 | $144.7300 | $53.98 | 6.13% | triple_bottom_breakout | TP | 8 |
| 2025-04-25 18:00 | 2025-04-28 00:00 | LONG | $150.8200 | $149.7400 | $-6.65 | -0.72% | triple_bottom_breakout | Time | 9 |
| 2025-04-28 00:00 | 2025-04-30 06:00 | LONG | $149.7400 | $147.9400 | $-11.10 | -1.20% | triple_bottom_breakout | Time | 9 |
| 2025-05-01 18:00 | 2025-05-04 00:00 | LONG | $150.8500 | $146.2400 | $-27.91 | -3.06% | triple_bottom_breakout | Time | 9 |
| 2025-05-09 12:00 | 2025-05-11 18:00 | LONG | $171.9700 | $173.1900 | $6.30 | 0.71% | triple_bottom_breakout | Time | 9 |
| 2025-05-12 06:00 | 2025-05-13 18:00 | LONG | $174.1100 | $183.7500 | $49.48 | 5.54% | triple_bottom_breakout | TP | 6 |
| 2025-05-14 06:00 | 2025-05-16 12:00 | LONG | $181.0600 | $170.3800 | $-55.34 | -5.90% | triple_bottom_breakout | Time | 9 |
| 2025-05-17 00:00 | 2025-05-19 06:00 | LONG | $167.5000 | $162.1900 | $-28.16 | -3.17% | triple_bottom_breakout | Time | 9 |
| 2025-05-21 12:00 | 2025-05-23 18:00 | SHORT | $167.1300 | $174.0100 | $-35.53 | -4.12% | triple_top_breakdown | Time | 9 |
| 2025-05-24 12:00 | 2025-05-26 18:00 | LONG | $176.8500 | $174.9100 | $-9.12 | -1.10% | triple_bottom_breakout | Time | 9 |
| 2025-05-28 06:00 | 2025-05-30 12:00 | LONG | $174.5100 | $158.5700 | $-75.16 | -9.13% | triple_bottom_breakout | Time | 9 |
| 2025-06-02 12:00 | 2025-06-04 18:00 | SHORT | $153.6700 | $153.2600 | $2.02 | 0.27% | triple_top_breakdown | Time | 9 |
| 2025-06-05 06:00 | 2025-06-05 18:00 | SHORT | $152.3700 | $144.2900 | $40.15 | 5.30% | triple_top_breakdown | TP | 2 |
| 2025-06-06 12:00 | 2025-06-08 18:00 | SHORT | $150.1000 | $152.4500 | $-12.42 | -1.57% | triple_top_breakdown | Time | 9 |
| 2025-06-08 18:00 | 2025-06-11 00:00 | SHORT | $152.4500 | $164.9400 | $-64.07 | -8.19% | triple_top_breakdown | Time | 9 |
| 2025-06-11 00:00 | 2025-06-13 06:00 | LONG | $164.9400 | $145.4500 | $-85.59 | -11.82% | triple_bottom_breakout | Time | 9 |
| 2025-06-14 18:00 | 2025-06-17 00:00 | SHORT | $144.6400 | $153.6100 | $-40.14 | -6.20% | triple_top_breakdown | Time | 9 |
| 2025-06-17 18:00 | 2025-06-20 00:00 | SHORT | $147.5700 | $145.3400 | $9.24 | 1.51% | triple_top_breakdown | Time | 9 |
| 2025-06-22 06:00 | 2025-06-24 12:00 | SHORT | $133.2500 | $144.8000 | $-53.70 | -8.67% | triple_top_breakdown | Time | 9 |
| 2025-06-24 12:00 | 2025-06-26 18:00 | LONG | $144.8000 | $139.0600 | $-22.64 | -3.96% | triple_bottom_breakout | Time | 9 |
| 2025-06-29 12:00 | 2025-06-29 12:00 | LONG | $151.4300 | $151.4300 | $0.00 | 0.00% | triple_bottom_breakout | End | 0 |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|
| 2025-04-16 12:00 | 2025-04-23 00:00 | SHORT | $125.1500 | $150.6800 | $-183.60 | -20.40% | triple_top_breakdown | Time | 26 |
| 2025-04-25 18:00 | 2025-05-02 06:00 | LONG | $150.8200 | $150.7300 | $-0.44 | -0.06% | triple_bottom_breakout | Time | 26 |
| 2025-05-03 00:00 | 2025-05-09 12:00 | SHORT | $147.7400 | $171.9700 | $-120.44 | -16.40% | triple_top_breakdown | Time | 26 |
| 2025-05-09 12:00 | 2025-05-13 18:00 | LONG | $171.9700 | $183.7500 | $42.88 | 6.85% | triple_bottom_breakout | TP | 17 |
| 2025-05-14 06:00 | 2025-05-20 18:00 | LONG | $181.0600 | $168.5900 | $-45.77 | -6.89% | triple_bottom_breakout | Time | 26 |
| 2025-05-21 12:00 | 2025-05-28 00:00 | SHORT | $167.1300 | $174.6000 | $-27.86 | -4.47% | triple_top_breakdown | Time | 26 |
| 2025-05-28 06:00 | 2025-06-03 18:00 | LONG | $174.5100 | $155.1900 | $-66.24 | -11.07% | triple_bottom_breakout | Time | 26 |
| 2025-06-04 06:00 | 2025-06-05 18:00 | SHORT | $155.9200 | $144.2900 | $40.18 | 7.46% | triple_top_breakdown | TP | 6 |
| 2025-06-06 12:00 | 2025-06-13 00:00 | SHORT | $150.1000 | $143.7600 | $24.28 | 4.22% | triple_top_breakdown | Time | 26 |
| 2025-06-14 18:00 | 2025-06-21 06:00 | SHORT | $144.6400 | $142.0800 | $10.56 | 1.77% | triple_top_breakdown | Time | 26 |
| 2025-06-22 06:00 | 2025-06-28 18:00 | SHORT | $133.2500 | $150.7200 | $-79.48 | -13.11% | triple_top_breakdown | Time | 26 |
| 2025-06-29 12:00 | 2025-06-29 12:00 | LONG | $151.4300 | $151.4300 | $0.00 | 0.00% | triple_bottom_breakout | End | 0 |

## Analysis

**Winner: 9 Periods Strategy**

The 9-period exit strategy outperformed with -38.80% return vs -40.59%.

### Key Observations:
- **Trade Frequency**: 23 vs 12 trades
- **Win Rate Difference**: 30.43% vs 33.33%
- **Return Difference**: 1.79% gap
- **Position Management**: Only 1 position at a time
- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)

---
*Báo cáo được tạo tự động bởi Triple Pattern Backtest System*
