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
    print(f"Ket noi DB: {DB_HOST}:{DB_PORT}/{DB_NAME}")
    engine = create_engine(DATABASE_URL)
    print("Ket noi DB thanh cong")
except Exception as e:
    engine = None
    print(f"Khong tao duoc ket noi DB: {e}")

# --- Hàm đọc data từ Database ---
def get_binance_data(symbol, interval):
    """

    """
    print(f"Lay du lieu tu DB: {symbol} {interval}")
    if engine is None:
        print("Chua co ket noi DB hop le.")
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
            print("Thieu cot 'open_time' trong du lieu tra ve tu DB.")
            print(f"   Columns: {list(df.columns)}")
            return pd.DataFrame()

        required_cols = {'open', 'high', 'low', 'close'}
        if not required_cols.issubset(df.columns):
            print(f"Thieu cot can thiet: {required_cols - set(df.columns)}")
            return pd.DataFrame()

        df['datetime'] = pd.to_datetime(df['open_time'], unit='s')
        df = df.sort_values('datetime').reset_index(drop=True)

        print(f"Da doc {len(df)} dong tu DB bang {table_name}")
        if len(df) > 0:
            print(f"   Thời gian: {df['datetime'].min()} đến {df['datetime'].max()}")
            print(f"   Giá cuối: ${df.iloc[-1]['close']:.4f}")

        return df
    except Exception as e:
        print(f"Loi khi doc du lieu tu DB: {e}")
        return pd.DataFrame()


# ========== Diamond detection utilities (no ML, mirrors backtest) ==========

def calculate_atr(data, period=14):
    high = data['high']
    low = data['low']
    close = data['close'].shift(1)
    tr1 = high - low
    tr2 = abs(high - close)
    tr3 = abs(low - close)
    true_range = np.maximum(tr1, np.maximum(tr2, tr3))
    return true_range.rolling(window=period).mean()


def find_enhanced_pivots(data, base_window=3, atr_multiplier=2.0, min_distance_multiplier=1.5):
    atr = calculate_atr(data)
    avg_price = (data['high'] + data['low'] + data['close']) / 3
    pivot_highs, pivot_lows = [], []
    for i in range(14, len(data) - base_window):
        current_atr = atr.iloc[i]
        current_avg_price = avg_price.iloc[i]
        if pd.notna(current_atr) and current_avg_price > 0:
            adaptive_factor = (current_atr / current_avg_price) * atr_multiplier
            window = max(base_window, min(8, int(base_window + adaptive_factor * 10)))
        else:
            window = base_window
        if i < window or i >= len(data) - window:
            continue
        highs = data['high'].iloc[i-window:i+window+1]
        if data['high'].iloc[i] == highs.max():
            if (data['high'].iloc[i] > data['high'].iloc[i-1] and data['high'].iloc[i] > data['high'].iloc[i+1]):
                pivot_highs.append((i, data['high'].iloc[i]))
        lows = data['low'].iloc[i-window:i+window+1]
        if data['low'].iloc[i] == lows.min():
            if (data['low'].iloc[i] < data['low'].iloc[i-1] and data['low'].iloc[i] < data['low'].iloc[i+1]):
                pivot_lows.append((i, data['low'].iloc[i]))
    pivot_highs = _filter_close_pivots(pivot_highs, atr, data, min_distance_multiplier)
    pivot_lows = _filter_close_pivots(pivot_lows, atr, data, min_distance_multiplier)
    return pivot_highs, pivot_lows


def _filter_close_pivots(pivots, atr, data, min_distance_multiplier):
    if len(pivots) <= 1:
        return pivots
    filtered = []
    for i, (idx, price) in enumerate(pivots):
        if i == 0:
            filtered.append((idx, price))
            continue
        prev_idx, prev_price = filtered[-1]
        time_distance = idx - prev_idx
        current_atr = atr.iloc[idx] if pd.notna(atr.iloc[idx]) else data['high'].iloc[idx] * 0.01
        price_distance = abs(price - prev_price)
        min_price_distance = current_atr * min_distance_multiplier
        if time_distance >= 3 or price_distance >= min_price_distance:
            filtered.append((idx, price))
    return filtered


def validate_diamond_shape(points, pattern_type):
    if len(points) != 5:
        return False
    p1, p2, p3, p4, p5 = points
    if pattern_type == 'bottom':
        broadening = p3[1] > p1[1] and p2[1] < p1[1]
        contracting = p5[1] < p3[1] and p4[1] > p2[1]
        return broadening and contracting
    elif pattern_type == 'top':
        broadening = p3[1] < p1[1] and p2[1] > p1[1]
        contracting = p5[1] > p3[1] and p4[1] < p2[1]
        return broadening and contracting
    return False


def _simple_slope(points):
    if len(points) < 2:
        return 0
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    dx = x[-1] - x[0]
    dy = y[-1] - y[0]
    return dy / dx if dx != 0 else 0


def _trendline_consistency(points):
    if len(points) < 3:
        return 1.0
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    slope = _simple_slope(points)
    intercept = y[0] - slope * x[0]
    deviations = []
    for i in range(len(points)):
        expected = slope * x[i] + intercept
        deviations.append(abs(y[i] - expected))
    max_dev = max(deviations) if deviations else 0
    avg_price = float(np.mean(y)) if len(y) else 0
    if max_dev == 0 or avg_price == 0:
        return 1.0
    rel = max_dev / avg_price
    return max(0.0, 1 - rel * 10)


def validate_trendlines(points, pattern_type, min_consistency=0.6):
    if len(points) != 5:
        return False, {}
    if pattern_type == 'bottom':
        highs = [points[0], points[2], points[4]]
        lows = [points[1], points[3]]
    else:
        lows = [points[0], points[2], points[4]]
        highs = [points[1], points[3]]
    high_slope = _simple_slope(highs) if len(highs) >= 2 else 0
    low_slope = _simple_slope(lows) if len(lows) >= 2 else 0
    high_cons = _trendline_consistency(highs) if len(highs) >= 2 else 1.0
    low_cons = _trendline_consistency(lows) if len(lows) >= 2 else 1.0
    valid_conv = (high_slope < 0 and low_slope > 0)
    valid_cons = (high_cons >= min_consistency and low_cons >= min_consistency)
    return valid_conv and valid_cons, {
        'high_slope': high_slope,
        'low_slope': low_slope,
        'high_consistency': high_cons,
        'low_consistency': low_cons,
    }


def check_volume_confirmation(df, signal_idx, volume_period=20):
    if 'volume' not in df.columns:
        return True
    if signal_idx < volume_period:
        return True
    try:
        sma = df['volume'].iloc[signal_idx-volume_period:signal_idx].mean()
        cur = df['volume'].iloc[signal_idx]
        return cur > sma
    except Exception:
        return True


def find_diamond_signals(df, use_rsi_filter=False, rsi_oversold=30, rsi_overbought=70, rsi_column='rsi14',
                         use_volume_filter=True, use_trendline_validation=True, min_consistency=0.6,
                         max_pattern_length=72):
    signals = []
    pivot_highs, pivot_lows = find_enhanced_pivots(df)
    all_pivots = []
    for idx, price in pivot_highs:
        all_pivots.append((idx, price, 'high'))
    for idx, price in pivot_lows:
        all_pivots.append((idx, price, 'low'))
    all_pivots.sort(key=lambda x: x[0])
    for i in range(len(all_pivots) - 4):
        p1, p2, p3, p4, p5 = all_pivots[i:i+5]
        pattern_length = p5[0] - p1[0]
        if pattern_length > max_pattern_length:
            continue
        signal_idx = p5[0] + 1
        if signal_idx >= len(df):
            continue
        entry_price = df.iloc[signal_idx]['close']
        # Bottom (BUY)
        if (p1[2]=='high' and p2[2]=='low' and p3[2]=='high' and p4[2]=='low' and p5[2]=='high'):
            if not validate_diamond_shape([p1,p2,p3,p4,p5], 'bottom'):
                continue
            ok, stats = (True, {})
            if use_trendline_validation:
                ok, stats = validate_trendlines([p1,p2,p3,p4,p5], 'bottom', min_consistency)
                if not ok:
                    continue
            if use_volume_filter and not check_volume_confirmation(df, signal_idx):
                continue
            rsi_valid = True
            cur_rsi = None
            if use_rsi_filter:
                if rsi_column in df.columns:
                    cur_rsi = df.iloc[signal_idx][rsi_column]
                    rsi_valid = cur_rsi < rsi_oversold
            if rsi_valid:
                signals.append({
                    'type': 'Diamond Bottom',
                    'entry_idx': signal_idx,
                    'entry_time': df.iloc[signal_idx]['datetime'],
                    'entry_price': entry_price,
                    'direction': 'LONG',
                    'trendline_stats': stats,
                })
        # Top (SELL)
        elif (p1[2]=='low' and p2[2]=='high' and p3[2]=='low' and p4[2]=='high' and p5[2]=='low'):
            if not validate_diamond_shape([p1,p2,p3,p4,p5], 'top'):
                continue
            ok, stats = (True, {})
            if use_trendline_validation:
                ok, stats = validate_trendlines([p1,p2,p3,p4,p5], 'top', min_consistency)
                if not ok:
                    continue
            if use_volume_filter and not check_volume_confirmation(df, signal_idx):
                continue
            rsi_valid = True
            cur_rsi = None
            if use_rsi_filter:
                if rsi_column in df.columns:
                    cur_rsi = df.iloc[signal_idx][rsi_column]
                    rsi_valid = cur_rsi > rsi_overbought
            if rsi_valid:
                signals.append({
                    'type': 'Diamond Top',
                    'entry_idx': signal_idx,
                    'entry_time': df.iloc[signal_idx]['datetime'],
                    'entry_price': entry_price,
                    'direction': 'SHORT',
                    'trendline_stats': stats,
                })
    return signals


# ===== Evaluation helpers (same structure as butterfly) =====

def evaluate_signal_performance(df, signals, direction, horizon):
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
    symbol = "XRPUSDT"
    interval = "1h"

    print(f"Dang lay du lieu {symbol}...")
    df = get_binance_data(symbol, interval)
    if df.empty:
        print("Khong co du lieu. Kiem tra ket noi database.")
        return
    print(f"Da co {len(df)} nen du lieu\n")

    print("=== DIAMOND PREDICT ===")
    print("Tim Diamond Pattern...")
    signals = find_diamond_signals(df)
    if not signals:
        print("Khong tim thay Diamond Pattern.")
        return
    print(f"Tim thay {len(signals)} Diamond Pattern")

    current_index = len(df) - 1
    current_signal = None
    for s in reversed(signals):
        if s.get('entry_idx') == current_index:
            current_signal = s
            break

    if not current_signal:
        print("\nKhong co tin hieu moi -> Khong dua ra du doan.")
        for dir_label, dir_key in (("Bullish (LONG)", 'up'), ("Bearish (SHORT)", 'down')):
            print(f"\n{dir_label}:")
            for horizon in (9, 26):
                avg_correct_pct, acc, total, correct = evaluate_signal_performance_percent(
                    df, signals, dir_key, horizon
                )
                print(
                    f"   - Sau {horizon} phien: Do chinh xac {acc:.2f}% ({correct}/{total}), "
                    f"Trung binh thay doi khi dung: {avg_correct_pct:.4f}%"
                )
    else:
        sig_dir = current_signal.get('direction')
        print("\nCo tin hieu hien tai:")
        print(f"   Loai: {current_signal.get('type')} | Huong: {sig_dir} | Entry time: {current_signal.get('entry_time')}")
        print(f"   Entry price: ${current_signal.get('entry_price'):.4f}")
        last_close = df.iloc[-1]['close']
        for horizon in (9, 26):
            avg_change, acc, total, correct = evaluate_signal_performance(
                df, signals, 'up' if sig_dir == 'LONG' else 'down', horizon
            )
            predicted_price = last_close + avg_change if sig_dir == 'LONG' else last_close - abs(avg_change)
            change_pct = (predicted_price - last_close) / last_close * 100
            print(f"   -> Du doan sau {horizon} phien: ${predicted_price:.4f} ({change_pct:+.2f}%) | Do chinh xac lich su: {acc:.1f}% ({correct}/{total})")


if __name__ == "__main__":
    main()