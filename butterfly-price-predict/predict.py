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

    """
    print(f"📊 Lấy dữ liệu từ DB: {symbol} {interval}")
    if engine is None:
        print("❌ Chưa có kết nối DB hợp lệ.")
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

def is_within_tolerance(actual, expected, tolerance=0.15):
    """Check if actual value is within tolerance of expected Fibonacci ratio"""
    return abs(actual - expected) / expected <= tolerance

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

def predict_price_with_accuracy(df, signal_func=None, direction='up', lookback=LOOKBACK_PERIOD, precomputed_signals=None):
    """
    Dự đoán giá tiếp theo dựa trên chỉ báo với tỉ lệ chính xác cải tiến.
    
    Args:
        df: DataFrame chứa dữ liệu giá
        signal_func: Hàm kiểm tra tín hiệu (should_buy hoặc should_sell)
        direction: 'up' cho tín hiệu mua, 'down' cho tín hiệu bán
        lookback: Số nến lookback tối thiểu
    """
    if len(df) < lookback + 1:
        return None, 0, 0, 0

    direction = direction.lower()

    # Tối ưu: tiền xử lý danh sách tín hiệu để tra cứu O(1) theo entry_idx
    signals_list = precomputed_signals
    if signals_list is None:
        # Fallback: vẫn hỗ trợ gọi hàm, nhưng chi phí cao hơn
        signals_list = signal_func(df) if signal_func is not None else []

    signals_by_entry = {}
    for s in signals_list:
        idx = s.get('entry_idx')
        if idx is None:
            continue
        # Nếu có nhiều tín hiệu trùng entry_idx, ưu tiên tín hiệu cuối cùng (gần hiện tại hơn)
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
    symbol = "SOLUSDT"
    interval = "1h"

    print(f"Đang lấy dữ liệu {symbol}...")
    df = get_binance_data(symbol, interval)

    if df.empty:
        print("❌ Không có dữ liệu. Kiểm tra kết nối database.")
        return

    print(f"✅ Đã có {len(df)} nến dữ liệu\n")

    print("=== KHỞI ĐỘNG PHÂN TÍCH DỰ ĐOÁN GIÁ ===")

    print(f"Đang tìm Butterfly Pattern...")
    signals = find_butterfly_patterns(df)

    if not signals:
        print("❌ Không tìm thấy Butterfly Pattern.")
        return

    print(f"✅ Đã tìm thấy {len(signals)} Butterfly Pattern")

    print("\n=== PHÂN TÍCH TÍN HIỆU ===")
    
    # Dự đoán cho tín hiệu tăng (Bullish)
    bullish_pred_price, bullish_acc, bullish_total, bullish_correct = \
        predict_price_with_accuracy(df, direction='up', precomputed_signals=signals)

    # Dự đoán cho tín hiệu giảm (Bearish)
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