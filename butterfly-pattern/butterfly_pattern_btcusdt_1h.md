# Butterfly Pattern Strategy Comparison - BTCUSDT 1h

## Strategy Overview
- **Pattern**: Butterfly Pattern (Bullish & Bearish)
- **Entry**: At close price when pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods

- **Take Profit**: 5.0%

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 23 | 17 |
| Win Rate | 43.48% | 47.06% |
| Total Return | 0.62% | 0.65% |
| Final Capital | $1006.25 | $1006.50 |
| Total PnL | $6.25 | $6.50 |
| Average PnL per Trade | $0.27 | $0.38 |
| Best Trade | $14.25 | $14.77 |
| Worst Trade | $-11.20 | $-15.13 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-06-19 08:00 | 2025-06-19 17:00 | LONG | $104746.1200 | $104521.3100 | $-2.04 | -0.21% | Bullish Butterfly | Time |
| 2025-06-24 14:00 | 2025-06-24 23:00 | LONG | $105517.5000 | $106083.0000 | $5.08 | 0.54% | Bullish Butterfly | Time |
| 2025-06-26 00:00 | 2025-06-26 09:00 | LONG | $107320.0000 | $107325.1200 | $0.05 | 0.00% | Bullish Butterfly | Time |
| 2025-06-26 10:00 | 2025-06-26 19:00 | LONG | $107389.0100 | $107532.9800 | $1.28 | 0.13% | Bullish Butterfly | Time |
| 2025-06-27 09:00 | 2025-06-27 18:00 | LONG | $107083.8000 | $106704.6000 | $-3.38 | -0.35% | Bullish Butterfly | Time |
| 2025-06-27 19:00 | 2025-06-28 04:00 | LONG | $106801.0200 | $107191.1900 | $3.47 | 0.37% | Bullish Butterfly | Time |
| 2025-06-29 01:00 | 2025-06-29 10:00 | SHORT | $107311.0000 | $108153.2600 | $-7.49 | -0.78% | Bearish Butterfly | Time |
| 2025-07-01 02:00 | 2025-07-01 11:00 | SHORT | $107101.6900 | $106605.8000 | $4.39 | 0.46% | Bearish Butterfly | Time |
| 2025-07-03 22:00 | 2025-07-04 07:00 | SHORT | $109699.1700 | $108700.0000 | $8.66 | 0.91% | Bearish Butterfly | Time |
| 2025-07-05 03:00 | 2025-07-05 12:00 | LONG | $108154.7200 | $108148.5700 | $-0.05 | -0.01% | Bullish Butterfly | Time |
| 2025-07-05 14:00 | 2025-07-05 23:00 | SHORT | $108193.2300 | $108198.1200 | $-0.04 | -0.00% | Bearish Butterfly | Time |
| 2025-07-06 07:00 | 2025-07-06 16:00 | SHORT | $108040.3100 | $108856.9200 | $-7.25 | -0.76% | Bearish Butterfly | Time |
| 2025-07-17 10:00 | 2025-07-17 19:00 | SHORT | $118340.0100 | $118959.6600 | $-4.99 | -0.52% | Bearish Butterfly | Time |
| 2025-07-18 02:00 | 2025-07-18 11:00 | SHORT | $120096.4300 | $119171.3400 | $7.30 | 0.77% | Bearish Butterfly | Time |
| 2025-07-27 11:00 | 2025-07-27 20:00 | SHORT | $118072.7100 | $118754.1300 | $-5.51 | -0.58% | Bearish Butterfly | Time |
| 2025-07-28 08:00 | 2025-07-28 17:00 | LONG | $119072.4500 | $117667.8600 | $-11.20 | -1.18% | Bullish Butterfly | Time |
| 2025-07-29 21:00 | 2025-07-30 06:00 | LONG | $117606.7900 | $118287.3100 | $5.43 | 0.58% | Bullish Butterfly | Time |
| 2025-08-04 08:00 | 2025-08-04 17:00 | SHORT | $114546.2500 | $115193.4100 | $-5.33 | -0.56% | Bearish Butterfly | Time |
| 2025-08-08 08:00 | 2025-08-08 17:00 | SHORT | $116620.6300 | $116708.8600 | $-0.71 | -0.08% | Bearish Butterfly | Time |
| 2025-08-12 06:00 | 2025-08-12 15:00 | LONG | $118839.9700 | $119933.0000 | $8.63 | 0.92% | Bullish Butterfly | Time |
| 2025-08-27 05:00 | 2025-08-27 14:00 | SHORT | $111372.1800 | $111815.9400 | $-3.77 | -0.40% | Bearish Butterfly | Time |
| 2025-08-27 21:00 | 2025-08-28 06:00 | LONG | $111528.1900 | $113213.7800 | $14.25 | 1.51% | Bullish Butterfly | Time |
| 2025-09-06 04:00 | 2025-09-06 13:00 | SHORT | $110876.1200 | $110936.8200 | $-0.52 | -0.05% | Bearish Butterfly | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-06-19 08:00 | 2025-06-20 10:00 | LONG | $104746.1200 | $105958.8700 | $11.00 | 1.16% | Bullish Butterfly | Time |
| 2025-06-24 14:00 | 2025-06-25 16:00 | LONG | $105517.5000 | $107139.8100 | $14.77 | 1.54% | Bullish Butterfly | Time |
| 2025-06-26 00:00 | 2025-06-27 02:00 | LONG | $107320.0000 | $107253.6000 | $-0.60 | -0.06% | Bullish Butterfly | Time |
| 2025-06-27 09:00 | 2025-06-28 11:00 | LONG | $107083.8000 | $107373.3900 | $2.63 | 0.27% | Bullish Butterfly | Time |
| 2025-06-29 01:00 | 2025-06-30 03:00 | SHORT | $107311.0000 | $108503.7400 | $-10.85 | -1.11% | Bearish Butterfly | Time |
| 2025-07-01 02:00 | 2025-07-02 04:00 | SHORT | $107101.6900 | $106382.8600 | $6.48 | 0.67% | Bearish Butterfly | Time |
| 2025-07-03 22:00 | 2025-07-05 00:00 | SHORT | $109699.1700 | $108196.0100 | $13.32 | 1.37% | Bearish Butterfly | Time |
| 2025-07-05 03:00 | 2025-07-06 05:00 | LONG | $108154.7200 | $108003.3500 | $-1.38 | -0.14% | Bullish Butterfly | Time |
| 2025-07-06 07:00 | 2025-07-07 09:00 | SHORT | $108040.3100 | $108849.0600 | $-7.36 | -0.75% | Bearish Butterfly | Time |
| 2025-07-17 10:00 | 2025-07-18 12:00 | SHORT | $118340.0100 | $119442.4400 | $-9.10 | -0.93% | Bearish Butterfly | Time |
| 2025-07-27 11:00 | 2025-07-28 13:00 | SHORT | $118072.7100 | $118434.7800 | $-2.97 | -0.31% | Bearish Butterfly | Time |
| 2025-07-29 21:00 | 2025-07-30 23:00 | LONG | $117606.7900 | $117840.3000 | $1.92 | 0.20% | Bullish Butterfly | Time |
| 2025-08-04 08:00 | 2025-08-05 10:00 | SHORT | $114546.2500 | $114841.2700 | $-2.49 | -0.26% | Bearish Butterfly | Time |
| 2025-08-08 08:00 | 2025-08-09 10:00 | SHORT | $116620.6300 | $117424.1600 | $-6.65 | -0.69% | Bearish Butterfly | Time |
| 2025-08-12 06:00 | 2025-08-13 08:00 | LONG | $118839.9700 | $120044.4900 | $9.71 | 1.01% | Bullish Butterfly | Time |
| 2025-08-27 05:00 | 2025-08-28 07:00 | SHORT | $111372.1800 | $113114.1100 | $-15.13 | -1.56% | Bearish Butterfly | Time |
| 2025-09-06 04:00 | 2025-09-07 06:00 | SHORT | $110876.1200 | $110504.1500 | $3.20 | 0.34% | Bearish Butterfly | Time |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 0.65% return vs 0.62%.

### Key Observations:
- **Trade Frequency**: 23 vs 17 trades
- **Win Rate Difference**: 43.48% vs 47.06%
- **Return Difference**: 0.03% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
