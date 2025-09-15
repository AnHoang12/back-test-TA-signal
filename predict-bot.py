import pandas as pd
import numpy as np
import argparse
from dotenv import load_dotenv
from sqlalchemy import create_engine
from datetime import datetime, timedelta
import os
from enum import Enum
import sys
import importlib.util

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

try:
    print(f"Connecting to DB: {DB_HOST}:{DB_PORT}/{DB_NAME}")
    engine = create_engine(DATABASE_URL)
    print("Connected to DB successfully")
except Exception as e:
    engine = None
    print(f"Failed to connect to DB: {e}")

def get_binance_data(symbol, interval):
    if engine is None:
        print("No valid DB connection.")
        return pd.DataFrame()

    print(f"Getting data from DB: {symbol} {interval}")
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
            params={
                "symbol": symbol,
            },
        )

        if 'open_time' not in df.columns:
            print("Missing 'open_time' column in data returned from DB.")
            return pd.DataFrame()
        
        df['datetime'] = pd.to_datetime(df['open_time'], unit='s')
        
        df = df.sort_values('datetime').reset_index(drop=True)
        print(f"Read {len(df)} rows from DB table {table_name}")
        if len(df) > 0:
            print(f"   Time: {df['datetime'].min()} to {df['datetime'].max()}")
            print(f"   Last price: ${df.iloc[-1]['close']:.4f}")
        
        return df
    except Exception as e:
        print(f"Error reading data from DB: {e}")
        return pd.DataFrame()

class TradeSide(Enum):
    LONG = "LONG"
    SHORT = "SHORT"


class StrategyBase:
    def __init__(self, symbol: str, interval: str, side: TradeSide):
        self.symbol = symbol
        self.interval = interval
        self.side = side
        self.df = get_binance_data(symbol, interval)

    def name(self) -> str:
        return self.__class__.__name__.replace("Strategy", "")

    def run(self):
        print(f"Running {self.name()} {self.side.value} for {self.symbol} {self.interval}")
        # Placeholder: add per-strategy signal generation/backtest here
        print(self.df.tail(3))

    def evaluate_signal_performance(self, signals, direction, horizon):
        """Đánh giá hiệu suất tín hiệu theo horizon (số phiên sau entry)."""
        if self.df.empty:
            return 0.0, 0.0, 0, 0

        direction = direction.lower()
        last_index = len(self.df) - 1

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
            change = self.df.iloc[e + horizon]['close'] - self.df.iloc[e]['close']
            signed_changes.append(change)
            if (direction == 'up' and change > 0) or (direction == 'down' and change < 0):
                correct += 1

        total = len(filtered)
        accuracy = correct / total * 100 if total > 0 else 0.0
        avg_signed_change = float(np.mean(signed_changes)) if signed_changes else 0.0
        return avg_signed_change, accuracy, total, correct

    def evaluate_signal_performance_percent(self, signals, direction, horizon):
        """Đánh giá hiệu suất tín hiệu (theo %) sau horizon phiên."""
        if self.df.empty:
            return 0.0, 0.0, 0, 0

        direction = direction.lower()
        last_index = len(self.df) - 1
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
            start = self.df.iloc[e]['close']
            end = self.df.iloc[e + horizon]['close']
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


class WedgeStrategy(StrategyBase):
    def __init__(self, symbol: str, interval: str, side: TradeSide):
        super().__init__(symbol, interval, side)
        # Import implementation
        from strategy_implementations import WedgeStrategy as WedgeImpl
        self._impl = WedgeImpl()

    def run(self):
        print(f"=== {self.name()} {self.side.value} - {self.symbol} {self.interval} ===")
        
        if self.df.empty:
            print("No data found.")
            return

        print(f"Found {len(self.df)} rows of data")
        print(f"Finding Wedge Pattern...")
        
        signals = self._impl.find_wedge_patterns(self.df)

        if not signals:
            print("No Wedge Pattern found.")
            return

        print(f"Found {len(signals)} Wedge Patterns")

        # Check if there is a current signal
        current_index = len(self.df) - 1
        current_signal = None
        if signals:
            for s in reversed(signals):
                if s.get('entry_idx') == current_index:
                    current_signal = s
                    break

        if not current_signal:
            print("\nNo new signal found → No prediction.")
            # Hiển thị thống kê lịch sử
            for dir_label, dir_key in (("Falling Wedge (LONG)", 'up'), ("Rising Wedge (SHORT)", 'down')):
                print(f"\n{dir_label}:")
                for horizon in (9, 26):
                    avg_correct_pct, acc, total, correct = self.evaluate_signal_performance_percent(
                        signals, dir_key, horizon
                    )
                    print(
                        f"   - After {horizon} sessions: Accuracy {acc:.2f}% ({correct}/{total}), "
                        f"Average change when correct: {avg_correct_pct:.4f}%"
                    )
        else:
            sig_dir = current_signal.get('direction')
            print("\nCurrent signal found:")
            print(f"   Type: {current_signal.get('type')} | Direction: {sig_dir} | Entry time: {current_signal.get('entry_time')}")
            print(f"   Entry price: ${current_signal.get('entry_price'):.4f}")

            last_close = self.df.iloc[-1]['close']
            # Evaluate history by horizon 9 and 26 sessions
            for horizon in (9, 26):
                avg_change, acc, total, correct = self.evaluate_signal_performance(
                    signals, 'up' if sig_dir == 'LONG' else 'down', horizon
                )
                predicted_price = last_close + avg_change if sig_dir == 'LONG' else last_close - abs(avg_change)
                change_pct = (predicted_price - last_close) / last_close * 100
                print(f"   ▶ Prediction after {horizon} sessions: ${predicted_price:.4f} ({change_pct:+.2f}%) | History accuracy: {acc:.1f}% ({correct}/{total})")


class TripleStrategy(StrategyBase):
    def __init__(self, symbol: str, interval: str, side: TradeSide):
        super().__init__(symbol, interval, side)
        # Import implementation
        from strategy_implementations import TripleStrategy as TripleImpl
        self._impl = TripleImpl()

    def run(self):
        print(f"=== {self.name()} {self.side.value} - {self.symbol} {self.interval} ===")
        
        if self.df.empty:
            print("No data found. Check database connection.")
            return

        print(f"Found {len(self.df)} rows of data")
        print(f"Finding Triple Pattern...")
        
        signals = self._impl.find_triple_signals(self.df)

        if not signals:
            print("No Triple Pattern found.")
            return

        print(f"Found {len(signals)} Triple Patterns")

        # Check 
        current_index = len(self.df) - 1
        current_signal = None
        if signals:
            for s in reversed(signals):
                if s.get('entry_idx') == current_index:
                    current_signal = s
                    break

        if not current_signal:
            print("\nNo new signal found → No prediction.")
            for dir_label, dir_key in (("Bullish (LONG)", 'up'), ("Bearish (SHORT)", 'down')):
                print(f"\n{dir_label}:")
                for horizon in (9, 26):
                    avg_correct_pct, acc, total, correct = self.evaluate_signal_performance_percent(
                        signals, dir_key, horizon
                    )
                    print(
                        f"   - After {horizon} sessions: Accuracy {acc:.2f}% ({correct}/{total}), "
                        f"Average change when correct: {avg_correct_pct:.4f}%"
                    )
        else:
            sig_dir = current_signal.get('direction')
            print("\nCurrent signal found:")
            print(f"   Type: {current_signal.get('type')} | Direction: {sig_dir} | Entry time: {current_signal.get('entry_time')}")
            print(f"   Entry price: ${current_signal.get('entry_price'):.4f}")

            last_close = self.df.iloc[-1]['close']
            for horizon in (9, 26):
                avg_change, acc, total, correct = self.evaluate_signal_performance(
                    signals, 'up' if sig_dir == 'LONG' else 'down', horizon
                )
                predicted_price = last_close + avg_change if sig_dir == 'LONG' else last_close - abs(avg_change)
                change_pct = (predicted_price - last_close) / last_close * 100
                print(f"   ▶ Prediction after {horizon} sessions: ${predicted_price:.4f} ({change_pct:+.2f}%) | History accuracy: {acc:.1f}% ({correct}/{total})")


class ButterflyStrategy(StrategyBase):
    def __init__(self, symbol: str, interval: str, side: TradeSide):
        super().__init__(symbol, interval, side)
        # Import implementation
        from strategy_implementations import ButterflyStrategy as ButterflyImpl
        self._impl = ButterflyImpl()

    def run(self):
        print(f"=== {self.name()} {self.side.value} - {self.symbol} {self.interval} ===")
        
        if self.df.empty:
            print("No data found. Check database connection.")
            return

        print(f"Found {len(self.df)} rows of data")
        print(f"Finding Butterfly Pattern...")
        
        signals = self._impl.find_butterfly_patterns(self.df)

        if not signals:
            print("No Butterfly Pattern found.")
            return

        print(f"Found {len(signals)} Butterfly Patterns")

        # Check if there is a current signal
        current_index = len(self.df) - 1
        current_signal = None
        if signals:
            for s in reversed(signals):
                if s.get('entry_idx') == current_index:
                    current_signal = s
                    break

        if not current_signal:
            print("\nNo new signal found → No prediction.")
            for dir_label, dir_key in (("Bullish (LONG)", 'up'), ("Bearish (SHORT)", 'down')):
                print(f"\n{dir_label}:")
                for horizon in (9, 26):
                    avg_correct_pct, acc, total, correct = self.evaluate_signal_performance_percent(
                        signals, dir_key, horizon
                    )
                    print(
                        f"   - After {horizon} sessions: Accuracy {acc:.2f}% ({correct}/{total}), "
                        f"Average change when correct: {avg_correct_pct:.4f}%"
                    )
        else:
            sig_dir = current_signal.get('direction')
            print("\nCurrent signal found:")
            print(f"   Type: {current_signal.get('type')} | Direction: {sig_dir} | Entry time: {current_signal.get('entry_time')}")
            print(f"   Entry price: ${current_signal.get('entry_price'):.4f}")

            last_close = self.df.iloc[-1]['close']
            for horizon in (9, 26):
                avg_change, acc, total, correct = self.evaluate_signal_performance(
                    signals, 'up' if sig_dir == 'LONG' else 'down', horizon
                )
                predicted_price = last_close + avg_change if sig_dir == 'LONG' else last_close - abs(avg_change)
                change_pct = (predicted_price - last_close) / last_close * 100
                print(f"   ▶ Prediction after {horizon} sessions: ${predicted_price:.4f} ({change_pct:+.2f}%) | History accuracy: {acc:.1f}% ({correct}/{total})")


class TriangleStrategy(StrategyBase):
    def __init__(self, symbol: str, interval: str, side: TradeSide):
        super().__init__(symbol, interval, side)
        # Import implementation
        from strategy_implementations import TriangleStrategy as TriangleImpl
        self._impl = TriangleImpl()

    def run(self):
        print(f"=== {self.name()} {self.side.value} - {self.symbol} {self.interval} ===")
        
        if self.df.empty:
            print("No data found. Check database connection.")
            return

        print(f"Found {len(self.df)} rows of data")
        print(f"Finding Triangle Pattern...")
        
        signals = self._impl.find_triangle_patterns(self.df)

        if not signals:
            print("No Triangle Pattern found.")
            return

        print(f"Found {len(signals)} Triangle Patterns")

        # Check if there is a current signal
        current_index = len(self.df) - 1
        current_signal = None
        if signals:
            for s in reversed(signals):
                if s.get('entry_idx') == current_index:
                    current_signal = s
                    break

        if not current_signal:
            print("\nNo new signal found → No prediction.")
            for dir_label, dir_key in (("Ascending Triangle (LONG)", 'up'), ("Descending Triangle (SHORT)", 'down')):
                print(f"\n{dir_label}:")
                for horizon in (9, 26):
                    avg_correct_pct, acc, total, correct = self.evaluate_signal_performance_percent(
                        signals, dir_key, horizon
                    )
                    print(
                        f"   - After {horizon} sessions: Accuracy {acc:.2f}% ({correct}/{total}), "
                        f"Average change when correct: {avg_correct_pct:.4f}%"
                    )
        else:
            sig_dir = current_signal.get('direction')
            print("\nCurrent signal found:")
            print(f"   Type: {current_signal.get('type')} | Direction: {sig_dir} | Entry time: {current_signal.get('entry_time')}")
            print(f"   Entry price: ${current_signal.get('entry_price'):.4f}")

            last_close = self.df.iloc[-1]['close']
            for horizon in (9, 26):
                avg_change, acc, total, correct = self.evaluate_signal_performance(
                    signals, 'up' if sig_dir == 'LONG' else 'down', horizon
                )
                predicted_price = last_close + avg_change if sig_dir == 'LONG' else last_close - abs(avg_change)
                change_pct = (predicted_price - last_close) / last_close * 100
                print(f"   ▶ Prediction after {horizon} sessions: ${predicted_price:.4f} ({change_pct:+.2f}%) | History accuracy: {acc:.1f}% ({correct}/{total})")


# Backtest list per request

# 1. Wedge-pattern: LONG: ETH, BTC
# 2. Triple: LONG: BTC, BNB, XRP
# 3. Butterfly: LONG: SOL, BTC, ETH, BNB, XRP | SHORT: BNB
# 4. Triangle: LONG: BTC, ETH, BNB | SHORT: BNB
STRATEGY_TOKEN_LISTS = {
    "Wedge": {
        "LONG": ["ETHUSDT", "BTCUSDT"],
        "SHORT": [],
    },
    "Triple": {
        "LONG": ["BTCUSDT", "BNBUSDT", "XRPUSDT"],
        "SHORT": [],
    },
    "Butterfly": {
        "LONG": ["SOLUSDT", "BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT"],
        "SHORT": ["BNBUSDT"],
    },
    "Triangle": {
        "LONG": ["BTCUSDT", "ETHUSDT", "BNBUSDT"],
        "SHORT": ["BNBUSDT"],
    },
}


def make_strategy(strategy_name: str, symbol: str, interval: str, side: TradeSide) -> StrategyBase:
    name = strategy_name.lower()
    if name == "wedge":
        return WedgeStrategy(symbol, interval, side)
    if name == "triple":
        return TripleStrategy(symbol, interval, side)
    if name == "butterfly":
        return ButterflyStrategy(symbol, interval, side)
    if name == "triangle":
        return TriangleStrategy(symbol, interval, side)
    raise ValueError(f"Unknown strategy: {strategy_name}")


def parse_args():
    parser = argparse.ArgumentParser(description="Predict Bot - Strategy Runner")
    parser.add_argument("--timeframe", default="1h", help="Timeframe, e.g. 1h, 2h, 4h")
    parser.add_argument("--only", nargs="*", default=[], help="Run only these strategies (names)")
    return parser.parse_args()


def main():
    args = parse_args()
    timeframe = args.timeframe
    only = {s.lower() for s in (args.only or [])}

    for strategy_name, sides in STRATEGY_TOKEN_LISTS.items():
        if only and strategy_name.lower() not in only:
            continue
        for side_name, symbols in sides.items():
            if not symbols:
                continue
            side = TradeSide(side_name)
            for sym in symbols:
                strat = make_strategy(strategy_name, sym, timeframe, side)
                strat.run()


if __name__ == "__main__":
    main()
