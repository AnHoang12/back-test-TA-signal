#!/usr/bin/env python3
"""
ADX Pattern Backtest - Xác định xu hướng giá dựa trên ADX và giá trung bình
Logic: 4 phiên trước + phiên hiện tại + 1 phiên sau
"""

import os
import pandas as pd
import numpy as np
import argparse
from datetime import datetime
from dotenv import load_dotenv
import ta

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
    filename = f"/home/anhoang/trade-bot/back-test/binance_data/{symbol}_{interval}.csv"
    
    try:
        df = pd.read_csv(filename)
        df['datetime'] = pd.to_datetime(df['timestamp'])
        
        start_dt = pd.to_datetime(start_date)
        end_dt = pd.to_datetime(end_date)
        
        df = df[(df['datetime'] >= start_dt) & (df['datetime'] <= end_dt)]
        df = df.sort_values('datetime').reset_index(drop=True)
        
        print(f"Đã đọc data từ {filename}")
        print(f"Tổng số candles: {len(df)}")
        print(f"Thời gian: {df['datetime'].min()} đến {df['datetime'].max()}")
        
        return df
        
    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
        return pd.DataFrame()

# --- Argument Parser ---
def parse_arguments():
    parser = argparse.ArgumentParser(description='ADX Pattern Backtest')
    parser.add_argument('symbol', help='Symbol (e.g., BTCUSDT, ETHUSDT)')
    parser.add_argument('timeframe', help='Timeframe (e.g., 1h, 2h, 4h, 1d)')
    parser.add_argument('--start-date', default='2025-04-01', help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end-date', default='2025-06-30', help='End date (YYYY-MM-DD)')
    parser.add_argument('--initial-balance', type=float, default=1000, help='Initial balance')
    parser.add_argument('--position-size', type=float, default=0.2, help='Position size as percentage of capital')
    parser.add_argument('--exit-periods-1', type=int, default=9, help='Exit periods for strategy 1')
    parser.add_argument('--exit-periods-2', type=int, default=26, help='Exit periods for strategy 2')
    parser.add_argument('--take-profit', type=float, default=5.0, help='Take profit percentage')
    parser.add_argument('--behind-periods', type=int, default=4, help='Number of periods to look back')
    parser.add_argument('--adx-period', type=int, default=14, help='ADX calculation period')
    
    return parser.parse_args()

# --- Cấu hình ---
args = parse_arguments()

SYMBOL = args.symbol.upper()
TIMEFRAME = args.timeframe
START_DATE = args.start_date
END_DATE = args.end_date
INITIAL_BALANCE = args.initial_balance
POSITION_SIZE_PCT = args.position_size
EXIT_PERIODS_1 = args.exit_periods_1
EXIT_PERIODS_2 = args.exit_periods_2
TAKE_PROFIT_PERCENT = args.take_profit
BEHIND_PERIODS = args.behind_periods
ADX_PERIOD = args.adx_period

print(f"=== ADX PATTERN BACKTEST ===")
print(f"Symbol: {SYMBOL}")
print(f"Timeframe: {TIMEFRAME}")
print(f"Period: {START_DATE} to {END_DATE}")
print(f"Initial Balance: ${INITIAL_BALANCE}")
print(f"Position Size: {POSITION_SIZE_PCT*100}% of capital")
print(f"Exit Strategy 1: {EXIT_PERIODS_1} periods")
print(f"Exit Strategy 2: {EXIT_PERIODS_2} periods")
print(f"Take Profit: {TAKE_PROFIT_PERCENT}%")
print(f"Behind Periods: {BEHIND_PERIODS}")
print(f"ADX Period: {ADX_PERIOD}")
print("=" * 40)

# --- Đọc data từ folder binance_data ---
df = get_binance_data(SYMBOL, TIMEFRAME, START_DATE, END_DATE)

if len(df) == 0:
    print("Không có dữ liệu để backtest!")
    exit()

# --- Tính toán ADX và các chỉ báo ---
def calculate_adx_indicators(df, adx_period=ADX_PERIOD, behind_periods=BEHIND_PERIODS):
    """
    Tính toán ADX và các chỉ báo theo logic SQL
    """
    df = df.copy()
    
    # Tính ADX
    df['adx'] = ta.trend.ADXIndicator(df['high'], df['low'], df['close'], window=adx_period).adx()
    
    # Tính các chỉ báo xu hướng giá
    df['close_avg'] = df['close'].rolling(window=behind_periods).mean()
    df['low_avg'] = df['low'].rolling(window=behind_periods).mean()
    df['high_avg'] = df['high'].rolling(window=behind_periods).mean()
    
    # Tính c_trend, l_trend, h_trend
    df['c_trend'] = (df['close'] > df['close_avg']).astype(int)
    df['l_trend'] = (df['low'] > df['low_avg']).astype(int)
    df['h_trend'] = (df['high'] > df['high_avg']).astype(int)
    
    # Tính ADX high/low trong window (behind + 1 following)
    df['adx_high'] = df['adx'].rolling(window=behind_periods + 2, center=True).max()
    df['adx_low'] = df['adx'].rolling(window=behind_periods + 2, center=True).min()
    
    # Tính adx_check (số phiên có ADX trong window)
    df['adx_check'] = df['adx'].rolling(window=3, center=True).count()
    
    return df

def detect_adx_trend(df):
    """
    Xác định ADX trend theo logic SQL
    """
    df = df.copy()
    
    # ADX Type detection
    df['adx_type'] = ''
    mask_top = (df['adx_check'] >= 3) & (df['adx'] >= df['adx_high'])
    mask_bottom = (df['adx_check'] >= 3) & (df['adx'] <= df['adx_low'])
    
    df.loc[mask_top, 'adx_type'] = 'TOP'
    df.loc[mask_bottom, 'adx_type'] = 'BOTTOM'
    
    # Price trend detection
    df['trend'] = 'DOWN'
    mask_up = (df['c_trend'] + df['l_trend'] + df['h_trend']) >= 2
    df.loc[mask_up, 'trend'] = 'UP'
    
    return df

def should_buy(df, i):
    """
    Điều kiện mua: ADX BOTTOM + Price UP trend
    """
    if i < BEHIND_PERIODS + 1 or i >= len(df) - 1:
        return False, None, None
    
    current_row = df.iloc[i]
    
    # Kiểm tra ADX BOTTOM
    if current_row['adx_type'] != 'BOTTOM':
        return False, None, None
    
    # Kiểm tra Price UP trend
    if current_row['trend'] != 'UP':
        return False, None, None
    
    # Kiểm tra ADX đang tăng (confirmation)
    if i > 0:
        prev_adx = df.iloc[i-1]['adx']
        if current_row['adx'] <= prev_adx:
            return False, None, None
    
    return True, current_row['close'], 'adx_bottom_up_trend'

def should_sell(df, i):
    """
    Điều kiện bán: ADX TOP + Price DOWN trend
    """
    if i < BEHIND_PERIODS + 1 or i >= len(df) - 1:
        return False, None, None
    
    current_row = df.iloc[i]
    
    # Kiểm tra ADX TOP
    if current_row['adx_type'] != 'TOP':
        return False, None, None
    
    # Kiểm tra Price DOWN trend
    if current_row['trend'] != 'DOWN':
        return False, None, None
    
    # Kiểm tra ADX đang giảm (confirmation)
    if i > 0:
        prev_adx = df.iloc[i-1]['adx']
        if current_row['adx'] >= prev_adx:
            return False, None, None
    
    return True, current_row['close'], 'adx_top_down_trend'

# --- Backtest với chỉ 1 position tại 1 thời điểm ---
def calculate_backtest_results(df, exit_periods, initial_balance=INITIAL_BALANCE, position_size_pct=POSITION_SIZE_PCT):
    """
    Backtest với chỉ 1 position tại 1 thời điểm
    """
    results = []
    balance = initial_balance
    position = None
    
    # Tính toán indicators
    df = calculate_adx_indicators(df)
    df = detect_adx_trend(df)
    
    for i in range(BEHIND_PERIODS + 1, len(df)):
        current_date = df.iloc[i]['datetime']
        current_close = df.iloc[i]['close']
        
        # Close existing position if conditions are met
        if position is not None:
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
                # Close position
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
                    'bars_held': bars_held,
                    'exit_reason': exit_reason,
                    'adx_entry': position['adx_entry'],
                    'adx_exit': df.iloc[i]['adx']
                })
                position = None
        
        # Look for new signals to enter (chỉ khi không có position)
        if position is None:
            # Check for buy signal (ADX BOTTOM + UP trend)
            buy_signal, buy_price, buy_pattern = should_buy(df, i)
            if buy_signal:
                # Execute buy
                position_value = balance * position_size_pct
                quantity = position_value / buy_price
                
                position = {
                    'type': 'LONG',
                    'entry_time': current_date,
                    'entry_index': i,
                    'entry_price': buy_price,
                    'quantity': quantity,
                    'value': position_value,
                    'pattern_type': buy_pattern,
                    'adx_entry': df.iloc[i]['adx']
                }
                balance -= position_value
                continue
            
            # Check for sell signal (ADX TOP + DOWN trend) 
            sell_signal, sell_price, sell_pattern = should_sell(df, i)
            if sell_signal:
                # Execute sell
                position_value = balance * position_size_pct
                quantity = position_value / sell_price
                
                position = {
                    'type': 'SHORT',
                    'entry_time': current_date,
                    'entry_index': i,
                    'entry_price': sell_price,
                    'quantity': quantity,
                    'value': position_value,
                    'pattern_type': sell_pattern,
                    'adx_entry': df.iloc[i]['adx']
                }
                balance -= position_value
    
    # Close any remaining position at the end
    if position is not None:
        final_close = df.iloc[-1]['close']
        final_date = df.iloc[-1]['datetime']
        
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
            'exit_reason': 'End',
            'adx_entry': position['adx_entry'],
            'adx_exit': df.iloc[-1]['adx']
        })
    
    return results, balance

# --- Xuất báo cáo so sánh ---
def export_adx_comparison_report(results_9, results_26, final_balance_9, final_balance_26, filename=None):
    if filename is None:
        start_date_formatted = START_DATE.replace('-', '')
        end_date_formatted = END_DATE.replace('-', '')
        filename = f"adx_pattern_{SYMBOL.lower()}_{TIMEFRAME}_{start_date_formatted}_{end_date_formatted}.md"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# ADX Pattern Strategy Comparison - {SYMBOL} {TIMEFRAME}\n\n")
        f.write(f"## Strategy Overview\n")
        f.write(f"- **Pattern**: ADX Trend Detection + Price Trend Analysis\n")
        f.write(f"- **Logic**: 4 phiên trước + phiên hiện tại + 1 phiên sau\n")
        f.write(f"- **ADX TOP**: ADX >= ADX cao nhất trong window\n")
        f.write(f"- **ADX BOTTOM**: ADX <= ADX thấp nhất trong window\n")
        f.write(f"- **Price UP**: Ít nhất 2/3 chỉ số (close, low, high) > trung bình\n")
        f.write(f"- **Price DOWN**: Ít nhất 2/3 chỉ số < trung bình\n")
        f.write(f"- **Entry LONG**: ADX BOTTOM + Price UP trend\n")
        f.write(f"- **Entry SHORT**: ADX TOP + Price DOWN trend\n")
        f.write(f"- **Position Management**: Only 1 position at a time\n")
        f.write(f"- **Exit Strategy 1**: Hold for {EXIT_PERIODS_1} periods\n")
        f.write(f"- **Exit Strategy 2**: Hold for {EXIT_PERIODS_2} periods\n")
        f.write(f"- **Take Profit**: {TAKE_PROFIT_PERCENT}%\n")
        f.write(f"- **Position Size**: {POSITION_SIZE_PCT*100}% of capital\n")
        f.write(f"- **Behind Periods**: {BEHIND_PERIODS}\n")
        f.write(f"- **ADX Period**: {ADX_PERIOD}\n\n")
        
        # Tính toán metrics
        def calculate_metrics(results):
            if not results:
                return {
                    'total_trades': 0, 'win_rate': 0, 'total_return': 0,
                    'final_capital': INITIAL_BALANCE, 'total_pnl': 0,
                    'avg_pnl': 0, 'best_trade': 0, 'worst_trade': 0,
                    'long_trades': 0, 'short_trades': 0
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
            
            return {
                'total_trades': total_trades, 'win_rate': win_rate, 'total_return': total_return,
                'final_capital': final_capital, 'total_pnl': total_pnl,
                'avg_pnl': avg_pnl, 'best_trade': best_trade, 'worst_trade': worst_trade,
                'long_trades': long_trades, 'short_trades': short_trades
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
        f.write(f"| Short Trades | {metrics_9['short_trades']} | {metrics_26['short_trades']} |\n\n")
        
        # Chi tiết giao dịch Strategy 1
        if results_9:
            f.write(f"## Strategy 1: Exit after {EXIT_PERIODS_1} periods\n\n")
            f.write(f"| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held | ADX Entry | ADX Exit |\n")
            f.write(f"|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|-----------|----------|\n")
            for r in results_9:
                f.write(f"| {r['entry_time'].strftime('%Y-%m-%d %H:%M')} | {r['exit_time'].strftime('%Y-%m-%d %H:%M')} | {r['type']} | ${r['entry_price']:.4f} | ${r['exit_price']:.4f} | ${r['pnl']:.2f} | {r['pnl_percent']:.2f}% | {r['pattern_type']} | {r['exit_reason']} | {r['bars_held']} | {r['adx_entry']:.2f} | {r['adx_exit']:.2f} |\n")
            f.write(f"\n")
        
        # Chi tiết giao dịch Strategy 2
        if results_26:
            f.write(f"## Strategy 2: Exit after {EXIT_PERIODS_2} periods\n\n")
            f.write(f"| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held | ADX Entry | ADX Exit |\n")
            f.write(f"|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|-----------|----------|\n")
            for r in results_26:
                f.write(f"| {r['entry_time'].strftime('%Y-%m-%d %H:%M')} | {r['exit_time'].strftime('%Y-%m-%d %H:%M')} | {r['type']} | ${r['entry_price']:.4f} | ${r['exit_price']:.4f} | ${r['pnl']:.2f} | {r['pnl_percent']:.2f}% | {r['pattern_type']} | {r['exit_reason']} | {r['bars_held']} | {r['adx_entry']:.2f} | {r['adx_exit']:.2f} |\n")
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
        f.write(f"- **Position Management**: Only 1 position at a time\n")
        f.write(f"- **Pattern Types**: ADX BOTTOM + UP trend (LONG) and ADX TOP + DOWN trend (SHORT)\n\n")
        
        f.write(f"---\n")
        f.write(f"*Báo cáo được tạo tự động bởi ADX Pattern Backtest System*\n")
    
    return filename

# --- Chạy backtest ---
if __name__ == "__main__":
    # Backtest với 2 exit strategies
    print("Running strategy 1: Exit after", EXIT_PERIODS_1, "periods")
    results_9, final_balance_9 = calculate_backtest_results(df, EXIT_PERIODS_1)
    
    print("Running strategy 2: Exit after", EXIT_PERIODS_2, "periods")
    results_26, final_balance_26 = calculate_backtest_results(df, EXIT_PERIODS_2)
    
    # Xuất báo cáo
    report_file = export_adx_comparison_report(results_9, results_26, final_balance_9, final_balance_26)
    print(f"Đã xuất báo cáo: {report_file}")
    
    # In kết quả tóm tắt
    print(f"\n=== KẾT QUẢ TÓM TẮT ===")
    print(f"Strategy 1 ({EXIT_PERIODS_1} periods): {len(results_9)} trades, ${final_balance_9:.2f}")
    print(f"Strategy 2 ({EXIT_PERIODS_2} periods): {len(results_26)} trades, ${final_balance_26:.2f}")
    
    if final_balance_26 > final_balance_9:
        print(f"Winner: Strategy 2 ({EXIT_PERIODS_2} periods) with {((final_balance_26 - INITIAL_BALANCE) / INITIAL_BALANCE * 100):.2f}% return")
    else:
        print(f"Winner: Strategy 1 ({EXIT_PERIODS_1} periods) with {((final_balance_9 - INITIAL_BALANCE) / INITIAL_BALANCE * 100):.2f}% return")
