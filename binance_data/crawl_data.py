#!/usr/bin/env python3
"""
Crawl data từ Binance API
Usage: python crawl_data.py <symbol> <timeframe>
Example: python crawl_data.py BTCUSDT 1h
"""

import sys
import os
import pandas as pd
import requests
import time
from datetime import datetime, timedelta
import argparse

def create_binance_data_folder():
    """Tạo thư mục binance_data nếu chưa có"""
    if not os.path.exists('binance_data'):
        os.makedirs('binance_data')
        print("Đã tạo thư mục binance_data/")

def get_binance_data(symbol, interval, start_date, end_date):
    """
    Crawl data từ Binance API
    Args:
        symbol: BTCUSDT, ETHUSDT, etc.
        interval: 1h, 2h, 4h, 1d, etc.
        start_date: '2025-01-01'
        end_date: '2025-06-30'
    """
    # Chuyển đổi interval
    interval_map = {
        '1m': '1m', '3m': '3m', '5m': '5m', '15m': '15m', '30m': '30m',
        '1h': '1h', '2h': '2h', '4h': '4h', '6h': '6h', '8h': '8h', '12h': '12h',
        '1d': '1d', '3d': '3d', '1w': '1w', '1M': '1M'
    }
    
    if interval not in interval_map:
        raise ValueError(f"Interval không hợp lệ: {interval}")
    
    # Chuyển đổi ngày thành timestamp
    start_ts = int(datetime.strptime(start_date, '%Y-%m-%d').timestamp() * 1000)
    end_ts = int(datetime.strptime(end_date, '%Y-%m-%d').timestamp() * 1000)
    
    # URL Binance API
    url = "https://api.binance.com/api/v3/klines"
    
    all_data = []
    current_start = start_ts
    
    print(f"Bắt đầu crawl data cho {symbol} {interval} từ {start_date} đến {end_date}")
    print("=" * 60)
    
    while current_start < end_ts:
        params = {
            'symbol': symbol,
            'interval': interval_map[interval],
            'startTime': current_start,
            'endTime': end_ts,
            'limit': 1000  # Max limit của Binance
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            if not data:
                print("Không có dữ liệu thêm, dừng crawl")
                break
                
            all_data.extend(data)
            
            # Cập nhật start time cho request tiếp theo
            last_timestamp = data[-1][0]
            current_start = last_timestamp + 1
            
            # Hiển thị progress
            progress_date = datetime.fromtimestamp(last_timestamp / 1000).strftime('%Y-%m-%d %H:%M')
            print(f"Đã crawl {len(all_data)} candles... (đến {progress_date})")
            
            # Rate limiting để tránh bị block
            time.sleep(0.1)
            
        except requests.exceptions.RequestException as e:
            print(f"Lỗi khi crawl data: {e}")
            break
        except Exception as e:
            print(f"Lỗi không xác định: {e}")
            break
    
    if not all_data:
        print("Không có dữ liệu nào được crawl")
        return None
    
    # Chuyển đổi thành DataFrame
    df = pd.DataFrame(all_data, columns=[
        'open_time', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'number_of_trades',
        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
    ])
    
    # Chuyển đổi kiểu dữ liệu
    numeric_columns = ['open', 'high', 'low', 'close', 'volume']
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Chuyển đổi timestamp thành datetime
    df['timestamp'] = pd.to_datetime(df['open_time'], unit='ms')
    
    # Chọn các cột cần thiết và đổi tên
    df = df[['timestamp', 'open', 'high', 'low', 'close', 'volume']]
    
    # Sắp xếp theo thời gian
    df = df.sort_values('timestamp').reset_index(drop=True)
    
    print(f"\nHoàn thành crawl data:")
    print(f"- Tổng số candles: {len(df)}")
    print(f"- Thời gian: {df['timestamp'].min()} đến {df['timestamp'].max()}")
    print(f"- Symbol: {symbol}")
    print(f"- Timeframe: {interval}")
    
    return df

def save_to_csv(df, symbol, interval):
    """Lưu DataFrame thành file CSV"""
    filename = f"binance_data/{symbol}_{interval}.csv"
    
    try:
        df.to_csv(filename, index=False)
        print(f"Đã lưu file: {filename}")
        print(f"Kích thước file: {os.path.getsize(filename) / 1024:.2f} KB")
        return filename
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Crawl data từ Binance API')
    parser.add_argument('symbol', help='Symbol (e.g., BTCUSDT, ETHUSDT)')
    parser.add_argument('timeframe', help='Timeframe (e.g., 1h, 2h, 4h, 1d)')
    parser.add_argument('--start-date', default='2025-01-01', help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end-date', default='2025-06-30', help='End date (YYYY-MM-DD)')
    
    args = parser.parse_args()
    
    symbol = args.symbol.upper()
    timeframe = args.timeframe
    start_date = args.start_date
    end_date = args.end_date
    
    print(f"=== BINANCE DATA CRAWLER ===")
    print(f"Symbol: {symbol}")
    print(f"Timeframe: {timeframe}")
    print(f"Period: {start_date} to {end_date}")
    print("=" * 40)
    
    # Tạo thư mục binance_data
    create_binance_data_folder()
    
    # Crawl data
    df = get_binance_data(symbol, timeframe, start_date, end_date)
    
    if df is not None and len(df) > 0:
        # Lưu file CSV
        filename = save_to_csv(df, symbol, timeframe)
        
        if filename:
            print(f"\n✅ Hoàn thành crawl data cho {symbol} {timeframe}")
            print(f"📁 File: {filename}")
            print(f"📊 Số candles: {len(df)}")
        else:
            print("❌ Lỗi khi lưu file")
    else:
        print("❌ Không có dữ liệu để lưu")

if __name__ == "__main__":
    main() 