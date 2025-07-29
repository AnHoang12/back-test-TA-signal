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
| Total Trades | 23 | 19 |
| Win Rate | 69.57% | 57.89% |
| Total Return | 6.47% | 5.02% |
| Final Capital | $1064.66 | $1050.24 |
| Total PnL | $64.66 | $50.24 |
| Average PnL per Trade | $2.81 | $2.64 |
| Best Trade | $26.60 | $48.51 |
| Worst Trade | $-26.69 | $-35.41 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-02 13:00 | 2025-04-02 22:00 | LONG | $85215.8200 | $82821.5900 | $-26.69 | -2.81% | Bullish Butterfly | Time |
| 2025-04-08 03:00 | 2025-04-08 12:00 | SHORT | $79904.0000 | $79837.9900 | $0.76 | 0.08% | Bearish Butterfly | Time |
| 2025-04-08 14:00 | 2025-04-08 23:00 | SHORT | $78479.9100 | $76322.4200 | $25.44 | 2.75% | Bearish Butterfly | Time |
| 2025-04-11 01:00 | 2025-04-11 10:00 | LONG | $80452.7200 | $82706.8600 | $26.60 | 2.80% | Bullish Butterfly | Time |
| 2025-04-12 11:00 | 2025-04-12 20:00 | LONG | $83528.3000 | $85517.2900 | $23.21 | 2.38% | Bullish Butterfly | Time |
| 2025-04-19 00:00 | 2025-04-19 09:00 | LONG | $84436.6700 | $85328.1200 | $10.52 | 1.06% | Bullish Butterfly | Time |
| 2025-04-20 03:00 | 2025-04-20 12:00 | SHORT | $85168.8100 | $84365.5600 | $9.50 | 0.94% | Bearish Butterfly | Time |
| 2025-05-01 03:00 | 2025-05-01 12:00 | SHORT | $94782.6000 | $96373.2000 | $-17.05 | -1.68% | Bearish Butterfly | Time |
| 2025-05-03 22:00 | 2025-05-04 07:00 | SHORT | $96170.1800 | $95879.9900 | $3.02 | 0.30% | Bearish Butterfly | Time |
| 2025-05-09 14:00 | 2025-05-09 23:00 | SHORT | $103155.9900 | $102971.9900 | $1.79 | 0.18% | Bearish Butterfly | Time |
| 2025-05-16 09:00 | 2025-05-16 18:00 | LONG | $103793.6500 | $103691.5500 | $-0.99 | -0.10% | Bullish Butterfly | Time |
| 2025-05-30 13:00 | 2025-05-30 22:00 | SHORT | $105495.5900 | $103966.3300 | $14.54 | 1.45% | Bearish Butterfly | Time |
| 2025-06-02 10:00 | 2025-06-02 19:00 | LONG | $104370.8500 | $104425.6300 | $0.53 | 0.05% | Bullish Butterfly | Time |
| 2025-06-04 07:00 | 2025-06-04 16:00 | LONG | $105320.7500 | $105445.8900 | $1.21 | 0.12% | Bullish Butterfly | Time |
| 2025-06-04 21:00 | 2025-06-05 06:00 | LONG | $104930.6100 | $104452.9300 | $-4.64 | -0.46% | Bullish Butterfly | Time |
| 2025-06-08 04:00 | 2025-06-08 13:00 | LONG | $105614.3800 | $105627.9000 | $0.13 | 0.01% | Bullish Butterfly | Time |
| 2025-06-19 08:00 | 2025-06-19 17:00 | LONG | $104746.1200 | $104521.3100 | $-2.18 | -0.21% | Bullish Butterfly | Time |
| 2025-06-24 14:00 | 2025-06-24 23:00 | LONG | $105517.5000 | $106083.0000 | $5.43 | 0.54% | Bullish Butterfly | Time |
| 2025-06-26 00:00 | 2025-06-26 09:00 | LONG | $107320.0000 | $107325.1200 | $0.05 | 0.00% | Bullish Butterfly | Time |
| 2025-06-26 10:00 | 2025-06-26 19:00 | LONG | $107389.0100 | $107532.9800 | $1.36 | 0.13% | Bullish Butterfly | Time |
| 2025-06-27 09:00 | 2025-06-27 18:00 | LONG | $107083.8000 | $106704.6000 | $-3.61 | -0.35% | Bullish Butterfly | Time |
| 2025-06-27 19:00 | 2025-06-28 04:00 | LONG | $106801.0200 | $107191.1900 | $3.71 | 0.37% | Bullish Butterfly | Time |
| 2025-06-29 01:00 | 2025-06-29 10:00 | SHORT | $107311.0000 | $108153.2600 | $-8.00 | -0.78% | Bearish Butterfly | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-02 13:00 | 2025-04-03 15:00 | LONG | $85215.8200 | $82039.3100 | $-35.41 | -3.73% | Bullish Butterfly | Time |
| 2025-04-08 03:00 | 2025-04-09 02:00 | SHORT | $79904.0000 | $75674.4400 | $48.51 | 5.29% | Bearish Butterfly | TP |
| 2025-04-11 01:00 | 2025-04-12 03:00 | LONG | $80452.7200 | $82973.1300 | $30.15 | 3.13% | Bullish Butterfly | Time |
| 2025-04-12 11:00 | 2025-04-13 13:00 | LONG | $83528.3000 | $83599.1300 | $0.84 | 0.08% | Bullish Butterfly | Time |
| 2025-04-19 00:00 | 2025-04-20 02:00 | LONG | $84436.6700 | $85226.4400 | $9.28 | 0.94% | Bullish Butterfly | Time |
| 2025-04-20 03:00 | 2025-04-21 05:00 | SHORT | $85168.8100 | $87550.0000 | $-27.98 | -2.80% | Bearish Butterfly | Time |
| 2025-05-01 03:00 | 2025-05-02 05:00 | SHORT | $94782.6000 | $96707.5400 | $-19.78 | -2.03% | Bearish Butterfly | Time |
| 2025-05-03 22:00 | 2025-05-05 00:00 | SHORT | $96170.1800 | $94724.1100 | $14.36 | 1.50% | Bearish Butterfly | Time |
| 2025-05-09 14:00 | 2025-05-10 16:00 | SHORT | $103155.9900 | $103435.2200 | $-2.62 | -0.27% | Bearish Butterfly | Time |
| 2025-05-16 09:00 | 2025-05-17 11:00 | LONG | $103793.6500 | $102994.1700 | $-7.44 | -0.77% | Bullish Butterfly | Time |
| 2025-05-30 13:00 | 2025-05-31 15:00 | SHORT | $105495.5900 | $104556.0800 | $8.54 | 0.89% | Bearish Butterfly | Time |
| 2025-06-02 10:00 | 2025-06-03 12:00 | LONG | $104370.8500 | $105307.9400 | $8.69 | 0.90% | Bullish Butterfly | Time |
| 2025-06-04 07:00 | 2025-06-05 09:00 | LONG | $105320.7500 | $104900.0000 | $-3.90 | -0.40% | Bullish Butterfly | Time |
| 2025-06-08 04:00 | 2025-06-09 06:00 | LONG | $105614.3800 | $105692.8300 | $0.72 | 0.07% | Bullish Butterfly | Time |
| 2025-06-19 08:00 | 2025-06-20 10:00 | LONG | $104746.1200 | $105958.8700 | $11.26 | 1.16% | Bullish Butterfly | Time |
| 2025-06-24 14:00 | 2025-06-25 16:00 | LONG | $105517.5000 | $107139.8100 | $15.12 | 1.54% | Bullish Butterfly | Time |
| 2025-06-26 00:00 | 2025-06-27 02:00 | LONG | $107320.0000 | $107253.6000 | $-0.62 | -0.06% | Bullish Butterfly | Time |
| 2025-06-27 09:00 | 2025-06-28 11:00 | LONG | $107083.8000 | $107373.3900 | $2.70 | 0.27% | Bullish Butterfly | Time |
| 2025-06-29 01:00 | 2025-06-29 17:00 | SHORT | $107311.0000 | $107544.4400 | $-2.17 | -0.22% | Bearish Butterfly | End |

## Analysis

**Winner: 9 Periods Strategy**

The 9-period exit strategy outperformed with 6.47% return vs 5.02%.

### Key Observations:
- **Trade Frequency**: 23 vs 19 trades
- **Win Rate Difference**: 69.57% vs 57.89%
- **Return Difference**: 1.44% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
