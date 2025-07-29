# Butterfly Pattern Strategy Comparison - BTCUSDT 6h

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
| Win Rate | 0.00% | 20.00% |
| Total Return | -9.99% | -11.55% |
| Final Capital | $900.08 | $884.53 |
| Total PnL | $-99.92 | $-115.47 |
| Average PnL per Trade | $-19.98 | $-23.09 |
| Best Trade | $-0.99 | $47.59 |
| Worst Trade | $-41.69 | $-106.66 |

## Strategy 1: Exit after 9 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-05 18:00 | 2025-04-08 00:00 | LONG | $83537.9900 | $79872.2500 | $-41.69 | -4.39% | Bullish Butterfly | Time |
| 2025-04-16 18:00 | 2025-04-19 00:00 | SHORT | $84030.3800 | $85079.9900 | $-11.37 | -1.25% | Bearish Butterfly | Time |
| 2025-04-28 06:00 | 2025-04-30 12:00 | LONG | $95319.9900 | $94100.3900 | $-11.51 | -1.28% | Bullish Butterfly | Time |
| 2025-05-15 18:00 | 2025-05-18 00:00 | LONG | $103763.7100 | $103648.2000 | $-0.99 | -0.11% | Bullish Butterfly | Time |
| 2025-06-05 18:00 | 2025-06-08 00:00 | SHORT | $101508.6800 | $105438.3400 | $-34.37 | -3.87% | Bearish Butterfly | Time |

## Strategy 2: Exit after 26 periods

| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |
|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|
| 2025-04-05 18:00 | 2025-04-12 06:00 | LONG | $83537.9900 | $83528.3000 | $-0.11 | -0.01% | Bullish Butterfly | Time |
| 2025-04-16 18:00 | 2025-04-23 06:00 | SHORT | $84030.3800 | $93466.0100 | $-106.66 | -11.23% | Bearish Butterfly | Time |
| 2025-04-28 06:00 | 2025-05-04 18:00 | LONG | $95319.9900 | $94277.6200 | $-9.28 | -1.09% | Bullish Butterfly | Time |
| 2025-05-15 18:00 | 2025-05-21 18:00 | LONG | $103763.7100 | $109643.9900 | $47.59 | 5.67% | Bullish Butterfly | TP |
| 2025-06-05 18:00 | 2025-06-12 06:00 | SHORT | $101508.6800 | $106900.9500 | $-47.01 | -5.31% | Bearish Butterfly | Time |

## Analysis

**Winner: 9 Periods Strategy**

The 9-period exit strategy outperformed with -9.99% return vs -11.55%.

### Key Observations:
- **Trade Frequency**: 5 vs 5 trades
- **Win Rate Difference**: 0.00% vs 20.00%
- **Return Difference**: 1.55% gap

---
*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*
