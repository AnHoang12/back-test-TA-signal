# Back Test Report

Đây là báo cáo kết quả back test cho các chỉ báo, mỗi chỉ báo làm với các timeframe {1h, 2h, 4h, 6h, 12h, 1d}. Áp dụng cho 5 mã là {BTC, ETH, XRP, BNB, SOL} cho khoảng thời gian từ 01/04/2025 đến 30/06/2025.

## Butterfly Pattern

### Strategy Overview
- **Pattern**: Butterfly Pattern (Bullish & Bearish)
- **Entry**: At close price when the pattern is detected
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods
- **Take Profit**: 5.0%
- **Position Size**: 90.0% of capital

### 1. BTC

| Timeframe | **9 Periods** |  |  | **26 Periods** |  |  |
|-----------|---------------|--|--|----------------|--|--|
|           | Total trades  | Winrate | Return | Total trades | Winrate | Return |
| 1h        | 23           | 69.57% | 6.47% | 19          | 57.89% | 5.02% |
| 2h        | 11           | 45.45% | 3.75% | 8           | 25.00% | 1.92% |
| 4h        | 5            | 20%    | -4.17% | 5           | 40%    | -5.00% |
| 6h        | 5            | 0%     | -9.99% | 5           | 20%    | -11.55% |
| 12h       | 2            | 0%     | -9.08% | 2           | 0%     | -15.74% |

### 2. ETH

| Timeframe | **9 Periods** |  |  | **26 Periods** |  |  |
|-----------|---------------|--|--|----------------|--|--|
|           | Total trades  | Winrate | Return | Total trades | Winrate | Return |
| 1h        | 21           | 57.14% | -4.07% | 19          | 47.37% | -9.43% |
| 2h        | 13           | 53.85% | 11.87% | 11          | 54.55% | 13.78% |
| 4h        | 6            | 50%    | 10.66% | 6           | 33.33% | 7.96% |
| 6h        | 1            | 100%   | 2.96%  | 1           | 100%   | 7.35% |
| 12h       | -            | -      | -      | -           | -      | - |

### 3. XRP

| Timeframe | **9 Periods** |  |  | **26 Periods** |  |  |
|-----------|---------------|--|--|----------------|--|--|
|           | Total trades  | Winrate | Return | Total trades | Winrate | Return |
| 1h        | 25           | 40%    | 2.75%  | 19          | 57.89% | -4.53% |
| 2h        | 12           | 75%    | 14.72% | 11          | 63.64% | 17.89% |
| 4h        | 6            | 66.67% | 14.83% | 6           | 83.33% | 29.02% |
| 6h        | 3            | 100%   | 10.27% | 3           | 100%   | 15.78% |
| 12h       | 3            | 100%   | 7.90%  | 3           | 100%   | 12.97% |

### 4. BNB

| Timeframe | **9 Periods** |  |  | **26 Periods** |  |  |
|-----------|---------------|--|--|----------------|--|--|
|           | Total trades  | Winrate | Return | Total trades | Winrate | Return |
| 1h        | 19           | 68.42% | 9.44%  | 16          | 62.50% | 13.22% |
| 2h        | 9            | 55.56% | 2.39%  | 8           | 37.5%  | -2.03% |
| 4h        | 11           | 63.64% | 11.74% | 10          | 70%    | 16.18% |
| 6h        | 7            | 85.71% | 14.80% | 5           | 60%    | 9.18% |
| 12h       | 1            | 100%   | 1.08%  | 1           | 0%     | -9.34% |

### 5. SOL

| Timeframe | **9 Periods** |  |  | **26 Periods** |  |  |
|-----------|---------------|--|--|----------------|--|--|
|           | Total trades  | Winrate | Return | Total trades | Winrate | Return |
| 1h        | 16           | 62.5%  | 2.97%  | 12          | 58.33% | 0.62% |
| 2h        | 5            | 40%    | -6.49% | 5           | 80%    | -6.71% |
| 4h        | 3            | 0%     | -9.67% | 3           | 66.67% | -8.31% |
| 6h        | 1            | 0%     | -7.75% | 1           | 100%   | 3.38% |
| 12h       | -            | -      | -      | -           | -      | - |

---

## Triple Pattern

### Strategy 1 Overview
- **Pattern**: Triple Top & Triple Bottom Pattern
- **Entry**: Breakout/breakdown with reversal candles
- **Reversal Candles**: Hammer, Engulfing, Doji patterns
- **Position Management**: Only 1 position at a time
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods
- **Take Profit**: 5.0%
- **Position Size**: 90.0% of capital

### 1. BTC

| Timeframe | **9 Periods** |  |  | **26 Periods** |  |  |
|-----------|---------------|--|--|----------------|--|--|
|           | Total trades  | Winrate | Return | Total trades | Winrate | Return |
| 1h        | 154          | 55.19% | 19.73% | 72          | 47.22% | -14.4% |
| 2h        | 70           | 51.43% | -4.67% | 32          | 53.12% | 12.38% |
| 4h        | 36           | 55.56% | 3.59%  | 17          | 58.82% | 2.63% |
| 6h        | 23           | 56.52% | 13.65% | 11          | 72.73% | 13.49% |
| 12h       | 12           | 83.33% | 10.58% | 7           | 71.43% | 12.85% |
| 1d        | 3            | 66.67% | 2.93%  | 2           | 100%   | 6.39% |

### 2. ETH

| Timeframe | **9 Periods** |  |  | **26 Periods** |  |  |
|-----------|---------------|--|--|----------------|--|--|
|           | Total trades  | Winrate | Return | Total trades | Winrate | Return |
| 1h        | 143          | 46.15% | -1.25% | 69          | 44.93% | -8.93% |
| 2h        | 71           | 43.66% | -20.9% | 37          | 40.54% | -35.78% |
| 4h        | 37           | 45.95% | 7.99%  | 18          | 44.44% | -45.89% |
| 6h        | 20           | 65%    | -4.27% | 10          | 60%    | -29.66% |
| 12h       | 12           | 66.67% | 18.9%  | 7           | 71.43% | 10.54% |
| 1d        | 5            | 60%    | -4.72% | 5           | 80%    | 18.56% |

### 3. XRP

| Timeframe | **9 Periods** |  |  | **26 Periods** |  |  |
|-----------|---------------|--|--|----------------|--|--|
|           | Total trades  | Winrate | Return | Total trades | Winrate | Return |
| 1h        | 152          | 44.74% | -6.11% | 71          | 52.11% | 5.17% |
| 2h        | -            | -      | -      | -           | -      | - |
| 4h        | 38           | 36.84% | -43.65% | 18         | 38.89% | -19.34% |
| 6h        | 17           | 52.94% | -11.16% | 9          | 44.44% | -19.7% |
| 12h       | -            | -      | -      | -           | -      | - |

### 4. BNB

| Timeframe | **9 Periods** |  |  | **26 Periods** |  |  |
|-----------|---------------|--|--|----------------|--|--|
|           | Total trades  | Winrate | Return | Total trades | Winrate | Return |
| 1h        | -            | -      | -      | -           | -      | - |
| 2h        | 73           | 54.79% | 3.60%  | 33          | 39.39% | -1.30% |
| 4h        | 32           | 53.12% | 2.84%  | 18          | 38.89% | -12.85% |
| 6h        | 23           | 52.17% | 4.38%  | 12          | 58.33% | 15.06% |
| 12h       | 9            | 33.33% | 10.17% | 5           | 40.00% | -3.42% |

### 5. SOL

| Timeframe | **9 Periods** |  |  | **26 Periods** |  |  |
|-----------|---------------|--|--|----------------|--|--|
|           | Total trades  | Winrate | Return | Total trades | Winrate | Return |
| 1h        | -            | -      | -      | -           | -      | - |
| 2h        | -            | -      | -      | -           | -      | - |
| 4h        | 38           | 57.89% | -2.72% | 19          | 42.11% | -28.74% |
| 6h        | 23           | 30.43% | -38.80% | 12         | 33.33% | -40.59% |
| 12h       | -            | -      | -      | -           | -      | - |

### Strategy 2 Overview
- **Pattern**: Triple Top & Triple Bottom Pattern
- **Entry**: Breakout/breakdown with reversal candles
- **Reversal Candles**: Hammer, Engulfing, Doji patterns
- **Position Management**: Max 3 positions
- **Exit Strategy 1**: Hold for 9 periods
- **Exit Strategy 2**: Hold for 26 periods
- **Take Profit**: 5.0%
- **Position Size**: 20.0% of capital

### 6. BTC

| Timeframe | **9 Periods** |  |  | **26 Periods** |  |  |
|-----------|---------------|--|--|----------------|--|--|
|           | Total trades  | Winrate | Return | Total trades | Winrate | Return |
| 1h        | -            | -      | -      | -           | -      | - |
| 2h        | 160          | 52.50% | -0.29% | 91          | 57.14% | 6.29% |
| 4h        | 74           | 48.65% | 0.56%  | 44          | 47.73% | 0.74% |
| 6h        | 55           | 60.00% | 4.46%  | 31          | 77.42% | 8.04% |
| 12h       | 28           | 71.43% | 3.28%  | 17          | 70.59% | 6.12% |
| 1d        | -            | -      | -      | -           | -      | - |

### 7. ETH

| Timeframe | **9 Periods** |  |  | **26 Periods** |  |  |
|-----------|---------------|--|--|----------------|--|--|
|           | Total trades  | Winrate | Return | Total trades | Winrate | Return |
| 1h        | -            | -      | -      | -           | -      | - |
| 2h        | 139          | 48.20% | -4.62% | 95          | 42.11% | -5.9% |
| 4h        | 76           | 42.11% | -0.9%  | 51          | 54.9%  | -10.98% |
| 6h        | 39           | 58.97% | 3.1%   | 29          | 65.52% | 3.63% |
| 12h       | 20           | 60%    | 5.14%  | 17          | 82.35% | 11.4% |
| 1d        | -            | -      | -      | -           | -      | - |

### 8. XRP

| Timeframe | **9 Periods** |  |  | **26 Periods** |  |  |
|-----------|---------------|--|--|----------------|--|--|
|           | Total trades  | Winrate | Return | Total trades | Winrate | Return |
| 1h        | -            | -      | -      | -           | -      | - |
| 2h        | 174          | 47.7%  | -1.14% | 102         | 47.06% | -4.91% |
| 4h        | 88           | 39.77% | -15.14% | 53         | 39.62% | -10.49% |
| 6h        | -            | -      | -      | -           | -      | - |
| 12h       | 22           | 36.36% | -5.93% | 12          | 41.67% | -4.07% |

### 9. BNB

| Timeframe | **9 Periods** |  |  | **26 Periods** |  |  |
|-----------|---------------|--|--|----------------|--|--|
|           | Total trades  | Winrate | Return | Total trades | Winrate | Return |
| 1h        | -            | -      | -      | -           | -      | - |
| 2h        | -            | -      | -      | -           | -      | - |
| 4h        | 70           | 45.71% | -1.47% | 46          | 47.83% | -1.35% |
| 6h        | 51           | 43.14% | -0.6%  | 31          | 41.94% | 3.22% |
| 12h       | 19           | 36.84% | -2.14% | 13          | 53.85% | -0.07% |

### 10. SOL

| Timeframe | **9 Periods** |  |  | **26 Periods** |  |  |
|-----------|---------------|--|--|----------------|--|--|
|           | Total trades  | Winrate | Return | Total trades | Winrate | Return |
| 1h        | -            | -      | -      | -           | -      | - |
| 2h        | 170          | 44.71% | 2.45%  | 105         | 51.43% | -0.51% |
| 4h        | 73           | 56.16% | 2.14%  | 51          | 56.86% | 0.14% |
| 6h        | 47           | 44.38% | -9.31% | 32          | 53.12% | -8.6% |
| 12h       | -            | -      | -      | -           | -      | - |