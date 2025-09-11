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
import talib as ta
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

try:
    engine = create_engine(DATABASE_URL)
except Exception as e:
    engine = None
    print(f"Không tạo được kết nối DB: {e}")

def get_binance_data(symbol, interval):
    """
    Lấy dữ liệu từ database với xử lý lỗi và validation tốt hơn
    """
    print(f"Lấy dữ liệu từ DB: {symbol} {interval}")
    
    if engine is None:
        print("Chưa có kết nối DB hợp lệ.")
        return pd.DataFrame()

    table_name = f'"proddb"."coin_prices_1h"'

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
            params={"symbol": symbol}
        )

        if 'open_time' not in df.columns:
            print("Thiếu cột 'open_time' trong dữ liệu trả về từ DB.")
            print(f"   Columns: {list(df.columns)}")
            return pd.DataFrame()

        required_cols = {'open', 'high', 'low', 'close'}
        if not required_cols.issubset(df.columns):
            print(f"Thiếu cột cần thiết: {required_cols - set(df.columns)}")
            return pd.DataFrame()

        df['datetime'] = pd.to_datetime(df['open_time'], unit='s')
        df = df.sort_values('datetime').reset_index(drop=True)

        print(f"Đã đọc {len(df)} dòng từ DB bảng {table_name}")
        if len(df) > 0:
            print(f"   Thời gian: {df['datetime'].min()} đến {df['datetime'].max()}")
            print(f"   Giá cuối: ${df.iloc[-1]['close']:.4f}")

        return df
    except Exception as e:
        print(f"Lỗi khi đọc dữ liệu từ DB: {e}")
        return pd.DataFrame()

# --- Argument Parser ---
def parse_arguments():
    parser = argparse.ArgumentParser(description='ADX Pattern Backtest')
    parser.add_argument('symbol', help='Symbol (e.g., BTCUSDT, ETHUSDT)')
    parser.add_argument('timeframe', help='Timeframe (e.g., 1h, 2h, 4h, 1d)')
    parser.add_argument('--initial-balance', type=float, default=1000, help='Initial balance')
    parser.add_argument('--position-size', type=float, default=0.2, help='Position size as percentage of capital')
    parser.add_argument('--exit-periods-1', type=int, default=9, help='Exit periods for strategy 1')
    parser.add_argument('--exit-periods-2', type=int, default=26, help='Exit periods for strategy 2')
    parser.add_argument('--take-profit', type=float, default=5.0, help='Take profit percentage')
    parser.add_argument('--behind-periods', type=int, default=4, help='Number of periods to look back')
    parser.add_argument('--adx-period', type=int, default=14, help='ADX calculation period')
    # Optimization flags
    parser.add_argument('--use-mtf-adx', action='store_true', help='Enable multi-timeframe ADX confluence gating')
    parser.add_argument('--mtf-periods', default='7,14,21,28', help='Comma-separated ADX periods for MTF')
    parser.add_argument('--use-dynamic-thresholds', action='store_true', help='Enable dynamic ADX thresholds gating')
    parser.add_argument('--lookback-window', type=int, default=50, help='Lookback window for dynamic thresholds')
    parser.add_argument('--use-momentum',default=True, action='store_true', help='Enable ADX momentum gating')
    parser.add_argument('--use-structure', action='store_true', help='Enable support/resistance structure gating')
    
    return parser.parse_args()

# --- Cấu hình ---
args = parse_arguments()

SYMBOL = args.symbol.upper()
TIMEFRAME = args.timeframe
INITIAL_BALANCE = args.initial_balance
POSITION_SIZE_PCT = args.position_size
EXIT_PERIODS_1 = args.exit_periods_1
EXIT_PERIODS_2 = args.exit_periods_2
TAKE_PROFIT_PERCENT = args.take_profit
BEHIND_PERIODS = args.behind_periods
ADX_PERIOD = args.adx_period
USE_MTF_ADX = args.use_mtf_adx
# Parse comma-separated list of periods safely
try:
    MTF_PERIODS = [int(x.strip()) for x in str(args.mtf_periods).split(',') if x.strip().isdigit()]
except Exception:
    MTF_PERIODS = [7, 14, 21, 28]
USE_DYNAMIC_THRESHOLDS = args.use_dynamic_thresholds
LOOKBACK_WINDOW = args.lookback_window
USE_MOMENTUM = args.use_momentum
USE_STRUCTURE = args.use_structure

print(f"=== ADX PATTERN BACKTEST ===")
print(f"Symbol: {SYMBOL}")
print(f"Timeframe: {TIMEFRAME}")
print(f"Initial Balance: ${INITIAL_BALANCE}")
print(f"Position Size: {POSITION_SIZE_PCT*100}% of capital")
print(f"Exit Strategy 1: {EXIT_PERIODS_1} periods")
print(f"Exit Strategy 2: {EXIT_PERIODS_2} periods")
print(f"Take Profit: {TAKE_PROFIT_PERCENT}%")
print(f"Behind Periods: {BEHIND_PERIODS}")
print(f"ADX Period: {ADX_PERIOD}")
print(f"Use MTF ADX: {USE_MTF_ADX} | Periods: {MTF_PERIODS}")
print(f"Use Dynamic Thresholds: {USE_DYNAMIC_THRESHOLDS} | Lookback: {LOOKBACK_WINDOW}")
print(f"Use Momentum: {USE_MOMENTUM}")
print(f"Use Structure: {USE_STRUCTURE}")
print("=" * 40)

# --- Đọc data từ database ---
df = get_binance_data(SYMBOL, TIMEFRAME)

if len(df) == 0:
    print("Không có dữ liệu để backtest!")
    exit()

# --- Tính toán ADX và các chỉ báo ---
def calculate_adx_indicators(df, adx_period=ADX_PERIOD, behind_periods=BEHIND_PERIODS):
    """
    Tính toán ADX và các chỉ báo theo logic SQL
    """
    df = df.copy()
    
    # Tính ADX với TA-Lib
    df['adx'] = ta.ADX(df['high'].values, df['low'].values, df['close'].values, timeperiod=adx_period)
    
    # Fill NaN values for ADX (TA-Lib returns NaN for initial periods)
    df['adx'] = df['adx'].fillna(0)
    
    # Debug: check ADX calculation
    valid_adx = df['adx'][df['adx'] > 0]
    if len(valid_adx) > 0:
        print(f"ADX calculated successfully. Valid values: {len(valid_adx)}, Range: {valid_adx.min():.2f} - {valid_adx.max():.2f}")
    else:
        print("Warning: No valid ADX values calculated")
    
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
    
    # Optional: Multi-timeframe ADX
    if USE_MTF_ADX and MTF_PERIODS:
        for period in MTF_PERIODS:
            df[f'adx_{period}'] = ta.ADX(df['high'].values, df['low'].values, df['close'].values, timeperiod=period)
            df[f'adx_{period}'] = df[f'adx_{period}'].fillna(0)
            df[f'adx_slope_{period}'] = df[f'adx_{period}'].diff()
        mtf_cols = [f'adx_{p}' for p in MTF_PERIODS]
        df['adx_confluence'] = df[mtf_cols].mean(axis=1)
        # Gate: require at least 70% periods rising and 50% strong
        rising_counts = np.zeros(len(df), dtype=int)
        strong_counts = np.zeros(len(df), dtype=int)
        for period in MTF_PERIODS:
            rising_counts += (df[f'adx_slope_{period}'] > 0).astype(int)
            strong_counts += (df[f'adx_{period}'] > 20).astype(int)
        min_rising = max(1, int(len(MTF_PERIODS) * 0.5))
        min_strong = max(1, int(len(MTF_PERIODS) * 0.33))
        df['mtf_gate'] = ((rising_counts >= min_rising) & (strong_counts >= min_strong)).astype(int)

    # Optional: Dynamic thresholds
    if USE_DYNAMIC_THRESHOLDS:
        df['atr'] = ta.ATR(df['high'].values, df['low'].values, df['close'].values, timeperiod=14)
        # Avoid qcut errors by filling NaNs
        atr_series = df['atr'].fillna(method='bfill').fillna(method='ffill').fillna(df['atr'].median())
        try:
            df['volatility_regime'] = pd.qcut(atr_series, q=3, labels=['Low', 'Medium', 'High'])
        except Exception:
            df['volatility_regime'] = 'Medium'
        df['adx_rolling_mean'] = df['adx'].rolling(LOOKBACK_WINDOW).mean()
        df['adx_rolling_std'] = df['adx'].rolling(LOOKBACK_WINDOW).std()
        df['adx_threshold_low'] = df['adx_rolling_mean'] - 0.5 * df['adx_rolling_std']
        df['adx_threshold_high'] = df['adx_rolling_mean'] + 0.5 * df['adx_rolling_std']
        # Adjust thresholds based on regime
        mult_map = {'Low': 0.8, 'Medium': 1.0, 'High': 1.2}
        df['adx_threshold_low'] = df.apply(lambda r: r['adx_threshold_low'] * mult_map.get(r['volatility_regime'], 1.0), axis=1)
        df['adx_threshold_high'] = df.apply(lambda r: r['adx_threshold_high'] * mult_map.get(r['volatility_regime'], 1.0), axis=1)
        # Gates
        df['dyn_gate_bottom'] = ((df['adx'] < df['adx_threshold_low']) & (df['adx'].shift(1) >= df['adx_threshold_low'].shift(1))).astype(int)
        df['dyn_gate_top'] = ((df['adx'] > df['adx_threshold_high']) & (df['adx'].shift(1) <= df['adx_threshold_high'].shift(1))).astype(int)

    # Optional: Momentum analysis
    if USE_MOMENTUM:
        df['adx_velocity'] = df['adx'].diff()
        # EMA của velocity để lọc nhiễu ngắn hạn
        df['adx_momentum'] = df['adx_velocity'].ewm(span=5).mean()
        # Nhấn mạnh xu hướng đang mạnh lên thay vì chỉ ADX nhỏ
        df['mom_gate_up'] = ((df['adx_momentum'] > 0) & (df['adx'] > 20) & (df['adx'] < 40)).astype(int)
        df['mom_gate_down'] = ((df['adx_momentum'] < 0) & (df['adx'] > 30)).astype(int)

    # Optional: Price structure
    if USE_STRUCTURE:
        # Simple proximity to recent highs/lows
        recent_window = max(5, behind_periods)
        df['recent_high'] = df['high'].rolling(recent_window).max()
        df['recent_low'] = df['low'].rolling(recent_window).min()
        df['near_resistance'] = ((df['close'] >= df['recent_high'] * 0.99)).astype(int)
        df['near_support'] = ((df['close'] <= df['recent_low'] * 1.01)).astype(int)
        df['structure_gate_long'] = ((df['near_support'] == 1) & (df['trend'] == 'UP')).astype(int)
        df['structure_gate_short'] = ((df['near_resistance'] == 1) & (df['trend'] == 'DOWN')).astype(int)

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
    Điều kiện mua cải tiến: ADX BOTTOM + Price UP trend + Multiple confirmations
    """
    if i < BEHIND_PERIODS + 1 or i >= len(df) - 1:
        return False, None, None
    
    current_row = df.iloc[i]
    
    # 1. Kiểm tra ADX BOTTOM
    if current_row['adx_type'] != 'BOTTOM':
        return False, None, None
    
    # 2. Kiểm tra Price UP trend
    if current_row['trend'] != 'UP':
        return False, None, None
    
    # 3. Kiểm tra ADX đang tăng (momentum confirmation)
    if i > 0:
        prev_adx = df.iloc[i-1]['adx']
        if current_row['adx'] <= prev_adx:
            return False, None, None
    
    # 4. ADX phải trên ngưỡng tối thiểu (tránh sideways market) - hạ thấp để nhiều tín hiệu hơn
    if current_row['adx'] < 18:
        return False, None, None
    
    # 5. Volume confirmation (nếu có dữ liệu volume)
    if 'volume' in df.columns:
        # Volume hiện tại cao hơn trung bình 5 phiên
        if i >= 5:
            avg_volume = df.iloc[i-5:i]['volume'].mean()
            if current_row['volume'] < avg_volume * 1.2:
                return False, None, None
    
    # 6. Price action confirmation - giá phải break above recent resistance (nới lỏng buffer)
    if i >= 3:
        recent_highs = df.iloc[i-3:i]['high'].max()
        if current_row['close'] <= recent_highs * 1.0005:  # 0.05% buffer
            return False, None, None
    
    # Optional gates
    if USE_MTF_ADX and 'mtf_gate' in df.columns and df.iloc[i]['mtf_gate'] != 1:
        return False, None, None
    if USE_DYNAMIC_THRESHOLDS and 'dyn_gate_bottom' in df.columns and df.iloc[i]['dyn_gate_bottom'] != 1:
        return False, None, None
    if USE_MOMENTUM and 'mom_gate_up' in df.columns and df.iloc[i]['mom_gate_up'] != 1:
        return False, None, None
    if USE_STRUCTURE and 'structure_gate_long' in df.columns and df.iloc[i]['structure_gate_long'] != 1:
        return False, None, None

    return True, current_row['close'], 'adx_bottom_up_trend_confirmed'

def should_sell(df, i):
    """
    Điều kiện bán cải tiến: ADX TOP + Price DOWN trend + Multiple confirmations
    """
    if i < BEHIND_PERIODS + 1 or i >= len(df) - 1:
        return False, None, None
    
    current_row = df.iloc[i]
    
    # 1. Kiểm tra ADX TOP
    if current_row['adx_type'] != 'TOP':
        return False, None, None
    
    # 2. Kiểm tra Price DOWN trend
    if current_row['trend'] != 'DOWN':
        return False, None, None
    
    # 3. Kiểm tra ADX đang giảm (momentum confirmation)
    if i > 0:
        prev_adx = df.iloc[i-1]['adx']
        if current_row['adx'] >= prev_adx:
            return False, None, None
    
    # 4. ADX phải trên ngưỡng tối thiểu - hạ thấp để nhiều tín hiệu hơn
    if current_row['adx'] < 18:
        return False, None, None
    
    # 5. Volume confirmation (nếu có dữ liệu volume)
    if 'volume' in df.columns:
        if i >= 5:
            avg_volume = df.iloc[i-5:i]['volume'].mean()
            if current_row['volume'] < avg_volume * 1.2:
                return False, None, None
    
    # 6. Price action confirmation - giá phải break below recent support (nới lỏng buffer)
    if i >= 3:
        recent_lows = df.iloc[i-3:i]['low'].min()
        if current_row['close'] >= recent_lows * 0.9995:  # 0.05% buffer
            return False, None, None
    
    # Optional gates
    if USE_MTF_ADX and 'mtf_gate' in df.columns and df.iloc[i]['mtf_gate'] != 1:
        return False, None, None
    if USE_DYNAMIC_THRESHOLDS and 'dyn_gate_top' in df.columns and df.iloc[i]['dyn_gate_top'] != 1:
        return False, None, None
    if USE_MOMENTUM and 'mom_gate_down' in df.columns and df.iloc[i]['mom_gate_down'] != 1:
        return False, None, None
    if USE_STRUCTURE and 'structure_gate_short' in df.columns and df.iloc[i]['structure_gate_short'] != 1:
        return False, None, None

    return True, current_row['close'], 'adx_top_down_trend_confirmed'

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
                    'adx_exit': df.iloc[i]['adx'],
                    'trend_strength': position.get('trend_strength', 0)
                })
                position = None
        
        # Look for new signals to enter (chỉ khi không có position)
        if position is None:
            # Check for buy signal (ADX BOTTOM + UP trend)
            buy_signal, buy_price, buy_pattern = should_buy(df, i)
            if buy_signal:
                # Execute buy với position sizing cải tiến
                position_value = balance * position_size_pct
                quantity = position_value / buy_price
                
                # Thêm thông tin ADX và trend strength
                adx_value = df.iloc[i]['adx']
                trend_strength = (df.iloc[i]['c_trend'] + df.iloc[i]['l_trend'] + df.iloc[i]['h_trend']) / 3
                
                position = {
                    'type': 'LONG',
                    'entry_time': current_date,
                    'entry_index': i,
                    'entry_price': buy_price,
                    'quantity': quantity,
                    'value': position_value,
                    'pattern_type': buy_pattern,
                    'adx_entry': adx_value,
                    'trend_strength': trend_strength
                }
                balance -= position_value
                print(f"📈 LONG Entry: ${buy_price:.4f} | ADX: {adx_value:.2f} | Trend: {trend_strength:.2f}")
                continue
            
            # Check for sell signal (ADX TOP + DOWN trend) 
            sell_signal, sell_price, sell_pattern = should_sell(df, i)
            if sell_signal:
                # Execute sell với position sizing cải tiến
                position_value = balance * position_size_pct
                quantity = position_value / sell_price
                
                adx_value = df.iloc[i]['adx']
                trend_strength = (df.iloc[i]['c_trend'] + df.iloc[i]['l_trend'] + df.iloc[i]['h_trend']) / 3
                
                position = {
                    'type': 'SHORT',
                    'entry_time': current_date,
                    'entry_index': i,
                    'entry_price': sell_price,
                    'quantity': quantity,
                    'value': position_value,
                    'pattern_type': sell_pattern,
                    'adx_entry': adx_value,
                    'trend_strength': trend_strength
                }
                balance -= position_value
                print(f"📉 SHORT Entry: ${sell_price:.4f} | ADX: {adx_value:.2f} | Trend: {trend_strength:.2f}")
    
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
            'adx_exit': df.iloc[-1]['adx'],
            'trend_strength': position.get('trend_strength', 0)
        })
    
    return results, balance

# --- Xuất báo cáo so sánh ---
def export_adx_comparison_report(results_9, results_26, final_balance_9, final_balance_26, filename=None):
    if filename is None:
        # Xác định khoảng thời gian từ kết quả giao dịch hoặc dữ liệu đã tải
        all_times = []
        for r in (results_9 or []):
            if 'entry_time' in r and r['entry_time'] is not None:
                all_times.append(r['entry_time'])
            if 'exit_time' in r and r['exit_time'] is not None:
                all_times.append(r['exit_time'])
        for r in (results_26 or []):
            if 'entry_time' in r and r['entry_time'] is not None:
                all_times.append(r['entry_time'])
            if 'exit_time' in r and r['exit_time'] is not None:
                all_times.append(r['exit_time'])

        if all_times:
            start_dt = min(all_times)
            end_dt = max(all_times)
        else:
            try:
                start_dt = df['datetime'].min()
                end_dt = df['datetime'].max()
            except Exception:
                end_dt = pd.Timestamp.utcnow()
                start_dt = end_dt - pd.DateOffset(days=60)

        start_date_formatted = pd.to_datetime(start_dt).strftime('%Y%m%d')
        end_date_formatted = pd.to_datetime(end_dt).strftime('%Y%m%d')
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
        
        # Chi tiết giao dịch Strategy 1 với ADX metrics
        if results_9:
            f.write(f"## Strategy 1: Exit after {EXIT_PERIODS_1} periods\n\n")
            f.write(f"| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held | ADX Entry | ADX Exit | Trend Str |\n")
            f.write(f"|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|-----------|----------|----------|\n")
            for r in results_9:
                trend_str = r.get('trend_strength', 0)
                f.write(f"| {r['entry_time'].strftime('%Y-%m-%d %H:%M')} | {r['exit_time'].strftime('%Y-%m-%d %H:%M')} | {r['type']} | ${r['entry_price']:.4f} | ${r['exit_price']:.4f} | ${r['pnl']:.2f} | {r['pnl_percent']:.2f}% | {r['pattern_type']} | {r['exit_reason']} | {r['bars_held']} | {r['adx_entry']:.2f} | {r['adx_exit']:.2f} | {trend_str:.2f} |\n")
            f.write(f"\n")
            
            # Thống kê ADX cho Strategy 1
            adx_entries = [r['adx_entry'] for r in results_9 if 'adx_entry' in r]
            if adx_entries:
                f.write(f"### ADX Statistics - Strategy 1\n")
                f.write(f"- **Average ADX at Entry**: {np.mean(adx_entries):.2f}\n")
                f.write(f"- **Min ADX at Entry**: {np.min(adx_entries):.2f}\n")
                f.write(f"- **Max ADX at Entry**: {np.max(adx_entries):.2f}\n")
                f.write(f"- **Strong Trend Entries (ADX > 25)**: {sum(1 for adx in adx_entries if adx > 25)}/{len(adx_entries)}\n\n")
        
        # Chi tiết giao dịch Strategy 2 với ADX metrics
        if results_26:
            f.write(f"## Strategy 2: Exit after {EXIT_PERIODS_2} periods\n\n")
            f.write(f"| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type | Exit Reason | Bars Held | ADX Entry | ADX Exit | Trend Str |\n")
            f.write(f"|------------|-----------|------|-------------|------------|-----|-------|-------------|-------------|-----------|-----------|----------|----------|\n")
            for r in results_26:
                trend_str = r.get('trend_strength', 0)
                f.write(f"| {r['entry_time'].strftime('%Y-%m-%d %H:%M')} | {r['exit_time'].strftime('%Y-%m-%d %H:%M')} | {r['type']} | ${r['entry_price']:.4f} | ${r['exit_price']:.4f} | ${r['pnl']:.2f} | {r['pnl_percent']:.2f}% | {r['pattern_type']} | {r['exit_reason']} | {r['bars_held']} | {r['adx_entry']:.2f} | {r['adx_exit']:.2f} | {trend_str:.2f} |\n")
            f.write(f"\n")
            
            # Thống kê ADX cho Strategy 2
            adx_entries = [r['adx_entry'] for r in results_26 if 'adx_entry' in r]
            if adx_entries:
                f.write(f"### ADX Statistics - Strategy 2\n")
                f.write(f"- **Average ADX at Entry**: {np.mean(adx_entries):.2f}\n")
                f.write(f"- **Min ADX at Entry**: {np.min(adx_entries):.2f}\n")
                f.write(f"- **Max ADX at Entry**: {np.max(adx_entries):.2f}\n")
                f.write(f"- **Strong Trend Entries (ADX > 25)**: {sum(1 for adx in adx_entries if adx > 25)}/{len(adx_entries)}\n\n")
        
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
