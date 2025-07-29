# Butterfly Pattern Strategy Comparison - BNBUSDT 4h

## Strategy Overview
- **Pattern**: Butterfly Pattern (Bullish & Bearish)
- **Entry**: At close price when pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods

- **Take Profit**: 5.0%

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 11 | 10 |
| Win Rate | 63.64% | 70.00% |
| Total Return | 11.74% | 16.18% |
| Final Capital | $1117.42 | $1161.78 |
| Total PnL | $117.42 | $161.78 |
| Average PnL per Trade | $10.67 | $16.18 |
| Best Trade | $55.71 | $55.05 |
| Worst Trade | $-19.58 | $-22.35 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-09 04:00 | 2025-04-10 16:00 | LONG | $556.6200 | $574.9400 | $31.27 | 3.29% | Bullish Butterfly | Time |
| 2025-04-15 12:00 | 2025-04-17 00:00 | SHORT | $584.5300 | $582.0700 | $4.12 | 0.42% | Bearish Butterfly | Time |
| 2025-04-17 12:00 | 2025-04-19 00:00 | SHORT | $589.7500 | $593.3500 | $-6.00 | -0.61% | Bearish Butterfly | Time |
| 2025-04-20 12:00 | 2025-04-22 00:00 | SHORT | $588.2000 | $599.9800 | $-19.58 | -2.00% | Bearish Butterfly | Time |
| 2025-04-28 20:00 | 2025-04-30 08:00 | LONG | $606.1600 | $602.4300 | $-5.90 | -0.62% | Bullish Butterfly | Time |
| 2025-05-15 20:00 | 2025-05-17 08:00 | SHORT | $651.8800 | $641.5200 | $15.16 | 1.59% | Bearish Butterfly | Time |
| 2025-05-20 16:00 | 2025-05-22 00:00 | LONG | $648.0500 | $685.3400 | $55.71 | 5.75% | Bullish Butterfly | TP |
| 2025-05-29 04:00 | 2025-05-30 16:00 | SHORT | $685.2900 | $666.3200 | $28.26 | 2.77% | Bearish Butterfly | Time |
| 2025-06-07 04:00 | 2025-06-08 16:00 | LONG | $648.6200 | $654.6000 | $9.66 | 0.92% | Bullish Butterfly | Time |
| 2025-06-15 08:00 | 2025-06-16 20:00 | SHORT | $648.2300 | $650.7400 | $-4.09 | -0.39% | Bearish Butterfly | Time |
| 2025-06-27 20:00 | 2025-06-29 08:00 | LONG | $645.7100 | $651.1200 | $8.82 | 0.84% | Bullish Butterfly | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-09 04:00 | 2025-04-11 12:00 | LONG | $556.6200 | $585.2800 | $48.91 | 5.15% | Bullish Butterfly | TP |
| 2025-04-15 12:00 | 2025-04-19 20:00 | SHORT | $584.5300 | $591.7300 | $-12.27 | -1.23% | Bearish Butterfly | Time |
| 2025-04-20 12:00 | 2025-04-24 20:00 | SHORT | $588.2000 | $601.5500 | $-22.35 | -2.27% | Bearish Butterfly | Time |
| 2025-04-28 20:00 | 2025-05-03 04:00 | LONG | $606.1600 | $597.4700 | $-13.81 | -1.43% | Bullish Butterfly | Time |
| 2025-05-15 20:00 | 2025-05-20 04:00 | SHORT | $651.8800 | $647.3400 | $6.62 | 0.70% | Bearish Butterfly | Time |
| 2025-05-20 16:00 | 2025-05-22 00:00 | LONG | $648.0500 | $685.3400 | $55.05 | 5.75% | Bullish Butterfly | TP |
| 2025-05-29 04:00 | 2025-05-31 00:00 | SHORT | $685.2900 | $650.6900 | $50.95 | 5.05% | Bearish Butterfly | TP |
| 2025-06-07 04:00 | 2025-06-11 12:00 | LONG | $648.6200 | $669.6600 | $34.30 | 3.24% | Bullish Butterfly | Time |
| 2025-06-15 08:00 | 2025-06-19 16:00 | SHORT | $648.2300 | $642.6500 | $9.38 | 0.86% | Bearish Butterfly | Time |
| 2025-06-27 20:00 | 2025-06-29 16:00 | LONG | $645.7100 | $648.6500 | $5.00 | 0.46% | Bullish Butterfly | End |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 16.18% return vs 11.74%.

### Key Observations:
- **Trade Frequency**: 11 vs 10 trades
- **Win Rate Difference**: 63.64% vs 70.00%
- **Return Difference**: 4.44% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
