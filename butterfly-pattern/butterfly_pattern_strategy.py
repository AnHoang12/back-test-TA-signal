#!/usr/bin/env python3
"""
Butterfly Pattern Strategy
Détection des patterns Butterfly (Bullish/Bearish) et backtesting avec 2 stratégies de sortie:
- Stratégie 1: Sortie après 9 périodes
- Stratégie 2: Sortie après 26 périodes
"""

import sys
import os
import pandas as pd
import numpy as np
import logging
from datetime import datetime, timedelta
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ButterflyPatternStrategy:
    def __init__(self, initial_capital=1000.0):
        self.initial_capital = initial_capital
    
    def load_local_data(self, symbol, timeframe):
        """Load data from local CSV files"""
        try:
            # Try multiple possible paths
            possible_paths = [
                f"binance_data/{symbol}_{timeframe}.csv",
                f"../binance_data/{symbol}_{timeframe}.csv", 
                f"agent/binance_data/{symbol}_{timeframe}.csv"
            ]
            
            for path in possible_paths:
                if os.path.exists(path):
                    logger.info(f"Loading data from: {path}")
                    df = pd.read_csv(path)
                    break
            else:
                raise FileNotFoundError(f"No data file found for {symbol}_{timeframe}")
            
            # Ensure proper column names
            expected_columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
            if len(df.columns) >= 6:
                df.columns = expected_columns[:len(df.columns)]
            
            # Convert timestamp to datetime
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            
            # Ensure numeric columns
            numeric_columns = ['open', 'high', 'low', 'close', 'volume']
            for col in numeric_columns:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
            
            df = df.dropna()
            df = df.sort_values('timestamp').reset_index(drop=True)
            
            logger.info(f"Loaded {len(df)} candles for {symbol}")
            return df
            
        except Exception as e:
            logger.error(f"Error loading local data: {e}")
            return None
    
    def detect_swing_points(self, df, window=3):  # Giảm từ 5 xuống 3
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
    
    def is_within_tolerance(self, actual, expected, tolerance=0.15):  # Tăng từ 0.05 lên 0.15
        """Check if actual value is within tolerance of expected Fibonacci ratio"""
        return abs(actual - expected) / expected <= tolerance
    
    def detect_bullish_butterfly(self, df, i):
        """
        Detect Bullish Butterfly Pattern
        X-A-B-C-D structure where D is the entry point
        Ratios:
        - AB = 0.786 of XA
        - BC = 0.382 or 0.886 of AB  
        - CD = 1.27 or 1.618 of BC
        - AD = 0.786 of XA
        """
        if i < 15:  # Giảm từ 20 xuống 15
            return False, None
        
        # Look for swing points in recent history
        recent_data = df.iloc[max(0, i-15):i+1]  # Giảm từ 20 xuống 15
        
        # Find potential X, A, B, C points
        swing_highs = recent_data[recent_data['swing_high'] == True]
        swing_lows = recent_data[recent_data['swing_low'] == True]
        
        if len(swing_highs) < 2 or len(swing_lows) < 2:
            return False, None
        
        # Get the most recent swing points
        try:
            # For bullish butterfly: X(low), A(high), B(low), C(high), D(low - current)
            C = swing_highs.iloc[-1]  # Most recent high
            B = swing_lows.iloc[-1]   # Most recent low before C
            A = swing_highs.iloc[-2] if len(swing_highs) >= 2 else None
            X = swing_lows.iloc[-2] if len(swing_lows) >= 2 else None
            
            if A is None or X is None:
                return False, None
            
            # Current point D (potential entry)
            D_price = df.loc[i, 'low']
            
            # Calculate ratios
            XA = abs(A['high'] - X['low'])
            AB = abs(B['low'] - A['high']) 
            BC = abs(C['high'] - B['low'])
            CD = abs(D_price - C['high'])
            AD = abs(D_price - A['high'])
            
            if XA == 0 or AB == 0 or BC == 0:
                return False, None
            
            # Check Fibonacci ratios
            AB_XA_ratio = AB / XA
            BC_AB_ratio = BC / AB
            CD_BC_ratio = CD / BC if BC > 0 else 0
            AD_XA_ratio = AD / XA
            
            # Butterfly pattern ratios (with increased tolerance)
            valid_AB = self.is_within_tolerance(AB_XA_ratio, 0.786, 0.2)  # Tăng tolerance
            valid_BC = (self.is_within_tolerance(BC_AB_ratio, 0.382, 0.2) or 
                       self.is_within_tolerance(BC_AB_ratio, 0.886, 0.2))
            valid_CD = (self.is_within_tolerance(CD_BC_ratio, 1.27, 0.25) or
                       self.is_within_tolerance(CD_BC_ratio, 1.618, 0.25))
            valid_AD = self.is_within_tolerance(AD_XA_ratio, 0.786, 0.2)
            
            if valid_AB and valid_BC and valid_CD and valid_AD:
                # Đơn giản hóa: Bỏ điều kiện D < X
                pattern_info = {
                    'type': 'bullish_butterfly',
                    'X': X['low'],
                    'A': A['high'], 
                    'B': B['low'],
                    'C': C['high'],
                    'D': D_price,
                    'ratios': {
                        'AB_XA': AB_XA_ratio,
                        'BC_AB': BC_AB_ratio, 
                        'CD_BC': CD_BC_ratio,
                        'AD_XA': AD_XA_ratio
                    }
                }
                return True, pattern_info
        
        except Exception as e:
            logger.debug(f"Error in bullish butterfly detection: {e}")
        
        return False, None
    
    def detect_bearish_butterfly(self, df, i):
        """
        Detect Bearish Butterfly Pattern  
        X-A-B-C-D structure where D is the entry point
        Similar ratios but inverted structure
        """
        if i < 15:  # Giảm từ 20 xuống 15
            return False, None
        
        recent_data = df.iloc[max(0, i-15):i+1]  # Giảm từ 20 xuống 15
        
        swing_highs = recent_data[recent_data['swing_high'] == True]
        swing_lows = recent_data[recent_data['swing_low'] == True]
        
        if len(swing_highs) < 2 or len(swing_lows) < 2:
            return False, None
        
        try:
            # For bearish butterfly: X(high), A(low), B(high), C(low), D(high - current)
            C = swing_lows.iloc[-1]   # Most recent low
            B = swing_highs.iloc[-1]  # Most recent high before C  
            A = swing_lows.iloc[-2] if len(swing_lows) >= 2 else None
            X = swing_highs.iloc[-2] if len(swing_highs) >= 2 else None
            
            if A is None or X is None:
                return False, None
            
            D_price = df.loc[i, 'high']
            
            # Calculate ratios
            XA = abs(A['low'] - X['high'])
            AB = abs(B['high'] - A['low'])
            BC = abs(C['low'] - B['high']) 
            CD = abs(D_price - C['low'])
            AD = abs(D_price - A['low'])
            
            if XA == 0 or AB == 0 or BC == 0:
                return False, None
            
            AB_XA_ratio = AB / XA
            BC_AB_ratio = BC / AB
            CD_BC_ratio = CD / BC if BC > 0 else 0
            AD_XA_ratio = AD / XA
            
            # Check ratios with increased tolerance
            valid_AB = self.is_within_tolerance(AB_XA_ratio, 0.786, 0.2)
            valid_BC = (self.is_within_tolerance(BC_AB_ratio, 0.382, 0.2) or
                       self.is_within_tolerance(BC_AB_ratio, 0.886, 0.2))
            valid_CD = (self.is_within_tolerance(CD_BC_ratio, 1.27, 0.25) or
                       self.is_within_tolerance(CD_BC_ratio, 1.618, 0.25))
            valid_AD = self.is_within_tolerance(AD_XA_ratio, 0.786, 0.2)
            
            if valid_AB and valid_BC and valid_CD and valid_AD:
                # Đơn giản hóa: Bỏ điều kiện D > X
                pattern_info = {
                    'type': 'bearish_butterfly',
                    'X': X['high'],
                    'A': A['low'],
                    'B': B['high'], 
                    'C': C['low'],
                    'D': D_price,
                    'ratios': {
                        'AB_XA': AB_XA_ratio,
                        'BC_AB': BC_AB_ratio,
                        'CD_BC': CD_BC_ratio, 
                        'AD_XA': AD_XA_ratio
                    }
                }
                return True, pattern_info
        
        except Exception as e:
            logger.debug(f"Error in bearish butterfly detection: {e}")
        
        return False, None
    
    def backtest_strategy(self, df, exit_bars, strategy_name):
        """Backtest butterfly strategy with specific exit bars"""
        capital = self.initial_capital
        positions = []
        trades = []
        
        # Add swing point detection
        df = self.detect_swing_points(df)
        
        for i in range(15, len(df)):  # Giảm từ 20 xuống 15
            current_date = df.loc[i, 'timestamp']
            current_close = df.loc[i, 'close']
            
            # Close existing positions that have reached exit time
            positions_to_close = []
            for pos_idx, position in enumerate(positions):
                bars_held = i - position['entry_index']
                if bars_held >= exit_bars:
                    positions_to_close.append(pos_idx)
            
            # Close positions (reverse order to maintain indices)
            for pos_idx in reversed(positions_to_close):
                position = positions[pos_idx]
                exit_price = current_close
                
                if position['type'] == 'long':
                    pnl = (exit_price - position['entry_price']) * position['quantity']
                else:  # short
                    pnl = (position['entry_price'] - exit_price) * position['quantity']
                
                capital += position['value'] + pnl
                
                trade_record = {
                    'entry_date': position['entry_date'],
                    'exit_date': current_date, 
                    'type': position['type'],
                    'entry_price': position['entry_price'],
                    'exit_price': exit_price,
                    'quantity': position['quantity'],
                    'pnl': pnl,
                    'pnl_percent': (pnl / position['value']) * 100,
                    'bars_held': exit_bars,
                    'pattern_info': position['pattern_info']
                }
                trades.append(trade_record)
                positions.pop(pos_idx)
            
            # Look for new patterns to enter
            if len(positions) == 0:  # Only enter if no existing positions
                # Check for bullish butterfly
                is_bullish, bullish_info = self.detect_bullish_butterfly(df, i)
                if is_bullish:
                    # Enter long position
                    position_value = capital * 0.95  # Use 95% of capital
                    quantity = position_value / current_close
                    
                    position = {
                        'type': 'long',
                        'entry_date': current_date,
                        'entry_index': i,
                        'entry_price': current_close,
                        'quantity': quantity,
                        'value': position_value,
                        'pattern_info': bullish_info
                    }
                    positions.append(position)
                    capital -= position_value
                    
                    logger.info(f"LONG entry at {current_date}: {current_close:.4f} (Bullish Butterfly)")
                
                # Check for bearish butterfly
                is_bearish, bearish_info = self.detect_bearish_butterfly(df, i)
                if is_bearish:
                    # Enter short position
                    position_value = capital * 0.95
                    quantity = position_value / current_close
                    
                    position = {
                        'type': 'short', 
                        'entry_date': current_date,
                        'entry_index': i,
                        'entry_price': current_close,
                        'quantity': quantity,
                        'value': position_value,
                        'pattern_info': bearish_info
                    }
                    positions.append(position)
                    capital -= position_value
                    
                    logger.info(f"SHORT entry at {current_date}: {current_close:.4f} (Bearish Butterfly)")
        
        # Close any remaining positions at the end
        if positions:
            final_close = df.iloc[-1]['close']
            final_date = df.iloc[-1]['timestamp']
            
            for position in positions:
                if position['type'] == 'long':
                    pnl = (final_close - position['entry_price']) * position['quantity']
                else:
                    pnl = (position['entry_price'] - final_close) * position['quantity']
                
                capital += position['value'] + pnl
                
                bars_held = len(df) - 1 - position['entry_index']
                trade_record = {
                    'entry_date': position['entry_date'],
                    'exit_date': final_date,
                    'type': position['type'], 
                    'entry_price': position['entry_price'],
                    'exit_price': final_close,
                    'quantity': position['quantity'],
                    'pnl': pnl,
                    'pnl_percent': (pnl / position['value']) * 100,
                    'bars_held': bars_held,
                    'pattern_info': position['pattern_info']
                }
                trades.append(trade_record)
        
        return trades, capital
    
    def run_backtest(self, symbol, timeframe, start_date, end_date):
        """Run backtest for both exit strategies"""
        logger.info(f"Starting Butterfly Pattern backtest from {start_date} to {end_date}")
        
        # Load data
        df = self.load_local_data(symbol, timeframe)
        if df is None:
            logger.error("Failed to load data")
            return
        
        # Filter by date range
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        start_dt = pd.to_datetime(start_date)
        end_dt = pd.to_datetime(end_date)
        df = df[(df['timestamp'] >= start_dt) & (df['timestamp'] <= end_dt)]
        
        if df.empty:
            logger.error("No data in specified date range")
            return
        
        df = df.reset_index(drop=True)
        logger.info(f"Loaded {len(df)} candles for {symbol}")
        
        # Run both strategies
        logger.info("Running strategy 1: Exit after 9 bars")
        trades_9, capital_9 = self.backtest_strategy(df, 9, 'exit_9_bars')
        
        logger.info("Running strategy 2: Exit after 26 bars") 
        trades_26, capital_26 = self.backtest_strategy(df, 26, 'exit_26_bars')
        
        # Generate comparison report
        self.generate_comparison_report(symbol, timeframe, trades_9, capital_9, trades_26, capital_26)
        
        # Log summary
        return_9 = ((capital_9 - self.initial_capital) / self.initial_capital) * 100
        return_26 = ((capital_26 - self.initial_capital) / self.initial_capital) * 100
        win_rate_9 = (len([t for t in trades_9 if t['pnl'] > 0]) / len(trades_9)) * 100 if trades_9 else 0
        win_rate_26 = (len([t for t in trades_26 if t['pnl'] > 0]) / len(trades_26)) * 100 if trades_26 else 0
        
        logger.info(f"Strategy 1 (9 bars): {len(trades_9)} trades, {win_rate_9:.2f}% win rate, {return_9:.2f}% return")
        logger.info(f"Strategy 2 (26 bars): {len(trades_26)} trades, {win_rate_26:.2f}% win rate, {return_26:.2f}% return")
    
    def generate_comparison_report(self, symbol, timeframe, trades_9, capital_9, trades_26, capital_26):
        """Generate markdown comparison report"""
        
        def calculate_stats(trades, capital):
            if not trades:
                return {
                    'total_trades': 0,
                    'winning_trades': 0,
                    'losing_trades': 0,
                    'win_rate': 0,
                    'total_pnl': 0,
                    'avg_pnl': 0,
                    'best_trade': 0,
                    'worst_trade': 0,
                    'final_capital': capital,
                    'total_return': 0
                }
            
            winning_trades = [t for t in trades if t['pnl'] > 0]
            losing_trades = [t for t in trades if t['pnl'] <= 0]
            
            return {
                'total_trades': len(trades),
                'winning_trades': len(winning_trades),
                'losing_trades': len(losing_trades), 
                'win_rate': (len(winning_trades) / len(trades)) * 100,
                'total_pnl': sum(t['pnl'] for t in trades),
                'avg_pnl': sum(t['pnl'] for t in trades) / len(trades),
                'best_trade': max(t['pnl'] for t in trades),
                'worst_trade': min(t['pnl'] for t in trades),
                'final_capital': capital,
                'total_return': ((capital - self.initial_capital) / self.initial_capital) * 100
            }
        
        stats_9 = calculate_stats(trades_9, capital_9)
        stats_26 = calculate_stats(trades_26, capital_26)
        
        # Generate report
        report_filename = f"butterfly_pattern_comparison_{symbol.lower()}_{timeframe}.md"
        
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write(f"# Butterfly Pattern Strategy Comparison - {symbol} {timeframe}\n\n")
            f.write("## Strategy Overview\n")
            f.write("- **Pattern**: Butterfly Pattern (Bullish & Bearish)\n")
            f.write("- **Entry**: At close price when pattern is detected\n") 
            f.write("- **Exit Strategy 1**: Hold for 9 periods\n")
            f.write("- **Exit Strategy 2**: Hold for 26 periods\n\n")
            
            f.write("## Performance Comparison\n\n")
            f.write("| Metric | 9 Periods | 26 Periods |\n")
            f.write("|--------|-----------|------------|\n")
            f.write(f"| Total Trades | {stats_9['total_trades']} | {stats_26['total_trades']} |\n")
            f.write(f"| Win Rate | {stats_9['win_rate']:.2f}% | {stats_26['win_rate']:.2f}% |\n")
            f.write(f"| Total Return | {stats_9['total_return']:.2f}% | {stats_26['total_return']:.2f}% |\n")
            f.write(f"| Final Capital | ${stats_9['final_capital']:.2f} | ${stats_26['final_capital']:.2f} |\n")
            f.write(f"| Total PnL | ${stats_9['total_pnl']:.2f} | ${stats_26['total_pnl']:.2f} |\n")
            f.write(f"| Average PnL per Trade | ${stats_9['avg_pnl']:.2f} | ${stats_26['avg_pnl']:.2f} |\n")
            f.write(f"| Best Trade | ${stats_9['best_trade']:.2f} | ${stats_26['best_trade']:.2f} |\n")
            f.write(f"| Worst Trade | ${stats_9['worst_trade']:.2f} | ${stats_26['worst_trade']:.2f} |\n\n")
            
            # Trade details for both strategies
            if trades_9:
                f.write("## Strategy 1: Exit after 9 periods\n\n")
                f.write("| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type |\n")
                f.write("|------------|-----------|------|-------------|------------|-----|-------|-------------|\n")
                for trade in trades_9:
                    pattern_type = trade['pattern_info']['type'].replace('_', ' ').title()
                    f.write(f"| {trade['entry_date'].strftime('%Y-%m-%d %H:%M')} | {trade['exit_date'].strftime('%Y-%m-%d %H:%M')} | {trade['type'].upper()} | ${trade['entry_price']:.4f} | ${trade['exit_price']:.4f} | ${trade['pnl']:.2f} | {trade['pnl_percent']:.2f}% | {pattern_type} |\n")
                f.write("\n")
            
            if trades_26:
                f.write("## Strategy 2: Exit after 26 periods\n\n")
                f.write("| Entry Date | Exit Date | Type | Entry Price | Exit Price | PnL | PnL % | Pattern Type |\n")
                f.write("|------------|-----------|------|-------------|------------|-----|-------|-------------|\n") 
                for trade in trades_26:
                    pattern_type = trade['pattern_info']['type'].replace('_', ' ').title()
                    f.write(f"| {trade['entry_date'].strftime('%Y-%m-%d %H:%M')} | {trade['exit_date'].strftime('%Y-%m-%d %H:%M')} | {trade['type'].upper()} | ${trade['entry_price']:.4f} | ${trade['exit_price']:.4f} | ${trade['pnl']:.2f} | {trade['pnl_percent']:.2f}% | {pattern_type} |\n")
                f.write("\n")
            
            f.write("## Analysis\n\n")
            
            if stats_9['total_return'] > stats_26['total_return']:
                f.write("**Winner: 9 Periods Strategy**\n\n")
                f.write(f"The 9-period exit strategy outperformed with {stats_9['total_return']:.2f}% return vs {stats_26['total_return']:.2f}%.\n\n")
            elif stats_26['total_return'] > stats_9['total_return']:
                f.write("**Winner: 26 Periods Strategy**\n\n") 
                f.write(f"The 26-period exit strategy outperformed with {stats_26['total_return']:.2f}% return vs {stats_9['total_return']:.2f}%.\n\n")
            else:
                f.write("**Result: Tie**\n\n")
                f.write("Both strategies achieved similar returns.\n\n")
            
            f.write("### Key Observations:\n")
            f.write(f"- **Trade Frequency**: {stats_9['total_trades']} vs {stats_26['total_trades']} trades\n")
            f.write(f"- **Win Rate Difference**: {stats_9['win_rate']:.2f}% vs {stats_26['win_rate']:.2f}%\n")
            f.write(f"- **Return Difference**: {abs(stats_9['total_return'] - stats_26['total_return']):.2f}% gap\n\n")
            
            if not trades_9 and not trades_26:
                f.write("**Note**: No butterfly patterns were detected in this timeframe and period.\n\n")
            elif not trades_9:
                f.write("**Note**: No trades executed in 9-period strategy.\n\n")
            elif not trades_26:
                f.write("**Note**: No trades executed in 26-period strategy.\n\n")
        
        logger.info(f"Comparison report generated: {report_filename}")

def main():
    if len(sys.argv) != 6:
        print("Usage: python butterfly_pattern_strategy.py <start_date> <end_date> <capital> <timeframe> <symbol>")
        print("Example: python butterfly_pattern_strategy.py 2024-07-01 2024-12-31 1000 6h BTCUSDT")
        sys.exit(1)
    
    start_date = sys.argv[1]
    end_date = sys.argv[2] 
    capital = float(sys.argv[3])
    timeframe = sys.argv[4]
    symbol = sys.argv[5]
    
    strategy = ButterflyPatternStrategy(capital)
    strategy.run_backtest(symbol, timeframe, start_date, end_date)

if __name__ == "__main__":
    main() 