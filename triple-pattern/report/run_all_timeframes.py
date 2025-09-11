#!/usr/bin/env python3
"""
Script để chạy backtest cho tất cả các khung giờ và xuất kết quả ra file txt
"""

import subprocess
import sys
import os
from datetime import datetime
import pandas as pd

def run_backtest_for_timeframe(symbol, timeframe, start_date, end_date, initial_balance=1000, position_size=0.2, exit_periods_1=9, exit_periods_2=26, take_profit=5.0):
    """Chạy backtest cho một khung giờ cụ thể"""
    
    # Tạo command để chạy backtest
    cmd = [
        'python', 'backtest.py',
        symbol, timeframe,
        '--start-date', start_date,
        '--end-date', end_date,
        '--initial-balance', str(initial_balance),
        '--position-size', str(position_size),
        '--exit-periods-1', str(exit_periods_1),
        '--exit-periods-2', str(exit_periods_2),
        '--take-profit', str(take_profit)
    ]
    
    print(f"Running backtest for {symbol} {timeframe}...")
    
    try:
        # Chạy command và capture output
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.getcwd())
        
        if result.returncode == 0:
            # Parse output để lấy kết quả
            output_lines = result.stdout.split('\n')
            
            # Tìm dòng kết quả tóm tắt
            summary_line = None
            for line in output_lines:
                if "Strategy 1 (" in line and "Strategy 2 (" in line:
                    summary_line = line
                    break
            
            if summary_line:
                # Parse kết quả từ summary line
                try:
                    # Extract số trades và balance
                    parts = summary_line.split(',')
                    strategy1_part = parts[0].strip()
                    strategy2_part = parts[1].strip()
                    
                    # Parse Strategy 1
                    strategy1_trades = int(strategy1_part.split('(')[1].split(')')[0].split()[0])
                    strategy1_balance = float(strategy1_part.split('$')[1])
                    
                    # Parse Strategy 2  
                    strategy2_trades = int(strategy2_part.split('(')[1].split(')')[0].split()[0])
                    strategy2_balance = float(strategy2_part.split('$')[1])
                    
                    # Tính toán metrics
                    strategy1_return = ((strategy1_balance - initial_balance) / initial_balance) * 100
                    strategy2_return = ((strategy2_balance - initial_balance) / initial_balance) * 100
                    
                    # Tạm thời set winrate = 0 (sẽ cần parse từ report file)
                    strategy1_winrate = 0
                    strategy2_winrate = 0
                    
                    return {
                        'timeframe': timeframe,
                        'strategy1_trades': strategy1_trades,
                        'strategy1_winrate': strategy1_winrate,
                        'strategy1_return': strategy1_return,
                        'strategy2_trades': strategy2_trades,
                        'strategy2_winrate': strategy2_winrate,
                        'strategy2_return': strategy2_return,
                        'success': True
                    }
                    
                except Exception as e:
                    print(f"Error parsing results for {timeframe}: {e}")
                    return {
                        'timeframe': timeframe,
                        'strategy1_trades': 0,
                        'strategy1_winrate': 0,
                        'strategy1_return': 0,
                        'strategy2_trades': 0,
                        'strategy2_winrate': 0,
                        'strategy2_return': 0,
                        'success': False,
                        'error': str(e)
                    }
            else:
                print(f"No summary line found for {timeframe}")
                return {
                    'timeframe': timeframe,
                    'strategy1_trades': 0,
                    'strategy1_winrate': 0,
                    'strategy1_return': 0,
                    'strategy2_trades': 0,
                    'strategy2_winrate': 0,
                    'strategy2_return': 0,
                    'success': False,
                    'error': 'No summary line found'
                }
        else:
            print(f"Error running backtest for {timeframe}: {result.stderr}")
            return {
                'timeframe': timeframe,
                'strategy1_trades': 0,
                'strategy1_winrate': 0,
                'strategy1_return': 0,
                'strategy2_trades': 0,
                'strategy2_winrate': 0,
                'strategy2_return': 0,
                'success': False,
                'error': result.stderr
            }
            
    except Exception as e:
        print(f"Exception running backtest for {timeframe}: {e}")
        return {
            'timeframe': timeframe,
            'strategy1_trades': 0,
            'strategy1_winrate': 0,
            'strategy1_return': 0,
            'strategy2_trades': 0,
            'strategy2_winrate': 0,
            'strategy2_return': 0,
            'success': False,
            'error': str(e)
        }

def parse_report_file_for_winrate(symbol, timeframe, start_date, end_date):
    """Parse report file để lấy winrate"""
    try:
        # Format filename
        start_date_formatted = start_date.replace('-', '')
        end_date_formatted = end_date.replace('-', '')
        filename = f"triple_pattern_multi_{symbol.lower()}_{timeframe}_{start_date_formatted}_{end_date_formatted}.md"
        
        if not os.path.exists(filename):
            return 0, 0
        
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Tìm winrate trong content
        lines = content.split('\n')
        for line in lines:
            if '| Win Rate |' in line:
                parts = line.split('|')
                if len(parts) >= 4:
                    try:
                        strategy1_winrate = float(parts[2].strip().replace('%', ''))
                        strategy2_winrate = float(parts[3].strip().replace('%', ''))
                        return strategy1_winrate, strategy2_winrate
                    except:
                        pass
        
        return 0, 0
        
    except Exception as e:
        print(f"Error parsing winrate for {timeframe}: {e}")
        return 0, 0

def run_all_timeframes(symbol, start_date, end_date, initial_balance=1000, position_size=0.2, exit_periods_1=9, exit_periods_2=26, take_profit=5.0):
    """Chạy backtest cho tất cả các khung giờ"""
    
    timeframes = ['1h', '2h', '4h', '6h', '12h', '1d']
    results = []
    
    print(f"=== RUNNING BACKTEST FOR ALL TIMEFRAMES ===")
    print(f"Symbol: {symbol}")
    print(f"Period: {start_date} to {end_date}")
    print(f"Initial Balance: ${initial_balance}")
    print(f"Position Size: {position_size*100}%")
    print(f"Exit Periods: {exit_periods_1} vs {exit_periods_2}")
    print(f"Take Profit: {take_profit}%")
    print("=" * 50)
    
    for timeframe in timeframes:
        print(f"\nProcessing {timeframe}...")
        
        # Chạy backtest
        result = run_backtest_for_timeframe(
            symbol, timeframe, start_date, end_date,
            initial_balance, position_size,
            exit_periods_1, exit_periods_2, take_profit
        )
        
        # Parse winrate từ report file
        if result['success']:
            strategy1_winrate, strategy2_winrate = parse_report_file_for_winrate(symbol, timeframe, start_date, end_date)
            result['strategy1_winrate'] = strategy1_winrate
            result['strategy2_winrate'] = strategy2_winrate
        
        results.append(result)
        
        if result['success']:
            print(f"✅ {timeframe}: {result['strategy1_trades']} trades, {result['strategy1_return']:.2f}% return")
        else:
            print(f"❌ {timeframe}: {result.get('error', 'Unknown error')}")
    
    return results

def export_results_to_txt(results, symbol, start_date, end_date, filename=None):
    """Xuất kết quả ra file txt"""
    
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"triple_pattern_results_{symbol.lower()}_{start_date.replace('-', '')}_{end_date.replace('-', '')}_{timestamp}.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"TRIPLE PATTERN BACKTEST RESULTS\n")
        f.write(f"Symbol: {symbol}\n")
        f.write(f"Period: {start_date} to {end_date}\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")
        
        # Header
        f.write(f"{'Timeframe':<8} {'9 Periods':<30} {'26 Periods':<30}\n")
        f.write(f"{'':<8} {'Trades':<8} {'Winrate':<8} {'Return':<8} {'Trades':<8} {'Winrate':<8} {'Return':<8}\n")
        f.write("-" * 60 + "\n")
        
        # Data rows
        for result in results:
            if result['success']:
                f.write(f"{result['timeframe']:<8} "
                       f"{result['strategy1_trades']:<8} "
                       f"{result['strategy1_winrate']:<8.1f} "
                       f"{result['strategy1_return']:<8.2f} "
                       f"{result['strategy2_trades']:<8} "
                       f"{result['strategy2_winrate']:<8.1f} "
                       f"{result['strategy2_return']:<8.2f}\n")
            else:
                f.write(f"{result['timeframe']:<8} {'ERROR':<8} {'ERROR':<8} {'ERROR':<8} {'ERROR':<8} {'ERROR':<8} {'ERROR':<8}\n")
        
        f.write("\n" + "=" * 60 + "\n")
        
        # Summary statistics
        successful_results = [r for r in results if r['success']]
        if successful_results:
            f.write("SUMMARY STATISTICS:\n")
            
            # Best performing timeframe
            best_9 = max(successful_results, key=lambda x: x['strategy1_return'])
            best_26 = max(successful_results, key=lambda x: x['strategy2_return'])
            
            f.write(f"Best 9-period strategy: {best_9['timeframe']} ({best_9['strategy1_return']:.2f}%)\n")
            f.write(f"Best 26-period strategy: {best_26['timeframe']} ({best_26['strategy2_return']:.2f}%)\n")
            
            # Average performance
            avg_return_9 = sum(r['strategy1_return'] for r in successful_results) / len(successful_results)
            avg_return_26 = sum(r['strategy2_return'] for r in successful_results) / len(successful_results)
            
            f.write(f"Average 9-period return: {avg_return_9:.2f}%\n")
            f.write(f"Average 26-period return: {avg_return_26:.2f}%\n")
            
            # Overall winner
            if avg_return_26 > avg_return_9:
                f.write(f"Overall winner: 26-period strategy\n")
            else:
                f.write(f"Overall winner: 9-period strategy\n")
    
    print(f"\nResults exported to: {filename}")
    return filename

def main():
    if len(sys.argv) < 4:
        print("Usage: python run_all_timeframes.py <symbol> <start_date> <end_date> [initial_balance] [position_size]")
        print("Example: python run_all_timeframes.py BTCUSDT 2025-04-01 2025-06-30 1000 0.2")
        sys.exit(1)
    
    symbol = sys.argv[1].upper()
    start_date = sys.argv[2]
    end_date = sys.argv[3]
    initial_balance = float(sys.argv[4]) if len(sys.argv) > 4 else 1000
    position_size = float(sys.argv[5]) if len(sys.argv) > 5 else 0.2
    
    # Chạy backtest cho tất cả timeframes
    results = run_all_timeframes(
        symbol, start_date, end_date,
        initial_balance, position_size
    )
    
    # Xuất kết quả ra file txt
    export_results_to_txt(results, symbol, start_date, end_date)
    
    # In kết quả tóm tắt
    print(f"\n=== FINAL SUMMARY ===")
    print(f"{'Timeframe':<8} {'9 Periods':<20} {'26 Periods':<20}")
    print(f"{'':<8} {'Trades':<8} {'Winrate':<8} {'Return':<8} {'Trades':<8} {'Winrate':<8} {'Return':<8}")
    print("-" * 50)
    
    for result in results:
        if result['success']:
            print(f"{result['timeframe']:<8} "
                  f"{result['strategy1_trades']:<8} "
                  f"{result['strategy1_winrate']:<8.1f} "
                  f"{result['strategy1_return']:<8.2f} "
                  f"{result['strategy2_trades']:<8} "
                  f"{result['strategy2_winrate']:<8.1f} "
                  f"{result['strategy2_return']:<8.2f}")
        else:
            print(f"{result['timeframe']:<8} {'ERROR':<8} {'ERROR':<8} {'ERROR':<8} {'ERROR':<8} {'ERROR':<8} {'ERROR':<8}")

if __name__ == "__main__":
    main() 