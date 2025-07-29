# Butterfly Pattern Strategy Comparison - SOLUSDT 1h

## Strategy Overview
- **Pattern**: Butterfly Pattern (Bullish & Bearish)
- **Entry**: At close price when pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods

- **Take Profit**: 5.0%

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 16 | 12 |
| Win Rate | 62.50% | 58.33% |
| Total Return | 2.97% | 0.62% |
| Final Capital | $1029.70 | $1006.17 |
| Total PnL | $29.70 | $6.17 |
| Average PnL per Trade | $1.86 | $0.51 |
| Best Trade | $24.07 | $48.66 |
| Worst Trade | $-33.44 | $-51.84 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-02 02:00 | 2025-04-02 11:00 | LONG | $124.7600 | $125.6900 | $7.08 | 0.75% | Bullish Butterfly | Time |
| 2025-04-17 15:00 | 2025-04-18 00:00 | LONG | $133.4500 | $134.2400 | $5.66 | 0.59% | Bullish Butterfly | Time |
| 2025-04-18 06:00 | 2025-04-18 15:00 | LONG | $134.3700 | $132.9100 | $-10.45 | -1.09% | Bullish Butterfly | Time |
| 2025-04-24 00:00 | 2025-04-24 09:00 | SHORT | $150.1500 | $146.8900 | $20.67 | 2.17% | Bearish Butterfly | Time |
| 2025-04-26 08:00 | 2025-04-26 17:00 | SHORT | $150.7700 | $149.0700 | $10.96 | 1.13% | Bearish Butterfly | Time |
| 2025-04-26 20:00 | 2025-04-27 05:00 | LONG | $148.3500 | $146.3300 | $-13.37 | -1.36% | Bullish Butterfly | Time |
| 2025-05-07 10:00 | 2025-05-07 19:00 | SHORT | $147.7600 | $145.7700 | $13.06 | 1.35% | Bearish Butterfly | Time |
| 2025-05-16 03:00 | 2025-05-16 12:00 | SHORT | $172.6200 | $172.1400 | $2.73 | 0.28% | Bearish Butterfly | Time |
| 2025-05-18 02:00 | 2025-05-18 11:00 | SHORT | $167.0100 | $170.7900 | $-22.28 | -2.26% | Bearish Butterfly | Time |
| 2025-05-22 22:00 | 2025-05-23 07:00 | LONG | $178.1000 | $182.5500 | $24.07 | 2.50% | Bullish Butterfly | Time |
| 2025-05-23 07:00 | 2025-05-23 16:00 | LONG | $182.5500 | $181.2000 | $-7.29 | -0.74% | Bullish Butterfly | Time |
| 2025-06-11 13:00 | 2025-06-11 22:00 | LONG | $165.7700 | $160.1100 | $-33.44 | -3.41% | Bullish Butterfly | Time |
| 2025-06-18 05:00 | 2025-06-18 14:00 | SHORT | $148.3000 | $145.2800 | $19.30 | 2.04% | Bearish Butterfly | Time |
| 2025-06-19 11:00 | 2025-06-19 20:00 | SHORT | $145.0900 | $145.3400 | $-1.66 | -0.17% | Bearish Butterfly | Time |
| 2025-06-24 03:00 | 2025-06-24 12:00 | LONG | $143.2400 | $144.4300 | $8.01 | 0.83% | Bullish Butterfly | Time |
| 2025-06-24 12:00 | 2025-06-24 21:00 | LONG | $144.4300 | $145.4200 | $6.66 | 0.69% | Bullish Butterfly | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-02 02:00 | 2025-04-02 16:00 | LONG | $124.7600 | $131.1500 | $48.66 | 5.12% | Bullish Butterfly | TP |
| 2025-04-17 15:00 | 2025-04-18 17:00 | LONG | $133.4500 | $133.9200 | $3.51 | 0.35% | Bullish Butterfly | Time |
| 2025-04-24 00:00 | 2025-04-25 02:00 | SHORT | $150.1500 | $150.9500 | $-5.33 | -0.53% | Bearish Butterfly | Time |
| 2025-04-26 08:00 | 2025-04-27 10:00 | SHORT | $150.7700 | $148.6300 | $14.12 | 1.42% | Bearish Butterfly | Time |
| 2025-05-07 10:00 | 2025-05-08 12:00 | SHORT | $147.7600 | $154.5800 | $-46.52 | -4.62% | Bearish Butterfly | Time |
| 2025-05-16 03:00 | 2025-05-17 05:00 | SHORT | $172.6200 | $167.5000 | $28.58 | 2.97% | Bearish Butterfly | Time |
| 2025-05-18 02:00 | 2025-05-19 04:00 | SHORT | $167.0100 | $163.4600 | $21.06 | 2.13% | Bearish Butterfly | Time |
| 2025-05-22 22:00 | 2025-05-24 00:00 | LONG | $178.1000 | $172.7500 | $-30.37 | -3.00% | Bullish Butterfly | Time |
| 2025-06-11 13:00 | 2025-06-12 15:00 | LONG | $165.7700 | $157.0200 | $-51.84 | -5.28% | Bullish Butterfly | Time |
| 2025-06-18 05:00 | 2025-06-19 07:00 | SHORT | $148.3000 | $145.0700 | $20.32 | 2.18% | Bearish Butterfly | Time |
| 2025-06-19 11:00 | 2025-06-20 13:00 | SHORT | $145.0900 | $146.6500 | $-10.24 | -1.08% | Bearish Butterfly | Time |
| 2025-06-24 03:00 | 2025-06-25 05:00 | LONG | $143.2400 | $145.4000 | $14.21 | 1.51% | Bullish Butterfly | Time |

## Analysis

**Winner: 9 Periods Strategy**

The 9-period exit strategy outperformed with 2.97% return vs 0.62%.

### Key Observations:
- **Trade Frequency**: 16 vs 12 trades
- **Win Rate Difference**: 62.50% vs 58.33%
- **Return Difference**: 2.35% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
