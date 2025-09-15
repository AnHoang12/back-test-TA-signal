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
    
    print(f"Lấy dữ liệu từ DB: {symbol} {interval}")
    
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
        print(f"Đã đọc {len(df)} dòng từ DB bảng {table_name}")
        if len(df) > 0:
            print(f"   Thời gian: {df['datetime'].min()} đến {df['datetime'].max()}")
            print(f"   Giá cuối: ${df.iloc[-1]['close']:.4f}")
        
        return df
    except Exception as e:
        print(f"Error reading data from DB: {e}")
        return pd.DataFrame()




# --- Argument Parser ---
def parse_arguments():
    parser = argparse.ArgumentParser(description='Enhanced Diamond Pattern Backtest')
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

print(f"=== ENHANCED DIAMOND PATTERN BACKTEST ===")
print(f"Symbol: {SYMBOL}")
print(f"Timeframe: {TIMEFRAME}")
print(f"Initial Balance: ${INITIAL_BALANCE}")
print(f"Trade Amount: ${TRADE_AMOUNT}")
print(f"Exit Strategy 1: {EXIT_PERIODS_1} periods")
print(f"Exit Strategy 2: {EXIT_PERIODS_2} periods")
print(f"Take Profit: {TAKE_PROFIT_PERCENT}%")
print("=" * 40)

# ENHANCED CONFIGURATION
USE_ENHANCED_PIVOTS = True     # Use ATR-based pivot detection
USE_SHAPE_VALIDATION = True    # Validate diamond shape (broadening->contracting)
USE_TRENDLINE_VALIDATION = True # Use simple trendline validation
USE_VOLUME_FILTER = True       # Volume confirmation for breakouts
MIN_CONSISTENCY = 0.6         # Minimum consistency score for trendline validation

# BỘ LỌC RSI (CÓ THỂ THAY ĐỔI)
USE_RSI_FILTER = False     # Sử dụng bộ lọc RSI
RSI_OVERSOLD = 35          # RSI oversold level 
RSI_OVERBOUGHT = 65       # RSI overbought level 
RSI_COLUMN = 'rsi14'       # Cột RSI trong data 

# === ENHANCED PIVOT DETECTION ===

def calculate_atr(data, period=14):
    """Calculate Average True Range for volatility measurement"""
    high = data['high']
    low = data['low']
    close = data['close'].shift(1)
    
    tr1 = high - low
    tr2 = abs(high - close)
    tr3 = abs(low - close)
    
    true_range = np.maximum(tr1, np.maximum(tr2, tr3))
    atr = true_range.rolling(window=period).mean()
    
    return atr

def find_enhanced_pivots(data, base_window=3, atr_multiplier=2.0, min_distance_multiplier=1.5):
    """
    Enhanced pivot detection with ATR-based dynamic window and quality filtering
    """
    atr = calculate_atr(data)
    avg_price = (data['high'] + data['low'] + data['close']) / 3
    
    pivot_highs = []
    pivot_lows = []
    
    for i in range(14, len(data) - base_window):  # Start after ATR period
        # Calculate adaptive window size based on volatility
        current_atr = atr.iloc[i]
        current_avg_price = avg_price.iloc[i]
        
        if pd.notna(current_atr) and current_avg_price > 0:
            adaptive_factor = (current_atr / current_avg_price) * atr_multiplier
            window = max(base_window, min(8, int(base_window + adaptive_factor * 10)))
        else:
            window = base_window
        
        if i < window or i >= len(data) - window:
            continue
            
        # Find pivot high
        highs = data['high'].iloc[i-window:i+window+1]
        if data['high'].iloc[i] == highs.max():
            # Quality check: ensure it's significantly higher than neighbors
            if (data['high'].iloc[i] > data['high'].iloc[i-1] and 
                data['high'].iloc[i] > data['high'].iloc[i+1]):
                pivot_highs.append((i, data['high'].iloc[i]))
        
        # Find pivot low
        lows = data['low'].iloc[i-window:i+window+1]
        if data['low'].iloc[i] == lows.min():
            # Quality check: ensure it's significantly lower than neighbors
            if (data['low'].iloc[i] < data['low'].iloc[i-1] and 
                data['low'].iloc[i] < data['low'].iloc[i+1]):
                pivot_lows.append((i, data['low'].iloc[i]))
    
    # Filter out pivots that are too close to each other
    pivot_highs = filter_close_pivots(pivot_highs, atr, data, min_distance_multiplier)
    pivot_lows = filter_close_pivots(pivot_lows, atr, data, min_distance_multiplier)
    
    return pivot_highs, pivot_lows

def filter_close_pivots(pivots, atr, data, min_distance_multiplier):
    """Remove pivots that are too close to each other based on ATR"""
    if len(pivots) <= 1:
        return pivots
    
    filtered_pivots = []
    
    for i, (idx, price) in enumerate(pivots):
        if i == 0:
            filtered_pivots.append((idx, price))
            continue
        
        # Check distance from previous pivot
        prev_idx, prev_price = filtered_pivots[-1]
        
        # Time distance
        time_distance = idx - prev_idx
        
        # Price distance relative to ATR
        current_atr = atr.iloc[idx] if pd.notna(atr.iloc[idx]) else data['high'].iloc[idx] * 0.01
        price_distance = abs(price - prev_price)
        min_price_distance = current_atr * min_distance_multiplier
        
        # Keep pivot if it's far enough in time OR significantly different in price
        if time_distance >= 3 or price_distance >= min_price_distance:
            filtered_pivots.append((idx, price))
    
    return filtered_pivots

# === DIAMOND SHAPE VALIDATION ===

def validate_diamond_shape(points, pattern_type):
    """
    Validate that the pattern forms a proper diamond shape:
    - First 2 pivots: broadening (expanding range)
    - Last 3 pivots: contracting (narrowing range)
    """
    if len(points) != 5:
        return False
    
    p1, p2, p3, p4, p5 = points
    
    if pattern_type == 'bottom':  # H-L-H-L-H
        # Broadening phase: H2 > H1, L1 > previous lows
        broadening = p3[1] > p1[1] and p2[1] < p1[1]  # Higher high, lower low
        
        # Contracting phase: H3 < H2, L2 > L1
        contracting = p5[1] < p3[1] and p4[1] > p2[1]  # Lower high, higher low
        
        return broadening and contracting
    
    elif pattern_type == 'top':  # L-H-L-H-L
        # Broadening phase: L2 < L1, H1 > previous highs
        broadening = p3[1] < p1[1] and p2[1] > p1[1]  # Lower low, higher high
        
        # Contracting phase: L3 > L2, H2 < H1
        contracting = p5[1] > p3[1] and p4[1] < p2[1]  # Higher low, lower high
        
        return broadening and contracting
    
    return False

# === SIMPLE TRENDLINE VALIDATION ===

def calculate_simple_slope(points):
    """Calculate simple slope between points"""
    if len(points) < 2:
        return 0
    
    x_values = [p[0] for p in points]
    y_values = [p[1] for p in points]
    
    # Simple linear slope calculation
    x_diff = x_values[-1] - x_values[0]
    y_diff = y_values[-1] - y_values[0]
    
    return y_diff / x_diff if x_diff != 0 else 0

def calculate_trendline_consistency(points):
    """
    Calculate how consistent points are with a straight line
    Returns a score from 0 to 1 (1 = perfect line)
    """
    if len(points) < 3:
        return 1.0
    
    x_values = [p[0] for p in points]
    y_values = [p[1] for p in points]
    
    # Calculate expected y values based on first and last points
    slope = calculate_simple_slope(points)
    intercept = y_values[0] - slope * x_values[0]
    
    # Calculate deviations from expected line
    deviations = []
    for i in range(len(points)):
        expected_y = slope * x_values[i] + intercept
        actual_y = y_values[i]
        deviation = abs(actual_y - expected_y)
        deviations.append(deviation)
    
    # Convert to consistency score (lower deviation = higher consistency)
    max_deviation = max(deviations) if deviations else 0
    avg_price = np.mean(y_values)
    
    if max_deviation == 0 or avg_price == 0:
        return 1.0
    
    # Normalize deviation relative to average price
    relative_deviation = max_deviation / avg_price
    consistency = max(0, 1 - relative_deviation * 10)  # Scale factor of 10
    
    return consistency

def validate_trendlines(points, pattern_type, min_consistency=0.6):
    """
    Validate diamond pattern using simple mathematical trendline analysis
    """
    if len(points) != 5:
        return False, {}
    
    try:
        if pattern_type == 'bottom':  # H-L-H-L-H
            highs = [points[0], points[2], points[4]]  # H1, H2, H3
            lows = [points[1], points[3]]             # L1, L2
        else:  # top: L-H-L-H-L
            lows = [points[0], points[2], points[4]]   # L1, L2, L3
            highs = [points[1], points[3]]            # H1, H2
        
        # Calculate slopes and consistency
        high_slope = calculate_simple_slope(highs) if len(highs) >= 2 else 0
        low_slope = calculate_simple_slope(lows) if len(lows) >= 2 else 0
        
        high_consistency = calculate_trendline_consistency(highs) if len(highs) >= 2 else 1.0
        low_consistency = calculate_trendline_consistency(lows) if len(lows) >= 2 else 1.0
        
        # Validation logic
        if pattern_type == 'bottom':
            # For diamond bottom: highs should trend down, lows should trend up
            valid_convergence = high_slope < 0 and low_slope > 0
            valid_consistency = high_consistency >= min_consistency and low_consistency >= min_consistency
        else:
            # For diamond top: highs should trend down, lows should trend up (converging)
            valid_convergence = high_slope < 0 and low_slope > 0
            valid_consistency = high_consistency >= min_consistency and low_consistency >= min_consistency
        
        return valid_convergence and valid_consistency, {
            'high_slope': high_slope,
            'low_slope': low_slope,
            'high_consistency': high_consistency,
            'low_consistency': low_consistency
        }
    
    except Exception as e:
        return False, {}

# === VOLUME CONFIRMATION ===

def check_volume_confirmation(df, signal_idx, volume_period=20):
    """
    Check if breakout candle has volume confirmation
    """
    if 'volume' not in df.columns:
        return True  # Skip volume check if not available
    
    if signal_idx < volume_period:
        return True
    
    try:
        # Calculate volume SMA
        volume_sma = df['volume'].iloc[signal_idx-volume_period:signal_idx].mean()
        current_volume = df['volume'].iloc[signal_idx]
        
        # Volume should be above average
        return current_volume > volume_sma
    except:
        return True  # Default to True if calculation fails

def find_enhanced_diamond_patterns(df, pivot_highs, pivot_lows, max_pattern_length=72,
                                  use_rsi_filter=False, rsi_oversold=30, rsi_overbought=70, rsi_column='rsi14',
                                  use_volume_filter=True, use_trendline_validation=True, min_consistency=0.6):
    """
    Enhanced diamond pattern detection with multiple validation layers:
    1. Basic pattern structure (H-L-H-L-H or L-H-L-H-L)
    2. Diamond shape validation (broadening -> contracting)
    3. Simple trendline validation
    4. Volume confirmation
    5. RSI filter (optional)
    """
    signals = []
    
    # Combine và sort tất cả pivots
    all_pivots = []
    for idx, price in pivot_highs:
        all_pivots.append((idx, price, 'high'))
    for idx, price in pivot_lows:
        all_pivots.append((idx, price, 'low'))
    
    all_pivots.sort(key=lambda x: x[0])
    
    print(f"🔍 Analyzing {len(all_pivots)} total pivots for diamond patterns...")
    
    # Tìm pattern với 5 pivot points
    patterns_tested = 0
    patterns_passed_basic = 0
    patterns_passed_shape = 0
    patterns_passed_trendline = 0
    patterns_passed_volume = 0
    
    for i in range(len(all_pivots) - 4):
        p1, p2, p3, p4, p5 = all_pivots[i:i+5]
        patterns_tested += 1
        
        # Kiểm tra độ dài pattern
        pattern_length = p5[0] - p1[0]
        if pattern_length > max_pattern_length:
            continue
            
        signal_idx = p5[0] + 1
        if signal_idx >= len(df):
            continue
            
        entry_price = df.iloc[signal_idx]['open']
        
        # DIAMOND BOTTOM (BUY Signal): H-L-H-L-H
        if (p1[2] == 'high' and p2[2] == 'low' and p3[2] == 'high' and 
            p4[2] == 'low' and p5[2] == 'high'):
            
            patterns_passed_basic += 1
            
            # Enhanced validation layers
            pattern_points = [p1, p2, p3, p4, p5]
            
            # 1. Diamond shape validation
            if not validate_diamond_shape(pattern_points, 'bottom'):
                continue
            patterns_passed_shape += 1
            
            # 2. Simple trendline validation
            trendline_valid = True
            trendline_stats = {}
            if use_trendline_validation:
                trendline_valid, trendline_stats = validate_trendlines(pattern_points, 'bottom', min_consistency)
                if not trendline_valid:
                    continue
            patterns_passed_trendline += 1
            
            # 3. Volume confirmation
            volume_valid = True
            if use_volume_filter:
                volume_valid = check_volume_confirmation(df, signal_idx)
                if not volume_valid:
                    continue
            patterns_passed_volume += 1
            
            # 4. RSI filter
            rsi_valid = True
            current_rsi = None
            if use_rsi_filter:
                if rsi_column in df.columns:
                    current_rsi = df.iloc[signal_idx][rsi_column]
                    rsi_valid = current_rsi < rsi_oversold
                else:
                    print(f"RSI column '{rsi_column}' not found, skipping RSI filter")
            
            if rsi_valid:
                    signals.append({
                        'signal_type': 'BUY',
                        'signal_idx': signal_idx,
                        'datetime': df.iloc[signal_idx]['datetime'],
                        'entry_price': entry_price,
                    'pattern_points': pattern_points,
                        'pattern_length': pattern_length,
                        'pattern_name': 'Diamond Bottom',
                    'rsi_value': current_rsi,
                    'volume_confirmed': volume_valid,
                    'trendline_stats': trendline_stats
                    })
        
        # DIAMOND TOP (SELL Signal): L-H-L-H-L  
        elif (p1[2] == 'low' and p2[2] == 'high' and p3[2] == 'low' and 
              p4[2] == 'high' and p5[2] == 'low'):
            
            patterns_passed_basic += 1
            
            # Enhanced validation layers
            pattern_points = [p1, p2, p3, p4, p5]
            
            # 1. Diamond shape validation
            if not validate_diamond_shape(pattern_points, 'top'):
                continue
            patterns_passed_shape += 1
            
            # 2. Simple trendline validation
            trendline_valid = True
            trendline_stats = {}
            if use_trendline_validation:
                trendline_valid, trendline_stats = validate_trendlines(pattern_points, 'top', min_consistency)
                if not trendline_valid:
                    continue
            patterns_passed_trendline += 1
            
            # 3. Volume confirmation
            volume_valid = True
            if use_volume_filter:
                volume_valid = check_volume_confirmation(df, signal_idx)
                if not volume_valid:
                    continue
            patterns_passed_volume += 1
            
            # 4. RSI filter
            rsi_valid = True
            current_rsi = None
            if use_rsi_filter:
                if rsi_column in df.columns:
                    current_rsi = df.iloc[signal_idx][rsi_column]
                    rsi_valid = current_rsi > rsi_overbought
                else:
                    print(f"RSI column '{rsi_column}' not found, skipping RSI filter")
            
            if rsi_valid:
                    signals.append({
                        'signal_type': 'SELL',
                        'signal_idx': signal_idx,
                        'datetime': df.iloc[signal_idx]['datetime'],
                        'entry_price': entry_price,
                    'pattern_points': pattern_points,
                        'pattern_length': pattern_length,
                        'pattern_name': 'Diamond Top',
                    'rsi_value': current_rsi,
                    'volume_confirmed': volume_valid,
                    'trendline_stats': trendline_stats
                })
    
    # Print validation statistics
    print(f"Pattern Validation Statistics:")
    print(f"Patterns tested: {patterns_tested}")
    print(f"Passed basic structure: {patterns_passed_basic}")
    print(f"Passed shape validation: {patterns_passed_shape}")
    if use_trendline_validation:
        print(f"   Passed trendline validation: {patterns_passed_trendline}")
    if use_volume_filter:
        print(f"   Passed volume confirmation: {patterns_passed_volume}")
    print(f"   Final signals: {len(signals)}")
    
    return signals

# Hàm tính toán kết quả back test (hỗ trợ cả BUY và SELL với quản lý tài khoản)
def calculate_backtest_results(df, signals, tp_percent=5.0, sl_percent=2.0, max_hold_bars=24, 
                             initial_balance=1000, trade_amount=100, 
                             use_trailing_stop=False, trailing_percent=2.5):
    """
    Tính toán kết quả back test với take profit và stop loss (cả BUY và SELL)
    Bao gồm quản lý tài khoản thực tế
    
    tp_percent: take profit %
    sl_percent: stop loss %
    max_hold_bars: số candle tối đa giữ lệnh
    initial_balance: số dư ban đầu ($)
    trade_amount: số tiền đầu tư mỗi lần ($)
    """
    results = []
    current_balance = initial_balance
    
    for signal in signals:
        # Kiểm tra có đủ tiền để giao dịch không
        if current_balance < trade_amount:
            print(f"Not enough money to trade at {signal['datetime']} (Balance: ${current_balance:.2f})")
            continue
            
        signal_idx = signal['signal_idx']
        entry_price = signal['entry_price']
        signal_type = signal['signal_type']
        
        # Calculate the quantity of coins that can be bought/sold
        coin_quantity = trade_amount / entry_price
        
        # Calculate target prices theo hướng
        if signal_type == 'BUY':
            tp_price = entry_price * (1 + tp_percent/100)
            initial_sl_price = entry_price * (1 - sl_percent/100)
        else:  # SELL
            tp_price = entry_price * (1 - tp_percent/100)  # TP lower than entry
            initial_sl_price = entry_price * (1 + sl_percent/100)  # SL higher than entry
        
        # Initialize trailing stop
        current_sl_price = initial_sl_price
        best_price = entry_price  # Best price reached
        
        # Tìm exit point
        exit_idx = None
        exit_price = None
        exit_reason = None
        
        for i in range(signal_idx + 1, min(signal_idx + max_hold_bars, len(df))):
            current_high = df.iloc[i]['high']
            current_low = df.iloc[i]['low']
            current_close = df.iloc[i]['close']
            
            if signal_type == 'BUY':
                # Update best price and trailing stop for BUY
                if current_high > best_price:
                    best_price = current_high
                    if use_trailing_stop:
                        # Move SL up the best price
                        new_sl = best_price * (1 - trailing_percent/100)
                        current_sl_price = max(current_sl_price, new_sl)
                
                # Check exit conditions for BUY
                if current_high >= tp_price:
                    exit_idx = i
                    exit_price = tp_price
                    exit_reason = 'TP'
                    break
                elif current_low <= current_sl_price:
                    exit_idx = i  
                    exit_price = current_sl_price
                    exit_reason = 'TSL' if use_trailing_stop and current_sl_price > initial_sl_price else 'SL'
                    break
                    
            else:  # SELL
                # Update best price and trailing stop for SELL
                if current_low < best_price:
                    best_price = current_low
                    if use_trailing_stop:
                        # Move SL down the best price
                        new_sl = best_price * (1 + trailing_percent/100)
                        current_sl_price = min(current_sl_price, new_sl)
                
                # Check exit conditions for SELL
                if current_low <= tp_price:
                    exit_idx = i
                    exit_price = tp_price
                    exit_reason = 'TP'
                    break
                elif current_high >= current_sl_price:
                    exit_idx = i  
                    exit_price = current_sl_price
                    exit_reason = 'TSL' if use_trailing_stop and current_sl_price < initial_sl_price else 'SL'
                    break
        
        # If no TP/SL, exit at max hold
        if exit_idx is None and signal_idx + max_hold_bars < len(df):
            exit_idx = signal_idx + max_hold_bars
            exit_price = df.iloc[exit_idx]['close']
            exit_reason = 'Time'
        
        if exit_idx is not None:
            # Calculate PnL theo hướng
            if signal_type == 'BUY':
                pnl_percent = ((exit_price - entry_price) / entry_price) * 100
                pnl_dollar = coin_quantity * (exit_price - entry_price)
            else:  # SELL
                pnl_percent = ((entry_price - exit_price) / entry_price) * 100
                pnl_dollar = coin_quantity * (entry_price - exit_price)
            
            # Update the balance
            current_balance += pnl_dollar
            is_win = pnl_dollar > 0
            
            results.append({
                'signal_type': signal_type,
                'pattern_name': signal['pattern_name'],
                'signal_datetime': signal['datetime'],
                'entry_price': entry_price,
                'exit_price': exit_price,
                'exit_reason': exit_reason,
                'pnl_percent': pnl_percent,
                'pnl_dollar': pnl_dollar,
                'coin_quantity': coin_quantity,
                'balance_after': current_balance,
                'is_win': is_win,
                'hold_bars': exit_idx - signal_idx
            })
    
    return results, current_balance

# --- Backtest with Exit Strategy from butterfly ---
def calculate_backtest_results_butterfly_style(df, signals, exit_periods, initial_balance=INITIAL_BALANCE, trade_amount=TRADE_AMOUNT):
    """
    Backtest with Exit Strategy from butterfly pattern:
    - Manage positions by time
    - Use percentage of the balance
    - Close positions by bars held or take profit
    """
    results = []
    balance = initial_balance
    positions = []
    
    # Sort signals by entry time
    signals = sorted(signals, key=lambda x: x['signal_idx'])
    
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
                'exit_reason': exit_reason,
                'trendline_stats': position.get('trendline_stats', {}),
                'volume_confirmed': position.get('volume_confirmed', True)
            })
            positions.pop(pos_idx)
        
        # Look for new signals to enter (chỉ 1 trade tại 1 thời điểm)
        if len(positions) == 0:  # Only enter if no existing positions
            for sig in signals:
                if sig['signal_idx'] == i:
                    # Use percentage of capital like butterfly
                    position_value = balance * 0.95  # Use 95% of capital
                    quantity = position_value / current_close
                    
                    # Convert signal type to LONG/SHORT
                    direction = 'LONG' if sig['signal_type'] == 'BUY' else 'SHORT'
                    
                    position = {
                        'type': direction,
                        'entry_time': sig['datetime'],
                        'entry_index': i,
                        'entry_price': current_close,
                        'quantity': quantity,
                        'value': position_value,
                        'pattern_type': sig['pattern_name'],
                        'trendline_stats': sig.get('trendline_stats', {}),
                        'volume_confirmed': sig.get('volume_confirmed', True)
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
                'exit_reason': 'End',
                'trendline_stats': position.get('trendline_stats', {}),
                'volume_confirmed': position.get('volume_confirmed', True)
            })
    
    return results, balance

# Function to export the backtest report to a file
def export_backtest_report(signals, results, final_balance, filename=None):
    """
    Export the backtest report to a markdown file
    """
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"diamond_pattern_backtest_{timestamp}.md"
    
    # Basic statistics
    buy_signals = [s for s in signals if s['signal_type'] == 'BUY']
    sell_signals = [s for s in signals if s['signal_type'] == 'SELL']
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# DIAMOND PATTERN BACKTEST REPORT\n\n")
        f.write(f"**Thời gian tạo báo cáo:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## SETTINGS\n\n")
        f.write(f"- **Symbol:** {SYMBOL}\n")
        f.write(f"- **Initial Balance:** ${INITIAL_BALANCE:,.2f}\n")
        f.write(f"- **Số tiền mỗi lần giao dịch:** ${TRADE_AMOUNT:,.2f}\n")
        f.write(f"- **Take Profit:** {TAKE_PROFIT_PERCENT}%\n")
        f.write(f"- **Stop Loss:** 2.0%\n")
        f.write(f"- **Max Hold Time:** 24 hours\n")
        f.write(f"- **Trailing Stop:** OFF\n")
        f.write(f"- **RSI Filter:** {'ON' if USE_RSI_FILTER else 'OFF'}\n")
        
        if USE_RSI_FILTER:
            f.write(f"  - RSI Column: {RSI_COLUMN}\n")
            f.write(f"  - BUY when RSI < {RSI_OVERSOLD}\n")
            f.write(f"  - SELL when RSI > {RSI_OVERBOUGHT}\n")
        f.write("\n")
        
        if len(results) > 0:
            # Calculate metrics
            total_signals = len(results)
            winning_trades = sum(1 for r in results if r['is_win'])
            losing_trades = total_signals - winning_trades
            win_rate = (winning_trades / total_signals) * 100
            
            total_pnl_dollar = sum(r['pnl_dollar'] for r in results)
            total_roi = ((final_balance - INITIAL_BALANCE) / INITIAL_BALANCE) * 100
            
            winning_pnl_dollar = sum(r['pnl_dollar'] for r in results if r['is_win'])
            losing_pnl_dollar = sum(r['pnl_dollar'] for r in results if not r['is_win'])
            
            avg_win_dollar = winning_pnl_dollar / winning_trades if winning_trades > 0 else 0
            avg_loss_dollar = losing_pnl_dollar / losing_trades if losing_trades > 0 else 0
            
            profit_factor = abs(winning_pnl_dollar / losing_pnl_dollar) if losing_pnl_dollar != 0 else float('inf')
            
            f.write("## TOTAL RESULTS\n\n")
            f.write(f"- **Total Signals:** {total_signals}\n")
            f.write(f"- **Diamond Bottom (BUY):** {len(buy_signals)} signals\n")
            f.write(f"- **Diamond Top (SELL):** {len(sell_signals)} signals\n")
            f.write(f"- **Win Rate:** {win_rate:.1f}%\n")
            f.write(f"- **Final Balance:** ${final_balance:,.2f}\n")
            f.write(f"- **Total Profit:** ${total_pnl_dollar:+,.2f}\n")
            f.write(f"- **ROI:** {total_roi:+.2f}%\n")
            f.write(f"- **Profit Factor:** {profit_factor:.2f}\n\n")
            
            # Analyze by pattern type
            if len(buy_signals) > 0:
                buy_results = [r for r in results if r['signal_type'] == 'BUY']
                buy_win_rate = (sum(1 for r in buy_results if r['is_win']) / len(buy_results)) * 100
                buy_pnl_dollar = sum(r['pnl_dollar'] for r in buy_results)
                
                f.write("### Diamond Bottom (BUY) Analysis\n\n")
                f.write(f"- **Signals:** {len(buy_signals)}\n")
                f.write(f"- **Win Rate:** {buy_win_rate:.1f}%\n")
                f.write(f"- **PnL:** ${buy_pnl_dollar:+,.2f}\n")
                
                if USE_RSI_FILTER:
                    buy_rsi = [s['rsi_value'] for s in buy_signals if s['rsi_value'] is not None]
                    if buy_rsi:
                        f.write(f"- **RSI Values:** {[f'{rsi:.1f}' for rsi in buy_rsi]}\n")
                f.write("\n")
            
            if len(sell_signals) > 0:
                sell_results = [r for r in results if r['signal_type'] == 'SELL']
                sell_win_rate = (sum(1 for r in sell_results if r['is_win']) / len(sell_results)) * 100
                sell_pnl_dollar = sum(r['pnl_dollar'] for r in sell_results)
                
                f.write("### Diamond Top (SELL) Analysis\n\n")
                f.write(f"- **Signals:** {len(sell_signals)}\n")
                f.write(f"- **Win Rate:** {sell_win_rate:.1f}%\n")
                f.write(f"- **PnL:** ${sell_pnl_dollar:+,.2f}\n")
                
                if USE_RSI_FILTER:
                    sell_rsi = [s['rsi_value'] for s in sell_signals if s['rsi_value'] is not None]
                    if sell_rsi:
                        f.write(f"- **RSI Values:** {[f'{rsi:.1f}' for rsi in sell_rsi]}\n")
                f.write("\n")
            
            # Detailed transaction
            f.write("## DETAILS OF TRANSACTIONS\n\n")
            if USE_RSI_FILTER:
                f.write("| STT | Time | Type | Pattern | RSI | Entry | Exit | PnL ($) | PnL (%) | Balance | Exit |\n")
                f.write("|-----|-----------|------|---------|-----|-------|------|---------|---------|---------|------|\n")
            else:
                f.write("| STT | Time | Type | Pattern | Entry | Exit | PnL ($) | PnL (%) | Balance | Exit |\n")
                f.write("|-----|-----------|------|---------|-------|------|---------|---------|---------|------|\n")
            
            for i, result in enumerate(results):
                signal_type = result['signal_type']
                pattern_name = result['pattern_name']
                
                if USE_RSI_FILTER:
                    # Find RSI value from signals
                    matching_signal = None
                    for signal in signals:
                        if (signal['datetime'] == result['signal_datetime'] and 
                            signal['signal_type'] == result['signal_type']):
                            matching_signal = signal
                            break
                    
                    rsi_display = f"{matching_signal['rsi_value']:.1f}" if matching_signal and matching_signal['rsi_value'] is not None else "N/A"
                    
                    f.write(f"| {i+1} | {result['signal_datetime'].strftime('%m/%d %H:%M')} | "
                           f"{signal_type} | {pattern_name} | {rsi_display} | "
                           f"${result['entry_price']:.2f} | ${result['exit_price']:.2f} | "
                           f"${result['pnl_dollar']:+.2f} | {result['pnl_percent']:+.2f}% | "
                           f"${result['balance_after']:.2f} | {result['exit_reason']} |\n")
                else:
                    f.write(f"| {i+1} | {result['signal_datetime'].strftime('%m/%d %H:%M')} | "
                           f"{signal_type} | {pattern_name} | "
                           f"${result['entry_price']:.2f} | ${result['exit_price']:.2f} | "
                           f"${result['pnl_dollar']:+.2f} | {result['pnl_percent']:+.2f}% | "
                           f"${result['balance_after']:.2f} | {result['exit_reason']} |\n")
        else:
            f.write("## RESULT\n\n")
            f.write("Không tìm thấy diamond pattern nào phù hợp với điều kiện lọc.\n\n")
        
        f.write("---\n")
        f.write(f"*The report was automatically created by the Diamond Pattern Backtest System*\n")
    
    return filename

# --- Read data from database ---
df = get_binance_data(SYMBOL, TIMEFRAME)

if len(df) == 0:
    print("No data to backtest!")
    exit()

# Enhanced pivot detection
print(f"\nEnhanced Pivot Detection:")
print(f"   ATR-based dynamic window: {'ON' if USE_ENHANCED_PIVOTS else 'OFF'}")
print(f"   Shape validation: {'ON' if USE_SHAPE_VALIDATION else 'OFF'}")
print(f"   Trendline validation: {'ON' if USE_TRENDLINE_VALIDATION else 'OFF'}")
print(f"   Volume confirmation: {'ON' if USE_VOLUME_FILTER else 'OFF'}")

if USE_ENHANCED_PIVOTS:
    pivot_highs, pivot_lows = find_enhanced_pivots(df, base_window=3, atr_multiplier=2.0, min_distance_multiplier=1.5)
else:
    # Fallback to basic pivot detection
    def find_pivots(data, window=3):
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
    
pivot_highs, pivot_lows = find_pivots(df, window=3)

print(f"Found {len(pivot_highs)} pivot highs and {len(pivot_lows)} pivot lows")

# Enhanced diamond pattern detection
signals = find_enhanced_diamond_patterns(
    df, pivot_highs, pivot_lows, 
    max_pattern_length=72,
                               use_rsi_filter=USE_RSI_FILTER, 
                               rsi_oversold=RSI_OVERSOLD,
                               rsi_overbought=RSI_OVERBOUGHT,
    rsi_column=RSI_COLUMN,
    use_volume_filter=USE_VOLUME_FILTER,
    use_trendline_validation=USE_TRENDLINE_VALIDATION,
    min_consistency=MIN_CONSISTENCY
)

# --- Run backtest ---
if __name__ == "__main__":
    if len(signals) > 0:
            # Statistics by signal type
        buy_signals = [s for s in signals if s['signal_type'] == 'BUY']
        sell_signals = [s for s in signals if s['signal_type'] == 'SELL']
        
        print(f"Found {len(buy_signals)} Diamond Bottom (BUY) and {len(sell_signals)} Diamond Top (SELL) signals")
        
        # Run dual exit strategy backtests
        results_9, final_balance_9 = calculate_backtest_results_butterfly_style(df, signals, EXIT_PERIODS_1)
        results_26, final_balance_26 = calculate_backtest_results_butterfly_style(df, signals, EXIT_PERIODS_2)
        
        # Export comparison report
        def export_diamond_comparison_report(signals, results_9, results_26, final_balance_9, final_balance_26, filename=None):
            if filename is None:
                filename = f"enhanced_diamond_pattern_{SYMBOL.lower()}_{TIMEFRAME}.md"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"# Enhanced Diamond Pattern Strategy Comparison - {SYMBOL} {TIMEFRAME}\n\n")
                f.write(f"## Strategy Overview\n")
                f.write(f"- **Pattern**: Enhanced Diamond Pattern (Bottom & Top)\n")
                f.write(f"- **Entry**: At close price when pattern is detected\n")
                f.write(f"- **Exit Strategy 1**: Hold for {EXIT_PERIODS_1} periods\n")
                f.write(f"- **Exit Strategy 2**: Hold for {EXIT_PERIODS_2} periods\n")
                f.write(f"- **Take Profit**: {TAKE_PROFIT_PERCENT}%\n\n")
                
                f.write(f"## Enhanced Features\n")
                f.write(f"- **ATR-based Pivots**: {'ON' if USE_ENHANCED_PIVOTS else 'OFF'}\n")
                f.write(f"- **Shape Validation**: {'ON' if USE_SHAPE_VALIDATION else 'OFF'}\n")
                f.write(f"- **Trendline Validation**: {'ON' if USE_TRENDLINE_VALIDATION else 'OFF'}\n")
                f.write(f"- **Volume Confirmation**: {'ON' if USE_VOLUME_FILTER else 'OFF'}\n")
                f.write(f"- **RSI Filter**: {'ON' if USE_RSI_FILTER else 'OFF'}\n\n")
                
                # Calculate metrics
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
                
                # Analysis
                f.write(f"## Analysis\n\n")
                if metrics_26['total_return'] > metrics_9['total_return']:
                    winner = f"{EXIT_PERIODS_2} periods Strategy"
                    return_diff = metrics_26['total_return'] - metrics_9['total_return']
                    f.write(f"**Winner: {winner}**\n\n")
                    f.write(f"The {EXIT_PERIODS_2}-period exit strategy outperformed with {metrics_26['total_return']:.2f}% return vs {metrics_9['total_return']:.2f}%.\n\n")
                else:
                    winner = f"{EXIT_PERIODS_1} Periods Strategy"
                    return_diff = metrics_9['total_return'] - metrics_26['total_return']
                    f.write(f"**Winner: {winner}**\n\n")
                    f.write(f"The {EXIT_PERIODS_1}-period exit strategy outperformed with {metrics_9['total_return']:.2f}% return vs {metrics_26['total_return']:.2f}%.\n\n")
                
                f.write(f"---\n")
                f.write(f"*Enhanced Diamond Pattern Backtest System*\n")
            
            return filename
        
        report_file = export_diamond_comparison_report(signals, results_9, results_26, final_balance_9, final_balance_26)
        print(f"Report exported: {report_file}")
        
        print(f"\n=== SUMMARY RESULTS ===")
        print(f"Total signals: {len(signals)}")
        print(f"Strategy 1 ({EXIT_PERIODS_1} periods): {len(results_9)} trades, ${final_balance_9:.2f}")
        print(f"Strategy 2 ({EXIT_PERIODS_2} periods): {len(results_26)} trades, ${final_balance_26:.2f}")
        
        # Enhanced signal statistics
        if USE_TRENDLINE_VALIDATION and signals:
            avg_high_consistency = np.mean([s.get('trendline_stats', {}).get('high_consistency', 0) for s in signals])
            avg_low_consistency = np.mean([s.get('trendline_stats', {}).get('low_consistency', 0) for s in signals])
            print(f"\nEnhanced Statistics:")
            print(f"Average High Trendline Consistency: {avg_high_consistency:.3f}")
            print(f"Average Low Trendline Consistency: {avg_low_consistency:.3f}")
            
        if USE_VOLUME_FILTER and signals:
            volume_confirmed = sum(1 for s in signals if s.get('volume_confirmed', True))
            print(f"Volume confirmed signals: {volume_confirmed}/{len(signals)} ({volume_confirmed/len(signals)*100:.1f}%)")
        
    else:
        print("No enhanced diamond patterns found!")
        # Create empty report
        def export_diamond_comparison_report(signals, results_9, results_26, final_balance_9, final_balance_26, filename=None):
            if filename is None:
                filename = f"enhanced_diamond_pattern_{SYMBOL.lower()}_{TIMEFRAME}.md"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"# Enhanced Diamond Pattern Strategy Comparison - {SYMBOL} {TIMEFRAME}\n\n")
                f.write(f"## Strategy Overview\n")
                f.write(f"- **Pattern**: Enhanced Diamond Pattern (Bottom & Top)\n")
                f.write(f"- **Entry**: At close price when pattern is detected\n")
                f.write(f"- **Exit Strategy 1**: Hold for {EXIT_PERIODS_1} periods\n")
                f.write(f"- **Exit Strategy 2**: Hold for {EXIT_PERIODS_2} periods\n")
                f.write(f"- **Take Profit**: {TAKE_PROFIT_PERCENT}%\n\n")
                
                f.write(f"## Enhanced Features\n")
                f.write(f"- **ATR-based Pivots**: {'ON' if USE_ENHANCED_PIVOTS else 'OFF'}\n")
                f.write(f"- **Shape Validation**: {'ON' if USE_SHAPE_VALIDATION else 'OFF'}\n")
                f.write(f"- **Trendline Validation**: {'ON' if USE_TRENDLINE_VALIDATION else 'OFF'}\n")
                f.write(f"- **Volume Confirmation**: {'ON' if USE_VOLUME_FILTER else 'OFF'}\n")
                f.write(f"- **RSI Filter**: {'ON' if USE_RSI_FILTER else 'OFF'}\n\n")
                
                f.write(f"No enhanced diamond patterns found in the selected timeframe.\n\n")
                f.write(f"---\n")
                f.write(f"*Enhanced Diamond Pattern Backtest System*\n")
            
            return filename
        
        report_file = export_diamond_comparison_report([], [], [], INITIAL_BALANCE, INITIAL_BALANCE)
        print(f"Report exported: {report_file}")