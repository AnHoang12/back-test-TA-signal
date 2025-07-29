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
| Total Trades | 19 | 16 |
| Win Rate | 68.42% | 62.50% |
| Total Return | 9.44% | 13.22% |
| Final Capital | $1094.40 | $1132.18 |
| Total PnL | $94.40 | $132.18 |
| Average PnL per Trade | $4.97 | $8.26 |
| Best Trade | $25.13 | $56.09 |
| Worst Trade | $-11.23 | $-27.93 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-01 16:00 | 2025-04-02 01:00 | SHORT | $610.6400 | $606.9900 | $5.68 | 0.60% | Bearish Butterfly | Time |
| 2025-04-06 07:00 | 2025-04-06 16:00 | SHORT | $590.3100 | $574.7800 | $25.13 | 2.63% | Bearish Butterfly | Time |
| 2025-04-12 05:00 | 2025-04-12 14:00 | LONG | $587.0900 | $599.2500 | $20.28 | 2.07% | Bullish Butterfly | Time |
| 2025-04-16 22:00 | 2025-04-17 07:00 | SHORT | $585.1000 | $583.4400 | $2.83 | 0.28% | Bearish Butterfly | Time |
| 2025-04-18 04:00 | 2025-04-18 13:00 | SHORT | $589.6100 | $591.7400 | $-3.62 | -0.36% | Bearish Butterfly | Time |
| 2025-04-22 03:00 | 2025-04-22 12:00 | SHORT | $599.9800 | $606.7300 | $-11.23 | -1.13% | Bearish Butterfly | Time |
| 2025-04-26 06:00 | 2025-04-26 15:00 | LONG | $603.7800 | $607.9500 | $6.82 | 0.69% | Bullish Butterfly | Time |
| 2025-04-26 23:00 | 2025-04-27 08:00 | SHORT | $607.2300 | $600.2000 | $11.50 | 1.16% | Bearish Butterfly | Time |
| 2025-05-02 15:00 | 2025-05-03 00:00 | SHORT | $599.7500 | $599.4000 | $0.59 | 0.06% | Bearish Butterfly | Time |
| 2025-05-11 08:00 | 2025-05-11 17:00 | LONG | $654.7100 | $652.9000 | $-2.78 | -0.28% | Bullish Butterfly | Time |
| 2025-05-17 16:00 | 2025-05-18 01:00 | SHORT | $638.9600 | $642.5700 | $-5.66 | -0.56% | Bearish Butterfly | Time |
| 2025-05-30 13:00 | 2025-05-30 22:00 | SHORT | $668.1300 | $656.0300 | $18.06 | 1.81% | Bearish Butterfly | Time |
| 2025-06-10 16:00 | 2025-06-11 01:00 | LONG | $664.0600 | $668.9300 | $7.44 | 0.73% | Bullish Butterfly | Time |
| 2025-06-12 10:00 | 2025-06-12 19:00 | SHORT | $666.0000 | $658.4600 | $11.56 | 1.13% | Bearish Butterfly | Time |
| 2025-06-13 17:00 | 2025-06-14 02:00 | SHORT | $652.4900 | $651.8000 | $1.09 | 0.11% | Bearish Butterfly | Time |
| 2025-06-14 02:00 | 2025-06-14 11:00 | LONG | $651.8000 | $650.7100 | $-1.73 | -0.17% | Bullish Butterfly | Time |
| 2025-06-21 04:00 | 2025-06-21 13:00 | SHORT | $642.5400 | $636.6900 | $9.39 | 0.91% | Bearish Butterfly | Time |
| 2025-06-26 00:00 | 2025-06-26 09:00 | LONG | $647.2000 | $646.1000 | $-1.77 | -0.17% | Bullish Butterfly | Time |
| 2025-06-26 09:00 | 2025-06-26 18:00 | SHORT | $646.1000 | $645.6000 | $0.80 | 0.08% | Bearish Butterfly | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-01 16:00 | 2025-04-02 18:00 | SHORT | $610.6400 | $603.8900 | $10.50 | 1.11% | Bearish Butterfly | Time |
| 2025-04-06 07:00 | 2025-04-06 18:00 | SHORT | $590.3100 | $555.8200 | $56.09 | 5.84% | Bearish Butterfly | TP |
| 2025-04-12 05:00 | 2025-04-13 07:00 | LONG | $587.0900 | $593.3300 | $10.77 | 1.06% | Bullish Butterfly | Time |
| 2025-04-16 22:00 | 2025-04-18 00:00 | SHORT | $585.1000 | $588.9300 | $-6.70 | -0.65% | Bearish Butterfly | Time |
| 2025-04-18 04:00 | 2025-04-19 06:00 | SHORT | $589.6100 | $592.7000 | $-5.33 | -0.52% | Bearish Butterfly | Time |
| 2025-04-22 03:00 | 2025-04-23 05:00 | SHORT | $599.9800 | $616.5400 | $-27.93 | -2.76% | Bearish Butterfly | Time |
| 2025-04-26 06:00 | 2025-04-27 08:00 | LONG | $603.7800 | $600.2000 | $-5.84 | -0.59% | Bullish Butterfly | Time |
| 2025-05-02 15:00 | 2025-05-03 17:00 | SHORT | $599.7500 | $599.3000 | $0.74 | 0.08% | Bearish Butterfly | Time |
| 2025-05-11 08:00 | 2025-05-12 10:00 | LONG | $654.7100 | $676.6100 | $32.80 | 3.34% | Bullish Butterfly | Time |
| 2025-05-17 16:00 | 2025-05-18 18:00 | SHORT | $638.9600 | $644.0100 | $-8.00 | -0.79% | Bearish Butterfly | Time |
| 2025-05-30 13:00 | 2025-05-31 15:00 | SHORT | $668.1300 | $656.3400 | $17.72 | 1.76% | Bearish Butterfly | Time |
| 2025-06-10 16:00 | 2025-06-11 18:00 | LONG | $664.0600 | $667.5600 | $5.38 | 0.53% | Bullish Butterfly | Time |
| 2025-06-12 10:00 | 2025-06-13 12:00 | SHORT | $666.0000 | $651.1900 | $22.82 | 2.22% | Bearish Butterfly | Time |
| 2025-06-13 17:00 | 2025-06-14 19:00 | SHORT | $652.4900 | $640.7300 | $18.89 | 1.80% | Bearish Butterfly | Time |
| 2025-06-21 04:00 | 2025-06-22 06:00 | SHORT | $642.5400 | $634.1400 | $13.93 | 1.31% | Bearish Butterfly | Time |
| 2025-06-26 00:00 | 2025-06-27 02:00 | LONG | $647.2000 | $645.0100 | $-3.65 | -0.34% | Bullish Butterfly | Time |

## Analysis

**Winner: 26 Periods Strategy**

The 26-period exit strategy outperformed with 13.22% return vs 9.44%.

### Key Observations:
- **Trade Frequency**: 19 vs 16 trades
- **Win Rate Difference**: 68.42% vs 62.50%
- **Return Difference**: 3.78% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
