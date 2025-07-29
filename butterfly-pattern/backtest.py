import os
import pandas as pd
import argparse
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# --- Hàm đọc data từ folder binance_data ---
def get_binance_data(symbol, interval, start_date, end_date):
    """
    Đọc data từ folder binance_data
    Args:
        symbol: BTCUSDT, ETHUSDT, etc.
        interval: 1h, 2h, 4h, 1d, etc.
        start_date: '2025-05-01'
        end_date: '2025-06-30'
    """
    # Tạo tên file theo format: binance_data/BTCUSDT_2h.csv
    filename = f"/home/anhoang/trade-bot/back-test/binance_data/{symbol}_{interval}.csv"
    
    try:
        # Đọc file CSV
        df = pd.read_csv(filename)
        
        # Chuyển đổi cột timestamp thành datetime
        df['datetime'] = pd.to_datetime(df['timestamp'])
        
        # Lọc theo khoảng thời gian
        start_dt = pd.to_datetime(start_date)
        end_dt = pd.to_datetime(end_date)
        
        df = df[(df['datetime'] >= start_dt) & (df['datetime'] <= end_dt)]
        
        # Sắp xếp theo thời gian
        df = df.sort_values('datetime').reset_index(drop=True)
        
        print(f"Đã đọc data từ {filename}")
        print(f"Tổng số candles: {len(df)}")
        print(f"Thời gian: {df['datetime'].min()} đến {df['datetime'].max()}")
        
        return df
        
    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
        print("Vui lòng đảm bảo file tồn tại trong folder binance_data/")
        print("Format tên file: {symbol}_{interval}.csv")
        print("Cấu trúc file cần có các cột: timestamp,open,high,low,close,volume")
        return pd.DataFrame()
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
        return pd.DataFrame()

# --- Argument Parser ---
def parse_arguments():
    parser = argparse.ArgumentParser(description='Butterfly Pattern Backtest')
    parser.add_argument('symbol', help='Symbol (e.g., BTCUSDT, ETHUSDT)')
    parser.add_argument('timeframe', help='Timeframe (e.g., 1h, 2h, 4h, 1d)')
    parser.add_argument('--start-date', default='2025-04-01', help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end-date', default='2025-06-30', help='End date (YYYY-MM-DD)')
    parser.add_argument('--initial-balance', type=float, default=1000, help='Initial balance')
    parser.add_argument('--trade-amount', type=float, default=100, help='Trade amount per signal')
    parser.add_argument('--exit-periods-1', type=int, default=9, help='Exit periods for strategy 1')
    parser.add_argument('--exit-periods-2', type=int, default=26, help='Exit periods for strategy 2')
    parser.add_argument('--take-profit', type=float, default=5.0, help='Take profit percentage')
    
    return parser.parse_args()

# --- Cấu hình ---
args = parse_arguments()

SYMBOL = args.symbol.upper()
TIMEFRAME = args.timeframe
START_DATE = args.start_date
END_DATE = args.end_date
INITIAL_BALANCE = args.initial_balance
TRADE_AMOUNT = args.trade_amount
EXIT_PERIODS_1 = args.exit_periods_1
EXIT_PERIODS_2 = args.exit_periods_2
TAKE_PROFIT_PERCENT = args.take_profit

print(f"=== BUTTERFLY PATTERN BACKTEST ===")
print(f"Symbol: {SYMBOL}")
print(f"Timeframe: {TIMEFRAME}")
print(f"Period: {START_DATE} to {END_DATE}")
print(f"Initial Balance: ${INITIAL_BALANCE}")
print(f"Trade Amount: ${TRADE_AMOUNT}")
print(f"Exit Strategy 1: {EXIT_PERIODS_1} periods")
print(f"Exit Strategy 2: {EXIT_PERIODS_2} periods")
print(f"Take Profit: {TAKE_PROFIT_PERCENT}%")
print("=" * 40)

# --- Đọc data từ folder binance_data ---
df = get_binance_data(SYMBOL, TIMEFRAME, START_DATE, END_DATE)

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

# --- Detect swing points (từ cách 2) ---
def detect_swing_points(df, window=3):
    """Detect swing highs and lows"""
    df = df.copy()
    df['swing_high'] = False
    df['swing_low'] = False
    
    for i in range(window, len(df) - window):
        # Swing high: highest point in the window
        if df.loc[i, 'high'] == df.loc[i-window:i+window, 'high'].max():
            df.loc[i, 'swing_high'] = True
        
        # Swing low: lowest point in the window  
        if df.loc[i, 'low'] == df.loc[i-window:i+window, 'low'].min():
            df.loc[i, 'swing_low'] = True
    
    return df

# --- Check Fibonacci tolerance (từ cách 2) ---
def is_within_tolerance(actual, expected, tolerance=0.15):
    """Check if actual value is within tolerance of expected Fibonacci ratio"""
    return abs(actual - expected) / expected <= tolerance

# --- Nhận diện Butterfly Pattern (áp dụng cách 2) ---
def find_butterfly_patterns(df, max_pattern_length=72):
    """
    Tìm Butterfly Pattern theo cách 2 với swing points và tolerance cao hơn:
    
    🟢 Bullish Butterfly Pattern:
    Cấu trúc: X(low) → A(high) → B(low) → C(high) → D(low - entry point)
    Tỷ lệ Fibonacci với tolerance 15-25%:
    - AB = 0.786 của XA
    - BC = 0.382 hoặc 0.886 của AB  
    - CD = 1.27 hoặc 1.618 của BC
    - AD = 0.786 của XA
    
    🔴 Bearish Butterfly Pattern:
    Cấu trúc: X(high) → A(low) → B(high) → C(low) → D(high - entry point)
    """
    signals = []
    
    # Detect swing points
    df = detect_swing_points(df, window=3)
    
    # Tìm Bullish Butterfly Pattern
    for i in range(15, len(df)):  # Bắt đầu từ index 15 như cách 2
        if i < 15:
            continue
            
        # Look for swing points in recent history
        recent_data = df.iloc[max(0, i-15):i+1]
        
        # Find potential X, A, B, C points
        swing_highs = recent_data[recent_data['swing_high'] == True]
        swing_lows = recent_data[recent_data['swing_low'] == True]
        
        if len(swing_highs) < 2 or len(swing_lows) < 2:
            continue
        
        try:
            # For bullish butterfly: X(low), A(high), B(low), C(high), D(low - current)
            C = swing_highs.iloc[-1]  # Most recent high
            B = swing_lows.iloc[-1]   # Most recent low before C
            A = swing_highs.iloc[-2] if len(swing_highs) >= 2 else None
            X = swing_lows.iloc[-2] if len(swing_lows) >= 2 else None
            
            if A is None or X is None:
                continue
            
            # Current point D (potential entry)
            D_price = df.loc[i, 'low']
            
            # Calculate ratios
            XA = abs(A['high'] - X['low'])
            AB = abs(B['low'] - A['high']) 
            BC = abs(C['high'] - B['low'])
            CD = abs(D_price - C['high'])
            AD = abs(D_price - A['high'])
            
            if XA == 0 or AB == 0 or BC == 0:
                continue
            
            # Check Fibonacci ratios với tolerance cao hơn
            AB_XA_ratio = AB / XA
            BC_AB_ratio = BC / AB
            CD_BC_ratio = CD / BC if BC > 0 else 0
            AD_XA_ratio = AD / XA
            
            # Butterfly pattern ratios với tolerance 15-25%
            valid_AB = is_within_tolerance(AB_XA_ratio, 0.786, 0.2)
            valid_BC = (is_within_tolerance(BC_AB_ratio, 0.382, 0.2) or 
                       is_within_tolerance(BC_AB_ratio, 0.886, 0.2))
            valid_CD = (is_within_tolerance(CD_BC_ratio, 1.27, 0.25) or
                       is_within_tolerance(CD_BC_ratio, 1.618, 0.25))
            valid_AD = is_within_tolerance(AD_XA_ratio, 0.786, 0.2)
            
            if valid_AB and valid_BC and valid_CD and valid_AD:
                entry_idx = i + 1
                if entry_idx < len(df):
                    entry_price = df.iloc[entry_idx]['close']
                    signals.append({
                        'type': 'Bullish Butterfly',
                        'entry_idx': entry_idx,
                        'entry_time': df.iloc[entry_idx]['datetime'],
                        'entry_price': entry_price,
                        'pattern_points': [X, A, B, C, {'low': D_price}],
                        'direction': 'LONG',
                        'fibonacci_ratios': {
                            'AB/XA': AB_XA_ratio,
                            'BC/AB': BC_AB_ratio, 
                            'CD/BC': CD_BC_ratio,
                            'AD/XA': AD_XA_ratio
                        }
                    })
        
        except Exception as e:
            continue
    
    # Tìm Bearish Butterfly Pattern
    for i in range(15, len(df)):
        if i < 15:
            continue
            
        recent_data = df.iloc[max(0, i-15):i+1]
        
        swing_highs = recent_data[recent_data['swing_high'] == True]
        swing_lows = recent_data[recent_data['swing_low'] == True]
        
        if len(swing_highs) < 2 or len(swing_lows) < 2:
            continue
        
        try:
            # For bearish butterfly: X(high), A(low), B(high), C(low), D(high - current)
            C = swing_lows.iloc[-1]   # Most recent low
            B = swing_highs.iloc[-1]  # Most recent high before C  
            A = swing_lows.iloc[-2] if len(swing_lows) >= 2 else None
            X = swing_highs.iloc[-2] if len(swing_highs) >= 2 else None
            
            if A is None or X is None:
                continue
            
            D_price = df.loc[i, 'high']
            
            # Calculate ratios
            XA = abs(A['low'] - X['high'])
            AB = abs(B['high'] - A['low'])
            BC = abs(C['low'] - B['high']) 
            CD = abs(D_price - C['low'])
            AD = abs(D_price - A['low'])
            
            if XA == 0 or AB == 0 or BC == 0:
                continue
            
            AB_XA_ratio = AB / XA
            BC_AB_ratio = BC / AB
            CD_BC_ratio = CD / BC if BC > 0 else 0
            AD_XA_ratio = AD / XA
            
            # Check ratios với tolerance cao hơn
            valid_AB = is_within_tolerance(AB_XA_ratio, 0.786, 0.2)
            valid_BC = (is_within_tolerance(BC_AB_ratio, 0.382, 0.2) or
                       is_within_tolerance(BC_AB_ratio, 0.886, 0.2))
            valid_CD = (is_within_tolerance(CD_BC_ratio, 1.27, 0.25) or
                       is_within_tolerance(CD_BC_ratio, 1.618, 0.25))
            valid_AD = is_within_tolerance(AD_XA_ratio, 0.786, 0.2)
            
            if valid_AB and valid_BC and valid_CD and valid_AD:
                entry_idx = i + 1
                if entry_idx < len(df):
                    entry_price = df.iloc[entry_idx]['close']
                    signals.append({
                        'type': 'Bearish Butterfly',
                        'entry_idx': entry_idx,
                        'entry_time': df.iloc[entry_idx]['datetime'],
                        'entry_price': entry_price,
                        'pattern_points': [X, A, B, C, {'high': D_price}],
                        'direction': 'SHORT',
                        'fibonacci_ratios': {
                            'AB/XA': AB_XA_ratio,
                            'BC/AB': BC_AB_ratio,
                            'CD/BC': CD_BC_ratio, 
                            'AD/XA': AD_XA_ratio
                        }
                    })
        
        except Exception as e:
            continue
    
    return signals

# --- Backtest với Exit Strategy từ cách 2 ---
def calculate_backtest_results(df, signals, exit_periods, initial_balance=INITIAL_BALANCE, trade_amount=TRADE_AMOUNT):
    """
    Backtest với Exit Strategy từ cách 2:
    - Quản lý positions theo thời gian
    - Sử dụng percentage của vốn
    - Close positions theo bars held hoặc take profit
    """
    results = []
    balance = initial_balance
    positions = []
    
    # Sort signals by entry time
    signals = sorted(signals, key=lambda x: x['entry_idx'])
    
    for i in range(len(df)):
        current_date = df.iloc[i]['datetime']
        current_close = df.iloc[i]['close']
        
        # Close existing positions that have reached exit time or take profit
        positions_to_close = []
        for pos_idx, position in enumerate(positions):
            bars_held = i - position['entry_index']
            
            # Check if position should be closed
            should_close = False
            exit_reason = ""
            
            # Exit after N periods
            if bars_held >= exit_periods:
                should_close = True
                exit_reason = "Time"
            
            # Take profit check
            if position['type'] == 'LONG':
                current_pnl_percent = ((current_close - position['entry_price']) / position['entry_price']) * 100
                if current_pnl_percent >= TAKE_PROFIT_PERCENT:
                    should_close = True
                    exit_reason = "TP"
            else:  # SHORT
                current_pnl_percent = ((position['entry_price'] - current_close) / position['entry_price']) * 100
                if current_pnl_percent >= TAKE_PROFIT_PERCENT:
                    should_close = True
                    exit_reason = "TP"
            
            if should_close:
                positions_to_close.append((pos_idx, exit_reason))
        
        # Close positions (reverse order to maintain indices)
        for pos_idx, exit_reason in reversed(positions_to_close):
            position = positions[pos_idx]
            exit_price = current_close
            
            if position['type'] == 'LONG':
                pnl = (exit_price - position['entry_price']) * position['quantity']
            else:  # SHORT
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
                'bars_held': i - position['entry_index'],
                'exit_reason': exit_reason
            })
            positions.pop(pos_idx)
        
        # Look for new signals to enter (chỉ 1 trade tại 1 thời điểm)
        if len(positions) == 0:  # Only enter if no existing positions
            for sig in signals:
                if sig['entry_idx'] == i:
                    # Use percentage of capital like cách 2
                    position_value = balance * 0.95  # Use 95% of capital
                    quantity = position_value / current_close
                    
                    position = {
                        'type': sig['direction'],
                        'entry_time': sig['entry_time'],
                        'entry_index': i,
                        'entry_price': current_close,
                        'quantity': quantity,
                        'value': position_value,
                        'pattern_type': sig['type']
                    }
                    positions.append(position)
                    balance -= position_value
                    break  # Chỉ enter 1 position đầu tiên tìm thấy
    
    # Close any remaining positions at the end
    if positions:
        final_close = df.iloc[-1]['close']
        final_date = df.iloc[-1]['datetime']
        
        for position in positions:
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

# --- Xuất báo cáo so sánh ---
def export_butterfly_comparison_report(signals, results_9, results_26, final_balance_9, final_balance_26, filename=None):
    if filename is None:
        # Format ngày: YYYYMMDD
        start_date_formatted = START_DATE.replace('-', '')
        end_date_formatted = END_DATE.replace('-', '')
        filename = f"butterfly_pattern_{SYMBOL.lower()}_{TIMEFRAME}_{start_date_formatted}_{end_date_formatted}.md"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# Butterfly Pattern Strategy Comparison - {SYMBOL} {TIMEFRAME}\n\n")
        f.write(f"## Strategy Overview\n")
        f.write(f"- **Pattern**: Butterfly Pattern (Bullish & Bearish)\n")
        f.write(f"- **Entry**: At close price when pattern is detected\n")
        f.write(f"- **Exit Strategy 1**: Hold for {EXIT_PERIODS_1} periods\n")
        f.write(f"- **Exit Strategy 2**: Hold for {EXIT_PERIODS_2} periods\n\n")
        f.write(f"- **Take Profit**: {TAKE_PROFIT_PERCENT}%\n\n")
        
        # Tính toán metrics
        def calculate_metrics(results):
            if not results:
                return {
                    'total_trades': 0, 'win_rate': 0, 'total_return': 0,
                    'final_capital': INITIAL_BALANCE, 'total_pnl': 0,
                    'avg_pnl': 0, 'best_trade': 0, 'worst_trade': 0
                }
            
            total_trades = len(results)
            win_trades = sum(1 for r in results if r['pnl'] > 0)
            win_rate = (win_trades / total_trades) * 100
            total_pnl = sum(r['pnl'] for r in results)
            final_capital = results[-1]['balance']
            total_return = ((final_capital - INITIAL_BALANCE) / INITIAL_BALANCE) * 100
            avg_pnl = total_pnl / total_trades
            best_trade = max(r['pnl'] for r in results)
            worst_trade = min(r['pnl'] for r in results)
            
            return {
                'total_trades': total_trades, 'win_rate': win_rate, 'total_return': total_return,
                'final_capital': final_capital, 'total_pnl': total_pnl,
                'avg_pnl': avg_pnl, 'best_trade': best_trade, 'worst_trade': worst_trade
            }
        
        metrics_9 = calculate_metrics(results_9)
        metrics_26 = calculate_metrics(results_26)
        
        f.write(f"## Performance Comparison\n\n")
        f.write(f"| Metric | {EXIT_PERIODS_1} Periods | {EXIT_PERIODS_2} Periods |\n")
        f.write(f"|--------|-----------|------------|\n")
        f.write(f"| Total Trades | {metrics_9['total_trades']} | {metrics_26['total_trades']} |\n")
        f.write(f"| Win Rate | {metrics_9['win_rate']:.2f}% | {metrics_26['win_rate']:.2f}% |\n")
        f.write(f"| Total Return | {metrics_9['total_return']:.2f}% | {metrics_26['total_return']:.2f}% |\n")
        f.write(f"| Final Capital | ${metrics_9['final_capital']:.2f} | ${metrics_26['final_capital']:.2f} |\n")
        f.write(f"| Total PnL | ${metrics_9['total_pnl']:.2f} | ${metrics_26['total_pnl']:.2f} |\n")
        f.write(f"| Average PnL per Trade | ${metrics_9['avg_pnl']:.2f} | ${metrics_26['avg_pnl']:.2f} |\n")
        f.write(f"| Best Trade | ${metrics_9['best_trade']:.2f} | ${metrics_26['best_trade']:.2f} |\n")
        f.write(f"| Worst Trade | ${metrics_9['worst_trade']:.2f} | ${metrics_26['worst_trade']:.2f} |\n\n")
        
        # Chi tiết giao dịch Strategy 1
        if results_9:
            f.write(f"## Strategy 1: Exit after {EXIT_PERIODS_1} periods\n\n")
            f.write(f"| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |\n")
            f.write(f"|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|\n")
            for r in results_9:
                f.write(f"| {r['entry_time'].strftime('%Y-%m-%d %H:%M')} | {r['exit_time'].strftime('%Y-%m-%d %H:%M')} | {r['type']} | ${r['entry_price']:.4f} | ${r['exit_price']:.4f} | ${r['pnl']:.2f} | {r['pnl_percent']:.2f}% | {r['pattern_type']} | {r['exit_reason']} |\n")
            f.write(f"\n")
        
        # Chi tiết giao dịch Strategy 2
        if results_26:
            f.write(f"## Strategy 2: Exit after {EXIT_PERIODS_2} periods\n\n")
            f.write(f"| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason |\n")
            f.write(f"|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|\n")
            for r in results_26:
                f.write(f"| {r['entry_time'].strftime('%Y-%m-%d %H:%M')} | {r['exit_time'].strftime('%Y-%m-%d %H:%M')} | {r['type']} | ${r['entry_price']:.4f} | ${r['exit_price']:.4f} | ${r['pnl']:.2f} | {r['pnl_percent']:.2f}% | {r['pattern_type']} | {r['exit_reason']} |\n")
            f.write(f"\n")
        
        # Phân tích
        f.write(f"## Analysis\n\n")
        if metrics_26['total_return'] > metrics_9['total_return']:
            winner = f"{EXIT_PERIODS_2} Periods Strategy"
            return_diff = metrics_26['total_return'] - metrics_9['total_return']
            f.write(f"**Winner: {winner}**\n\n")
            f.write(f"The {EXIT_PERIODS_2}-period exit strategy outperformed with {metrics_26['total_return']:.2f}% return vs {metrics_9['total_return']:.2f}%.\n\n")
        else:
            winner = f"{EXIT_PERIODS_1} Periods Strategy"
            return_diff = metrics_9['total_return'] - metrics_26['total_return']
            f.write(f"**Winner: {winner}**\n\n")
            f.write(f"The {EXIT_PERIODS_1}-period exit strategy outperformed with {metrics_9['total_return']:.2f}% return vs {metrics_26['total_return']:.2f}%.\n\n")
        
        f.write(f"### Key Observations:\n")
        f.write(f"- **Trade Frequency**: {metrics_9['total_trades']} vs {metrics_26['total_trades']} trades\n")
        f.write(f"- **Win Rate Difference**: {metrics_9['win_rate']:.2f}% vs {metrics_26['win_rate']:.2f}%\n")
        f.write(f"- **Return Difference**: {return_diff:.2f}% gap\n\n")
        
        f.write(f"---\n")
        f.write(f"*Báo cáo được tạo tự động bởi Butterfly Pattern Backtest System*\n")
    
    return filename

# --- Chạy backtest ---
if __name__ == "__main__":
    # Sử dụng cách 2: không cần pivot_highs, pivot_lows
    signals = find_butterfly_patterns(df)
    
    # Backtest với 2 exit strategies
    results_9, final_balance_9 = calculate_backtest_results(df, signals, EXIT_PERIODS_1)
    results_26, final_balance_26 = calculate_backtest_results(df, signals, EXIT_PERIODS_2)
    
    # Xuất báo cáo
    report_file = export_butterfly_comparison_report(signals, results_9, results_26, final_balance_9, final_balance_26)
    print(f"Đã xuất báo cáo: {report_file}")
    
    # In kết quả tóm tắt
    print(f"\n=== KẾT QUẢ TÓM TẮT ===")
    print(f"Tổng số tín hiệu: {len(signals)}")
    print(f"Strategy 1 ({EXIT_PERIODS_1} periods): {len(results_9)} trades, ${final_balance_9:.2f}")
    print(f"Strategy 2 ({EXIT_PERIODS_2} periods): {len(results_26)} trades, ${final_balance_26:.2f}") 