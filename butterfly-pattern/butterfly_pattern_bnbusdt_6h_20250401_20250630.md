# Butterfly Pattern Strategy Comparison - BNBUSDT 6h

## Strategy Overview
- **Pattern**: Butterfly Pattern (Bullish & Bearish)
- **Entry**: At close price when pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods

- **Take Profit**: 5.0%

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 7 | 5 |
| Win Rate | 85.71% | 60.00% |
| Total Return | 14.80% | 9.18% |
| Final Capital | $1147.99 | $1091.78 |
| Total PnL | $147.99 | $91.78 |
| Average PnL per Trade | $21.14 | $18.36 |
| Best Trade | $54.98 | $50.39 |
| Worst Trade | $-18.37 | $-51.25 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-27 06:00 | 2025-04-29 12:00 | LONG | $600.5300 | $603.6400 | $4.92 | 0.52% | Bullish Butterfly | Time |
| 2025-05-15 18:00 | 2025-05-18 00:00 | SHORT | $651.8800 | $645.8600 | $8.82 | 0.92% | Bearish Butterfly | Time |
| 2025-05-20 18:00 | 2025-05-22 06:00 | LONG | $650.0000 | $687.1100 | $54.98 | 5.71% | Bullish Butterfly | TP |
| 2025-05-23 18:00 | 2025-05-26 00:00 | LONG | $656.9800 | $673.8700 | $26.10 | 2.57% | Bullish Butterfly | Time |
| 2025-05-26 06:00 | 2025-05-28 12:00 | SHORT | $674.1700 | $686.0800 | $-18.37 | -1.77% | Bearish Butterfly | Time |
| 2025-05-29 06:00 | 2025-05-31 12:00 | SHORT | $685.7900 | $655.7800 | $44.75 | 4.38% | Bearish Butterfly | Time |
| 2025-06-05 18:00 | 2025-06-08 00:00 | LONG | $633.3200 | $649.2500 | $26.79 | 2.52% | Bullish Butterfly | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-27 06:00 | 2025-05-03 18:00 | LONG | $600.5300 | $599.3600 | $-1.85 | -0.19% | Bullish Butterfly | Time |
| 2025-05-15 18:00 | 2025-05-22 06:00 | SHORT | $651.8800 | $687.1100 | $-51.25 | -5.40% | Bearish Butterfly | Time |
| 2025-05-23 18:00 | 2025-05-27 12:00 | LONG | $656.9800 | $690.5400 | $45.95 | 5.11% | Bullish Butterfly | TP |
| 2025-05-29 06:00 | 2025-06-01 06:00 | SHORT | $685.7900 | $650.5000 | $48.54 | 5.15% | Bearish Butterfly | TP |
| 2025-06-05 18:00 | 2025-06-09 18:00 | LONG | $633.3200 | $665.5800 | $50.39 | 5.09% | Bullish Butterfly | TP |

## Analysis

**Winner: 9 Periods Strategy**

The 9-period exit strategy outperformed with 14.80% return vs 9.18%.

### Key Observations:
- **Trade Frequency**: 7 vs 5 trades
- **Win Rate Difference**: 85.71% vs 60.00%
- **Return Difference**: 5.62% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
