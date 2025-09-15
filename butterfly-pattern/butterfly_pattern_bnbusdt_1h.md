# Butterfly Pattern Strategy Comparison - BNBUSDT 1h

## Strategy Overview
- **Pattern**: Butterfly Pattern (Bullish & Bearish)
- **Entry**: At close price when pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods

- **Take Profit**: 5.0%

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 26 | 21 |
| Win Rate | 69.23% | 71.43% |
| Total Return | 7.53% | 21.13% |
| Final Capital | $1075.27 | $1211.27 |
| Total PnL | $75.27 | $211.27 |
| Average PnL per Trade | $2.90 | $10.06 |
| Best Trade | $22.26 | $36.55 |
| Worst Trade | $-46.21 | $-19.84 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-06-12 10:00 | 2025-06-12 19:00 | SHORT | $666.0000 | $658.4600 | $10.76 | 1.13% | Bearish Butterfly | Time |
| 2025-06-13 17:00 | 2025-06-14 02:00 | SHORT | $652.4900 | $651.8000 | $1.02 | 0.11% | Bearish Butterfly | Time |
| 2025-06-14 02:00 | 2025-06-14 11:00 | LONG | $651.8000 | $650.7100 | $-1.61 | -0.17% | Bullish Butterfly | Time |
| 2025-06-21 04:00 | 2025-06-21 13:00 | SHORT | $642.5400 | $636.6900 | $8.74 | 0.91% | Bearish Butterfly | Time |
| 2025-06-26 00:00 | 2025-06-26 09:00 | LONG | $647.2000 | $646.1000 | $-1.65 | -0.17% | Bullish Butterfly | Time |
| 2025-06-26 09:00 | 2025-06-26 18:00 | SHORT | $646.1000 | $645.6000 | $0.75 | 0.08% | Bearish Butterfly | Time |
| 2025-07-01 01:00 | 2025-07-01 10:00 | SHORT | $658.0200 | $653.1000 | $7.23 | 0.75% | Bearish Butterfly | Time |
| 2025-07-06 09:00 | 2025-07-06 18:00 | LONG | $654.0000 | $662.2500 | $12.29 | 1.26% | Bullish Butterfly | Time |
| 2025-07-07 22:00 | 2025-07-08 07:00 | LONG | $660.1900 | $659.8100 | $-0.57 | -0.06% | Bullish Butterfly | Time |
| 2025-07-08 22:00 | 2025-07-09 07:00 | LONG | $660.0700 | $662.6100 | $3.79 | 0.38% | Bullish Butterfly | Time |
| 2025-07-09 16:00 | 2025-07-10 01:00 | LONG | $662.8100 | $669.3900 | $9.82 | 0.99% | Bullish Butterfly | Time |
| 2025-07-13 20:00 | 2025-07-14 05:00 | SHORT | $692.4900 | $697.4900 | $-7.21 | -0.72% | Bearish Butterfly | Time |
| 2025-07-17 14:00 | 2025-07-17 23:00 | LONG | $724.5500 | $720.6500 | $-5.34 | -0.54% | Bullish Butterfly | Time |
| 2025-07-22 15:00 | 2025-07-23 00:00 | SHORT | $763.7900 | $799.5800 | $-46.21 | -4.69% | Bearish Butterfly | Time |
| 2025-07-26 12:00 | 2025-07-26 21:00 | LONG | $782.5100 | $789.1700 | $8.02 | 0.85% | Bullish Butterfly | Time |
| 2025-07-30 09:00 | 2025-07-30 18:00 | SHORT | $799.3100 | $780.5800 | $22.26 | 2.34% | Bearish Butterfly | Time |
| 2025-08-08 10:00 | 2025-08-08 19:00 | LONG | $788.0100 | $795.4600 | $9.18 | 0.95% | Bullish Butterfly | Time |
| 2025-08-13 19:00 | 2025-08-14 04:00 | LONG | $845.2100 | $854.6000 | $10.88 | 1.11% | Bullish Butterfly | Time |
| 2025-08-23 14:00 | 2025-08-23 23:00 | SHORT | $888.7000 | $880.4200 | $9.22 | 0.93% | Bearish Butterfly | Time |
| 2025-08-25 00:00 | 2025-08-25 09:00 | SHORT | $873.1100 | $860.9900 | $13.86 | 1.39% | Bearish Butterfly | Time |
| 2025-08-27 14:00 | 2025-08-27 23:00 | LONG | $862.3300 | $855.1800 | $-8.39 | -0.83% | Bullish Butterfly | Time |
| 2025-08-29 20:00 | 2025-08-30 05:00 | SHORT | $855.7700 | $858.6700 | $-3.40 | -0.34% | Bearish Butterfly | Time |
| 2025-08-30 07:00 | 2025-08-30 16:00 | SHORT | $860.3500 | $857.5600 | $3.25 | 0.32% | Bearish Butterfly | Time |
| 2025-09-03 07:00 | 2025-09-03 16:00 | LONG | $854.6500 | $858.6700 | $4.72 | 0.47% | Bullish Butterfly | Time |
| 2025-09-05 01:00 | 2025-09-05 10:00 | LONG | $846.5600 | $850.1500 | $4.28 | 0.42% | Bullish Butterfly | Time |
| 2025-09-05 22:00 | 2025-09-06 07:00 | LONG | $851.3600 | $859.4200 | $9.58 | 0.95% | Bullish Butterfly | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-06-12 10:00 | 2025-06-13 12:00 | SHORT | $666.0000 | $651.1900 | $21.13 | 2.22% | Bearish Butterfly | Time |
| 2025-06-13 17:00 | 2025-06-14 19:00 | SHORT | $652.4900 | $640.7300 | $17.48 | 1.80% | Bearish Butterfly | Time |
| 2025-06-21 04:00 | 2025-06-22 06:00 | SHORT | $642.5400 | $634.1400 | $12.90 | 1.31% | Bearish Butterfly | Time |
| 2025-06-26 00:00 | 2025-06-27 02:00 | LONG | $647.2000 | $645.0100 | $-3.38 | -0.34% | Bullish Butterfly | Time |
| 2025-07-01 01:00 | 2025-07-02 03:00 | SHORT | $658.0200 | $649.6000 | $12.74 | 1.28% | Bearish Butterfly | Time |
| 2025-07-06 09:00 | 2025-07-07 11:00 | LONG | $654.0000 | $662.3100 | $12.81 | 1.27% | Bullish Butterfly | Time |
| 2025-07-07 22:00 | 2025-07-09 00:00 | LONG | $660.1900 | $661.5800 | $2.15 | 0.21% | Bullish Butterfly | Time |
| 2025-07-09 16:00 | 2025-07-10 18:00 | LONG | $662.8100 | $675.5800 | $19.69 | 1.93% | Bullish Butterfly | Time |
| 2025-07-13 20:00 | 2025-07-14 22:00 | SHORT | $692.4900 | $690.8900 | $2.40 | 0.23% | Bearish Butterfly | Time |
| 2025-07-17 14:00 | 2025-07-18 16:00 | LONG | $724.5500 | $743.4000 | $27.14 | 2.60% | Bullish Butterfly | Time |
| 2025-07-22 15:00 | 2025-07-23 17:00 | SHORT | $763.7900 | $770.8600 | $-9.89 | -0.93% | Bearish Butterfly | Time |
| 2025-07-26 12:00 | 2025-07-27 14:00 | LONG | $782.5100 | $797.3100 | $20.04 | 1.89% | Bullish Butterfly | Time |
| 2025-07-30 09:00 | 2025-07-31 11:00 | SHORT | $799.3100 | $800.5900 | $-1.73 | -0.16% | Bearish Butterfly | Time |
| 2025-08-08 10:00 | 2025-08-09 12:00 | LONG | $788.0100 | $814.7600 | $36.55 | 3.39% | Bullish Butterfly | Time |
| 2025-08-13 19:00 | 2025-08-14 21:00 | LONG | $845.2100 | $830.1200 | $-19.84 | -1.79% | Bullish Butterfly | Time |
| 2025-08-23 14:00 | 2025-08-24 16:00 | SHORT | $888.7000 | $867.3700 | $26.23 | 2.40% | Bearish Butterfly | Time |
| 2025-08-25 00:00 | 2025-08-26 02:00 | SHORT | $873.1100 | $847.2100 | $33.15 | 2.97% | Bearish Butterfly | Time |
| 2025-08-27 14:00 | 2025-08-28 16:00 | LONG | $862.3300 | $864.7200 | $3.18 | 0.28% | Bullish Butterfly | Time |
| 2025-08-29 20:00 | 2025-08-30 22:00 | SHORT | $855.7700 | $861.6900 | $-7.97 | -0.69% | Bearish Butterfly | Time |
| 2025-09-03 07:00 | 2025-09-04 09:00 | LONG | $854.6500 | $847.8400 | $-9.12 | -0.80% | Bullish Butterfly | Time |
| 2025-09-05 01:00 | 2025-09-06 03:00 | LONG | $846.5600 | $858.2000 | $15.62 | 1.37% | Bullish Butterfly | Time |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 21.13% return vs 7.53%.

### Key Observations:
- **Trade Frequency**: 26 vs 21 trades
- **Win Rate Difference**: 69.23% vs 71.43%
- **Return Difference**: 13.60% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
