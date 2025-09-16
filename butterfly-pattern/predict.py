import os
import pandas as pd
import numpy as np
import argparse
from dotenv import load_dotenv
from sqlalchemy import create_engine
from datetime import datetime, timedelta

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Lookback period for scanning historical signals
LOOKBACK_PERIOD = 40

try:
    print(f"Connecting to DB: {DB_HOST}:{DB_PORT}/{DB_NAME}")
    engine = create_engine(DATABASE_URL)
    print("Connected to DB successfully")
except Exception as e:
    engine = None
    print(f"Failed to connect to DB: {e}")

# --- Hàm đọc data từ Database ---
def get_binance_data(symbol, interval):
    """

    """
    print(f"Getting data from DB: {symbol} {interval}")
    if engine is None:
        print("No valid DB connection.")
        return pd.DataFrame()

    table_name =  "proddb.coin_prices_1h"

    query = f"""
        SELECT *
        FROM {table_name}
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
            print("Missing 'open_time' column in data returned from DB.")
            print(f"   Columns: {list(df.columns)}")
            return pd.DataFrame()

        required_cols = {'open', 'high', 'low', 'close'}
        if not required_cols.issubset(df.columns):
            print(f"Missing required columns: {required_cols - set(df.columns)}")
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

def detect_swing_points(df, window=3, detect_current=True):
    """Detect swing highs and lows.

    If detect_current is True, detect potential swing points for the latest candles
    without requiring future candles by comparing only with previous candles.
    """
    df = df.copy()
    df['swing_high'] = False
    df['swing_low'] = False

    # Original logic: requires both past and future candles
    for i in range(window, len(df) - window):
        if df.loc[i, 'high'] == df.loc[i-window:i+window, 'high'].max():
            df.loc[i, 'swing_high'] = True
        if df.loc[i, 'low'] == df.loc[i-window:i+window, 'low'].min():
            df.loc[i, 'swing_low'] = True

    # Real-time extension: evaluate last candles using only historical lookback
    if detect_current and len(df) > 0:
        # Evaluate from the first index where original loop stops to the end
        start_idx = max(window, len(df) - window)
        for i in range(start_idx, len(df)):
            lookback_start = max(0, i - window * 2)
            if df.loc[i, 'high'] == df.loc[lookback_start:i+1, 'high'].max():
                df.loc[i, 'swing_high'] = True
            if df.loc[i, 'low'] == df.loc[lookback_start:i+1, 'low'].min():
                df.loc[i, 'swing_low'] = True

    return df

def is_within_tolerance(actual, expected, tolerance=0.15):
    """Check if actual value is within tolerance of expected Fibonacci ratio"""
    return abs(actual - expected) / expected <= tolerance

def find_butterfly_patterns(df, max_pattern_length=72, entry_on_current=True):
    """
    Find Butterfly Pattern using method 2 with swing points and higher tolerance:
    --------------------------------
    Bullish Butterfly Pattern:
    Structure: X(low) → A(high) → B(low) → C(high) → D(low - entry point)
    Fibonacci ratios with tolerance 15-25%:
    - AB = 0.786 of XA
    - BC = 0.382 or 0.886 of AB  
    - CD = 1.27 or 1.618 of BC
    - AD = 0.786 of XA
    
    Bearish Butterfly Pattern:
    Structure: X(high) → A(low) → B(high) → C(low) → D(high - entry point)
    """
    signals = []
    
    # Detect swing points (allow current-candle detection)
    df = detect_swing_points(df, window=3, detect_current=True)
    
    # Find Bullish Butterfly Pattern
    for i in range(15, len(df)):  # Start from index 15 like method 2
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

            # Check Fibonacci ratios with higher tolerance
            AB_XA_ratio = AB / XA
            BC_AB_ratio = BC / AB
            CD_BC_ratio = CD / BC if BC > 0 else 0
            AD_XA_ratio = AD / XA
            
            # Butterfly pattern ratios with tolerance 15-25%
            valid_AB = is_within_tolerance(AB_XA_ratio, 0.786, 0.2)
            valid_BC = (is_within_tolerance(BC_AB_ratio, 0.382, 0.2) or 
                       is_within_tolerance(BC_AB_ratio, 0.886, 0.2))
            valid_CD = (is_within_tolerance(CD_BC_ratio, 1.27, 0.25) or
                       is_within_tolerance(CD_BC_ratio, 1.618, 0.25))
            valid_AD = is_within_tolerance(AD_XA_ratio, 0.786, 0.2)
            
            if valid_AB and valid_BC and valid_CD and valid_AD:
                entry_idx = i if entry_on_current else i + 1
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
    
    # Find Bearish Butterfly Pattern
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

            valid_AB = is_within_tolerance(AB_XA_ratio, 0.786, 0.2)
            valid_BC = (is_within_tolerance(BC_AB_ratio, 0.382, 0.2) or
                       is_within_tolerance(BC_AB_ratio, 0.886, 0.2))
            valid_CD = (is_within_tolerance(CD_BC_ratio, 1.27, 0.25) or
                       is_within_tolerance(CD_BC_ratio, 1.618, 0.25))
            valid_AD = is_within_tolerance(AD_XA_ratio, 0.786, 0.2)
            
            if valid_AB and valid_BC and valid_CD and valid_AD:
                entry_idx = i if entry_on_current else i + 1
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

def print_signals_list(signals):
    if not signals:
        print("\nNo signals to list.")
        return
    print("\n=== DANH SÁCH PHIÊN DỰ ĐOÁN ===")
    for s in signals:
        et = s.get('entry_time')
        et_str = et.strftime('%Y-%m-%d %H:%M') if hasattr(et, 'strftime') else str(et)
        print(
            f" - {et_str} | {s.get('type')} | {s.get('direction')} | "
            f"Entry idx: {s.get('entry_idx')} | Entry price: ${s.get('entry_price'):.4f}"
        )

def predict_price_with_accuracy(df, signal_func=None, direction='up', lookback=LOOKBACK_PERIOD, precomputed_signals=None):
    """
    Predict next price based on indicator with improved accuracy.
    
    Args:
        df: DataFrame containing price data
        signal_func: Function to check signal (should_buy or should_sell)
        direction: 'up' for buy signal, 'down' for sell signal
        lookback: Minimum lookback period
    """
    if len(df) < lookback + 1:
        return None, 0, 0, 0

    direction = direction.lower()

    # Optimize: preprocess signal list for O(1) lookup by entry_idx
    signals_list = precomputed_signals
    if signals_list is None:
        # Fallback: still support calling function, but more expensive
        signals_list = signal_func(df) if signal_func is not None else []

    signals_by_entry = {}
    for s in signals_list:
        idx = s.get('entry_idx')
        if idx is None:
            continue
        # If there are multiple signals with the same entry_idx, prioritize the last one (closer to current)
        signals_by_entry[idx] = s

    actual_changes = []  # only changes for signals matching desired direction
    price_changes_when_correct = []

    for i in range(lookback, len(df) - 1):  # -1 to leave room for next candle to check
        entry_at_next = i + 1
        sig = signals_by_entry.get(entry_at_next)
        if not sig:
            continue

        direction_signal = sig.get('direction', '').upper()
        if not (
            (direction == 'up' and direction_signal == 'LONG') or
            (direction == 'down' and direction_signal == 'SHORT')
        ):
            continue

        close_now = df.iloc[i]['close']
        close_next = df.iloc[i+1]['close']
        price_change = close_next - close_now

        actual_changes.append(price_change)

        if direction == 'up' and price_change > 0:
            price_changes_when_correct.append(price_change)
        elif direction == 'down' and price_change < 0:
            price_changes_when_correct.append(abs(price_change))

    if not actual_changes:
        return None, 0, 0, 0

    # Calculate number of correct and accuracy
    if direction == 'up':
        correct = sum(1 for chg in actual_changes if chg > 0)
    else:
        correct = sum(1 for chg in actual_changes if chg < 0)

    total_signals = len(actual_changes)
    accuracy = correct / total_signals * 100 if total_signals > 0 else 0

    # Predicted price = average of actual increases/decreases (only take correct ones)
    if price_changes_when_correct:
        avg_change = float(np.mean(price_changes_when_correct))
        last_price = df.iloc[-1]['close']
        predicted_price = last_price + avg_change if direction == 'up' else last_price - avg_change
    else:
        predicted_price = None

    return predicted_price, accuracy, total_signals, correct

def evaluate_signal_performance(df, signals, direction, horizon):
    """Evaluate signal performance by horizon (number of candles after entry).

    Trả về: (avg_signed_change, accuracy_percent, total_samples, correct)
    - avg_signed_change: average price change after horizon from entry (signed)
    - accuracy: % number of correct directions (increase for LONG, decrease for SHORT)
    """
    if df.empty:
        return 0.0, 0.0, 0, 0

    direction = direction.lower()
    last_index = len(df) - 1

    # Filter signals by direction and enough data to evaluate
    filtered = [s for s in signals if (
        (direction == 'up' and s.get('direction') == 'LONG') or
        (direction == 'down' and s.get('direction') == 'SHORT')
    ) and isinstance(s.get('entry_idx'), (int, np.integer)) and s['entry_idx'] + horizon <= last_index]

    if not filtered:
        return 0.0, 0.0, 0, 0

    signed_changes = []
    correct = 0
    for s in filtered:
        e = s['entry_idx']
        change = df.iloc[e + horizon]['close'] - df.iloc[e]['close']
        signed_changes.append(change)
        if (direction == 'up' and change > 0) or (direction == 'down' and change < 0):
            correct += 1

    total = len(filtered)
    accuracy = correct / total * 100 if total > 0 else 0.0
    avg_signed_change = float(np.mean(signed_changes)) if signed_changes else 0.0
    return avg_signed_change, accuracy, total, correct

def evaluate_signal_performance_percent(df, signals, direction, horizon):
    """Evaluate signal performance (%) by horizon.

    Trả về: (avg_correct_change_percent, accuracy_percent, total_samples, correct)
    - avg_correct_change_percent: average % change when PREDICTED CORRECTLY
    - accuracy: % number of correct directions
    """
    if df.empty:
        return 0.0, 0.0, 0, 0

    direction = direction.lower()
    last_index = len(df) - 1
    filtered = [s for s in signals if (
        (direction == 'up' and s.get('direction') == 'LONG') or
        (direction == 'down' and s.get('direction') == 'SHORT')
    ) and isinstance(s.get('entry_idx'), (int, np.integer)) and s['entry_idx'] + horizon <= last_index]

    if not filtered:
        return 0.0, 0.0, 0, 0

    correct = 0
    correct_change_percents = []
    for s in filtered:
        e = s['entry_idx']
        start = df.iloc[e]['close']
        end = df.iloc[e + horizon]['close']
        if start == 0:
            continue
        pct = (end - start) / start * 100.0
        is_correct = (direction == 'up' and pct > 0) or (direction == 'down' and pct < 0)
        if is_correct:
            correct += 1
            correct_change_percents.append(abs(pct))

    total = len(filtered)
    accuracy = correct / total * 100 if total > 0 else 0.0
    avg_correct_change_percent = float(np.mean(correct_change_percents)) if correct_change_percents else 0.0
    return avg_correct_change_percent, accuracy, total, correct

def main():
    symbol = "ETHUSDT"
    interval = "1h"

    print(f"Getting data {symbol}...")
    df = get_binance_data(symbol, interval)

    if df.empty:
        print("No data. Check database connection.")
        return

    print(f"  {len(df)} candles data\n")

    print("=== STARTING PRICE PREDICTION ANALYSIS ===")

    print(f"Finding Butterfly Pattern...")
    signals = find_butterfly_patterns(df, entry_on_current=True)

    if not signals:
        print("No Butterfly Pattern found.")
        return

    print(f" Found {len(signals)} Butterfly Pattern")
    print_signals_list(signals)

    print("\n=== SIGNAL ANALYSIS ===")
    
    # Predict for buy signal (Bullish)
    bullish_pred_price, bullish_acc, bullish_total, bullish_correct = \
        predict_price_with_accuracy(df, direction='up', precomputed_signals=signals)

    # Predict for sell signal (Bearish)
    bearish_pred_price, bearish_acc, bearish_total, bearish_correct = \
        predict_price_with_accuracy(df, direction='down', precomputed_signals=signals)

    last_close = df.iloc[-1]['close'] if not df.empty else None

    # Check if there is a current signal (at the next candle entry_idx == len(df)-1)
    current_index = len(df) - 1
    current_signal = None
    if signals:
        # get signal with entry_idx == current_index
        for s in reversed(signals):
            if s.get('entry_idx') == current_index:
                current_signal = s
                break

    if not current_signal:
        print("\nNo new signal → No prediction.")
        # Show history statistics as requested
        for dir_label, dir_key in (("Bullish (LONG)", 'up'), ("Bearish (SHORT)", 'down')):
            print(f"\n🔹 {dir_label}:")
            for horizon in (9, 26):
                avg_correct_pct, acc, total, correct = evaluate_signal_performance_percent(
                    df, signals, dir_key, horizon
                )
                print(
                    f"   - After {horizon} sessions: Accuracy {acc:.2f}% ({correct}/{total}), "
                    f"Average change when correct: {avg_correct_pct:.4f}%"
                )   
    else:
        sig_dir = current_signal.get('direction')
        print("\n  Current signal found:")
        print(f"   Type: {current_signal.get('type')} | Direction: {sig_dir} | Entry time: {current_signal.get('entry_time')}")
        print(f"   Entry price: ${current_signal.get('entry_price'):.4f}")

        # Evaluate history by horizon 9 and 26 sessions
        for horizon in (9, 26):
            avg_change, acc, total, correct = evaluate_signal_performance(
                df, signals, 'up' if sig_dir == 'LONG' else 'down', horizon
            )
            if last_close is not None:
                predicted_price = last_close + avg_change if sig_dir == 'LONG' else last_close - abs(avg_change)
                change_pct = (predicted_price - last_close) / last_close * 100
                print(f"   Prediction after {horizon} sessions: ${predicted_price:.4f} ({change_pct:+.2f}%) | History accuracy: {acc:.1f}% ({correct}/{total})")

if __name__ == "__main__":
    main()