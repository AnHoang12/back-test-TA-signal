# Butterfly Pattern Strategy Comparison - BTCUSDT 2h

## Strategy Overview
- **Pattern**: Butterfly Pattern (Bullish & Bearish)
- **Entry**: At close price when pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 19 | 18 |
| Win Rate | 68.42% | 66.67% |
| Total Return | 12.26% | 25.31% |
| Final Capital | $1122.59 | $1253.11 |
| Total PnL | $122.59 | $253.11 |
| Average PnL per Trade | $6.45 | $14.06 |
| Best Trade | $35.90 | $74.70 |
| Worst Trade | $-21.87 | $-37.63 | 

## Strategy 1: Exit after 9 periods                             

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type |
|------------|-----------|------|-------------|------------|-----|-------|-------------|
| 2024-06-09 14:00 | 2024-06-10 08:00 | LONG | $69508.6400 | $69449.9900 | $-0.80 | -0.08% | Bullish Butterfly |
| 2024-06-28 14:00 | 2024-06-29 08:00 | SHORT | $61062.0100 | $60970.0000 | $1.43 | 0.15% | Bearish Butterfly |
| 2024-07-19 10:00 | 2024-07-20 04:00 | LONG | $64116.0000 | $66537.3200 | $35.90 | 3.78% | Bullish Butterfly |
| 2024-07-31 14:00 | 2024-08-01 08:00 | SHORT | $66379.9900 | $64466.0000 | $28.39 | 2.88% | Bearish Butterfly |
| 2024-08-10 20:00 | 2024-08-11 14:00 | SHORT | $61075.9900 | $60127.2900 | $15.71 | 1.55% | Bearish Butterfly |
| 2024-08-12 16:00 | 2024-08-13 10:00 | SHORT | $59296.1100 | $58830.0000 | $8.07 | 0.79% | Bearish Butterfly |
| 2024-08-22 16:00 | 2024-08-23 10:00 | LONG | $60164.7000 | $60741.6800 | $9.92 | 0.96% | Bullish Butterfly |
| 2024-08-25 10:00 | 2024-08-26 04:00 | LONG | $63873.9100 | $63950.0100 | $1.24 | 0.12% | Bullish Butterfly |
| 2024-09-04 18:00 | 2024-09-05 12:00 | SHORT | $58058.0100 | $57028.6200 | $18.53 | 1.77% | Bearish Butterfly |
| 2024-09-21 06:00 | 2024-09-22 00:00 | LONG | $63091.0200 | $63046.0000 | $-0.76 | -0.07% | Bullish Butterfly |
| 2024-09-29 02:00 | 2024-09-29 20:00 | SHORT | $65815.9200 | $65868.6000 | $-0.85 | -0.08% | Bearish Butterfly |
| 2024-10-05 14:00 | 2024-10-06 08:00 | SHORT | $62167.6600 | $62066.3800 | $1.73 | 0.16% | Bearish Butterfly |
| 2024-10-06 10:00 | 2024-10-07 04:00 | SHORT | $62101.9200 | $63380.0100 | $-21.87 | -2.06% | Bearish Butterfly |
| 2024-10-20 10:00 | 2024-10-21 04:00 | SHORT | $68420.0100 | $68979.9700 | $-8.53 | -0.82% | Bearish Butterfly |
| 2024-10-22 16:00 | 2024-10-23 10:00 | SHORT | $67331.5800 | $66414.0000 | $14.09 | 1.36% | Bearish Butterfly |
| 2024-11-02 16:00 | 2024-11-03 10:00 | LONG | $69401.9900 | $68358.8600 | $-15.74 | -1.50% | Bullish Butterfly |
| 2024-11-13 08:00 | 2024-11-14 02:00 | LONG | $87400.0200 | $89937.0200 | $29.96 | 2.90% | Bullish Butterfly |
| 2024-11-23 14:00 | 2024-11-24 08:00 | SHORT | $98400.0000 | $97936.4700 | $5.00 | 0.47% | Bearish Butterfly |
| 2024-12-06 22:00 | 2024-12-07 16:00 | SHORT | $99740.8400 | $99631.9700 | $1.16 | 0.11% | Bearish Butterfly |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type |
|------------|-----------|------|-------------|------------|-----|-------|-------------|
| 2024-06-09 14:00 | 2024-06-11 18:00 | LONG | $69508.6400 | $67407.0100 | $-28.72 | -3.02% | Bullish Butterfly |
| 2024-06-28 14:00 | 2024-06-30 18:00 | SHORT | $61062.0100 | $62026.8300 | $-14.58 | -1.58% | Bearish Butterfly |
| 2024-07-19 10:00 | 2024-07-21 14:00 | LONG | $64116.0000 | $67164.0000 | $43.21 | 4.75% | Bullish Butterfly |
| 2024-07-31 14:00 | 2024-08-02 18:00 | SHORT | $66379.9900 | $62633.5700 | $53.61 | 5.64% | Bearish Butterfly |
| 2024-08-10 20:00 | 2024-08-13 00:00 | SHORT | $61075.9900 | $59740.0000 | $21.89 | 2.19% | Bearish Butterfly |
| 2024-08-13 02:00 | 2024-08-15 06:00 | SHORT | $59040.0000 | $58060.3700 | $16.95 | 1.66% | Bearish Butterfly |
| 2024-08-22 16:00 | 2024-08-24 20:00 | LONG | $60164.7000 | $63612.3700 | $59.47 | 5.73% | Bullish Butterfly |
| 2024-08-25 10:00 | 2024-08-27 14:00 | LONG | $63873.9100 | $61709.1300 | $-37.09 | -3.39% | Bullish Butterfly |
| 2024-09-04 18:00 | 2024-09-06 22:00 | SHORT | $58058.0100 | $53962.9700 | $74.70 | 7.05% | Bearish Butterfly |
| 2024-09-21 06:00 | 2024-09-23 10:00 | LONG | $63091.0200 | $63435.0400 | $6.16 | 0.55% | Bullish Butterfly |
| 2024-09-29 02:00 | 2024-10-01 06:00 | SHORT | $65815.9200 | $64045.9200 | $30.55 | 2.69% | Bearish Butterfly |
| 2024-10-05 14:00 | 2024-10-07 18:00 | SHORT | $62167.6600 | $63382.0000 | $-22.75 | -1.95% | Bearish Butterfly |
| 2024-10-20 10:00 | 2024-10-22 14:00 | SHORT | $68420.0100 | $67282.2700 | $19.01 | 1.66% | Bearish Butterfly |
| 2024-10-22 16:00 | 2024-10-24 20:00 | SHORT | $67331.5800 | $68348.0100 | $-17.53 | -1.51% | Bearish Butterfly |
| 2024-11-02 16:00 | 2024-11-04 20:00 | LONG | $69401.9900 | $67120.5700 | $-37.63 | -3.29% | Bullish Butterfly |
| 2024-11-13 08:00 | 2024-11-15 12:00 | LONG | $87400.0200 | $90148.0000 | $34.86 | 3.14% | Bullish Butterfly |
| 2024-11-23 14:00 | 2024-11-25 18:00 | SHORT | $98400.0000 | $94669.4800 | $43.30 | 3.79% | Bearish Butterfly |
| 2024-12-06 22:00 | 2024-12-09 02:00 | SHORT | $99740.8400 | $99090.8400 | $7.71 | 0.65% | Bearish Butterfly |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 25.31% return vs 12.26%.

### Key Observations:
- **Trade Frequency**: 19 vs 18 trades
- **Win Rate Difference**: 68.42% vs 66.67%
- **Return Difference**: 13.05% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
