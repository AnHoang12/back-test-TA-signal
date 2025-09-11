import os
import pandas as pd
import argparse
from dotenv import load_dotenv
from datetime import datetime
from sqlalchemy import create_engine

# --- Tham số/Wedge config mặc định ---
NUM_HIGHS = 3
NUM_LOWS = 3
PIVOT_WINDOW = 3
MAX_PATTERN_LENGTH = 48

# --- Argparse giống cấu trúc triple pattern ---
def parse_arguments():
    parser = argparse.ArgumentParser(description='Wedge Pattern Backtest (triple-style)')
    parser.add_argument('symbol', help='Symbol (e.g., BTCUSDT, ETHUSDT)')
    parser.add_argument('timeframe', help='Timeframe (e.g., 1h, 2h, 4h, 1d)')
    parser.add_argument('--initial-balance', type=float, default=10000, help='Initial balance')
    parser.add_argument('--position-size', type=float, default=0.9, help='Position size as percentage of capital')
    parser.add_argument('--exit-periods-1', type=int, default=9, help='Exit periods for strategy 1')
    parser.add_argument('--exit-periods-2', type=int, default=26, help='Exit periods for strategy 2')
    parser.add_argument('--take-profit', type=float, default=3.0, help='Take profit percentage')
    parser.add_argument('--pivot-window', type=int, default=PIVOT_WINDOW, help='Pivot detection window')
    parser.add_argument('--max-pattern-length', type=int, default=MAX_PATTERN_LENGTH, help='Max bars between first and last pivot in pattern')
    parser.add_argument('--num-high-pivots', type=int, default=NUM_HIGHS, help='Number of pivot highs in wedge')
    parser.add_argument('--num-low-pivots', type=int, default=NUM_LOWS, help='Number of pivot lows in wedge')
    return parser.parse_args()

args = parse_arguments()

SYMBOL = args.symbol.upper()
TIMEFRAME = args.timeframe
INITIAL_BALANCE = args.initial_balance
POSITION_SIZE_PCT = args.position_size
EXIT_PERIODS_1 = args.exit_periods_1
EXIT_PERIODS_2 = args.exit_periods_2
TAKE_PROFIT_PERCENT = args.take_profit
NUM_HIGHS = args.num_high_pivots
NUM_LOWS = args.num_low_pivots

print(f"=== WEDGE PATTERN BACKTEST ===")
print(f"Symbol: {SYMBOL}")
print(f"Timeframe: {TIMEFRAME}")
print(f"Initial Balance: ${INITIAL_BALANCE}")
print(f"Position Size: {POSITION_SIZE_PCT*100}% of capital")
print(f"Exit Strategy 1: {EXIT_PERIODS_1} periods")
print(f"Exit Strategy 2: {EXIT_PERIODS_2} periods")
print(f"Take Profit: {TAKE_PROFIT_PERCENT}%")
print(f"Pivot window: {PIVOT_WINDOW}")
print(f"Pattern max length: {MAX_PATTERN_LENGTH}")
print(f"Num highs: {NUM_HIGHS} | Num lows: {NUM_LOWS}")
print("=" * 40)

# --- Kết nối DB giống triple pattern ---
load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

try:
    engine = create_engine(DATABASE_URL)
except Exception as e:
    engine = None
    print(f"Không tạo được kết nối DB: {e}")

def get_binance_data(symbol, interval):
    if engine is None:
        print("Chưa có kết nối DB hợp lệ.")
        return pd.DataFrame()

    table_name = f'"proddb"."coin_prices_1h"'

    query = f"""
        SELECT *
        FROM {table_name}
        WHERE symbol = %(symbol)s
        AND open_time >= EXTRACT(EPOCH FROM NOW()) - 90*24*3600
        AND open_time <= EXTRACT(EPOCH FROM NOW())
        ORDER BY open_time ASC
    """

    try:
        df = pd.read_sql(
            query,
            con=engine,
            params={
                "symbol": symbol,
            },
        )

        if 'open_time' not in df.columns:
            print("Thiếu cột 'open_time' trong dữ liệu trả về từ DB.")
            return pd.DataFrame()

        df['datetime'] = pd.to_datetime(df['open_time'], unit='s')

        required_cols = {'open', 'high', 'low', 'close'}
        if not required_cols.issubset(df.columns):
            print(f"Thiếu cột cần thiết: {required_cols - set(df.columns)}")
            return pd.DataFrame()

        df = df.sort_values('datetime').reset_index(drop=True)

        print(
            f"Đã đọc {len(df)} dòng từ DB bảng {table_name} cho {symbol} {interval}"
        )
        if len(df) > 0:
            print(
                f"Thời gian: {df['datetime'].min()} đến {df['datetime'].max()}"
            )

        return df
    except Exception as e:
        print(f"Lỗi khi đọc dữ liệu từ DB: {e}")
        return pd.DataFrame()

# --- Đọc data ---
df = get_binance_data(SYMBOL, TIMEFRAME)
if len(df) == 0:
    print("Không có dữ liệu để backtest!")
    exit()

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

# --- Backtest: 1 vị thế tại 1 thời điểm (giống triple) ---
def calculate_backtest_results(df, signals, exit_periods, initial_balance, position_size_pct, take_profit_percent):
    results = []
    balance = initial_balance
    position = None

    # Map entry index -> signal (chọn 1 tín hiệu đầu tiên nếu trùng index)
    signal_by_idx = {}
    for s in sorted(signals, key=lambda x: x['entry_idx']):
        signal_by_idx.setdefault(s['entry_idx'], s)

    for i in range(len(df)):
        current_date = df.iloc[i]['datetime']
        current_close = df.iloc[i]['close']

        # Quản lý vị thế đang mở
        if position is not None:
            bars_held = i - position['entry_index']
            should_close = False
            exit_reason = ""

            # Thoát theo thời gian nến giữ
            if bars_held >= exit_periods:
                should_close = True
                exit_reason = "Time"

            # Take profit
            if position['type'] == 'LONG':
                pnl_pct = ((current_close - position['entry_price']) / position['entry_price']) * 100
            else:
                pnl_pct = ((position['entry_price'] - current_close) / position['entry_price']) * 100

            if pnl_pct >= take_profit_percent:
                should_close = True
                exit_reason = "TP"

            if should_close:
                exit_price = current_close
                if position['type'] == 'LONG':
                    pnl = (exit_price - position['entry_price']) * position['quantity']
                else:
                    pnl = (position['entry_price'] - exit_price) * position['quantity']

                balance += position['value'] + pnl

                results.append({
                    'type': position['type'],
                    'pattern_type': position['pattern_type'],
                    'entry_time': position['entry_time'],
                    'entry_price': position['entry_price'],
                    'exit_time': current_date,
                    'exit_price': exit_price,
                    'pnl': pnl,
                    'pnl_percent': (pnl / position['value']) * 100,
                    'balance': balance,
                    'bars_held': bars_held,
                    'exit_reason': exit_reason
                })
                position = None

        # Nếu không có vị thế, xem có tín hiệu mở mới không
        if position is None and i in signal_by_idx:
            sig = signal_by_idx[i]
            entry_price = sig['entry_price']
            position_value = balance * position_size_pct
            quantity = position_value / entry_price if entry_price != 0 else 0

            position = {
                'type': 'LONG' if sig['type'] == 'FALLING' else 'SHORT',
                'entry_time': current_date,
                'entry_index': i,
                'entry_price': entry_price,
                'quantity': quantity,
                'value': position_value,
                'pattern_type': sig['type']
            }
            balance -= position_value

    # Đóng vị thế còn lại khi hết dữ liệu
    if position is not None:
        final_close = df.iloc[-1]['close']
        final_date = df.iloc[-1]['datetime']
        if position['type'] == 'LONG':
            pnl = (final_close - position['entry_price']) * position['quantity']
        else:
            pnl = (position['entry_price'] - final_close) * position['quantity']
        balance += position['value'] + pnl
        bars_held = len(df) - 1 - position['entry_index']
        results.append({
            'type': position['type'],
            'pattern_type': position['pattern_type'],
            'entry_time': position['entry_time'],
            'entry_price': position['entry_price'],
            'exit_time': final_date,
            'exit_price': final_close,
            'pnl': pnl,
            'pnl_percent': (pnl / position['value']) * 100,
            'balance': balance,
            'bars_held': bars_held,
            'exit_reason': 'End'
        })

    return results, balance

# --- Xuất báo cáo ---
def export_wedge_comparison_report(results_1, results_2, final_balance_1, final_balance_2, filename=None):
    if filename is None:
        # Xác định khoảng thời gian từ dữ liệu giao dịch
        all_times = []
        for r in (results_1 or []):
            if 'entry_time' in r and r['entry_time'] is not None:
                all_times.append(r['entry_time'])
            if 'exit_time' in r and r['exit_time'] is not None:
                all_times.append(r['exit_time'])
        for r in (results_2 or []):
            if 'entry_time' in r and r['entry_time'] is not None:
                all_times.append(r['entry_time'])
            if 'exit_time' in r and r['exit_time'] is not None:
                all_times.append(r['exit_time'])

        if all_times:
            start_dt = df['datetime'].min()
            end_dt = df['datetime'].max()
        else:
            end_dt = pd.Timestamp.utcnow()
            start_dt = end_dt - pd.DateOffset(months=2)

        start_date_formatted = pd.to_datetime(start_dt).strftime('%Y%m%d')
        end_date_formatted = pd.to_datetime(end_dt).strftime('%Y%m%d')
        filename = f"wedge_backtest_{SYMBOL.lower()}_{TIMEFRAME}_{start_date_formatted}_{end_date_formatted}.md"

    def calculate_metrics(results):
        if not results:
            return {
                'total_trades': 0, 'win_rate': 0, 'total_return': 0,
                'final_capital': INITIAL_BALANCE, 'total_pnl': 0,
                'avg_pnl': 0, 'best_trade': 0, 'worst_trade': 0,
                'long_trades': 0, 'short_trades': 0
            }

        total_trades = len(results)
        win_trades = sum(1 for r in results if r['pnl'] > 0)
        win_rate = (win_trades / total_trades) * 100
        total_pnl = sum(r['pnl'] for r in results)
        final_capital = results[-1]['balance']
        total_return = ((final_capital - INITIAL_BALANCE) / INITIAL_BALANCE) * 100
        avg_pnl = total_pnl / total_trades if total_trades > 0 else 0
        best_trade = max((r['pnl'] for r in results), default=0)
        worst_trade = min((r['pnl'] for r in results), default=0)
        long_trades = sum(1 for r in results if r['type'] == 'LONG')
        short_trades = sum(1 for r in results if r['type'] == 'SHORT')
        return {
            'total_trades': total_trades, 'win_rate': win_rate, 'total_return': total_return,
            'final_capital': final_capital, 'total_pnl': total_pnl,
            'avg_pnl': avg_pnl, 'best_trade': best_trade, 'worst_trade': worst_trade,
            'long_trades': long_trades, 'short_trades': short_trades
        }

    metrics_1 = calculate_metrics(results_1)
    metrics_2 = calculate_metrics(results_2)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# Wedge Pattern Strategy Comparison - {SYMBOL} {TIMEFRAME}\n\n")
        f.write(f"## Strategy Overview\n")
        f.write(f"- **Pattern**: Rising/Falling Wedge (pivot-based)\n")
        f.write(f"- **Entry**: Breakout after last pivot in wedge\n")
        f.write(f"- **Position Management**: Only 1 position at a time\n")
        f.write(f"- **Exit Strategy 1**: Hold for {EXIT_PERIODS_1} periods\n")
        f.write(f"- **Exit Strategy 2**: Hold for {EXIT_PERIODS_2} periods\n")
        f.write(f"- **Take Profit**: {TAKE_PROFIT_PERCENT}%\n")
        f.write(f"- **Pivot window**: {PIVOT_WINDOW}\n")
        f.write(f"- **Pattern max length**: {MAX_PATTERN_LENGTH}\n")
        f.write(f"- **Num Highs/Lows**: {NUM_HIGHS}/{NUM_LOWS}\n\n")

        f.write(f"## Performance Comparison\n\n")
        f.write(f"| Metric | {EXIT_PERIODS_1} Periods | {EXIT_PERIODS_2} Periods |\n")
        f.write(f"|--------|-----------|------------|\n")
        f.write(f"| Total Trades | {metrics_1['total_trades']} | {metrics_2['total_trades']} |\n")
        f.write(f"| Win Rate | {metrics_1['win_rate']:.2f}% | {metrics_2['win_rate']:.2f}% |\n")
        f.write(f"| Total Return | {metrics_1['total_return']:.2f}% | {metrics_2['total_return']:.2f}% |\n")
        f.write(f"| Final Capital | ${metrics_1['final_capital']:.2f} | ${metrics_2['final_capital']:.2f} |\n")
        f.write(f"| Total PnL | ${metrics_1['total_pnl']:.2f} | ${metrics_2['total_pnl']:.2f} |\n")
        f.write(f"| Average PnL per Trade | ${metrics_1['avg_pnl']:.2f} | ${metrics_2['avg_pnl']:.2f} |\n")
        f.write(f"| Best Trade | ${metrics_1['best_trade']:.2f} | ${metrics_2['best_trade']:.2f} |\n")
        f.write(f"| Worst Trade | ${metrics_1['worst_trade']:.2f} | ${metrics_2['worst_trade']:.2f} |\n")
        f.write(f"| Long Trades | {metrics_1['long_trades']} | {metrics_2['long_trades']} |\n")
        f.write(f"| Short Trades | {metrics_1['short_trades']} | {metrics_2['short_trades']} |\n\n")

        if results_1:
            f.write(f"## Strategy 1: Exit after {EXIT_PERIODS_1} periods\n\n")
            f.write(f"| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |\n")
            f.write(f"|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|\n")
            for r in results_1:
                f.write(f"| {r['entry_time']} | {r['exit_time']} | {r['type']} | ${r['entry_price']:.4f} | ${r['exit_price']:.4f} | ${r['pnl']:.2f} | {r['pnl_percent']:.2f}% | {r['pattern_type']} | {r['exit_reason']} | {r['bars_held']} |\n")
            f.write(f"\n")

        if results_2:
            f.write(f"## Strategy 2: Exit after {EXIT_PERIODS_2} periods\n\n")
            f.write(f"| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |\n")
            f.write(f"|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|\n")
            for r in results_2:
                f.write(f"| {r['entry_time']} | {r['exit_time']} | {r['type']} | ${r['entry_price']:.4f} | ${r['exit_price']:.4f} | ${r['pnl']:.2f} | {r['pnl_percent']:.2f}% | {r['pattern_type']} | {r['exit_reason']} | {r['bars_held']} |\n")
            f.write(f"\n")

        f.write(f"## Analysis\n\n")
        if metrics_2['total_return'] > metrics_1['total_return']:
            f.write(f"**Winner: {EXIT_PERIODS_2} Periods Strategy**\n\n")
            f.write(f"The {EXIT_PERIODS_2}-period exit strategy outperformed with {metrics_2['total_return']:.2f}% return vs {metrics_1['total_return']:.2f}%.\n\n")
        else:
            f.write(f"**Winner: {EXIT_PERIODS_1} Periods Strategy**\n\n")
            f.write(f"The {EXIT_PERIODS_1}-period exit strategy outperformed with {metrics_1['total_return']:.2f}% return vs {metrics_2['total_return']:.2f}%.\n\n")

        f.write("---\n")
        f.write(f"*Báo cáo được tạo tự động bởi Wedge Pattern Backtest System*\n")
    return filename

# --- Chạy backtest ---
if __name__ == "__main__":
    # Tạo tín hiệu wedge từ dữ liệu
    pivot_highs, pivot_lows = find_pivots(df, window=PIVOT_WINDOW)
    signals = find_wedge_patterns(
        df,
        pivot_highs,
        pivot_lows,
        num_highs=NUM_HIGHS,
        num_lows=NUM_LOWS,
        max_pattern_length=MAX_PATTERN_LENGTH,
    )

    print(f"Tổng tín hiệu wedge tìm được: {len(signals)}")

    # Chạy hai chiến lược thoát lệnh
    print("Running strategy 1: Exit after", EXIT_PERIODS_1, "periods")
    results_1, final_balance_1 = calculate_backtest_results(
        df, signals, EXIT_PERIODS_1, INITIAL_BALANCE, POSITION_SIZE_PCT, TAKE_PROFIT_PERCENT
    )

    print("Running strategy 2: Exit after", EXIT_PERIODS_2, "periods")
    results_2, final_balance_2 = calculate_backtest_results(
        df, signals, EXIT_PERIODS_2, INITIAL_BALANCE, POSITION_SIZE_PCT, TAKE_PROFIT_PERCENT
    )

    # Xuất báo cáo so sánh
    report_file = export_wedge_comparison_report(
        results_1, results_2, final_balance_1, final_balance_2
    )
    print(f"Đã xuất báo cáo: {report_file}")

    # In kết quả tóm tắt
    print(f"\n=== KẾT QUẢ TÓM TẮT ===")
    print(f"Strategy 1 ({EXIT_PERIODS_1} periods): {len(results_1)} trades, ${final_balance_1:.2f}")
    print(f"Strategy 2 ({EXIT_PERIODS_2} periods): {len(results_2)} trades, ${final_balance_2:.2f}")
    if final_balance_2 > final_balance_1:
        print(
            f"Winner: Strategy 2 ({EXIT_PERIODS_2} periods) with {((final_balance_2 - INITIAL_BALANCE) / INITIAL_BALANCE * 100):.2f}% return"
        )
    else:
        print(
            f"Winner: Strategy 1 ({EXIT_PERIODS_1} periods) with {((final_balance_1 - INITIAL_BALANCE) / INITIAL_BALANCE * 100):.2f}% return"
        )
