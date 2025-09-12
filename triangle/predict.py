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
    print(f"🔗 Kết nối DB: {DB_HOST}:{DB_PORT}/{DB_NAME}")
    engine = create_engine(DATABASE_URL)
    print("✅ Kết nối DB thành công")
except Exception as e:
    engine = None
    print(f"❌ Không tạo được kết nối DB: {e}")

# --- Hàm đọc data từ Database ---
def get_binance_data(symbol, interval):
    """
    Đọc dữ liệu từ database
    """
    print(f"📊 Lấy dữ liệu từ DB: {symbol} {interval}")
    if engine is None:
        print("❌ Chưa có kết nối DB hợp lệ.")
        return pd.DataFrame()

    table_name = "proddb.coin_prices_1h"

    query = f"""
        SELECT *
        FROM {table_name}
        WHERE symbol = %(symbol)s
          AND open_time >= EXTRACT(EPOCH FROM NOW()) - 90*24*3600 
          AND open_time <= EXTRACT(EPOCH FROM NOW())
        ORDER BY open_time ASC
    """

    try:
        print(f"🔍 Query {table_name}")
        df = pd.read_sql(
            query,
            con=engine,
            params={
                "symbol": symbol,
            },
        )

        if 'open_time' not in df.columns:
            print("❌ Thiếu cột 'open_time' trong dữ liệu trả về từ DB.")
            print(f"   Columns: {list(df.columns)}")
            return pd.DataFrame()

        required_cols = {'open', 'high', 'low', 'close'}
        if not required_cols.issubset(df.columns):
            print(f"❌ Thiếu cột cần thiết: {required_cols - set(df.columns)}")
            return pd.DataFrame()

        df['datetime'] = pd.to_datetime(df['open_time'], unit='s')
        df = df.sort_values('datetime').reset_index(drop=True)

        print(f"✅ Đã đọc {len(df)} dòng từ DB bảng {table_name}")
        if len(df) > 0:
            print(f"   Thời gian: {df['datetime'].min()} đến {df['datetime'].max()}")
            print(f"   Giá cuối: ${df.iloc[-1]['close']:.4f}")

        return df
    except Exception as e:
        print(f"❌ Lỗi khi đọc dữ liệu từ DB: {e}")
        return pd.DataFrame()

# --- Triangle Pattern Detection Functions ---

def calculate_atr(data, period=14):
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

def find_adaptive_pivots(data, base_window=3, atr_multiplier=2.0):
    """
    Find pivot with adaptive window size based on ATR
    """
    atr = calculate_atr(data)
    avg_price = (data['high'] + data['low'] + data['close']) / 3
    
    pivot_highs = []
    pivot_lows = []
    
    for i in range(len(data)):
        if i < 14 or i >= len(data) - base_window:  # 14 for ATR period
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

def is_horizontal_line(pivots, atr_values, indices, tolerance_mult=1.5):
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

def find_triangle_patterns(df, num_lows=3, num_highs=3, max_pattern_length=72, min_slope_threshold=0.001):
    """
    Tìm triangle pattern với các cải thiện:
    - ATR-based tolerance
    - Trendline slope validation
    - Pattern length control
    """
    signals = []
    
    pivot_highs, pivot_lows = find_adaptive_pivots(df)
    atr = calculate_atr(df)
    
    # Tam giác tăng: num_lows đáy cao dần + đỉnh ngang
    for i in range(len(pivot_lows) - (num_lows-1)):
        lows = pivot_lows[i:i+num_lows]
        
        # Kiểm tra pattern length
        pattern_length = lows[-1][0] - lows[0][0]
        if pattern_length > max_pattern_length:
            continue
        
        # Kiểm tra trendline slope của đáy
        slope = calculate_simple_slope(lows)
        if abs(slope) < min_slope_threshold or slope <= 0:  # Đáy phải tăng dần
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
                            'type': 'Ascending Triangle',
                            'entry_idx': breakout_idx,
                            'entry_time': df.iloc[breakout_idx]['datetime'],
                            'entry_price': entry_price,
                            'pattern_points': lows + highs_in_range,
                            'direction': 'LONG',
                            'slope': slope,
                            'pattern_length': pattern_length,
                            'resistance_level': resistance_level
                        })
    
    # Tam giác giảm: num_highs đỉnh thấp dần + đáy ngang
    for i in range(len(pivot_highs) - (num_highs-1)):
        highs = pivot_highs[i:i+num_highs]
        
        # Kiểm tra pattern length
        pattern_length = highs[-1][0] - highs[0][0]
        if pattern_length > max_pattern_length:
            continue
        
        # Kiểm tra trendline slope của đỉnh
        slope = calculate_simple_slope(highs)
        if abs(slope) < min_slope_threshold or slope >= 0:  # Đỉnh phải giảm dần
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
                            'type': 'Descending Triangle',
                            'entry_idx': breakout_idx,
                            'entry_time': df.iloc[breakout_idx]['datetime'],
                            'entry_price': entry_price,
                            'pattern_points': highs + lows_in_range,
                            'direction': 'SHORT',
                            'slope': slope,
                            'pattern_length': pattern_length,
                            'support_level': support_level
                        })
    
    return signals

def predict_price_with_accuracy(df, signal_func=None, direction='up', lookback=LOOKBACK_PERIOD, precomputed_signals=None):
    """
    Dự đoán giá tiếp theo dựa trên chỉ báo với tỉ lệ chính xác cải tiến.
    
    Args:
        df: DataFrame chứa dữ liệu giá
        signal_func: Hàm kiểm tra tín hiệu (không sử dụng cho triangle)
        direction: 'up' cho tín hiệu mua, 'down' cho tín hiệu bán
        lookback: Số nến lookback tối thiểu
        precomputed_signals: Danh sách tín hiệu đã tính sẵn
    """
    if len(df) < lookback + 1:
        return None, 0, 0, 0

    direction = direction.lower()

    # Sử dụng tín hiệu đã tính sẵn
    signals_list = precomputed_signals if precomputed_signals is not None else []

    signals_by_entry = {}
    for s in signals_list:
        idx = s.get('entry_idx')
        if idx is None:
            continue
        # Nếu có nhiều tín hiệu trùng entry_idx, ưu tiên tín hiệu cuối cùng
        signals_by_entry[idx] = s

    actual_changes = []  # only changes for signals matching desired direction
    price_changes_when_correct = []

    for i in range(lookback, len(df) - 1):  # -1 để còn nến tiếp theo để kiểm tra
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

    # Tính số lần đúng và tỉ lệ chính xác
    if direction == 'up':
        correct = sum(1 for chg in actual_changes if chg > 0)
    else:
        correct = sum(1 for chg in actual_changes if chg < 0)

    total_signals = len(actual_changes)
    accuracy = correct / total_signals * 100 if total_signals > 0 else 0

    # Giá dự đoán = trung bình các lần tăng/giảm thực sự (chỉ lấy các lần đúng)
    if price_changes_when_correct:
        avg_change = float(np.mean(price_changes_when_correct))
        last_price = df.iloc[-1]['close']
        predicted_price = last_price + avg_change if direction == 'up' else last_price - avg_change
    else:
        predicted_price = None

    return predicted_price, accuracy, total_signals, correct

def evaluate_signal_performance(df, signals, direction, horizon):
    """Đánh giá hiệu suất tín hiệu theo horizon (số phiên sau entry).

    Trả về: (avg_signed_change, accuracy_percent, total_samples, correct)
    - avg_signed_change: trung bình thay đổi giá sau horizon kể từ entry (có dấu)
    - accuracy: % số lần đúng hướng (tăng cho LONG, giảm cho SHORT)
    """
    if df.empty:
        return 0.0, 0.0, 0, 0

    direction = direction.lower()
    last_index = len(df) - 1

    # Lọc tín hiệu theo hướng và đủ dữ liệu để đánh giá
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
    """Đánh giá hiệu suất tín hiệu (theo %) sau horizon phiên.

    Trả về: (avg_correct_change_percent, accuracy_percent, total_samples, correct)
    - avg_correct_change_percent: trung bình % thay đổi khi DỰ ĐOÁN ĐÚNG
    - accuracy: % số lần đúng hướng
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
    symbol = "XRPUSDT"
    interval = "1h"

    print(f"Đang lấy dữ liệu {symbol}...")
    df = get_binance_data(symbol, interval)

    if df.empty:
        print("❌ Không có dữ liệu. Kiểm tra kết nối database.")
        return

    print(f"✅ Đã có {len(df)} nến dữ liệu\n")

    print("=== KHỞI ĐỘNG PHÂN TÍCH DỰ ĐOÁN GIÁ ===")

    print(f"Đang tìm Triangle Pattern...")
    signals = find_triangle_patterns(df)

    if not signals:
        print("❌ Không tìm thấy Triangle Pattern.")
        return

    print(f"✅ Đã tìm thấy {len(signals)} Triangle Pattern")

    print("\n=== PHÂN TÍCH TÍN HIỆU ===")
    
    # Dự đoán cho tín hiệu tăng (Ascending Triangle)
    bullish_pred_price, bullish_acc, bullish_total, bullish_correct = \
        predict_price_with_accuracy(df, direction='up', precomputed_signals=signals)

    # Dự đoán cho tín hiệu giảm (Descending Triangle)
    bearish_pred_price, bearish_acc, bearish_total, bearish_correct = \
        predict_price_with_accuracy(df, direction='down', precomputed_signals=signals)

    last_close = df.iloc[-1]['close'] if not df.empty else None

    # Xác định có tín hiệu hiện tại (tại nến kế tiếp entry_idx == len(df)-1)
    current_index = len(df) - 1
    current_signal = None
    if signals:
        # lấy tín hiệu có entry_idx == current_index
        for s in reversed(signals):
            if s.get('entry_idx') == current_index:
                current_signal = s
                break

    if not current_signal:
        print("\n⏳ Hiện tại KHÔNG có tín hiệu mới → Không đưa ra dự đoán.")
        # Hiển thị thống kê lịch sử theo ví dụ yêu cầu
        for dir_label, dir_key in (("Bullish (LONG)", 'up'), ("Bearish (SHORT)", 'down')):
            print(f"\n🔹 {dir_label}:")
            for horizon in (9, 26):
                avg_correct_pct, acc, total, correct = evaluate_signal_performance_percent(
                    df, signals, dir_key, horizon
                )
                print(
                    f"   - Sau {horizon} phiên: Độ chính xác {acc:.2f}% ({correct}/{total}), "
                    f"Trung bình thay đổi khi đúng: {avg_correct_pct:.4f}%"
                )
    else:
        sig_dir = current_signal.get('direction')
        print("\n✅ Có tín hiệu hiện tại:")
        print(f"   Loại: {current_signal.get('type')} | Hướng: {sig_dir} | Entry time: {current_signal.get('entry_time')}")
        print(f"   Entry price: ${current_signal.get('entry_price'):.4f}")

        # Đánh giá lịch sử theo horizon 9 và 26 phiên
        for horizon in (9, 26):
            avg_change, acc, total, correct = evaluate_signal_performance(
                df, signals, 'up' if sig_dir == 'LONG' else 'down', horizon
            )
            if last_close is not None:
                predicted_price = last_close + avg_change if sig_dir == 'LONG' else last_close - abs(avg_change)
                change_pct = (predicted_price - last_close) / last_close * 100
                print(f"   ▶ Dự đoán sau {horizon} phiên: ${predicted_price:.4f} ({change_pct:+.2f}%) | Độ chính xác lịch sử: {acc:.1f}% ({correct}/{total})")

if __name__ == "__main__":
    main()
