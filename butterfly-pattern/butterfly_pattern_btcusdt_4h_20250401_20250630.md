# Butterfly Pattern Strategy Comparison - BTCUSDT 4h

## Strategy Overview
- **Pattern**: Butterfly Pattern (Bullish & Bearish)
- **Entry**: At close price when pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods

- **Take Profit**: 5.0%

## Performance Comparison

| Metric | 9 Periods | 26 Periods |
|--------|-----------|------------|
| Total Trades | 5 | 5 |
| Win Rate | 20.00% | 40.00% |
| Total Return | -4.17% | -5.03% |
| Final Capital | $958.26 | $949.69 |
| Total PnL | $-41.74 | $-50.31 |
| Average PnL per Trade | $-8.35 | $-10.06 |
| Best Trade | $5.55 | $67.20 |
| Worst Trade | $-19.42 | $-74.95 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-04 12:00 | 2025-04-06 00:00 | LONG | $82860.0000 | $83344.1400 | $5.55 | 0.58% | Bullish Butterfly | Time |
| 2025-04-18 20:00 | 2025-04-20 08:00 | LONG | $84474.6900 | $84129.8300 | $-3.90 | -0.41% | Bullish Butterfly | Time |
| 2025-04-29 20:00 | 2025-05-01 08:00 | SHORT | $94256.8200 | $96180.0100 | $-19.42 | -2.04% | Bearish Butterfly | Time |
| 2025-05-10 20:00 | 2025-05-12 08:00 | LONG | $104809.5300 | $103762.9000 | $-9.32 | -1.00% | Bullish Butterfly | Time |
| 2025-06-16 00:00 | 2025-06-17 12:00 | LONG | $105921.8400 | $104241.6300 | $-14.66 | -1.59% | Bullish Butterfly | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-04 12:00 | 2025-04-08 20:00 | LONG | $82860.0000 | $76322.4200 | $-74.95 | -7.89% | Bullish Butterfly | Time |
| 2025-04-18 20:00 | 2025-04-22 12:00 | LONG | $84474.6900 | $90934.6100 | $67.20 | 7.65% | Bullish Butterfly | TP |
| 2025-04-29 20:00 | 2025-05-04 04:00 | SHORT | $94256.8200 | $95879.9900 | $-16.23 | -1.72% | Bearish Butterfly | Time |
| 2025-05-10 20:00 | 2025-05-15 04:00 | LONG | $104809.5300 | $101779.9900 | $-26.80 | -2.89% | Bullish Butterfly | Time |
| 2025-06-16 00:00 | 2025-06-20 08:00 | LONG | $105921.8400 | $105977.8200 | $0.48 | 0.05% | Bullish Butterfly | Time |

## Analysis

**Winner: 9 Periods Strategy**

The 9-period exit strategy outperformed with -4.17% return vs -5.03%.

### Key Observations:
- **Trade Frequency**: 5 vs 5 trades
- **Win Rate Difference**: 20.00% vs 40.00%
- **Return Difference**: 0.86% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
