import os
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime
from sqlalchemy import create_engine

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

SYMBOL = "BTCUSDT"


INITIAL_BALANCE = 10000    # Số dư ban đầu ($) 
TRADE_AMOUNT = 1000        # Số tiền đầu tư mỗi lần ($) 


# CHIẾN THUẬT EXIT (CÓ THỂ THAY ĐỔI)
TP_PERCENT = 4           # Take Profit % 
SL_PERCENT = 1.5           # Stop Loss % 
MAX_HOLD_HOURS = 24      # Thời gian giữ tối đa (giờ) 
USE_TRAILING_STOP = False  # Sử dụng trailing stop 
TRAILING_PERCENT = 2.5     # Trailing stop % 


# BỘ LỌC RSI (CÓ THỂ THAY ĐỔI)
USE_RSI_FILTER = False     # Sử dụng bộ lọc RSI
RSI_OVERSOLD = 35          # RSI oversold level 
RSI_OVERBOUGHT = 65       # RSI overbought level 
RSI_COLUMN = 'rsi7'       # Cột RSI trong data 


query = f"""
SELECT * FROM proddb.f_coin_signal_1h 
WHERE symbol = '{SYMBOL}' 
AND open_time >= UNIX_TIMESTAMP('2025-05-01 00:00:00')  
AND open_time < UNIX_TIMESTAMP('2025-07-01 00:00:00')   
ORDER BY open_time ASC;
"""

# print(query)
df = pd.read_sql_query(query, engine)

df['datetime'] = pd.to_datetime(df['open_time'], unit='s')
df = df.sort_values('open_time').reset_index(drop=True)

print(f"Dữ liệu từ {df['datetime'].min()} đến {df['datetime'].max()}")
print(f"Tổng số candle: {len(df)}")

# Hàm tìm pivot points (đỉnh và đáy)
def find_pivots(data, window=5):
    """
    Tìm pivot points với window size
    """
    highs = data['high'].values
    lows = data['low'].values
    pivot_highs = []
    pivot_lows = []
    
    for i in range(window, len(data) - window):
        # Pivot High: giá cao nhất trong window
        if all(highs[i] >= highs[j] for j in range(i-window, i+window+1) if j != i):
            pivot_highs.append((i, highs[i]))
            
        # Pivot Low: giá thấp nhất trong window  
        if all(lows[i] <= lows[j] for j in range(i-window, i+window+1) if j != i):
            pivot_lows.append((i, lows[i]))
    
    return pivot_highs, pivot_lows

# Hàm tìm diamond pattern (nâng cấp với cả BUY và SELL + RSI filter)
def find_diamond_patterns(df, pivot_highs, pivot_lows, max_pattern_length=72,
                         use_rsi_filter=False, rsi_oversold=30, rsi_overbought=70, rsi_column='rsi14'):
    """
    Tìm diamond pattern signals (cả BUY và SELL) với bộ lọc RSI
    
    Diamond Bottom (BUY signal): H-L-H-L-H pattern
    - H2 > H1, L2 > L1, H3 < H2, H3 > H1
    - RSI Filter: RSI < oversold level (nếu bật)
    
    Diamond Top (SELL signal): L-H-L-H-L pattern  
    - L2 < L1, H2 < H1, L3 > L2, L3 < L1
    - RSI Filter: RSI > overbought level (nếu bật)
    """
    signals = []
    
    # Combine và sort tất cả pivots
    all_pivots = []
    for idx, price in pivot_highs:
        all_pivots.append((idx, price, 'high'))
    for idx, price in pivot_lows:
        all_pivots.append((idx, price, 'low'))
    
    all_pivots.sort(key=lambda x: x[0])
    
    # Tìm pattern với 5 pivot points
    for i in range(len(all_pivots) - 4):
        p1, p2, p3, p4, p5 = all_pivots[i:i+5]
        
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
            
            # Kiểm tra điều kiện Diamond Bottom
            if (p3[1] > p1[1] and     # High2 > High1
                p4[1] > p2[1] and     # Low2 > Low1  
                p5[1] < p3[1] and     # High3 < High2
                p5[1] > p1[1]):       # High3 > High1
                
                # Kiểm tra bộ lọc RSI cho BUY signal
                rsi_valid = True
                current_rsi = None
                if use_rsi_filter:
                    current_rsi = df.iloc[signal_idx][rsi_column]
                    rsi_valid = current_rsi < rsi_oversold  # RSI oversold
                
                if rsi_valid:
                    signals.append({
                        'signal_type': 'BUY',
                        'signal_idx': signal_idx,
                        'datetime': df.iloc[signal_idx]['datetime'],
                        'entry_price': entry_price,
                        'pattern_points': [p1, p2, p3, p4, p5],
                        'pattern_length': pattern_length,
                        'pattern_name': 'Diamond Bottom',
                        'rsi_value': current_rsi
                    })
        
        # DIAMOND TOP (SELL Signal): L-H-L-H-L  
        elif (p1[2] == 'low' and p2[2] == 'high' and p3[2] == 'low' and 
              p4[2] == 'high' and p5[2] == 'low'):
            
            # Kiểm tra điều kiện Diamond Top
            if (p3[1] < p1[1] and     # Low2 < Low1
                p4[1] < p2[1] and     # High2 < High1
                p5[1] > p3[1] and     # Low3 > Low2
                p5[1] < p1[1]):       # Low3 < Low1
                
                # Kiểm tra bộ lọc RSI cho SELL signal
                rsi_valid = True
                current_rsi = None
                if use_rsi_filter:
                    current_rsi = df.iloc[signal_idx][rsi_column]
                    rsi_valid = current_rsi > rsi_overbought  # RSI overbought
                
                if rsi_valid:
                    signals.append({
                        'signal_type': 'SELL',
                        'signal_idx': signal_idx,
                        'datetime': df.iloc[signal_idx]['datetime'],
                        'entry_price': entry_price,
                        'pattern_points': [p1, p2, p3, p4, p5],
                        'pattern_length': pattern_length,
                        'pattern_name': 'Diamond Top',
                        'rsi_value': current_rsi
                    })
    
    return signals

# Hàm tính toán kết quả back test (hỗ trợ cả BUY và SELL với quản lý tài khoản)
def calculate_backtest_results(df, signals, tp_percent=TP_PERCENT, sl_percent=SL_PERCENT, max_hold_bars=MAX_HOLD_HOURS, 
                             initial_balance=INITIAL_BALANCE, trade_amount=TRADE_AMOUNT, 
                             use_trailing_stop=USE_TRAILING_STOP, trailing_percent=TRAILING_PERCENT):
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
            print(f"⚠️  Không đủ tiền để giao dịch tại {signal['datetime']} (Balance: ${current_balance:.2f})")
            continue
            
        signal_idx = signal['signal_idx']
        entry_price = signal['entry_price']
        signal_type = signal['signal_type']
        
        # Tính số lượng coin có thể mua/bán
        coin_quantity = trade_amount / entry_price
        
        # Tính target prices theo hướng
        if signal_type == 'BUY':
            tp_price = entry_price * (1 + tp_percent/100)
            initial_sl_price = entry_price * (1 - sl_percent/100)
        else:  # SELL
            tp_price = entry_price * (1 - tp_percent/100)  # TP thấp hơn entry
            initial_sl_price = entry_price * (1 + sl_percent/100)  # SL cao hơn entry
        
        # Khởi tạo trailing stop
        current_sl_price = initial_sl_price
        best_price = entry_price  # Giá tốt nhất đã đạt được
        
        # Tìm exit point
        exit_idx = None
        exit_price = None
        exit_reason = None
        
        for i in range(signal_idx + 1, min(signal_idx + max_hold_bars, len(df))):
            current_high = df.iloc[i]['high']
            current_low = df.iloc[i]['low']
            current_close = df.iloc[i]['close']
            
            if signal_type == 'BUY':
                # Cập nhật best price và trailing stop cho BUY
                if current_high > best_price:
                    best_price = current_high
                    if use_trailing_stop:
                        # Dịch chuyển SL lên theo giá tốt nhất
                        new_sl = best_price * (1 - trailing_percent/100)
                        current_sl_price = max(current_sl_price, new_sl)
                
                # Check exit conditions cho BUY
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
                # Cập nhật best price và trailing stop cho SELL
                if current_low < best_price:
                    best_price = current_low
                    if use_trailing_stop:
                        # Dịch chuyển SL xuống theo giá tốt nhất
                        new_sl = best_price * (1 + trailing_percent/100)
                        current_sl_price = min(current_sl_price, new_sl)
                
                # Check exit conditions cho SELL
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
        
        # Nếu không hit TP/SL, exit ở max hold
        if exit_idx is None and signal_idx + max_hold_bars < len(df):
            exit_idx = signal_idx + max_hold_bars
            exit_price = df.iloc[exit_idx]['close']
            exit_reason = 'Time'
        
        if exit_idx is not None:
            # Tính PnL theo hướng
            if signal_type == 'BUY':
                pnl_percent = ((exit_price - entry_price) / entry_price) * 100
                pnl_dollar = coin_quantity * (exit_price - entry_price)
            else:  # SELL
                pnl_percent = ((entry_price - exit_price) / entry_price) * 100
                pnl_dollar = coin_quantity * (entry_price - exit_price)
            
            # Cập nhật số dư tài khoản
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

# Hàm xuất báo cáo ra file
def export_backtest_report(signals, results, final_balance, filename=None):
    """
    Xuất báo cáo back test ra file markdown
    """
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"diamond_pattern_backtest_{timestamp}.md"
    
    # Thống kê cơ bản
    buy_signals = [s for s in signals if s['signal_type'] == 'BUY']
    sell_signals = [s for s in signals if s['signal_type'] == 'SELL']
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# 💎 DIAMOND PATTERN BACKTEST REPORT\n\n")
        f.write(f"**Thời gian tạo báo cáo:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## ⚙️ CÀI ĐẶT CHIẾN THUẬT\n\n")
        f.write(f"- **Symbol:** {SYMBOL}\n")
        f.write(f"- **Số dư ban đầu:** ${INITIAL_BALANCE:,.2f}\n")
        f.write(f"- **Số tiền mỗi lần giao dịch:** ${TRADE_AMOUNT:,.2f}\n")
        f.write(f"- **Take Profit:** {TP_PERCENT}%\n")
        f.write(f"- **Stop Loss:** {SL_PERCENT}%\n")
        f.write(f"- **Max Hold Time:** {MAX_HOLD_HOURS} giờ\n")
        f.write(f"- **Trailing Stop:** {'BẬT' if USE_TRAILING_STOP else 'TẮT'}\n")
        f.write(f"- **RSI Filter:** {'BẬT' if USE_RSI_FILTER else 'TẮT'}\n")
        
        if USE_RSI_FILTER:
            f.write(f"  - RSI Column: {RSI_COLUMN}\n")
            f.write(f"  - BUY khi RSI < {RSI_OVERSOLD}\n")
            f.write(f"  - SELL khi RSI > {RSI_OVERBOUGHT}\n")
        f.write("\n")
        
        if len(results) > 0:
            # Tính toán metrics
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
            
            f.write("## 📊 KẾT QUẢ TỔNG QUAN\n\n")
            f.write(f"- **Tổng số tín hiệu:** {total_signals}\n")
            f.write(f"- **Diamond Bottom (BUY):** {len(buy_signals)} signals\n")
            f.write(f"- **Diamond Top (SELL):** {len(sell_signals)} signals\n")
            f.write(f"- **Win Rate:** {win_rate:.2f}%\n")
            f.write(f"- **Số dư cuối kỳ:** ${final_balance:,.2f}\n")
            f.write(f"- **Tổng lợi nhuận:** ${total_pnl_dollar:+,.2f}\n")
            f.write(f"- **ROI:** {total_roi:+.2f}%\n")
            f.write(f"- **Profit Factor:** {profit_factor:.2f}\n\n")
            
            # Phân tích theo pattern type
            if len(buy_signals) > 0:
                buy_results = [r for r in results if r['signal_type'] == 'BUY']
                buy_win_rate = (sum(1 for r in buy_results if r['is_win']) / len(buy_results)) * 100
                buy_pnl_dollar = sum(r['pnl_dollar'] for r in buy_results)
                
                f.write("### 📈 Diamond Bottom (BUY) Analysis\n\n")
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
                
                f.write("### 📉 Diamond Top (SELL) Analysis\n\n")
                f.write(f"- **Signals:** {len(sell_signals)}\n")
                f.write(f"- **Win Rate:** {sell_win_rate:.1f}%\n")
                f.write(f"- **PnL:** ${sell_pnl_dollar:+,.2f}\n")
                
                if USE_RSI_FILTER:
                    sell_rsi = [s['rsi_value'] for s in sell_signals if s['rsi_value'] is not None]
                    if sell_rsi:
                        f.write(f"- **RSI Values:** {[f'{rsi:.1f}' for rsi in sell_rsi]}\n")
                f.write("\n")
            
            # Chi tiết giao dịch
            f.write("## 📋 CHI TIẾT GIAO DỊCH\n\n")
            if USE_RSI_FILTER:
                f.write("| STT | Thời gian | Type | Pattern | RSI | Entry | Exit | PnL ($) | PnL (%) | Balance | Exit |\n")
                f.write("|-----|-----------|------|---------|-----|-------|------|---------|---------|---------|------|\n")
            else:
                f.write("| STT | Thời gian | Type | Pattern | Entry | Exit | PnL ($) | PnL (%) | Balance | Exit |\n")
                f.write("|-----|-----------|------|---------|-------|------|---------|---------|---------|------|\n")
            
            for i, result in enumerate(results):
                signal_type = result['signal_type']
                pattern_name = result['pattern_name']
                
                if USE_RSI_FILTER:
                    # Tìm RSI value từ signals
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
            f.write("## ❌ KẾT QUẢ\n\n")
            f.write("Không tìm thấy diamond pattern nào phù hợp với điều kiện lọc.\n\n")
        
        f.write("---\n")
        f.write(f"*Báo cáo được tạo tự động bởi Diamond Pattern Backtest System*\n")
    
    return filename

# Tìm pivot points
pivot_highs, pivot_lows = find_pivots(df, window=3)

# Tìm diamond pattern signals với độ dài tối đa 72 candle (3 ngày) + RSI filter
signals = find_diamond_patterns(df, pivot_highs, pivot_lows, max_pattern_length=72,
                               use_rsi_filter=USE_RSI_FILTER, 
                               rsi_oversold=RSI_OVERSOLD,
                               rsi_overbought=RSI_OVERBOUGHT,
                               rsi_column=RSI_COLUMN)

print(f"💰 CÀI ĐẶT TÀI KHOẢN:")
print(f"  - Số dư ban đầu: ${INITIAL_BALANCE:,.2f}")
print(f"  - Số tiền mỗi lần giao dịch: ${TRADE_AMOUNT:,.2f}")

print(f"\n🎯 CHIẾN THUẬT EXIT:")
print(f"  - Take Profit: {TP_PERCENT}%")
print(f"  - Stop Loss: {SL_PERCENT}%") 
print(f"  - Max Hold Time: {MAX_HOLD_HOURS} giờ")
print(f"  - Trailing Stop: {'BẬT' if USE_TRAILING_STOP else 'TẮT'}")

print(f"\n📊 BỘ LỌC RSI:")
print(f"  - RSI Filter: {'BẬT' if USE_RSI_FILTER else 'TẮT'}")
if USE_RSI_FILTER:
    print(f"  - RSI Column: {RSI_COLUMN}")
    print(f"  - BUY khi RSI < {RSI_OVERSOLD} (oversold)")
    print(f"  - SELL khi RSI > {RSI_OVERBOUGHT} (overbought)")
print()

if len(signals) > 0:
    # Thống kê theo loại signal
    buy_signals = [s for s in signals if s['signal_type'] == 'BUY']
    sell_signals = [s for s in signals if s['signal_type'] == 'SELL']
    
    print(f"Tìm thấy {len(buy_signals)} Diamond Bottom (BUY) và {len(sell_signals)} Diamond Top (SELL)")
    
    if USE_RSI_FILTER:
        # Hiển thị RSI values của các signals
        if buy_signals:
            buy_rsi = [s['rsi_value'] for s in buy_signals if s['rsi_value'] is not None]
            if buy_rsi:
                print(f"  - BUY signals RSI: {[f'{rsi:.1f}' for rsi in buy_rsi]}")
        
        if sell_signals:
            sell_rsi = [s['rsi_value'] for s in sell_signals if s['rsi_value'] is not None]
            if sell_rsi:
                print(f"  - SELL signals RSI: {[f'{rsi:.1f}' for rsi in sell_rsi]}")
    
    # Tính toán kết quả với quản lý tài khoản
    results, final_balance = calculate_backtest_results(
        df, signals, 
        tp_percent=TP_PERCENT, sl_percent=SL_PERCENT, max_hold_bars=MAX_HOLD_HOURS,
        initial_balance=INITIAL_BALANCE, trade_amount=TRADE_AMOUNT,
        use_trailing_stop=USE_TRAILING_STOP, trailing_percent=TRAILING_PERCENT
    )
    
    if len(results) > 0:
        # Tính toán metrics
        total_signals = len(results)
        winning_trades = sum(1 for r in results if r['is_win'])
        losing_trades = total_signals - winning_trades
        win_rate = (winning_trades / total_signals) * 100
        
        # Metrics theo %
        total_pnl_percent = sum(r['pnl_percent'] for r in results)
        avg_pnl_percent = total_pnl_percent / total_signals
        
        winning_pnl_percent = sum(r['pnl_percent'] for r in results if r['is_win'])
        losing_pnl_percent = sum(r['pnl_percent'] for r in results if not r['is_win'])
        
        avg_win_percent = winning_pnl_percent / winning_trades if winning_trades > 0 else 0
        avg_loss_percent = losing_pnl_percent / losing_trades if losing_trades > 0 else 0
        
        profit_factor = abs(winning_pnl_percent / losing_pnl_percent) if losing_pnl_percent != 0 else float('inf')
        
        # Metrics theo tiền thật ($)
        total_pnl_dollar = sum(r['pnl_dollar'] for r in results)
        avg_pnl_dollar = total_pnl_dollar / total_signals
        
        winning_pnl_dollar = sum(r['pnl_dollar'] for r in results if r['is_win'])
        losing_pnl_dollar = sum(r['pnl_dollar'] for r in results if not r['is_win'])
        
        avg_win_dollar = winning_pnl_dollar / winning_trades if winning_trades > 0 else 0
        avg_loss_dollar = losing_pnl_dollar / losing_trades if losing_trades > 0 else 0
        
        # ROI tổng
        total_roi = ((final_balance - INITIAL_BALANCE) / INITIAL_BALANCE) * 100
        
        # In kết quả
        print("\n" + "="*60)
        print("KẾT QUẢ BACK TEST - QUẢN LÝ TÀI KHOẢN")
        print("="*60)
        
        print("📊 THỐNG KÊ GIAO DỊCH:")
        print(f"  Tổng số tín hiệu: {total_signals}")
        print(f"  Số lệnh thắng: {winning_trades}")
        print(f"  Số lệnh thua: {losing_trades}")
        print(f"  Win Rate: {win_rate:.2f}%")
        
        print(f"\n💰 TÀI KHOẢN:")
        print(f"  Số dư ban đầu: ${INITIAL_BALANCE:,.2f}")
        print(f"  Số dư cuối kỳ: ${final_balance:,.2f}")
        print(f"  Tổng lợi nhuận: ${total_pnl_dollar:+,.2f}")
        print(f"  ROI tổng: {total_roi:+.2f}%")
        print(f"  Số tiền mỗi lần giao dịch: ${TRADE_AMOUNT:,.2f}")
        
        print(f"\n📈 HIỆU SUẤT ($):")
        print(f"  Lợi nhuận trung bình mỗi lệnh: ${avg_pnl_dollar:+,.2f}")
        print(f"  Lợi nhuận trung bình khi thắng: ${avg_win_dollar:+,.2f}")
        print(f"  Thua lỗ trung bình khi thua: ${avg_loss_dollar:+,.2f}")
        
        print(f"\n📊 HIỆU SUẤT (%):")
        print(f"  Tỷ lệ lợi nhuận trung bình: {avg_pnl_percent:+.2f}%")
        print(f"  Lợi nhuận % trung bình khi thắng: {avg_win_percent:+.2f}%")
        print(f"  Thua lỗ % trung bình khi thua: {avg_loss_percent:+.2f}%")
        print(f"  Profit Factor: {profit_factor:.2f}")
        
        # Thống kê theo signal type
        buy_results = [r for r in results if r['signal_type'] == 'BUY']
        sell_results = [r for r in results if r['signal_type'] == 'SELL']
        
        print(f"\n🔺 PHÂN TÍCH THEO PATTERN:")
        if len(buy_results) > 0:
            buy_win_rate = (sum(1 for r in buy_results if r['is_win']) / len(buy_results)) * 100
            buy_pnl_dollar = sum(r['pnl_dollar'] for r in buy_results)
            buy_pnl_percent = sum(r['pnl_percent'] for r in buy_results)
            print(f"  Diamond Bottom (BUY): {len(buy_results)} signals | Win Rate: {buy_win_rate:.1f}% | "
                  f"PnL: ${buy_pnl_dollar:+,.2f} ({buy_pnl_percent:+.2f}%)")
        
        if len(sell_results) > 0:
            sell_win_rate = (sum(1 for r in sell_results if r['is_win']) / len(sell_results)) * 100
            sell_pnl_dollar = sum(r['pnl_dollar'] for r in sell_results)
            sell_pnl_percent = sum(r['pnl_percent'] for r in sell_results)
            print(f"  Diamond Top (SELL): {len(sell_results)} signals | Win Rate: {sell_win_rate:.1f}% | "
                  f"PnL: ${sell_pnl_dollar:+,.2f} ({sell_pnl_percent:+.2f}%)")

        # Chi tiết từng lệnh
        print(f"\n📋 CHI TIẾT {min(10, len(results))} GIAO DỊCH ĐẦU TIÊN:")
        if USE_RSI_FILTER:
            print("-" * 135)
            print("STT | Thời gian       | Type Pattern       | RSI   | Entry     | Exit      | Coin    | PnL ($)   | PnL (%) | Balance   | Exit")
            print("-" * 135)
            for i, result in enumerate(results[:10]):
                signal_type = result['signal_type']
                pattern_name = result['pattern_name']
                # Tìm RSI value từ signals
                matching_signal = None
                for signal in signals:
                    if (signal['datetime'] == result['signal_datetime'] and 
                        signal['signal_type'] == result['signal_type']):
                        matching_signal = signal
                        break
                
                rsi_display = f"{matching_signal['rsi_value']:5.1f}" if matching_signal and matching_signal['rsi_value'] is not None else "  N/A"
                
                print(f"{i+1:2d}. | {result['signal_datetime'].strftime('%Y-%m-%d %H:%M')} | "
                      f"{signal_type:4s} {pattern_name:12s} | "
                      f"{rsi_display} | "
                      f"${result['entry_price']:7.2f} | ${result['exit_price']:7.2f} | "
                      f"{result['coin_quantity']:7.4f} | "
                      f"${result['pnl_dollar']:+8.2f} | {result['pnl_percent']:+6.2f}% | "
                      f"${result['balance_after']:8.2f} | {result['exit_reason']}")
        else:
            print("-" * 120)
            print("STT | Thời gian       | Type Pattern       | Entry     | Exit      | Coin    | PnL ($)   | PnL (%) | Balance   | Exit")
            print("-" * 120)
            for i, result in enumerate(results[:10]):
                signal_type = result['signal_type']
                pattern_name = result['pattern_name']
                print(f"{i+1:2d}. | {result['signal_datetime'].strftime('%Y-%m-%d %H:%M')} | "
                      f"{signal_type:4s} {pattern_name:12s} | "
                      f"${result['entry_price']:7.2f} | ${result['exit_price']:7.2f} | "
                      f"{result['coin_quantity']:7.4f} | "
                      f"${result['pnl_dollar']:+8.2f} | {result['pnl_percent']:+6.2f}% | "
                      f"${result['balance_after']:8.2f} | {result['exit_reason']}")
    else:
        print("Không có kết quả giao dịch hợp lệ!")
        
    # Xuất báo cáo ra file
    if len(signals) > 0:
        report_filename = export_backtest_report(signals, results, final_balance)
        print(f"\n💾 Đã xuất báo cáo chi tiết ra file: {report_filename}")
    
else:
    print("Không tìm thấy diamond pattern nào trong khoảng thời gian này!")
    
    # Xuất báo cáo ngay cả khi không có signals
    report_filename = export_backtest_report([], [], INITIAL_BALANCE)
    print(f"\n💾 Đã xuất báo cáo ra file: {report_filename}")