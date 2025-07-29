#!/usr/bin/env python3
"""
Triple Top & Triple Bottom Pattern Strategy với Nến Đảo Chiều - So sánh 2 phương án
- Phát hiện triple top/bottom breakout
- Vào lệnh ở giá đóng nến của các nến đảo chiều đơn sau breakout
- So sánh 2 phương án: Chốt lệnh sau 9 nến vs 26 nến
"""

import sys
import json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import logging
import ta
import os

# Import các hàm nhận diện nến đảo chiều
from rsi14_candlestick_confluence import (
    detect_bullish_engulfing, detect_hammer, detect_bullish_doji,
    detect_bearish_engulfing, detect_shooting_star, detect_bearish_doji
)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TriplePatternReversalCandleStrategy:
    def __init__(self, initial_capital: float = 1000, timeframe: str = '6h', symbol: str = 'BTCUSDT'):
        self.initial_capital = float(initial_capital)
        self.symbol = symbol
        self.timeframe = timeframe
        
        # Pattern detection parameters
        self.lookback_period = 40  # Look back 40 candles for pattern detection
        self.price_threshold = 0.05  # 5% threshold for pattern confirmation
        
        # Trading parameters
        self.position_size_pct = 0.2  # 20% of capital per trade
        
        # Fee structure
        self.maker_fee = 0.001  # 0.1%
        self.taker_fee = 0.001  # 0.1%
        
        logger.info(f"Triple Pattern Reversal Candle Strategy: Initialized with ${self.initial_capital}")
        logger.info(f"Symbol: {self.symbol}, Timeframe: {self.timeframe}")
    
    def load_local_data(self, symbol):
        """Load local CSV data for a symbol"""
        file_path = f"binance_data/{symbol}_{self.timeframe}.csv"
        if not os.path.exists(file_path):
            logger.warning(f"Local data file not found: {file_path}")
            return None
        
        df = pd.read_csv(file_path)
        
        # Ensure timestamp is datetime
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
        else:
            df['timestamp'] = pd.to_datetime(df.iloc[:,0])
        
        # Ensure numeric columns
        for col in ['open', 'high', 'low', 'close', 'volume']:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        df = df.sort_values('timestamp').reset_index(drop=True)
        return df
    
    def detect_triple_top(self, df):
        """Detect triple top pattern"""
        if len(df) < self.lookback_period:
            return False, None, None
        
        window = df.tail(self.lookback_period)
        highs = window['high']
        
        if highs.empty:
            return False, None, None
        
        # Tìm 3 đỉnh cao nhất
        peaks_idx = highs.nlargest(3).index.tolist()
        if len(peaks_idx) < 3:
            return False, None, None
        
        # Sắp xếp theo thời gian
        peaks = sorted([(i, window.loc[i]) for i in peaks_idx], key=lambda x: x[0])
        idx1, p1 = peaks[0]
        idx2, p2 = peaks[1] 
        idx3, p3 = peaks[2]
        
        # Kiểm tra giá 3 đỉnh gần bằng nhau
        max_high = max(p1['high'], p2['high'], p3['high'])
        min_high = min(p1['high'], p2['high'], p3['high'])
        
        if (max_high - min_high) / max_high > self.price_threshold:
            return False, None, None
        
        # Tìm support level (đáy thấp nhất giữa các đỉnh)
        left = min(idx1, idx2, idx3)
        right = max(idx1, idx2, idx3)
        trough_data = window.loc[left:right]
        
        if trough_data.empty or 'low' not in trough_data:
            return False, None, None
        
        support_level = trough_data['low'].min()
        resistance_level = np.mean([p1['high'], p2['high'], p3['high']])
        
        return True, support_level, resistance_level
    
    def detect_triple_bottom(self, df):
        """Detect triple bottom pattern"""
        if len(df) < self.lookback_period:
            return False, None, None
        
        window = df.tail(self.lookback_period)
        lows = window['low']
        
        if lows.empty:
            return False, None, None
        
        # Tìm 3 đáy thấp nhất
        troughs_idx = lows.nsmallest(3).index.tolist()
        if len(troughs_idx) < 3:
            return False, None, None
        
        # Sắp xếp theo thời gian
        troughs = sorted([(i, window.loc[i]) for i in troughs_idx], key=lambda x: x[0])
        idx1, t1 = troughs[0]
        idx2, t2 = troughs[1]
        idx3, t3 = troughs[2]
        
        # Kiểm tra giá 3 đáy gần bằng nhau
        max_low = max(t1['low'], t2['low'], t3['low'])
        min_low = min(t1['low'], t2['low'], t3['low'])
        
        if (max_low - min_low) / max_low > self.price_threshold:
            return False, None, None
        
        # Tìm resistance level (đỉnh cao nhất giữa các đáy)
        left = min(idx1, idx2, idx3)
        right = max(idx1, idx2, idx3)
        peak_data = window.loc[left:right]
        
        if peak_data.empty or 'high' not in peak_data:
            return False, None, None
        
        resistance_level = peak_data['high'].max()
        support_level = np.mean([t1['low'], t2['low'], t3['low']])
        
        return True, support_level, resistance_level
    
    def is_bullish_reversal_candle(self, df):
        """Kiểm tra nến đảo chiều tăng"""
        if len(df) < 2:
            return False
        
        return (
            detect_hammer(df).iloc[-1] or
            detect_bullish_engulfing(df).iloc[-1] or
            detect_bullish_doji(df).iloc[-1]
        )
    
    def is_bearish_reversal_candle(self, df):
        """Kiểm tra nến đảo chiều giảm"""
        if len(df) < 2:
            return False
        
        return (
            detect_shooting_star(df).iloc[-1] or
            detect_bearish_engulfing(df).iloc[-1] or
            detect_bearish_doji(df).iloc[-1]
        )
    
    def should_buy(self, df):
        """Kiểm tra điều kiện mua - Triple bottom breakout với nến đảo chiều tăng"""
        if len(df) < self.lookback_period:
            return False, None, None
        
        # Detect triple bottom
        has_pattern, support_level, resistance_level = self.detect_triple_bottom(df)
        if not has_pattern:
            return False, None, None
        
        current_close = df.iloc[-1]['close']
        
        # Kiểm tra breakout (giá vượt resistance)
        if current_close > resistance_level:
            # Kiểm tra nến đảo chiều tăng
            if self.is_bullish_reversal_candle(df):
                return True, current_close, 'triple_bottom_breakout'
        
        return False, None, None
    
    def should_sell(self, df):
        """Kiểm tra điều kiện bán - Triple top breakdown với nến đảo chiều giảm"""
        if len(df) < self.lookback_period:
            return False, None, None
        
        # Detect triple top
        has_pattern, support_level, resistance_level = self.detect_triple_top(df)
        if not has_pattern:
            return False, None, None
        
        current_close = df.iloc[-1]['close']
        
        # Kiểm tra breakdown (giá xuống dưới support)
        if current_close < support_level:
            # Kiểm tra nến đảo chiều giảm
            if self.is_bearish_reversal_candle(df):
                return True, current_close, 'triple_top_breakdown'
        
        return False, None, None
    
    def backtest_strategy(self, df, exit_bars, strategy_name):
        """Backtest cho một phương án cụ thể"""
        capital = self.initial_capital
        positions = {}
        trades = []
        
        for i in range(self.lookback_period, len(df)):
            current_time = df.iloc[i]['timestamp']
            current_window = df.iloc[:i+1]
            
            # Update bars held for existing positions
            for symbol in positions:
                positions[symbol]['bars_held'] += 1
            
            # Check exit conditions first
            for symbol in list(positions.keys()):
                position = positions[symbol]
                if position['bars_held'] >= exit_bars:
                    current_price = df.iloc[i]['close']
                    
                    # Tính profit/loss
                    quantity = position['quantity']
                    entry_price = position['entry_price']
                    side = position['side']
                    
                    proceeds = quantity * current_price
                    fee = proceeds * self.taker_fee
                    net_proceeds = proceeds - fee
                    
                    if side == 'long':
                        profit = net_proceeds - (quantity * entry_price)
                    else:  # short
                        profit = (quantity * entry_price) - net_proceeds
                    
                    capital += net_proceeds
                    
                    trade = {
                        'entry_time': position['entry_time'],
                        'exit_time': current_time,
                        'side': side,
                        'entry_price': entry_price,
                        'exit_price': current_price,
                        'quantity': quantity,
                        'profit': profit,
                        'pattern': position['pattern'],
                        'bars_held': position['bars_held'],
                        'strategy': strategy_name
                    }
                    trades.append(trade)
                    
                    del positions[symbol]
            
            # Check entry conditions if no position
            if self.symbol not in positions:
                # Check for buy signal (triple bottom breakout)
                should_buy, buy_price, buy_pattern = self.should_buy(current_window)
                if should_buy:
                    # Execute buy
                    position_value = capital * self.position_size_pct
                    quantity = position_value / buy_price
                    fee = quantity * buy_price * self.taker_fee
                    actual_quantity = (position_value - fee) / buy_price
                    
                    if actual_quantity > 0:
                        positions[self.symbol] = {
                            'side': 'long',
                            'quantity': actual_quantity,
                            'entry_price': buy_price,
                            'entry_time': current_time,
                            'pattern': buy_pattern,
                            'bars_held': 0
                        }
                        capital -= position_value
                
                # Check for sell signal (triple top breakdown) 
                should_sell, sell_price, sell_pattern = self.should_sell(current_window)
                if should_sell:
                    # Execute sell
                    position_value = capital * self.position_size_pct
                    quantity = position_value / sell_price
                    fee = quantity * sell_price * self.taker_fee
                    actual_quantity = (position_value - fee) / sell_price
                    
                    if actual_quantity > 0:
                        positions[self.symbol] = {
                            'side': 'short',
                            'quantity': actual_quantity,
                            'entry_price': sell_price,
                            'entry_time': current_time,
                            'pattern': sell_pattern,
                            'bars_held': 0
                        }
                        capital -= position_value
        
        # Close any remaining positions
        for symbol in list(positions.keys()):
            final_price = df.iloc[-1]['close']
            final_time = df.iloc[-1]['timestamp']
            
            position = positions[symbol]
            quantity = position['quantity']
            entry_price = position['entry_price']
            side = position['side']
            
            proceeds = quantity * final_price
            fee = proceeds * self.taker_fee
            net_proceeds = proceeds - fee
            
            if side == 'long':
                profit = net_proceeds - (quantity * entry_price)
            else:  # short
                profit = (quantity * entry_price) - net_proceeds
            
            capital += net_proceeds
            
            trade = {
                'entry_time': position['entry_time'],
                'exit_time': final_time,
                'side': side,
                'entry_price': entry_price,
                'exit_price': final_price,
                'quantity': quantity,
                'profit': profit,
                'pattern': position['pattern'],
                'bars_held': position['bars_held'],
                'strategy': strategy_name
            }
            trades.append(trade)
        
        return trades, capital
    
    def run_backtest(self, start_date, end_date):
        """Chạy backtest cho cả 2 phương án"""
        logger.info(f"Starting Triple Pattern Reversal Candle backtest from {start_date} to {end_date}")
        
        # Load data
        df = self.load_local_data(self.symbol)
        if df is None:
            logger.error(f"Could not load data for {self.symbol}")
            return
        
        # Filter data by date range
        start_dt = pd.to_datetime(start_date)
        end_dt = pd.to_datetime(end_date)
        df = df[(df['timestamp'] >= start_dt) & (df['timestamp'] <= end_dt)].reset_index(drop=True)
        
        logger.info(f"Loaded {len(df)} candles for {self.symbol}")
        
        # Run backtest for both strategies
        logger.info("Running strategy 1: Exit after 9 bars")
        trades_9, capital_9 = self.backtest_strategy(df, 9, 'exit_9_bars')
        
        logger.info("Running strategy 2: Exit after 26 bars")
        trades_26, capital_26 = self.backtest_strategy(df, 26, 'exit_26_bars')
        
        # Generate comparison report
        self.generate_comparison_report(trades_9, capital_9, trades_26, capital_26)
    
    def generate_comparison_report(self, trades_9, capital_9, trades_26, capital_26):
        """Tạo báo cáo so sánh 2 phương án"""
        
        def calc_stats(trades, capital):
            total_trades = len(trades)
            winning_trades = len([t for t in trades if t['profit'] > 0])
            losing_trades = total_trades - winning_trades
            
            total_profit = sum([t['profit'] for t in trades])
            avg_profit = total_profit / total_trades if total_trades > 0 else 0
            win_rate = winning_trades / total_trades * 100 if total_trades > 0 else 0
            
            total_return = (capital - self.initial_capital) / self.initial_capital * 100
            
            long_trades = [t for t in trades if t['side'] == 'long']
            short_trades = [t for t in trades if t['side'] == 'short']
            
            return {
                'total_trades': total_trades,
                'winning_trades': winning_trades,
                'losing_trades': losing_trades,
                'total_profit': total_profit,
                'avg_profit': avg_profit,
                'win_rate': win_rate,
                'final_capital': capital,
                'total_return': total_return,
                'long_trades': long_trades,
                'short_trades': short_trades
            }
        
        stats_9 = calc_stats(trades_9, capital_9)
        stats_26 = calc_stats(trades_26, capital_26)
        
        # Tạo file báo cáo so sánh
        filename = f"triple_pattern_comparison_{self.symbol.lower()}_{self.timeframe}.md"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# So sánh Triple Pattern Reversal Candle Strategy - {self.symbol.upper()} ({self.timeframe})\n\n")
            
            f.write("## Tổng quan chiến lược\n")
            f.write("- **Phát hiện**: Triple top/bottom pattern\n")
            f.write("- **Vào lệnh**: Khi có breakout/breakdown + nến đảo chiều\n")
            f.write("- **Nến đảo chiều tăng**: Hammer, Bullish Engulfing, Bullish Doji\n")
            f.write("- **Nến đảo chiều giảm**: Shooting Star, Bearish Engulfing, Bearish Doji\n")
            f.write("- **So sánh**: 2 phương án chốt lệnh khác nhau\n\n")
            
            f.write("## So sánh kết quả tổng quan\n")
            f.write("| Chỉ số | Chốt sau 9 nến | Chốt sau 26 nến |\n")
            f.write("|--------|----------------|------------------|\n")
            f.write(f"| **Vốn cuối kỳ** | ${stats_9['final_capital']:,.2f} | ${stats_26['final_capital']:,.2f} |\n")
            f.write(f"| **Tổng lợi nhuận** | ${stats_9['total_profit']:,.2f} | ${stats_26['total_profit']:,.2f} |\n")
            f.write(f"| **Tỷ suất sinh lời** | {stats_9['total_return']:.2f}% | {stats_26['total_return']:.2f}% |\n")
            f.write(f"| **Tổng số lệnh** | {stats_9['total_trades']} | {stats_26['total_trades']} |\n")
            f.write(f"| **Lệnh thắng** | {stats_9['winning_trades']} | {stats_26['winning_trades']} |\n")
            f.write(f"| **Lệnh thua** | {stats_9['losing_trades']} | {stats_26['losing_trades']} |\n")
            f.write(f"| **Tỷ lệ thắng** | {stats_9['win_rate']:.2f}% | {stats_26['win_rate']:.2f}% |\n")
            f.write(f"| **Lợi nhuận TB/lệnh** | ${stats_9['avg_profit']:.2f} | ${stats_26['avg_profit']:.2f} |\n\n")
            
            # Phân tích kết quả
            f.write("## Phân tích\n")
            if stats_26['total_return'] > stats_9['total_return']:
                f.write(f"✅ **Phương án chốt sau 26 nến tốt hơn** với tỷ suất sinh lời {stats_26['total_return']:.2f}% so với {stats_9['total_return']:.2f}%\n\n")
            else:
                f.write(f"✅ **Phương án chốt sau 9 nến tốt hơn** với tỷ suất sinh lời {stats_9['total_return']:.2f}% so với {stats_26['total_return']:.2f}%\n\n")
            
            f.write("## Chi tiết phương án 1: Chốt sau 9 nến\n")
            f.write("### Thống kê theo hướng giao dịch\n")
            
            # Long trades cho 9 nến
            if stats_9['long_trades']:
                long_profit_9 = sum([t['profit'] for t in stats_9['long_trades']])
                long_win_9 = len([t for t in stats_9['long_trades'] if t['profit'] > 0])
                long_win_rate_9 = long_win_9 / len(stats_9['long_trades']) * 100
                f.write(f"**Long (Triple Bottom Breakout)**\n")
                f.write(f"- Số lệnh: {len(stats_9['long_trades'])}\n")
                f.write(f"- Lệnh thắng: {long_win_9}\n")
                f.write(f"- Tỷ lệ thắng: {long_win_rate_9:.2f}%\n")
                f.write(f"- Lợi nhuận: ${long_profit_9:.2f}\n\n")
            
            # Short trades cho 9 nến
            if stats_9['short_trades']:
                short_profit_9 = sum([t['profit'] for t in stats_9['short_trades']])
                short_win_9 = len([t for t in stats_9['short_trades'] if t['profit'] > 0])
                short_win_rate_9 = short_win_9 / len(stats_9['short_trades']) * 100
                f.write(f"**Short (Triple Top Breakdown)**\n")
                f.write(f"- Số lệnh: {len(stats_9['short_trades'])}\n")
                f.write(f"- Lệnh thắng: {short_win_9}\n")
                f.write(f"- Tỷ lệ thắng: {short_win_rate_9:.2f}%\n")
                f.write(f"- Lợi nhuận: ${short_profit_9:.2f}\n\n")
            
            f.write("### Chi tiết các giao dịch (9 nến)\n")
            f.write("| Thời gian vào | Thời gian ra | Hướng | Giá vào | Giá ra | Số lượng | Lợi nhuận | Pattern | Nến giữ |\n")
            f.write("|---------------|--------------|-------|---------|---------|----------|-----------|---------|----------|\n")
            
            for trade in trades_9:
                f.write(f"| {trade['entry_time']} | {trade['exit_time']} | {trade['side'].upper()} | "
                       f"{trade['entry_price']:.2f} | {trade['exit_price']:.2f} | {trade['quantity']:.4f} | "
                       f"{trade['profit']:.2f} | {trade['pattern']} | {trade['bars_held']} |\n")
            
            f.write("\n---\n")
            f.write("## Chi tiết phương án 2: Chốt sau 26 nến\n")
            f.write("### Thống kê theo hướng giao dịch\n")
            
            # Long trades cho 26 nến
            if stats_26['long_trades']:
                long_profit_26 = sum([t['profit'] for t in stats_26['long_trades']])
                long_win_26 = len([t for t in stats_26['long_trades'] if t['profit'] > 0])
                long_win_rate_26 = long_win_26 / len(stats_26['long_trades']) * 100
                f.write(f"**Long (Triple Bottom Breakout)**\n")
                f.write(f"- Số lệnh: {len(stats_26['long_trades'])}\n")
                f.write(f"- Lệnh thắng: {long_win_26}\n")
                f.write(f"- Tỷ lệ thắng: {long_win_rate_26:.2f}%\n")
                f.write(f"- Lợi nhuận: ${long_profit_26:.2f}\n\n")
            
            # Short trades cho 26 nến
            if stats_26['short_trades']:
                short_profit_26 = sum([t['profit'] for t in stats_26['short_trades']])
                short_win_26 = len([t for t in stats_26['short_trades'] if t['profit'] > 0])
                short_win_rate_26 = short_win_26 / len(stats_26['short_trades']) * 100
                f.write(f"**Short (Triple Top Breakdown)**\n")
                f.write(f"- Số lệnh: {len(stats_26['short_trades'])}\n")
                f.write(f"- Lệnh thắng: {short_win_26}\n")
                f.write(f"- Tỷ lệ thắng: {short_win_rate_26:.2f}%\n")
                f.write(f"- Lợi nhuận: ${short_profit_26:.2f}\n\n")
            
            f.write("### Chi tiết các giao dịch (26 nến)\n")
            f.write("| Thời gian vào | Thời gian ra | Hướng | Giá vào | Giá ra | Số lượng | Lợi nhuận | Pattern | Nến giữ |\n")
            f.write("|---------------|--------------|-------|---------|---------|----------|-----------|---------|----------|\n")
            
            for trade in trades_26:
                f.write(f"| {trade['entry_time']} | {trade['exit_time']} | {trade['side'].upper()} | "
                       f"{trade['entry_price']:.2f} | {trade['exit_price']:.2f} | {trade['quantity']:.4f} | "
                       f"{trade['profit']:.2f} | {trade['pattern']} | {trade['bars_held']} |\n")
            
            f.write(f"\n**Lưu ý**: Mỗi lệnh sử dụng {self.position_size_pct*100}% vốn. So sánh 2 phương án chốt lệnh khác nhau.\n")
        
        logger.info(f"Comparison report generated: {filename}")
        logger.info(f"Strategy 1 (9 bars): {stats_9['total_trades']} trades, {stats_9['win_rate']:.2f}% win rate, {stats_9['total_return']:.2f}% return")
        logger.info(f"Strategy 2 (26 bars): {stats_26['total_trades']} trades, {stats_26['win_rate']:.2f}% win rate, {stats_26['total_return']:.2f}% return")

def main():
    if len(sys.argv) < 5:
        print("Usage: python triple_pattern_reversal_candle_strategy.py <start_date> <end_date> <initial_capital> <timeframe> [symbol]")
        print("Example: python triple_pattern_reversal_candle_strategy.py 2024-07-01 2024-12-31 1000 6h BTCUSDT")
        sys.exit(1)
    
    start_date = sys.argv[1]
    end_date = sys.argv[2]
    initial_capital = float(sys.argv[3])
    timeframe = sys.argv[4]
    symbol = sys.argv[5] if len(sys.argv) > 5 else 'BTCUSDT'
    
    strategy = TriplePatternReversalCandleStrategy(initial_capital, timeframe, symbol)
    strategy.run_backtest(start_date, end_date)

if __name__ == "__main__":
    main() 