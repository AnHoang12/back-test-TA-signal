import os
import pandas as pd
import numpy as np
import argparse
from datetime import datetime
from dotenv import load_dotenv

# Import candlestick detection functions
from rsi14_candlestick_confluence import (
    detect_bullish_engulfing, detect_hammer, detect_bullish_doji,
    detect_bearish_engulfing, detect_shooting_star, detect_bearish_doji
)

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
    parser = argparse.ArgumentParser(description='Triple Pattern Backtest - Multi Position')
    parser.add_argument('symbol', help='Symbol (e.g., BTCUSDT, ETHUSDT)')
    parser.add_argument('timeframe', help='Timeframe (e.g., 1h, 2h, 4h, 1d)')
    parser.add_argument('--start-date', default='2025-04-01', help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end-date', default='2025-06-30', help='End date (YYYY-MM-DD)')
    parser.add_argument('--initial-balance', type=float, default=1000, help='Initial balance')
    parser.add_argument('--position-size', type=float, default=0.2, help='Position size as percentage of capital')
    parser.add_argument('--max-positions', type=int, default=3, help='Maximum number of concurrent positions')
    parser.add_argument('--exit-periods-1', type=int, default=9, help='Exit periods for strategy 1')
    parser.add_argument('--exit-periods-2', type=int, default=26, help='Exit periods for strategy 2')
    parser.add_argument('--take-profit', type=float, default=5.0, help='Take profit percentage')
    parser.add_argument('--lookback-period', type=int, default=40, help='Lookback period for pattern detection')
    parser.add_argument('--price-threshold', type=float, default=0.05, help='Price threshold for pattern confirmation')
    
    return parser.parse_args()

# --- Cấu hình ---
args = parse_arguments()

SYMBOL = args.symbol.upper()
TIMEFRAME = args.timeframe
START_DATE = args.start_date
END_DATE = args.end_date
INITIAL_BALANCE = args.initial_balance
POSITION_SIZE_PCT = args.position_size
MAX_POSITIONS = args.max_positions
EXIT_PERIODS_1 = args.exit_periods_1
EXIT_PERIODS_2 = args.exit_periods_2
TAKE_PROFIT_PERCENT = args.take_profit
LOOKBACK_PERIOD = args.lookback_period
PRICE_THRESHOLD = args.price_threshold

print(f"=== TRIPLE PATTERN BACKTEST - MULTI POSITION ===")
print(f"Symbol: {SYMBOL}")
print(f"Timeframe: {TIMEFRAME}")
print(f"Period: {START_DATE} to {END_DATE}")
print(f"Initial Balance: ${INITIAL_BALANCE}")
print(f"Position Size: {POSITION_SIZE_PCT*100}% of capital")
print(f"Max Positions: {MAX_POSITIONS}")
print(f"Exit Strategy 1: {EXIT_PERIODS_1} periods")
print(f"Exit Strategy 2: {EXIT_PERIODS_2} periods")
print(f"Take Profit: {TAKE_PROFIT_PERCENT}%")
print(f"Lookback Period: {LOOKBACK_PERIOD}")
print(f"Price Threshold: {PRICE_THRESHOLD*100}%")
print("=" * 40)

# --- Đọc data từ folder binance_data ---
df = get_binance_data(SYMBOL, TIMEFRAME, START_DATE, END_DATE)

if len(df) == 0:
    print("Không có dữ liệu để backtest!")
    exit()

# --- Triple Pattern Detection Functions ---
def detect_triple_top(df, lookback_period=LOOKBACK_PERIOD, price_threshold=PRICE_THRESHOLD):
    """Detect triple top pattern"""
    if len(df) < lookback_period:
        return False, None, None
    
    window = df.tail(lookback_period)
    highs = window['high']
    
    if highs.empty:
        return False, None, None
    
    # Tìm 3 đỉnh cao nhất
    peaks_idx = highs.nlargest(3).index.tolist()
    if len(peaks_idx) < 3:
        return False, None, None
    
    # Sắp xếp theo thời gian
    peaks = sorted([(i, window.loc[i]) for i in peaks_idx], key=lambda x: x[0])
    idx1, p1 = peaks[0]
    idx2, p2 = peaks[1] 
    idx3, p3 = peaks[2]
    
    # Kiểm tra giá 3 đỉnh gần bằng nhau
    max_high = max(p1['high'], p2['high'], p3['high'])
    min_high = min(p1['high'], p2['high'], p3['high'])
    
    if (max_high - min_high) / max_high > price_threshold:
        return False, None, None
    
    # Tìm support level (đáy thấp nhất giữa các đỉnh)
    left = min(idx1, idx2, idx3)
    right = max(idx1, idx2, idx3)
    trough_data = window.loc[left:right]
    
    if trough_data.empty or 'low' not in trough_data:
        return False, None, None
    
    support_level = trough_data['low'].min()
    resistance_level = np.mean([p1['high'], p2['high'], p3['high']])
    
    return True, support_level, resistance_level

def detect_triple_bottom(df, lookback_period=LOOKBACK_PERIOD, price_threshold=PRICE_THRESHOLD):
    """Detect triple bottom pattern"""
    if len(df) < lookback_period:
        return False, None, None
    
    window = df.tail(lookback_period)
    lows = window['low']
    
    if lows.empty:
        return False, None, None
    
    # Tìm 3 đáy thấp nhất
    troughs_idx = lows.nsmallest(3).index.tolist()
    if len(troughs_idx) < 3:
        return False, None, None
    
    # Sắp xếp theo thời gian
    troughs = sorted([(i, window.loc[i]) for i in troughs_idx], key=lambda x: x[0])
    idx1, t1 = troughs[0]
    idx2, t2 = troughs[1]
    idx3, t3 = troughs[2]
    
    # Kiểm tra giá 3 đáy gần bằng nhau
    max_low = max(t1['low'], t2['low'], t3['low'])
    min_low = min(t1['low'], t2['low'], t3['low'])
    
    if (max_low - min_low) / max_low > price_threshold:
        return False, None, None
    
    # Tìm resistance level (đỉnh cao nhất giữa các đáy)
    left = min(idx1, idx2, idx3)
    right = max(idx1, idx2, idx3)
    peak_data = window.loc[left:right]
    
    if peak_data.empty or 'high' not in peak_data:
        return False, None, None
    
    resistance_level = peak_data['high'].max()
    support_level = np.mean([t1['low'], t2['low'], t3['low']])
    
    return True, support_level, resistance_level

def is_bullish_reversal_candle(df):
    """Kiểm tra nến đảo chiều tăng"""
    if len(df) < 2:
        return False
    
    return (
        detect_hammer(df).iloc[-1] or
        detect_bullish_engulfing(df).iloc[-1] or
        detect_bullish_doji(df).iloc[-1]
    )

def is_bearish_reversal_candle(df):
    """Kiểm tra nến đảo chiều giảm"""
    if len(df) < 2:
        return False
    
    return (
        detect_shooting_star(df).iloc[-1] or
        detect_bearish_engulfing(df).iloc[-1] or
        detect_bearish_doji(df).iloc[-1]
    )

def should_buy(df):
    """Kiểm tra điều kiện mua - Triple bottom breakout với nến đảo chiều tăng"""
    if len(df) < LOOKBACK_PERIOD:
        return False, None, None
    
    # Detect triple bottom
    has_pattern, support_level, resistance_level = detect_triple_bottom(df)
    if not has_pattern:
        return False, None, None
    
    current_close = df.iloc[-1]['close']
    
    # Kiểm tra breakout (giá vượt resistance)
    if current_close > resistance_level:
        # Kiểm tra nến đảo chiều tăng
        if is_bullish_reversal_candle(df):
            return True, current_close, 'triple_bottom_breakout'
    
    return False, None, None

def should_sell(df):
    """Kiểm tra điều kiện bán - Triple top breakdown với nến đảo chiều giảm"""
    if len(df) < LOOKBACK_PERIOD:
        return False, None, None
    
    # Detect triple top
    has_pattern, support_level, resistance_level = detect_triple_top(df)
    if not has_pattern:
        return False, None, None
    
    current_close = df.iloc[-1]['close']
    
    # Kiểm tra breakdown (giá xuống dưới support)
    if current_close < support_level:
        # Kiểm tra nến đảo chiều giảm
        if is_bearish_reversal_candle(df):
            return True, current_close, 'triple_top_breakdown'
    
    return False, None, None

# --- Backtest với nhiều positions cùng lúc ---
def calculate_backtest_results(df, exit_periods, initial_balance=INITIAL_BALANCE, position_size_pct=POSITION_SIZE_PCT, max_positions=MAX_POSITIONS):
    """
    Backtest với nhiều positions cùng lúc:
    - Quản lý nhiều positions (tối đa max_positions)
    - Sử dụng percentage của vốn cho mỗi position
    - Close positions theo bars held hoặc take profit
    """
    results = []
    balance = initial_balance
    positions = []  # List of positions
    position_id = 0  # Unique ID for each position
    
    for i in range(LOOKBACK_PERIOD, len(df)):
        current_date = df.iloc[i]['datetime']
        current_close = df.iloc[i]['close']
        current_window = df.iloc[:i+1]
        
        # Close existing positions if conditions are met
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
                'position_id': position['position_id'],
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
        
        # Look for new signals to enter (chỉ khi chưa đạt max positions)
        if len(positions) < max_positions:
            # Check for buy signal (triple bottom breakout)
            buy_signal, buy_price, buy_pattern = should_buy(current_window)
            if buy_signal:
                # Execute buy
                position_value = balance * position_size_pct
                quantity = position_value / buy_price
                
                position = {
                    'position_id': position_id,
                    'type': 'LONG',
                    'entry_time': current_date,
                    'entry_index': i,
                    'entry_price': buy_price,
                    'quantity': quantity,
                    'value': position_value,
                    'pattern_type': buy_pattern
                }
                positions.append(position)
                balance -= position_value
                position_id += 1
                continue  # Skip to next iteration
            
            # Check for sell signal (triple top breakdown) 
            sell_signal, sell_price, sell_pattern = should_sell(current_window)
            if sell_signal:
                # Execute sell
                position_value = balance * position_size_pct
                quantity = position_value / sell_price
                
                position = {
                    'position_id': position_id,
                    'type': 'SHORT',
                    'entry_time': current_date,
                    'entry_index': i,
                    'entry_price': sell_price,
                    'quantity': quantity,
                    'value': position_value,
                    'pattern_type': sell_pattern
                }
                positions.append(position)
                balance -= position_value
                position_id += 1
    
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
                'position_id': position['position_id'],
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
def export_triple_pattern_comparison_report(results_9, results_26, final_balance_9, final_balance_26, filename=None):
    if filename is None:
        # Format ngày: YYYYMMDD
        start_date_formatted = START_DATE.replace('-', '')
        end_date_formatted = END_DATE.replace('-', '')
        filename = f"triple_pattern_multi_{SYMBOL.lower()}_{TIMEFRAME}_{start_date_formatted}_{end_date_formatted}.md"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# Triple Pattern Strategy Comparison - Multi Position - {SYMBOL} {TIMEFRAME}\n\n")
        f.write(f"## Strategy Overview\n")
        f.write(f"- **Pattern**: Triple Top & Triple Bottom Pattern\n")
        f.write(f"- **Entry**: Breakout/breakdown with reversal candles\n")
        f.write(f"- **Reversal Candles**: Hammer, Engulfing, Doji patterns\n")
        f.write(f"- **Position Management**: Up to {MAX_POSITIONS} positions at a time\n")
        f.write(f"- **Exit Strategy 1**: Hold for {EXIT_PERIODS_1} periods\n")
        f.write(f"- **Exit Strategy 2**: Hold for {EXIT_PERIODS_2} periods\n")
        f.write(f"- **Take Profit**: {TAKE_PROFIT_PERCENT}%\n")
        f.write(f"- **Position Size**: {POSITION_SIZE_PCT*100}% of capital per position\n\n")
        
        # Tính toán metrics
        def calculate_metrics(results):
            if not results:
                return {
                    'total_trades': 0, 'win_rate': 0, 'total_return': 0,
                    'final_capital': INITIAL_BALANCE, 'total_pnl': 0,
                    'avg_pnl': 0, 'best_trade': 0, 'worst_trade': 0,
                    'long_trades': 0, 'short_trades': 0,
                    'max_concurrent': 0, 'avg_concurrent': 0
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
            
            long_trades = sum(1 for r in results if r['type'] == 'LONG')
            short_trades = sum(1 for r in results if r['type'] == 'SHORT')
            
            # Calculate concurrent positions
            position_ids = set(r['position_id'] for r in results)
            max_concurrent = MAX_POSITIONS  # Theoretical max
            avg_concurrent = len(position_ids) / total_trades if total_trades > 0 else 0
            
            return {
                'total_trades': total_trades, 'win_rate': win_rate, 'total_return': total_return,
                'final_capital': final_capital, 'total_pnl': total_pnl,
                'avg_pnl': avg_pnl, 'best_trade': best_trade, 'worst_trade': worst_trade,
                'long_trades': long_trades, 'short_trades': short_trades,
                'max_concurrent': max_concurrent, 'avg_concurrent': avg_concurrent
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
        f.write(f"| Worst Trade | ${metrics_9['worst_trade']:.2f} | ${metrics_26['worst_trade']:.2f} |\n")
        f.write(f"| Long Trades | {metrics_9['long_trades']} | {metrics_26['long_trades']} |\n")
        f.write(f"| Short Trades | {metrics_9['short_trades']} | {metrics_26['short_trades']} |\n")
        f.write(f"| Max Concurrent Positions | {metrics_9['max_concurrent']} | {metrics_26['max_concurrent']} |\n\n")
        
        # Chi tiết giao dịch Strategy 1
        if results_9:
            f.write(f"## Strategy 1: Exit after {EXIT_PERIODS_1} periods\n\n")
            f.write(f"| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |\n")
            f.write(f"|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|\n")
            for r in results_9:
                f.write(f"| {r['position_id']} | {r['entry_time'].strftime('%Y-%m-%d %H:%M')} | {r['exit_time'].strftime('%Y-%m-%d %H:%M')} | {r['type']} | ${r['entry_price']:.4f} | ${r['exit_price']:.4f} | ${r['pnl']:.2f} | {r['pnl_percent']:.2f}% | {r['pattern_type']} | {r['exit_reason']} | {r['bars_held']} |\n")
            f.write(f"\n")
        
        # Chi tiết giao dịch Strategy 2
        if results_26:
            f.write(f"## Strategy 2: Exit after {EXIT_PERIODS_2} periods\n\n")
            f.write(f"| Position ID | Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held |\n")
            f.write(f"|-------------|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|\n")
            for r in results_26:
                f.write(f"| {r['position_id']} | {r['entry_time'].strftime('%Y-%m-%d %H:%M')} | {r['exit_time'].strftime('%Y-%m-%d %H:%M')} | {r['type']} | ${r['entry_price']:.4f} | ${r['exit_price']:.4f} | ${r['pnl']:.2f} | {r['pnl_percent']:.2f}% | {r['pattern_type']} | {r['exit_reason']} | {r['bars_held']} |\n")
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
        f.write(f"- **Return Difference**: {return_diff:.2f}% gap\n")
        f.write(f"- **Position Management**: Up to {MAX_POSITIONS} positions at a time\n")
        f.write(f"- **Pattern Types**: Triple Top Breakdown (SHORT) and Triple Bottom Breakout (LONG)\n")
        f.write(f"- **Position Size**: {POSITION_SIZE_PCT*100}% of capital per position\n\n")
        
        f.write(f"---\n")
        f.write(f"*Báo cáo được tạo tự động bởi Triple Pattern Multi-Position Backtest System*\n")
    
    return filename

# --- Chạy backtest ---
if __name__ == "__main__":
    # Backtest với 2 exit strategies
    print("Running strategy 1: Exit after", EXIT_PERIODS_1, "periods")
    results_9, final_balance_9 = calculate_backtest_results(df, EXIT_PERIODS_1)
    
    print("Running strategy 2: Exit after", EXIT_PERIODS_2, "periods")
    results_26, final_balance_26 = calculate_backtest_results(df, EXIT_PERIODS_2)
    
    # Xuất báo cáo
    report_file = export_triple_pattern_comparison_report(results_9, results_26, final_balance_9, final_balance_26)
    print(f"Đã xuất báo cáo: {report_file}")
    
    # In kết quả tóm tắt
    print(f"\n=== KẾT QUẢ TÓM TẮT ===")
    print(f"Strategy 1 ({EXIT_PERIODS_1} periods): {len(results_9)} trades, ${final_balance_9:.2f}")
    print(f"Strategy 2 ({EXIT_PERIODS_2} periods): {len(results_26)} trades, ${final_balance_26:.2f}")
    print(f"Max concurrent positions: {MAX_POSITIONS}")
    
    if final_balance_26 > final_balance_9:
        print(f"Winner: Strategy 2 ({EXIT_PERIODS_2} periods) with {((final_balance_26 - INITIAL_BALANCE) / INITIAL_BALANCE * 100):.2f}% return")
    else:
        print(f"Winner: Strategy 1 ({EXIT_PERIODS_1} periods) with {((final_balance_9 - INITIAL_BALANCE) / INITIAL_BALANCE * 100):.2f}% return") 