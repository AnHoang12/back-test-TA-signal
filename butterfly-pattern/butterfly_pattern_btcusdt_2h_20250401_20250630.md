# Butterfly Pattern Strategy Comparison - BTCUSDT 2h

## Strategy Overview
- **Pattern**: Butterfly Pattern (Bullish & Bearish)
- **Entry**: At close price when pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods

- **Take Profit**: 5.0%

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 11 | 8 |
| Win Rate | 45.45% | 25.00% |
| Total Return | 3.75% | 1.92% |
| Final Capital | $1037.48 | $1019.19 |
| Total PnL | $37.48 | $19.19 |
| Average PnL per Trade | $3.41 | $2.40 |
| Best Trade | $33.27 | $48.95 |
| Worst Trade | $-20.02 | $-25.00 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-11 02:00 | 2025-04-11 20:00 | LONG | $80842.9900 | $83674.0100 | $33.27 | 3.50% | Bullish Butterfly | Time |
| 2025-04-16 18:00 | 2025-04-17 12:00 | SHORT | $84334.0100 | $84475.1400 | $-1.64 | -0.17% | Bearish Butterfly | Time |
| 2025-04-17 18:00 | 2025-04-18 12:00 | SHORT | $84849.0600 | $84570.6100 | $3.22 | 0.33% | Bearish Butterfly | Time |
| 2025-04-29 02:00 | 2025-04-29 20:00 | SHORT | $94658.7600 | $94735.6600 | $-0.80 | -0.08% | Bearish Butterfly | Time |
| 2025-05-02 08:00 | 2025-05-03 02:00 | LONG | $96596.6800 | $96337.5000 | $-2.64 | -0.27% | Bullish Butterfly | Time |
| 2025-05-12 00:00 | 2025-05-12 18:00 | LONG | $103984.1400 | $101860.0000 | $-20.02 | -2.04% | Bullish Butterfly | Time |
| 2025-05-13 04:00 | 2025-05-13 22:00 | LONG | $102477.1500 | $104103.7200 | $15.25 | 1.59% | Bullish Butterfly | Time |
| 2025-05-17 22:00 | 2025-05-18 16:00 | SHORT | $103126.6500 | $104836.6700 | $-16.17 | -1.66% | Bearish Butterfly | Time |
| 2025-05-29 12:00 | 2025-05-30 06:00 | SHORT | $107601.0800 | $105028.0200 | $22.96 | 2.39% | Bearish Butterfly | Time |
| 2025-06-18 20:00 | 2025-06-19 14:00 | LONG | $105085.5000 | $104096.9300 | $-9.24 | -0.94% | Bullish Butterfly | Time |
| 2025-06-19 18:00 | 2025-06-20 12:00 | LONG | $104250.4400 | $105674.0000 | $13.29 | 1.37% | Bullish Butterfly | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-11 02:00 | 2025-04-12 14:00 | LONG | $80842.9900 | $85008.4000 | $48.95 | 5.15% | Bullish Butterfly | TP |
| 2025-04-16 18:00 | 2025-04-18 22:00 | SHORT | $84334.0100 | $84474.6900 | $-1.66 | -0.17% | Bearish Butterfly | Time |
| 2025-04-29 02:00 | 2025-05-01 06:00 | SHORT | $94658.7600 | $95025.8400 | $-3.86 | -0.39% | Bearish Butterfly | Time |
| 2025-05-02 08:00 | 2025-05-04 12:00 | LONG | $96596.6800 | $95369.3700 | $-12.59 | -1.27% | Bullish Butterfly | Time |
| 2025-05-12 00:00 | 2025-05-14 04:00 | LONG | $103984.1400 | $103896.7100 | $-0.82 | -0.08% | Bullish Butterfly | Time |
| 2025-05-17 22:00 | 2025-05-20 02:00 | SHORT | $103126.6500 | $105761.9200 | $-25.00 | -2.56% | Bearish Butterfly | Time |
| 2025-05-29 12:00 | 2025-05-31 16:00 | SHORT | $107601.0800 | $104349.0600 | $28.86 | 3.02% | Bearish Butterfly | Time |
| 2025-06-18 20:00 | 2025-06-21 00:00 | LONG | $105085.5000 | $103515.3600 | $-14.68 | -1.49% | Bullish Butterfly | Time |

## Analysis

**Winner: 9 Periods Strategy**

The 9-period exit strategy outperformed with 3.75% return vs 1.92%.

### Key Observations:
- **Trade Frequency**: 11 vs 8 trades
- **Win Rate Difference**: 45.45% vs 25.00%
- **Return Difference**: 1.83% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
