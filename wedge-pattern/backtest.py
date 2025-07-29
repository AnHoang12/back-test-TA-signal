import os
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime
from sqlalchemy import create_engine

# --- Cấu hình ---
NUM_HIGHS = 3  # Số đỉnh liên tiếp cho wedge
NUM_LOWS = 3   # Số đáy liên tiếp cho wedge
TP_PERCENT = 3
SL_PERCENT = 1.5
MAX_HOLD_BARS = 24
INITIAL_BALANCE = 10000
TRADE_AMOUNT = 1000

# --- Đọc dữ liệu ---
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
SELECT * FROM proddb.f_coin_signal_4h 
WHERE symbol = '{SYMBOL}' 
AND open_time >= UNIX_TIMESTAMP('2025-05-01 00:00:00')  
AND open_time < UNIX_TIMESTAMP('2025-07-01 00:00:00')   
ORDER BY open_time ASC;
"""
df = pd.read_sql_query(query, engine)
df['datetime'] = pd.to_datetime(df['open_time'], unit='s')
df = df.sort_values('open_time').reset_index(drop=True)

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

def calc_slope(points):
    # points: list of (idx, price)
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    if len(x) < 2:
        return 0
    return (y[-1] - y[0]) / (x[-1] - x[0])

# --- Nhận diện wedge pattern ---
def find_wedge_patterns(df, pivot_highs, pivot_lows, num_highs=NUM_HIGHS, num_lows=NUM_LOWS, max_pattern_length=72):
    signals = []
    # Rising wedge: N đỉnh cao dần, N đáy cao dần, slope đáy > slope đỉnh
    for i in range(len(pivot_highs) - (num_highs-1)):
        highs = pivot_highs[i:i+num_highs]
        if all(highs[j][1] < highs[j+1][1] for j in range(num_highs-1)):
            # Tìm N đáy cao dần trong cùng khoảng
            lows = [l for l in pivot_lows if highs[0][0] < l[0] < highs[-1][0]]
            for k in range(len(lows) - (num_lows-1)):
                lows_seq = lows[k:k+num_lows]
                if all(lows_seq[j][1] < lows_seq[j+1][1] for j in range(num_lows-1)):
                    # Kiểm tra độ dốc
                    slope_high = calc_slope(highs)
                    slope_low = calc_slope(lows_seq)
                    if slope_low > slope_high and (highs[-1][0] - highs[0][0]) <= max_pattern_length:
                        # Breakout xuống: giá close sau đáy cuối cùng
                        breakout_idx = lows_seq[-1][0] + 1
                        if breakout_idx < len(df):
                            entry_price = df.iloc[breakout_idx]['close']
                            signals.append({
                                'type': 'RISING',
                                'entry_idx': breakout_idx,
                                'entry_time': df.iloc[breakout_idx]['datetime'],
                                'entry_price': entry_price,
                                'pattern_points': highs + lows_seq,
                                'slope_high': slope_high,
                                'slope_low': slope_low
                            })
    # Falling wedge: N đỉnh thấp dần, N đáy thấp dần, slope đáy < slope đỉnh
    for i in range(len(pivot_highs) - (num_highs-1)):
        highs = pivot_highs[i:i+num_highs]
        if all(highs[j][1] > highs[j+1][1] for j in range(num_highs-1)):
            lows = [l for l in pivot_lows if highs[0][0] < l[0] < highs[-1][0]]
            for k in range(len(lows) - (num_lows-1)):
                lows_seq = lows[k:k+num_lows]
                if all(lows_seq[j][1] > lows_seq[j+1][1] for j in range(num_lows-1)):
                    slope_high = calc_slope(highs)
                    slope_low = calc_slope(lows_seq)
                    if slope_low < slope_high and (highs[-1][0] - highs[0][0]) <= max_pattern_length:
                        # Breakout lên: giá close sau đỉnh cuối cùng
                        breakout_idx = highs[-1][0] + 1
                        if breakout_idx < len(df):
                            entry_price = df.iloc[breakout_idx]['close']
                            signals.append({
                                'type': 'FALLING',
                                'entry_idx': breakout_idx,
                                'entry_time': df.iloc[breakout_idx]['datetime'],
                                'entry_price': entry_price,
                                'pattern_points': highs + lows_seq,
                                'slope_high': slope_high,
                                'slope_low': slope_low
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
        if direction == 'FALLING':  # breakout lên (mua)
            tp = entry * (1 + tp_percent/100)
            sl = entry * (1 - sl_percent/100)
        else:  # RISING: breakout xuống (bán)
            tp = entry * (1 - tp_percent/100)
            sl = entry * (1 + sl_percent/100)
        exit_idx = None
        exit_price = None
        exit_reason = None
        for i in range(idx+1, min(idx+max_hold_bars, len(df))):
            hi = df.iloc[i]['high']
            lo = df.iloc[i]['low']
            if direction == 'FALLING':
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
        if direction == 'FALLING':
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

# --- Xuất báo cáo ---
def export_wedge_report(signals, results, final_balance, filename=None):
    if filename is None:
        filename = f"wedge_backtest_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    rising_signals = [s for s in signals if s['type'] == 'RISING']
    falling_signals = [s for s in signals if s['type'] == 'FALLING']
    rising_results = [r for r in results if r['type'] == 'RISING']
    falling_results = [r for r in results if r['type'] == 'FALLING']
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# ⏸️ WEDGE PATTERN BACKTEST REPORT\n\n")
        f.write(f"**Thời gian tạo báo cáo:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"## ⚙️ CÀI ĐẶT CHIẾN THUẬT\n\n")
        f.write(f"- **Số dư ban đầu:** ${INITIAL_BALANCE:,.2f}\n")
        f.write(f"- **Số tiền mỗi lần giao dịch:** ${TRADE_AMOUNT:,.2f}\n")
        f.write(f"- **Take Profit:** {TP_PERCENT}%\n")
        f.write(f"- **Stop Loss:** {SL_PERCENT}%\n")
        f.write(f"- **Max Hold Time:** {MAX_HOLD_BARS} giờ\n")
        f.write(f"- **Pivot window:** 3\n")
        f.write(f"- **Pattern max length:** 72\n")
        f.write(f"- **Num Highs:** {NUM_HIGHS}\n")
        f.write(f"- **Num Lows:** {NUM_LOWS}\n\n")
        if len(results) > 0:
            total_signals = len(results)
            win_trades = sum(1 for r in results if r['pnl'] > 0)
            winrate = (win_trades / total_signals) * 100
            total_pnl = sum(r['pnl'] for r in results)
            roi = ((final_balance - INITIAL_BALANCE) / INITIAL_BALANCE) * 100
            profit_factor = abs(sum(r['pnl'] for r in results if r['pnl'] > 0) / sum(r['pnl'] for r in results if r['pnl'] < 0)) if any(r['pnl'] < 0 for r in results) else float('inf')
            f.write(f"## 📊 KẾT QUẢ TỔNG QUAN\n\n")
            f.write(f"- **Tổng số tín hiệu:** {total_signals}\n")
            f.write(f"- **Rising Wedge:** {len(rising_signals)}\n")
            f.write(f"- **Falling Wedge:** {len(falling_signals)}\n")
            f.write(f"- **Win Rate:** {winrate:.2f}%\n")
            f.write(f"- **Số dư cuối kỳ:** ${final_balance:,.2f}\n")
            f.write(f"- **Tổng lợi nhuận:** ${total_pnl:+,.2f}\n")
            f.write(f"- **ROI:** {roi:+.2f}%\n")
            f.write(f"- **Profit Factor:** {profit_factor:.2f}\n\n")
            if rising_results:
                rising_win = sum(1 for r in rising_results if r['pnl'] > 0)
                rising_pnl = sum(r['pnl'] for r in rising_results)
                f.write(f"### ⏫ Rising Wedge\n\n")
                f.write(f"- **Số tín hiệu:** {len(rising_results)}\n")
                f.write(f"- **Win Rate:** {(rising_win/len(rising_results))*100:.1f}%\n")
                f.write(f"- **PnL:** ${rising_pnl:+,.2f}\n\n")
            if falling_results:
                falling_win = sum(1 for r in falling_results if r['pnl'] > 0)
                falling_pnl = sum(r['pnl'] for r in falling_results)
                f.write(f"### ⏬ Falling Wedge\n\n")
                f.write(f"- **Số tín hiệu:** {len(falling_results)}\n")
                f.write(f"- **Win Rate:** {(falling_win/len(falling_results))*100:.1f}%\n")
                f.write(f"- **PnL:** ${falling_pnl:+,.2f}\n\n")
            f.write(f"## 📋 CHI TIẾT GIAO DỊCH\n\n")
            f.write(f"| STT | Type | Entry Time | Entry | Exit Time | Exit | PnL | Balance | Reason |\n")
            f.write(f"|-----|------|----------------|-------|----------------|-------|-------|---------|--------|\n")
            for i, r in enumerate(results, 1):
                f.write(f"| {i} | {r['type']} | {r['entry_time']} | ${r['entry_price']:.2f} | {r['exit_time']} | ${r['exit_price']:.2f} | ${r['pnl']:+.2f} | ${r['balance']:.2f} | {r['exit_reason']} |\n")
        else:
            f.write("## ❌ KẾT QUẢ\n\n")
            f.write("Không tìm thấy wedge pattern nào phù hợp với điều kiện lọc.\n\n")
        f.write("---\n")
        f.write(f"*Báo cáo được tạo tự động bởi Wedge Pattern Backtest System*\n")
    return filename

# --- Chạy backtest ---
pivot_highs, pivot_lows = find_pivots(df, window=3)
signals = find_wedge_patterns(df, pivot_highs, pivot_lows, num_highs=NUM_HIGHS, num_lows=NUM_LOWS)
results, final_balance = calculate_backtest_results(df, signals)
report_file = export_wedge_report(signals, results, final_balance)
print(f"Đã xuất báo cáo: {report_file}")
