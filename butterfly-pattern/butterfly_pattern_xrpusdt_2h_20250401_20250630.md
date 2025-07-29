# Butterfly Pattern Strategy Comparison - XRPUSDT 2h

## Strategy Overview
- **Pattern**: Butterfly Pattern (Bullish & Bearish)
- **Entry**: At close price when pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods

- **Take Profit**: 5.0%

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 12 | 11 |
| Win Rate | 75.00% | 63.64% |
| Total Return | 14.72% | 17.89% |
| Final Capital | $1147.17 | $1178.93 |
| Total PnL | $147.17 | $178.93 |
| Average PnL per Trade | $12.26 | $16.27 |
| Best Trade | $54.21 | $67.13 |
| Worst Trade | $-16.23 | $-86.77 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-08 14:00 | 2025-04-08 22:00 | SHORT | $1.9050 | $1.7963 | $54.21 | 5.71% | Bearish Butterfly | TP |
| 2025-04-15 02:00 | 2025-04-15 20:00 | LONG | $2.1531 | $2.1182 | $-16.23 | -1.62% | Bullish Butterfly | Time |
| 2025-04-17 14:00 | 2025-04-18 08:00 | SHORT | $2.0675 | $2.0765 | $-4.29 | -0.44% | Bearish Butterfly | Time |
| 2025-04-18 20:00 | 2025-04-19 14:00 | SHORT | $2.0815 | $2.0773 | $1.98 | 0.20% | Bearish Butterfly | Time |
| 2025-04-19 20:00 | 2025-04-20 14:00 | SHORT | $2.0899 | $2.0488 | $19.35 | 1.97% | Bearish Butterfly | Time |
| 2025-04-25 14:00 | 2025-04-26 08:00 | LONG | $2.2005 | $2.2081 | $3.46 | 0.35% | Bullish Butterfly | Time |
| 2025-04-29 12:00 | 2025-04-30 06:00 | SHORT | $2.2807 | $2.2202 | $26.67 | 2.65% | Bearish Butterfly | Time |
| 2025-05-13 20:00 | 2025-05-14 14:00 | SHORT | $2.5764 | $2.5616 | $5.92 | 0.57% | Bearish Butterfly | Time |
| 2025-06-04 12:00 | 2025-06-05 06:00 | SHORT | $2.2346 | $2.1863 | $22.40 | 2.16% | Bearish Butterfly | Time |
| 2025-06-11 02:00 | 2025-06-11 20:00 | LONG | $2.2979 | $2.2730 | $-11.46 | -1.08% | Bullish Butterfly | Time |
| 2025-06-13 20:00 | 2025-06-14 14:00 | LONG | $2.1388 | $2.1491 | $5.04 | 0.48% | Bullish Butterfly | Time |
| 2025-06-26 04:00 | 2025-06-26 22:00 | SHORT | $2.1889 | $2.1054 | $40.12 | 3.81% | Bearish Butterfly | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-08 14:00 | 2025-04-08 22:00 | SHORT | $1.9050 | $1.7963 | $54.21 | 5.71% | Bearish Butterfly | TP |
| 2025-04-15 02:00 | 2025-04-17 06:00 | LONG | $2.1531 | $2.0913 | $-28.75 | -2.87% | Bullish Butterfly | Time |
| 2025-04-17 14:00 | 2025-04-19 18:00 | SHORT | $2.0675 | $2.0839 | $-7.73 | -0.79% | Bearish Butterfly | Time |
| 2025-04-19 20:00 | 2025-04-22 00:00 | SHORT | $2.0899 | $2.0964 | $-3.01 | -0.31% | Bearish Butterfly | Time |
| 2025-04-25 14:00 | 2025-04-27 18:00 | LONG | $2.2005 | $2.2841 | $36.62 | 3.80% | Bullish Butterfly | Time |
| 2025-04-29 12:00 | 2025-04-30 12:00 | SHORT | $2.2807 | $2.1274 | $67.13 | 6.72% | Bearish Butterfly | TP |
| 2025-05-13 20:00 | 2025-05-15 20:00 | SHORT | $2.5764 | $2.4265 | $61.82 | 5.82% | Bearish Butterfly | TP |
| 2025-06-04 12:00 | 2025-06-05 20:00 | SHORT | $2.2346 | $2.1030 | $66.04 | 5.89% | Bearish Butterfly | TP |
| 2025-06-11 02:00 | 2025-06-13 06:00 | LONG | $2.2979 | $2.1295 | $-86.77 | -7.33% | Bullish Butterfly | Time |
| 2025-06-13 20:00 | 2025-06-16 00:00 | LONG | $2.1388 | $2.1737 | $17.98 | 1.63% | Bullish Butterfly | Time |
| 2025-06-26 04:00 | 2025-06-28 08:00 | SHORT | $2.1889 | $2.1862 | $1.38 | 0.12% | Bearish Butterfly | Time |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 17.89% return vs 14.72%.

### Key Observations:
- **Trade Frequency**: 12 vs 11 trades
- **Win Rate Difference**: 75.00% vs 63.64%
- **Return Difference**: 3.18% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
