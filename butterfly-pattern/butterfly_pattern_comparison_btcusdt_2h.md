# Butterfly Pattern Strategy Comparison - BTCUSDT 2h

## Strategy Overview
- **Pattern**: Butterfly Pattern (Bullish & Bearish)
- **Entry**: At close price when pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 17 | 16 |
| Win Rate | 76.47% | 75.00% |
| Total Return | 15.80% | 35.40% |
| Final Capital | $1158.01 | $1354.02 |
| Total PnL | $158.01 | $354.02 |
| Average PnL per Trade | $9.29 | $22.13 |
| Best Trade | $43.28 | $80.30 |
| Worst Trade | $-25.84 | $-33.71 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type |
|------------|-----------|------|-------------|------------|-----|-------|-------------|
| 2024-07-19 08:00 | 2024-07-20 02:00 | LONG | $63700.0000 | $66602.0100 | $43.28 | 4.56% | Bullish Butterfly |
| 2024-07-31 12:00 | 2024-08-01 06:00 | SHORT | $66508.0000 | $64328.5900 | $32.48 | 3.28% | Bearish Butterfly |
| 2024-08-10 18:00 | 2024-08-11 12:00 | SHORT | $61016.4500 | $60457.5400 | $9.36 | 0.92% | Bearish Butterfly |
| 2024-08-12 14:00 | 2024-08-13 08:00 | SHORT | $60207.3700 | $58946.0100 | $21.60 | 2.10% | Bearish Butterfly |
| 2024-08-22 14:00 | 2024-08-23 08:00 | LONG | $60407.4000 | $61022.1300 | $10.70 | 1.02% | Bullish Butterfly |
| 2024-08-25 08:00 | 2024-08-26 02:00 | LONG | $63861.3100 | $64114.9900 | $4.22 | 0.40% | Bullish Butterfly |
| 2024-09-04 16:00 | 2024-09-05 10:00 | SHORT | $57878.0000 | $56698.0100 | $21.72 | 2.04% | Bearish Butterfly |
| 2024-09-21 04:00 | 2024-09-21 22:00 | LONG | $62908.8200 | $63348.9600 | $7.60 | 0.70% | Bullish Butterfly |
| 2024-09-29 00:00 | 2024-09-29 18:00 | SHORT | $65872.9000 | $65958.8200 | $-1.43 | -0.13% | Bearish Butterfly |
| 2024-10-05 12:00 | 2024-10-06 06:00 | SHORT | $62153.3500 | $61949.0100 | $3.59 | 0.33% | Bearish Butterfly |
| 2024-10-06 08:00 | 2024-10-07 02:00 | SHORT | $62066.3800 | $63530.5100 | $-25.84 | -2.36% | Bearish Butterfly |
| 2024-10-20 08:00 | 2024-10-21 02:00 | SHORT | $68434.2000 | $68939.9900 | $-7.92 | -0.74% | Bearish Butterfly |
| 2024-10-22 14:00 | 2024-10-23 08:00 | SHORT | $67282.2700 | $66516.0000 | $12.11 | 1.14% | Bearish Butterfly |
| 2024-11-02 14:00 | 2024-11-03 08:00 | LONG | $69393.1700 | $68242.4300 | $-17.82 | -1.66% | Bullish Butterfly |
| 2024-11-13 06:00 | 2024-11-14 00:00 | LONG | $87356.0000 | $90372.0100 | $36.53 | 3.45% | Bullish Butterfly |
| 2024-11-23 12:00 | 2024-11-24 06:00 | SHORT | $98532.0800 | $98431.0500 | $1.12 | 0.10% | Bearish Butterfly |
| 2024-12-06 20:00 | 2024-12-07 14:00 | SHORT | $100372.0100 | $99756.0100 | $6.71 | 0.61% | Bearish Butterfly |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type |
|------------|-----------|------|-------------|------------|-----|-------|-------------|
| 2024-07-19 08:00 | 2024-07-21 12:00 | LONG | $63700.0000 | $66760.0100 | $45.64 | 4.80% | Bullish Butterfly |
| 2024-07-31 12:00 | 2024-08-02 16:00 | SHORT | $66508.0000 | $63098.0100 | $50.93 | 5.13% | Bearish Butterfly |
| 2024-08-10 18:00 | 2024-08-12 22:00 | SHORT | $61016.4500 | $59346.6400 | $28.51 | 2.74% | Bearish Butterfly |
| 2024-08-13 00:00 | 2024-08-15 04:00 | SHORT | $59740.0000 | $58315.0100 | $25.49 | 2.39% | Bearish Butterfly |
| 2024-08-22 14:00 | 2024-08-24 18:00 | LONG | $60407.4000 | $64210.6000 | $68.82 | 6.30% | Bullish Butterfly |
| 2024-08-25 08:00 | 2024-08-27 12:00 | LONG | $63861.3100 | $62232.6400 | $-29.54 | -2.55% | Bullish Butterfly |
| 2024-09-04 16:00 | 2024-09-06 20:00 | SHORT | $57878.0000 | $53766.5700 | $80.30 | 7.10% | Bearish Butterfly |
| 2024-09-21 04:00 | 2024-09-23 08:00 | LONG | $62908.8200 | $63635.6900 | $13.94 | 1.16% | Bullish Butterfly |
| 2024-09-29 00:00 | 2024-10-01 04:00 | SHORT | $65872.9000 | $63749.9900 | $39.31 | 3.22% | Bearish Butterfly |
| 2024-10-05 12:00 | 2024-10-07 16:00 | SHORT | $62153.3500 | $63819.9900 | $-33.71 | -2.68% | Bearish Butterfly |
| 2024-10-20 08:00 | 2024-10-22 12:00 | SHORT | $68434.2000 | $66998.2100 | $25.71 | 2.10% | Bearish Butterfly |
| 2024-10-22 14:00 | 2024-10-24 18:00 | SHORT | $67282.2700 | $68309.7900 | $-19.08 | -1.53% | Bearish Butterfly |
| 2024-11-02 14:00 | 2024-11-04 18:00 | LONG | $69393.1700 | $67856.0000 | $-27.28 | -2.22% | Bullish Butterfly |
| 2024-11-13 06:00 | 2024-11-15 10:00 | LONG | $87356.0000 | $89741.2500 | $32.92 | 2.73% | Bullish Butterfly |
| 2024-11-23 12:00 | 2024-11-25 16:00 | SHORT | $98532.0800 | $95238.0900 | $41.35 | 3.34% | Bearish Butterfly |
| 2024-12-06 20:00 | 2024-12-09 00:00 | SHORT | $100372.0100 | $99528.5400 | $10.72 | 0.84% | Bearish Butterfly |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 35.40% return vs 15.80%.

### Key Observations:
- **Trade Frequency**: 17 vs 16 trades
- **Win Rate Difference**: 76.47% vs 75.00%
- **Return Difference**: 19.60% gap

