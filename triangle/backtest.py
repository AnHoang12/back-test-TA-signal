import os
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime
from sqlalchemy import create_engine

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

SYMBOL = "BTCUSDT"

query = f"""
SELECT * FROM proddb.f_coin_signal_1d 
WHERE symbol = '{SYMBOL}' 
AND open_time >= UNIX_TIMESTAMP('2025-05-01 00:00:00')  
AND open_time < UNIX_TIMESTAMP('2025-07-01 00:00:00')   
ORDER BY open_time ASC;
"""

# print(query)
df = pd.read_sql_query(query, engine)

df['datetime'] = pd.to_datetime(df['open_time'], unit='s')
df = df.sort_values('open_time').reset_index(drop=True)

print(f"Dữ liệu từ {df['datetime'].min()} đến {df['datetime'].max()}")
print(f"Tổng số candle: {len(df)}")

# Cấu hình số lượng đáy/đỉnh liên tiếp
NUM_LOWS = 3   # Số đáy liên tiếp cao dần cho tam giác tăng (>=3)
NUM_HIGHS = 3  # Số đỉnh liên tiếp thấp dần cho tam giác giảm (>=3)
TP_PERCENT = 4
SL_PERCENT = 1.5
MAX_HOLD_BARS = 24
INITIAL_BALANCE = 10000
TRADE_AMOUNT = 1000

# --- Tìm pivot points ---
def find_pivots(data, window=5):
    highs = data['high'].values
    lows = data['low'].values
    pivot_highs = []
    pivot_lows = []
    for i in range(window, len(data) - window):
        if all(highs[i] >= highs[j] for j in range(i-window, i+window+1) if j != i):
            pivot_highs.append((i, highs[i]))
        if all(lows[i] <= lows[j] for j in range(i-window, i+window+1) if j != i):
            pivot_lows.append((i, lows[i]))
    return pivot_highs, pivot_lows



# --- Nhận diện triangle pattern ---
def find_triangle_patterns(df, pivot_highs, pivot_lows, max_pattern_length=72, num_lows=NUM_LOWS, num_highs=NUM_HIGHS):
    """
    Tìm triangle pattern (tam giác tăng/giảm) với số lượng đáy/đỉnh cấu hình được
    - Tam giác tăng: num_lows đáy liên tiếp cao dần, >=2 đỉnh gần ngang
    - Tam giác giảm: num_highs đỉnh liên tiếp thấp dần, >=2 đáy gần ngang
    """
    signals = []
    # Tam giác tăng: num_lows đáy cao dần
    for i in range(len(pivot_lows) - (num_lows-1)):
        lows = pivot_lows[i:i+num_lows]
        if all(lows[j][1] < lows[j+1][1] for j in range(num_lows-1)):
            # Tìm các đỉnh gần các đáy này
            highs = [h for h in pivot_highs if lows[0][0] < h[0] < lows[-1][0]]
            if len(highs) >= 2:
                h1, h2 = highs[0], highs[-1]
                if abs(h1[1] - h2[1]) / h1[1] < 0.01:
                    breakout_idx = h2[0] + 1
                    if breakout_idx < len(df):
                        entry_price = df.iloc[breakout_idx]['close']
                        signals.append({
                            'type': 'UP',
                            'entry_idx': breakout_idx,
                            'entry_time': df.iloc[breakout_idx]['datetime'],
                            'entry_price': entry_price,
                            'pattern_points': lows + [h1, h2]
                        })
    # Tam giác giảm: num_highs đỉnh thấp dần
    for i in range(len(pivot_highs) - (num_highs-1)):
        highs = pivot_highs[i:i+num_highs]
        if all(highs[j][1] > highs[j+1][1] for j in range(num_highs-1)):
            # Tìm các đáy gần các đỉnh này
            lows = [l for l in pivot_lows if highs[0][0] < l[0] < highs[-1][0]]
            if len(lows) >= 2:
                l1, l2 = lows[0], lows[-1]
                if abs(l1[1] - l2[1]) / l1[1] < 0.01:
                    breakout_idx = l2[0] + 1
                    if breakout_idx < len(df):
                        entry_price = df.iloc[breakout_idx]['close']
                        signals.append({
                            'type': 'DOWN',
                            'entry_idx': breakout_idx,
                            'entry_time': df.iloc[breakout_idx]['datetime'],
                            'entry_price': entry_price,
                            'pattern_points': highs + [l1, l2]
                        })
    return signals

# --- Backtest ---
def calculate_backtest_results(df, signals, tp_percent=TP_PERCENT, sl_percent=SL_PERCENT, max_hold_bars=MAX_HOLD_BARS, initial_balance=INITIAL_BALANCE, trade_amount=TRADE_AMOUNT):
    results = []
    balance = initial_balance
    for sig in signals:
        idx = sig['entry_idx']
        entry = sig['entry_price']
        direction = sig['type']
        qty = trade_amount / entry
        if direction == 'UP':
            tp = entry * (1 + tp_percent/100)
            sl = entry * (1 - sl_percent/100)
        else:
            tp = entry * (1 - tp_percent/100)
            sl = entry * (1 + sl_percent/100)
        exit_idx = None
        exit_price = None
        exit_reason = None
        for i in range(idx+1, min(idx+max_hold_bars, len(df))):
            hi = df.iloc[i]['high']
            lo = df.iloc[i]['low']
            if direction == 'UP':
                if hi >= tp:
                    exit_idx, exit_price, exit_reason = i, tp, 'TP'; break
                if lo <= sl:
                    exit_idx, exit_price, exit_reason = i, sl, 'SL'; break
            else:
                if lo <= tp:
                    exit_idx, exit_price, exit_reason = i, tp, 'TP'; break
                if hi >= sl:
                    exit_idx, exit_price, exit_reason = i, sl, 'SL'; break
        if exit_idx is None:
            exit_idx = min(idx+max_hold_bars, len(df)-1)
            exit_price = df.iloc[exit_idx]['close']
            exit_reason = 'Time'
        if direction == 'UP':
            pnl = (exit_price - entry) * qty
        else:
            pnl = (entry - exit_price) * qty
        balance += pnl
        results.append({
            'type': direction,
            'entry_time': sig['entry_time'],
            'entry_price': entry,
            'exit_time': df.iloc[exit_idx]['datetime'],
            'exit_price': exit_price,
            'exit_reason': exit_reason,
            'pnl': pnl,
            'balance': balance
        })
    return results, balance

# --- Xuất báo cáo đơn giản ---
def export_triangle_report(signals, results, final_balance, filename=None, initial_balance=INITIAL_BALANCE, tp_percent=TP_PERCENT, sl_percent=SL_PERCENT, max_hold_bars=MAX_HOLD_BARS):
    if filename is None:
        filename = f"triangle_backtest_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    up_signals = [s for s in signals if s['type'] == 'UP']
    down_signals = [s for s in signals if s['type'] == 'DOWN']
    up_results = [r for r in results if r['type'] == 'UP']
    down_results = [r for r in results if r['type'] == 'DOWN']
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# 🔺 TRIANGLE PATTERN BACKTEST REPORT\n\n")
        f.write(f"**Thời gian tạo báo cáo:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"## ⚙️ CÀI ĐẶT CHIẾN THUẬT\n\n")
        f.write(f"- **Số dư ban đầu:** ${initial_balance:,.2f}\n")
        f.write(f"- **Số tiền mỗi lần giao dịch:** $1,000.00\n")
        f.write(f"- **Take Profit:** {tp_percent}%\n")
        f.write(f"- **Stop Loss:** {sl_percent}%\n")
        f.write(f"- **Max Hold Time:** {max_hold_bars} giờ\n")
        f.write(f"- **Pivot window:** 3\n")
        f.write(f"- **Pattern max length:** 72\n")
        f.write(f"- **Num Lows (UP):** {NUM_LOWS}\n")
        f.write(f"- **Num Highs (DOWN):** {NUM_HIGHS}\n\n")
        if len(results) > 0:
            total_signals = len(results)
            win_trades = sum(1 for r in results if r['pnl'] > 0)
            lose_trades = total_signals - win_trades
            winrate = (win_trades / total_signals) * 100
            total_pnl = sum(r['pnl'] for r in results)
            roi = ((final_balance - initial_balance) / initial_balance) * 100
            profit_factor = abs(sum(r['pnl'] for r in results if r['pnl'] > 0) / sum(r['pnl'] for r in results if r['pnl'] < 0)) if any(r['pnl'] < 0 for r in results) else float('inf')
            f.write(f"## 📊 KẾT QUẢ TỔNG QUAN\n\n")
            f.write(f"- **Tổng số tín hiệu:** {total_signals}\n")
            f.write(f"- **Triangle Up (Breakout lên):** {len(up_signals)}\n")
            f.write(f"- **Triangle Down (Breakout xuống):** {len(down_signals)}\n")
            f.write(f"- **Win Rate:** {winrate:.2f}%\n")
            f.write(f"- **Số dư cuối kỳ:** ${final_balance:,.2f}\n")
            f.write(f"- **Tổng lợi nhuận:** ${total_pnl:+,.2f}\n")
            f.write(f"- **ROI:** {roi:+.2f}%\n")
            f.write(f"- **Profit Factor:** {profit_factor:.2f}\n\n")
            # Phân tích riêng từng loại
            if up_results:
                up_win = sum(1 for r in up_results if r['pnl'] > 0)
                up_pnl = sum(r['pnl'] for r in up_results)
                f.write(f"### 📈 Triangle Up (Breakout lên)\n\n")
                f.write(f"- **Số tín hiệu:** {len(up_results)}\n")
                f.write(f"- **Win Rate:** {(up_win/len(up_results))*100:.1f}%\n")
                f.write(f"- **PnL:** ${up_pnl:+,.2f}\n\n")
            if down_results:
                down_win = sum(1 for r in down_results if r['pnl'] > 0)
                down_pnl = sum(r['pnl'] for r in down_results)
                f.write(f"### 📉 Triangle Down (Breakout xuống)\n\n")
                f.write(f"- **Số tín hiệu:** {len(down_results)}\n")
                f.write(f"- **Win Rate:** {(down_win/len(down_results))*100:.1f}%\n")
                f.write(f"- **PnL:** ${down_pnl:+,.2f}\n\n")
            # Bảng chi tiết giao dịch
            f.write(f"## 📋 CHI TIẾT GIAO DỊCH\n\n")
            f.write(f"| STT | Type | Entry Time | Entry | Exit Time | Exit | PnL | Balance | Reason |\n")
            f.write(f"|-----|------|----------------|-------|----------------|-------|-------|---------|--------|\n")
            for i, r in enumerate(results, 1):
                f.write(f"| {i} | {r['type']} | {r['entry_time']} | ${r['entry_price']:.2f} | {r['exit_time']} | ${r['exit_price']:.2f} | ${r['pnl']:+.2f} | ${r['balance']:.2f} | {r['exit_reason']} |\n")
        else:
            f.write("## ❌ KẾT QUẢ\n\n")
            f.write("Không tìm thấy triangle pattern nào phù hợp với điều kiện lọc.\n\n")
        f.write("---\n")
        f.write(f"*Báo cáo được tạo tự động bởi Triangle Pattern Backtest System*\n")
    return filename

# --- Chạy backtest ---
pivot_highs, pivot_lows = find_pivots(df, window=3)
signals = find_triangle_patterns(df, pivot_highs, pivot_lows, max_pattern_length=72, num_lows=NUM_LOWS, num_highs=NUM_HIGHS)
results, final_balance = calculate_backtest_results(df, signals)
report_file = export_triangle_report(signals, results, final_balance)
print(f"Đã xuất báo cáo: {report_file}")