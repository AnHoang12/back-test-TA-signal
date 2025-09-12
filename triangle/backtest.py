import os
import pandas as pd
import numpy as np
import argparse
from dotenv import load_dotenv
from datetime import datetime
from sqlalchemy import create_engine

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
table_name = "proddb.coin_prices_1h"

try:
    print(f"Connecting to DB: {DB_HOST}:{DB_PORT}/{DB_NAME}")
    engine = create_engine(DATABASE_URL)
    print("Connected to DB successfully")
except Exception as e:
    engine = None
    print(f"Failed to connect to DB: {e}")

def get_binance_data(symbol, interval):
    if engine is None:
        print("No valid DB connection.")
        return pd.DataFrame()

    print(f"Getting data from DB: {symbol} {interval}")
    query = f"""
    SELECT * FROM {table_name}
    WHERE symbol = %(symbol)s
    AND open_time >= EXTRACT(EPOCH FROM NOW()) - 90*24*3600 
    AND open_time <= EXTRACT(EPOCH FROM NOW())
    ORDER BY open_time ASC
    """

    try:
        print(f"Query {table_name}")
        df = pd.read_sql(
            query,
            con=engine,
            params={
                "symbol": symbol,
            },
        )

        if 'open_time' not in df.columns:
            print("Missing 'open_time' column in the data returned from DB.")
            return pd.DataFrame()
        
        df['datetime'] = pd.to_datetime(df['open_time'], unit='s')
        
        df = df.sort_values('datetime').reset_index(drop=True)
        print(f"Read {len(df)} rows from DB table {table_name}")
        if len(df) > 0:
            print(f"   Time: {df['datetime'].min()} to {df['datetime'].max()}")
            print(f"   Last price: ${df.iloc[-1]['close']:.4f}")
        
        return df
    except Exception as e:
        print(f"Error reading data from DB: {e}")
        return pd.DataFrame()

# --- Argument Parser ---
def parse_arguments():
    parser = argparse.ArgumentParser(description='Triangle Pattern Backtest')
    parser.add_argument('symbol', help='Symbol (e.g., BTCUSDT, ETHUSDT)')
    parser.add_argument('timeframe', help='Timeframe (e.g., 1h, 2h, 4h, 1d)')
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
INITIAL_BALANCE = args.initial_balance
TRADE_AMOUNT = args.trade_amount
EXIT_PERIODS_1 = args.exit_periods_1
EXIT_PERIODS_2 = args.exit_periods_2
TAKE_PROFIT_PERCENT = args.take_profit

print(f"=== TRIANGLE PATTERN BACKTEST ===")
print(f"Symbol: {SYMBOL}")
print(f"Timeframe: {TIMEFRAME}")
print(f"Initial Balance: ${INITIAL_BALANCE}")
print(f"Trade Amount: ${TRADE_AMOUNT}")
print(f"Exit Strategy 1: {EXIT_PERIODS_1} periods")
print(f"Exit Strategy 2: {EXIT_PERIODS_2} periods")
print(f"Take Profit: {TAKE_PROFIT_PERCENT}%")
print("=" * 40)

# Cấu hình nâng cao
NUM_LOWS = 3
NUM_HIGHS = 3

# Enhanced parameters
ATR_PERIOD = 14
ATR_MULTIPLIER = 2.0  # K factor for ATR-based calculations
MIN_SLOPE_THRESHOLD = 0.001  # Minimum slope for trendline validation (simplified)
MAX_PATTERN_LENGTH = 72  # Maximum bars between first and last pivot
TOLERANCE_MULTIPLIER = 1.5  # For horizontal line tolerance
TOLERANCE_PERCENT = 0.01  # For horizontal line tolerance

# --- Calculate ATR ---
def calculate_atr(data, period=ATR_PERIOD):
    """Calculate Average True Range"""
    high = data['high']
    low = data['low']
    close = data['close'].shift(1)
    
    tr1 = high - low
    tr2 = abs(high - close)
    tr3 = abs(low - close)
    
    true_range = np.maximum(tr1, np.maximum(tr2, tr3))
    atr = true_range.rolling(window=period).mean()
    
    return atr

# --- Find pivot points with adaptive window ---
def find_adaptive_pivots(data, base_window=3, atr_multiplier=ATR_MULTIPLIER):
    """
    Find pivot with adaptive window size based on ATR
    """
    atr = calculate_atr(data)
    avg_price = (data['high'] + data['low'] + data['close']) / 3
    
    pivot_highs = []
    pivot_lows = []
    
    for i in range(len(data)):
        if i < ATR_PERIOD or i >= len(data) - base_window:
            continue
            
        # Calculate adaptive window size
        current_atr = atr.iloc[i]
        current_avg_price = avg_price.iloc[i]
        
        if pd.notna(current_atr) and current_avg_price > 0:
            adaptive_factor = (current_atr / current_avg_price) * atr_multiplier
            window = max(base_window, min(10, int(base_window + adaptive_factor * 10)))
        else:
            window = base_window
        
        # Check if there is enough data for the window
        if i < window or i >= len(data) - window:
            continue
            
        # Find pivot high
        highs = data['high'].iloc[i-window:i+window+1]
        if data['high'].iloc[i] == highs.max() and highs.iloc[window] >= highs.iloc[window-1] and highs.iloc[window] >= highs.iloc[window+1]:
            pivot_highs.append((i, data['high'].iloc[i]))
        
        # Find pivot low
        lows = data['low'].iloc[i-window:i+window+1]
        if data['low'].iloc[i] == lows.min() and lows.iloc[window] <= lows.iloc[window-1] and lows.iloc[window] <= lows.iloc[window+1]:
            pivot_lows.append((i, data['low'].iloc[i]))
    
    return pivot_highs, pivot_lows


# --- Kiểm tra horizontal line với ATR tolerance ---
def is_horizontal_line(pivots, atr_values, indices, tolerance_mult=TOLERANCE_MULTIPLIER):
    """
    Kiểm tra các pivot có tạo thành đường ngang với tolerance dựa trên ATR
    """
    if len(pivots) < 2:
        return False
    
    prices = [p[1] for p in pivots]
    pivot_indices = [p[0] for p in pivots]
    
    # Tính ATR trung bình tại các pivot points
    avg_atr = 0
    valid_atr_count = 0
    
    for idx in pivot_indices:
        if idx < len(atr_values) and pd.notna(atr_values[idx]):
            avg_atr += atr_values[idx]
            valid_atr_count += 1
    
    if valid_atr_count == 0:
        # Fallback to percentage if no ATR available
        return abs(max(prices) - min(prices)) / np.mean(prices) < 0.01
    
    avg_atr = avg_atr / valid_atr_count
    tolerance = avg_atr * tolerance_mult
    
    return abs(max(prices) - min(prices)) < tolerance

# --- Simple slope calculation function ---
def calculate_simple_slope(points):
    """
    Calculate simple slope for trendline validation
    Returns: slope value
    """
    if len(points) < 2:
        return 0
    
    x = [p[0] for p in points]  # indices
    y = [p[1] for p in points]  # prices
    
    # Simple linear slope calculation
    slope = (y[-1] - y[0]) / (x[-1] - x[0]) if (x[-1] - x[0]) != 0 else 0
    
    return slope

# --- Nhận diện triangle pattern cải thiện ---
def find_improved_triangle_patterns(df, pivot_highs, pivot_lows, num_lows=NUM_LOWS, num_highs=NUM_HIGHS):
    """
    Tìm triangle pattern với các cải thiện:
    - ATR-based tolerance
    - Trendline slope validation
    - Pattern length control
    """
    signals = []
    atr = calculate_atr(df)
    
    # Tam giác tăng: num_lows đáy cao dần + đỉnh ngang
    for i in range(len(pivot_lows) - (num_lows-1)):
        lows = pivot_lows[i:i+num_lows]
        
        # Kiểm tra pattern length
        pattern_length = lows[-1][0] - lows[0][0]
        if pattern_length > MAX_PATTERN_LENGTH:
            continue
        
        # Kiểm tra trendline slope của đáy
        slope = calculate_simple_slope(lows)
        if abs(slope) < MIN_SLOPE_THRESHOLD or slope <= 0:  # Đáy phải tăng dần
            continue
        
        # Tìm các đỉnh trong khoảng thời gian này
        highs_in_range = [h for h in pivot_highs if lows[0][0] <= h[0] <= lows[-1][0]]
        
        if len(highs_in_range) >= 2:
            # Kiểm tra đỉnh có tạo đường ngang không (với ATR tolerance)
            if is_horizontal_line(highs_in_range, atr, [h[0] for h in highs_in_range]):
                # Xác định breakout point
                last_high = max(highs_in_range, key=lambda x: x[0])
                breakout_idx = min(last_high[0] + 1, len(df) - 1)
                
                if breakout_idx < len(df):
                    entry_price = df.iloc[breakout_idx]['close']
                    resistance_level = np.mean([h[1] for h in highs_in_range])
                    
                    # Chỉ tạo signal nếu có breakout thực sự
                    if entry_price > resistance_level:
                        signals.append({
                            'type': 'UP',
                            'entry_idx': breakout_idx,
                            'entry_time': df.iloc[breakout_idx]['datetime'],
                            'entry_price': entry_price,
                            'pattern_points': lows + highs_in_range,
                            'slope': slope,
                            'pattern_length': pattern_length,
                            'resistance_level': resistance_level
                        })
    
    # Tam giác giảm: num_highs đỉnh thấp dần + đáy ngang
    for i in range(len(pivot_highs) - (num_highs-1)):
        highs = pivot_highs[i:i+num_highs]
        
        # Kiểm tra pattern length
        pattern_length = highs[-1][0] - highs[0][0]
        if pattern_length > MAX_PATTERN_LENGTH:
            continue
        
        # Kiểm tra trendline slope của đỉnh
        slope = calculate_simple_slope(highs)
        if abs(slope) < MIN_SLOPE_THRESHOLD or slope >= 0:  # Đỉnh phải giảm dần
            continue
        
        # Tìm các đáy trong khoảng thời gian này
        lows_in_range = [l for l in pivot_lows if highs[0][0] <= l[0] <= highs[-1][0]]
        
        if len(lows_in_range) >= 2:
            # Kiểm tra đáy có tạo đường ngang không
            if is_horizontal_line(lows_in_range, atr, [l[0] for l in lows_in_range]):
                # Xác định breakout point
                last_low = max(lows_in_range, key=lambda x: x[0])
                breakout_idx = min(last_low[0] + 1, len(df) - 1)
                
                if breakout_idx < len(df):
                    entry_price = df.iloc[breakout_idx]['close']
                    support_level = np.mean([l[1] for l in lows_in_range])
                    
                    # Chỉ tạo signal nếu có breakout thực sự
                    if entry_price < support_level:
                        signals.append({
                            'type': 'DOWN',
                            'entry_idx': breakout_idx,
                            'entry_time': df.iloc[breakout_idx]['datetime'],
                            'entry_price': entry_price,
                            'pattern_points': highs + lows_in_range,
                            'slope': slope,
                            'pattern_length': pattern_length,
                            'support_level': support_level
                        })
    
    return signals

# --- Backtest với Exit Strategy từ butterfly ---
def calculate_backtest_results(df, signals, exit_periods, initial_balance=INITIAL_BALANCE, trade_amount=TRADE_AMOUNT):
    """
    Backtest với Exit Strategy từ butterfly pattern:
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
                    # Use percentage of capital like butterfly
                    position_value = balance * 0.95  # Use 95% of capital
                    quantity = position_value / current_close
                    
                    # Convert triangle direction to LONG/SHORT
                    direction = 'LONG' if sig['type'] == 'UP' else 'SHORT'
                    
                    position = {
                        'type': direction,
                        'entry_time': sig['entry_time'],
                        'entry_index': i,
                        'entry_price': current_close,
                        'quantity': quantity,
                        'value': position_value,
                        'pattern_type': f"Triangle {sig['type']}"
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
                'type': position['type'],   # LONG or SHORT
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

# --- Enhanced metrics calculation ---
def calculate_advanced_metrics(results, equity_curve, initial_balance):
    """
    Tính toán các metrics nâng cao
    """
    if not results:
        return {}
    
    # Basic metrics
    total_trades = len(results)
    winning_trades = sum(1 for r in results if r['pnl'] > 0)
    losing_trades = total_trades - winning_trades
    win_rate = (winning_trades / total_trades) * 100
    
    # P&L metrics
    total_pnl = sum(r['pnl'] for r in results)
    gross_profit = sum(r['pnl'] for r in results if r['pnl'] > 0)
    gross_loss = abs(sum(r['pnl'] for r in results if r['pnl'] < 0))
    profit_factor = gross_profit / gross_loss if gross_loss > 0 else float('inf')
    
    # Returns calculation
    returns = []
    for i in range(1, len(equity_curve)):
        ret = (equity_curve[i] - equity_curve[i-1]) / equity_curve[i-1]
        returns.append(ret)
    
    returns = np.array(returns)
    
    # Advanced metrics
    annual_return = np.mean(returns) * 252 * 100  # Assuming daily data
    volatility = np.std(returns) * np.sqrt(252) * 100
    sharpe_ratio = annual_return / volatility if volatility > 0 else 0
    
    # Maximum drawdown
    peak = initial_balance
    max_dd = 0
    for balance in equity_curve:
        if balance > peak:
            peak = balance
        drawdown = (peak - balance) / peak
        if drawdown > max_dd:
            max_dd = drawdown
    
    max_drawdown = max_dd * 100
    
    # Calmar ratio
    calmar_ratio = annual_return / max_drawdown if max_drawdown > 0 else 0
    
    # Average metrics
    avg_win = gross_profit / winning_trades if winning_trades > 0 else 0
    avg_loss = gross_loss / losing_trades if losing_trades > 0 else 0
    avg_trade = total_pnl / total_trades
    
    # Pattern quality metrics
    avg_pattern_length = np.mean([r['pattern_length'] for r in results])
    avg_slope = np.mean([abs(r['slope']) for r in results])
    
    return {
        'total_trades': total_trades,
        'win_rate': win_rate,
        'profit_factor': profit_factor,
        'total_pnl': total_pnl,
        'annual_return': annual_return,
        'volatility': volatility,
        'sharpe_ratio': sharpe_ratio,
        'max_drawdown': max_drawdown,
        'calmar_ratio': calmar_ratio,
        'avg_win': avg_win,
        'avg_loss': avg_loss,
        'avg_trade': avg_trade,
        'avg_slope': avg_slope,
        'avg_pattern_length': avg_pattern_length
    }

# --- Xuất báo cáo so sánh ---
def export_triangle_comparison_report(signals, results_9, results_26, final_balance_9, final_balance_26, filename=None):
    if filename is None:
        # Format ngày: YYYYMMDD
        filename = f"triangle_pattern_{SYMBOL.lower()}_{TIMEFRAME}.md"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# Triangle Pattern Strategy Comparison - {SYMBOL} {TIMEFRAME}\n\n")
        f.write(f"## Strategy Overview\n")
        f.write(f"- **Pattern**: Triangle Pattern (Ascending & Descending)\n")
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
        f.write(f"*Báo cáo được tạo tự động bởi Triangle Pattern Backtest System*\n")
    
    return filename

# --- Đọc data từ database ---
df = get_binance_data(SYMBOL, TIMEFRAME)

if len(df) == 0:
    print("Không có dữ liệu để backtest!")
    exit()

# --- Chạy backtest ---
if __name__ == "__main__":
    print("🔍 Tìm pivot points với adaptive window...")
    pivot_highs, pivot_lows = find_adaptive_pivots(df)
    print(f"Tìm thấy {len(pivot_highs)} pivot highs và {len(pivot_lows)} pivot lows")

    print("🔺 Phân tích triangle patterns...")
    signals = find_improved_triangle_patterns(df, pivot_highs, pivot_lows)
    
    results_9, final_balance_9 = calculate_backtest_results(df, signals, EXIT_PERIODS_1)
    results_26, final_balance_26 = calculate_backtest_results(df, signals, EXIT_PERIODS_2)
    
    report_file = export_triangle_comparison_report(signals, results_9, results_26, final_balance_9, final_balance_26)
    print(f"Đã xuất báo cáo: {report_file}")
    
    print(f"\n=== KẾT QUẢ TÓM TẮT ===")
    print(f"Tổng số tín hiệu: {len(signals)}")
    print(f"Strategy 1 ({EXIT_PERIODS_1} periods): {len(results_9)} trades, ${final_balance_9:.2f}")
    print(f"Strategy 2 ({EXIT_PERIODS_2} periods): {len(results_26)} trades, ${final_balance_26:.2f}")