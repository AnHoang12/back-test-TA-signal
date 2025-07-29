# Butterfly Pattern Strategy Comparison - BNBUSDT 2h

## Strategy Overview
- **Pattern**: Butterfly Pattern (Bullish & Bearish)
- **Entry**: At close price when pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods

- **Take Profit**: 5.0%

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 9 | 8 |
| Win Rate | 55.56% | 37.50% |
| Total Return | 2.39% | -2.03% |
| Final Capital | $1023.85 | $979.74 |
| Total PnL | $23.85 | $-20.26 |
| Average PnL per Trade | $2.65 | $-2.53 |
| Best Trade | $16.53 | $20.80 |
| Worst Trade | $-9.40 | $-38.83 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-10 10:00 | 2025-04-11 04:00 | SHORT | $575.6900 | $579.8900 | $-6.93 | -0.73% | Bearish Butterfly | Time |
| 2025-04-15 12:00 | 2025-04-16 06:00 | SHORT | $587.0700 | $578.2500 | $14.17 | 1.50% | Bearish Butterfly | Time |
| 2025-04-28 00:00 | 2025-04-28 18:00 | SHORT | $599.0400 | $604.8600 | $-9.30 | -0.97% | Bearish Butterfly | Time |
| 2025-05-16 04:00 | 2025-05-16 22:00 | SHORT | $658.2400 | $646.7600 | $16.53 | 1.74% | Bearish Butterfly | Time |
| 2025-05-16 22:00 | 2025-05-17 16:00 | LONG | $646.7600 | $640.4500 | $-9.40 | -0.98% | Bullish Butterfly | Time |
| 2025-05-25 02:00 | 2025-05-25 20:00 | LONG | $665.9100 | $666.3100 | $0.57 | 0.06% | Bullish Butterfly | Time |
| 2025-06-14 00:00 | 2025-06-14 18:00 | SHORT | $650.9400 | $640.7300 | $14.98 | 1.57% | Bearish Butterfly | Time |
| 2025-06-26 04:00 | 2025-06-26 22:00 | SHORT | $647.0000 | $642.3000 | $7.04 | 0.73% | Bearish Butterfly | Time |
| 2025-06-28 18:00 | 2025-06-29 12:00 | SHORT | $647.5600 | $650.1000 | $-3.83 | -0.39% | Bearish Butterfly | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-10 10:00 | 2025-04-12 14:00 | SHORT | $575.6900 | $599.2200 | $-38.83 | -4.09% | Bearish Butterfly | Time |
| 2025-04-15 12:00 | 2025-04-17 16:00 | SHORT | $587.0700 | $592.0600 | $-7.76 | -0.85% | Bearish Butterfly | Time |
| 2025-04-28 00:00 | 2025-04-30 04:00 | SHORT | $599.0400 | $602.8000 | $-5.69 | -0.63% | Bearish Butterfly | Time |
| 2025-05-16 04:00 | 2025-05-18 08:00 | SHORT | $658.2400 | $645.1900 | $17.85 | 1.98% | Bearish Butterfly | Time |
| 2025-05-25 02:00 | 2025-05-27 06:00 | LONG | $665.9100 | $681.0100 | $20.80 | 2.27% | Bullish Butterfly | Time |
| 2025-06-14 00:00 | 2025-06-16 04:00 | SHORT | $650.9400 | $654.5900 | $-5.25 | -0.56% | Bearish Butterfly | Time |
| 2025-06-26 04:00 | 2025-06-28 08:00 | SHORT | $647.0000 | $646.7600 | $0.35 | 0.04% | Bearish Butterfly | Time |
| 2025-06-28 18:00 | 2025-06-29 16:00 | SHORT | $647.5600 | $648.7600 | $-1.73 | -0.19% | Bearish Butterfly | End |

## Analysis

**Winner: 9 Periods Strategy**

The 9-period exit strategy outperformed with 2.39% return vs -2.03%.

### Key Observations:
- **Trade Frequency**: 9 vs 8 trades
- **Win Rate Difference**: 55.56% vs 37.50%
- **Return Difference**: 4.41% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
