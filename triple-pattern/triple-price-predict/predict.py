import os
import pandas as pd
import numpy as np
import argparse
from dotenv import load_dotenv
from sqlalchemy import create_engine
from datetime import datetime, timedelta

# Import candlestick detection functions
from rsi14_candlestick_confluence import (
    detect_bullish_engulfing, detect_hammer, detect_bullish_doji,
    detect_bearish_engulfing, detect_shooting_star, detect_bearish_doji
)

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

LOOKBACK_PERIOD = 40
PRICE_THRESHOLD = 0.05


try:
    print(f"🔗 Kết nối DB: {DB_HOST}:{DB_PORT}/{DB_NAME}")
    engine = create_engine(DATABASE_URL)
    print("✅ Kết nối DB thành công")
except Exception as e:
    engine = None
    print(f"❌ Không tạo được kết nối DB: {e}")

def get_binance_data(symbol, interval):
    if engine is None:
        print("Chưa có kết nối DB hợp lệ.")
        return pd.DataFrame()

    print(f"📊 Lấy dữ liệu từ DB: {symbol} {interval}")
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
            print("Thiếu cột 'open_time' trong dữ liệu trả về từ DB.")
            return pd.DataFrame()
        
        df['datetime'] = pd.to_datetime(df['open_time'], unit='s')
        
        df = df.sort_values('datetime').reset_index(drop=True)
        print(f"✅ Đã đọc {len(df)} dòng từ DB bảng {table_name}")
        if len(df) > 0:
            print(f"   Thời gian: {df['datetime'].min()} đến {df['datetime'].max()}")
            print(f"   Giá cuối: ${df.iloc[-1]['close']:.4f}")
        
        return df
    except Exception as e:
        print(f"Lỗi khi đọc dữ liệu từ DB: {e}")
        return pd.DataFrame()

def detect_triple_top(df, lookback_period=LOOKBACK_PERIOD, price_threshold=PRICE_THRESHOLD):
    """Detect triple top pattern - causal version (no future data)"""
    if len(df) < lookback_period:
        return False, None, None
    
    # Chỉ sử dụng dữ liệu quá khứ, không bao gồm nến hiện tại
    window = df.iloc[-lookback_period:-1] if len(df) > lookback_period else df.iloc[:-1]
    highs = window['high']
    
    if highs.empty:
        return False, None, None
    
    peaks_idx = highs.nlargest(3).index.tolist()
    if len(peaks_idx) < 3:
        return False, None, None
    
    # Sắp xếp theo thời gian
    peaks = sorted([(i, window.loc[i]) for i in peaks_idx], key=lambda x: x[0])
    idx1, p1 = peaks[0]
    idx2, p2 = peaks[1] 
    idx3, p3 = peaks[2]
    
    max_high = max(p1['high'], p2['high'], p3['high'])
    min_high = min(p1['high'], p2['high'], p3['high'])
    
    if (max_high - min_high) / max_high > price_threshold:
        return False, None, None
        
    left = min(idx1, idx2, idx3)
    right = max(idx1, idx2, idx3)
    trough_data = window.loc[left:right]
    
    if trough_data.empty or 'low' not in trough_data:
        return False, None, None
    
    support_level = trough_data['low'].min()
    resistance_level = np.mean([p1['high'], p2['high'], p3['high']])
    
    return True, support_level, resistance_level

def detect_triple_bottom(df, lookback_period=LOOKBACK_PERIOD, price_threshold=PRICE_THRESHOLD):
    """Detect triple bottom pattern - causal version (no future data)"""
    if len(df) < lookback_period:
        return False, None, None
    
    # Chỉ sử dụng dữ liệu quá khứ, không bao gồm nến hiện tại
    window = df.iloc[-lookback_period:-1] if len(df) > lookback_period else df.iloc[:-1]
    lows = window['low']
    
    if lows.empty:
        return False, None, None
    
    troughs_idx = lows.nsmallest(3).index.tolist()
    if len(troughs_idx) < 3:
        return False, None, None
    
    troughs = sorted([(i, window.loc[i]) for i in troughs_idx], key=lambda x: x[0])
    idx1, t1 = troughs[0]
    idx2, t2 = troughs[1]
    idx3, t3 = troughs[2]
    
    max_low = max(t1['low'], t2['low'], t3['low'])
    min_low = min(t1['low'], t2['low'], t3['low'])
    
    if (max_low - min_low) / max_low > price_threshold:
        return False, None, None
    
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
    """Kiểm tra điều kiện mua - Triple bottom breakdown với nến đảo chiều tăng"""
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

    # INSERT_YOUR_CODE

def predict_price_with_accuracy(df, signal_func=None, direction='up', lookback=LOOKBACK_PERIOD, precomputed_signals=None):
    """
    Dự đoán giá tiếp theo dựa trên chỉ báo với tỉ lệ chính xác (chuẩn hoá theo butterfly).
    """
    if len(df) < lookback + 1:
        return None, 0, 0, 0

    direction = direction.lower()

    # Tối ưu: tiền xử lý danh sách tín hiệu để tra cứu O(1) theo entry_idx
    signals_list = precomputed_signals
    if signals_list is None:
        # Fallback: vẫn hỗ trợ gọi hàm, nhưng chi phí cao hơn
        signals_list = []
        if signal_func is not None:
            for i in range(lookback, len(df) - 1):
                window = df.iloc[:i+1]
                has_signal, _, _ = signal_func(window)
                if has_signal:
                    signals_list.append({
                        'entry_idx': i + 1,
                        'entry_time': df.iloc[i+1]['datetime'] if 'datetime' in df.columns else i+1,
                        'entry_price': df.iloc[i+1]['close'],
                        'direction': 'LONG' if direction == 'up' else 'SHORT'
                    })

    signals_by_entry = {}
    for s in signals_list:
        idx = s.get('entry_idx')
        if idx is None:
            continue
        signals_by_entry[idx] = s

    actual_changes = []
    price_changes_when_correct = []

    for i in range(lookback, len(df) - 1):
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

    if direction == 'up':
        correct = sum(1 for chg in actual_changes if chg > 0)
    else:
        correct = sum(1 for chg in actual_changes if chg < 0)

    total_signals = len(actual_changes)
    accuracy = correct / total_signals * 100 if total_signals > 0 else 0

    if price_changes_when_correct:
        avg_change = float(np.mean(price_changes_when_correct))
        last_price = df.iloc[-1]['close']
        predicted_price = last_price + avg_change if direction == 'up' else last_price - avg_change
    else:
        predicted_price = None

    return predicted_price, accuracy, total_signals, correct

def predict_triple_bottom_v2(df):
    """
    Dự đoán giá khi gặp triple bottom breakout - phiên bản cải tiến.
    """
    return predict_price_with_accuracy(df, should_buy, direction='up')

def predict_triple_top_v2(df):
    """
    Dự đoán giá khi gặp triple top breakdown - phiên bản cải tiến.
    """
    return predict_price_with_accuracy(df, should_sell, direction='down')

def analyze_signal_performance(df, signal_func, signal_name, direction='up', lookback=LOOKBACK_PERIOD):
    """
    Phân tích chi tiết hiệu suất của một tín hiệu.
    
    Returns:
        dict: Thống kê chi tiết về hiệu suất
    """
    if len(df) < lookback + 1:
        return {"error": "Không đủ dữ liệu"}

    results = []
    
    for i in range(lookback, len(df) - 1):
        window = df.iloc[:i+1]
        has_signal, signal_price, pattern_type = signal_func(window)
        
        if has_signal:
            current_time = df.iloc[i]['datetime'] if 'datetime' in df.columns else i
            current_close = df.iloc[i]['close']
            next_close = df.iloc[i+1]['close']
            change_percent = (next_close - current_close) / current_close * 100
            
            is_correct = (direction == 'up' and change_percent > 0) or \
                        (direction == 'down' and change_percent < 0)
            
            results.append({
                'time': current_time,
                'current_price': current_close,
                'next_price': next_close,
                'change_percent': change_percent,
                'is_correct': is_correct,
                'pattern_type': pattern_type
            })
    
    if not results:
        return {"error": "Không tìm thấy tín hiệu nào"}
    
    # Tính toán thống kê
    total_signals = len(results)
    correct_signals = sum(1 for r in results if r['is_correct'])
    accuracy = correct_signals / total_signals * 100
    
    all_changes = [r['change_percent'] for r in results]
    correct_changes = [r['change_percent'] for r in results if r['is_correct']]
    wrong_changes = [r['change_percent'] for r in results if not r['is_correct']]
    
    stats = {
        'signal_name': signal_name,
        'direction': direction,
        'total_signals': total_signals,
        'correct_signals': correct_signals,
        'wrong_signals': total_signals - correct_signals,
        'accuracy_percent': round(accuracy, 2),
        'avg_all_change': round(sum(all_changes) / len(all_changes), 4) if all_changes else 0,
        'avg_correct_change': round(sum(correct_changes) / len(correct_changes), 4) if correct_changes else 0,
        'avg_wrong_change': round(sum(wrong_changes) / len(wrong_changes), 4) if wrong_changes else 0,
        'max_gain': round(max(all_changes), 4) if all_changes else 0,
        'max_loss': round(min(all_changes), 4) if all_changes else 0,
        'details': results
    }
    
    return stats

def comprehensive_prediction_analysis(df):
    """
    Phân tích tổng hợp cả hai loại tín hiệu.
    """
    print("=== PHÂN TÍCH DỰ ĐOÁN GIÁ TOÀN DIỆN ===\n")
    
    # Phân tích Triple Bottom (tín hiệu mua)
    print("📈 TRIPLE BOTTOM BREAKOUT (Tín hiệu MUA):")
    predicted_price, accuracy, total, correct = predict_triple_bottom_v2(df)
    
    if predicted_price:
        current_price = df.iloc[-1]['close']
        potential_gain = (predicted_price - current_price) / current_price * 100
        print(f"   Giá hiện tại: ${current_price:.4f}")
        print(f"   Giá dự đoán: ${predicted_price:.4f}")
        print(f"   Tiềm năng tăng: {potential_gain:+.2f}%")
        print(f"   Tỉ lệ chính xác: {accuracy:.1f}% ({correct}/{total})")
    else:
        print("   Không đủ dữ liệu lịch sử")
    
    # Phân tích Triple Top (tín hiệu bán)
    print("\n📉 TRIPLE TOP BREAKDOWN (Tín hiệu BÁN):")
    predicted_price, accuracy, total, correct = predict_triple_top_v2(df)
    
    if predicted_price:
        current_price = df.iloc[-1]['close']
        potential_loss = (predicted_price - current_price) / current_price * 100
        print(f"   Giá hiện tại: ${current_price:.4f}")
        print(f"   Giá dự đoán: ${predicted_price:.4f}")
        print(f"   Tiềm năng giảm: {potential_loss:+.2f}%")
        print(f"   Tỉ lệ chính xác: {accuracy:.1f}% ({correct}/{total})")
    else:
        print("   Không đủ dữ liệu lịch sử")
    
    # Kiểm tra tín hiệu hiện tại
    print("\n🔍 TÍNH HIỆU HIỆN TẠI:")
    buy_signal, buy_price, buy_pattern = should_buy(df)
    sell_signal, sell_price, sell_pattern = should_sell(df)
    
    if buy_signal:
        print(f"   ✅ Có tín hiệu MUA: {buy_pattern} tại ${buy_price:.4f}")
    if sell_signal:
        print(f"   ✅ Có tín hiệu BÁN: {sell_pattern} tại ${sell_price:.4f}")
    if not buy_signal and not sell_signal:
        print("   ⏳ Không có tín hiệu")

# ===================== Chuẩn hoá đầu ra giống butterfly =====================
def precompute_candle_flags(df):
    """Tính sẵn cờ nến đảo chiều cho toàn bộ dataframe một lần."""
    flags = {
        'is_hammer': detect_hammer(df).astype(bool).values,
        'is_bullish_engulfing': detect_bullish_engulfing(df).astype(bool).values,
        'is_bullish_doji': detect_bullish_doji(df).astype(bool).values,
        'is_shooting_star': detect_shooting_star(df).astype(bool).values,
        'is_bearish_engulfing': detect_bearish_engulfing(df).astype(bool).values,
        'is_bearish_doji': detect_bearish_doji(df).astype(bool).values,
    }
    return flags

def is_bullish_reversal_at_index(flags, i):
    return bool(
        flags['is_hammer'][i] or flags['is_bullish_engulfing'][i] or flags['is_bullish_doji'][i]
    )

def is_bearish_reversal_at_index(flags, i):
    return bool(
        flags['is_shooting_star'][i] or flags['is_bearish_engulfing'][i] or flags['is_bearish_doji'][i]
    )
def find_triple_signals(df, lookback=LOOKBACK_PERIOD):
    """Chuẩn hoá danh sách tín hiệu theo định dạng butterfly (tối ưu hiệu năng)."""
    signals = []
    if len(df) < lookback + 1:
        return signals

    flags = precompute_candle_flags(df)
    n = len(df)
    for i in range(lookback, n - 1):
        # Log tiến trình để không bị hiểu nhầm là treo
        if (i - lookback) % 300 == 0 and i > lookback:
            print(f"   ... quét tín hiệu: {i}/{n-1}")

        window = df.iloc[:i+1]
        try:
            # Triple Bottom breakout + bullish reversal tại i
            has_bottom, _, resistance = detect_triple_bottom(window)
            if has_bottom:
                current_close = df.iloc[i]['close']
                if resistance is not None and current_close > resistance and is_bullish_reversal_at_index(flags, i):
                    signals.append({
                        'type': 'Triple Bottom Breakout',
                        'entry_idx': i + 1,
                        'entry_time': df.iloc[i+1]['datetime'] if 'datetime' in df.columns else i+1,
                        'entry_price': df.iloc[i+1]['close'],
                        'direction': 'LONG'
                    })
        except Exception:
            pass

        try:
            # Triple Top breakdown + bearish reversal tại i
            has_top, support, _ = detect_triple_top(window)
            if has_top:
                current_close = df.iloc[i]['close']
                if support is not None and current_close < support and is_bearish_reversal_at_index(flags, i):
                    signals.append({
                        'type': 'Triple Top Breakdown',
                        'entry_idx': i + 1,
                        'entry_time': df.iloc[i+1]['datetime'] if 'datetime' in df.columns else i+1,
                        'entry_price': df.iloc[i+1]['close'],
                        'direction': 'SHORT'
                    })
        except Exception:
            pass
    return signals

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
    print("=== KHỞI ĐỘNG PHÂN TÍCH DỰ ĐOÁN GIÁ ===")

    symbol = "BTCUSDT"
    interval = "1h"

    print(f"Đang lấy dữ liệu {symbol}...")
    df = get_binance_data(symbol, interval)

    if df.empty:
        print("❌ Không có dữ liệu. Kiểm tra kết nối database.")
        return

    print(f"✅ Đã có {len(df)} nến dữ liệu")

    print("=== KHỞI ĐỘNG PHÂN TÍCH DỰ ĐOÁN GIÁ ===")

    print(f"Đang tìm Triple Pattern...")
    signals = find_triple_signals(df)

    if not signals:
        print("❌ Không tìm thấy Triple Pattern.")
        return

    print(f"✅ Đã tìm thấy {len(signals)} Triple Pattern")

    print("\n=== PHÂN TÍCH TÍN HIỆU ===")

    bullish_pred_price, bullish_acc, bullish_total, bullish_correct = \
        predict_price_with_accuracy(df, direction='up', precomputed_signals=signals)

    bearish_pred_price, bearish_acc, bearish_total, bearish_correct = \
        predict_price_with_accuracy(df, direction='down', precomputed_signals=signals)

    last_close = df.iloc[-1]['close'] if not df.empty else None

    current_index = len(df) - 1
    current_signal = None
    if signals:
        for s in reversed(signals):
            if s.get('entry_idx') == current_index:
                current_signal = s
                break

    if not current_signal:
        print("\n⏳ Hiện tại KHÔNG có tín hiệu mới → Không đưa ra dự đoán.")
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

        for horizon in (9, 26):
            avg_change, acc, total, correct = evaluate_signal_performance(
                df, signals, 'up' if sig_dir == 'LONG' else 'down', horizon
            )
            if last_close is not None:
                predicted_price = last_close + avg_change if sig_dir == 'LONG' else last_close - abs(avg_change)
                change_pct = (predicted_price - last_close) / last_close * 100
                print(f"   ▶ Dự đoán sau {horizon} phiên: ${predicted_price:.4f} ({change_pct:+.2f}%) | Độ chính xác lịch sử: {acc:.1f}% ({correct}/{total})")

if __name__ == "__main__":
    try:
        # Chạy phân tích cơ bản
        main()
        
        # Uncomment dòng dưới để test nhiều symbol
        # test_with_multiple_symbols()
        
    except KeyboardInterrupt:
        print("\n⏹️ Đã dừng bởi người dùng")
    except Exception as e:
        print(f"❌ Lỗi không mong đợi: {e}")
        print("💡 Kiểm tra:")
        print("   - File .env có đúng thông tin database?")
        print("   - Database có chạy không?")
        print("   - Có file rsi14_candlestick_confluence.py không?")