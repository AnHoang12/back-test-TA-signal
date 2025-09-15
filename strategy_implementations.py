#!/usr/bin/env python3
"""
Strategy implementations for predict-bot
"""

import pandas as pd
import numpy as np
import importlib.util


class WedgeStrategy:
    def find_pivots(self, data, window=5):
        """Find pivot highs and lows"""
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

    def calc_slope(self, points):
        """Calculate slope between points"""
        x = [p[0] for p in points]
        y = [p[1] for p in points]
        if len(x) < 2:
            return 0
        return (y[-1] - y[0]) / (x[-1] - x[0])

    def find_wedge_patterns(self, df, num_highs=3, num_lows=3, max_pattern_length=48):
        """Tìm Wedge Pattern"""
        signals = []
        pivot_highs, pivot_lows = self.find_pivots(df, window=3)
        
        # Rising wedge: N đỉnh cao dần, N đáy cao dần, slope đáy > slope đỉnh
        for i in range(len(pivot_highs) - (num_highs-1)):
            highs = pivot_highs[i:i+num_highs]
            if all(highs[j][1] < highs[j+1][1] for j in range(num_highs-1)):
                # Tìm N đáy cao dần trong cùng khoảng
                lows = [l for l in pivot_lows if highs[0][0] < l[0] < highs[-1][0]]
                for k in range(len(lows) - (num_lows-1)):
                    lows_seq = lows[k:k+num_lows]
                    if all(lows_seq[j][1] < lows_seq[j+1][1] for j in range(num_lows-1)):
                        # Kiểm tra độ dốc
                        slope_high = self.calc_slope(highs)
                        slope_low = self.calc_slope(lows_seq)
                        if slope_low > slope_high and (highs[-1][0] - highs[0][0]) <= max_pattern_length:
                            # Breakout xuống: giá close sau đáy cuối cùng
                            breakout_idx = lows_seq[-1][0] + 1
                            if breakout_idx < len(df):
                                entry_price = df.iloc[breakout_idx]['close']
                                signals.append({
                                    'type': 'Rising Wedge',
                                    'entry_idx': breakout_idx,
                                    'entry_time': df.iloc[breakout_idx]['datetime'],
                                    'entry_price': entry_price,
                                    'pattern_points': highs + lows_seq,
                                    'direction': 'SHORT',
                                    'slope_high': slope_high,
                                    'slope_low': slope_low
                                })
        
        # Falling wedge: N đỉnh thấp dần, N đáy thấp dần, slope đáy < slope đỉnh
        for i in range(len(pivot_highs) - (num_highs-1)):
            highs = pivot_highs[i:i+num_highs]
            if all(highs[j][1] > highs[j+1][1] for j in range(num_highs-1)):
                lows = [l for l in pivot_lows if highs[0][0] < l[0] < highs[-1][0]]
                for k in range(len(lows) - (num_lows-1)):
                    lows_seq = lows[k:k+num_lows]
                    if all(lows_seq[j][1] > lows_seq[j+1][1] for j in range(num_lows-1)):
                        slope_high = self.calc_slope(highs)
                        slope_low = self.calc_slope(lows_seq)
                        if slope_low < slope_high and (highs[-1][0] - highs[0][0]) <= max_pattern_length:
                            # Breakout lên: giá close sau đỉnh cuối cùng
                            breakout_idx = highs[-1][0] + 1
                            if breakout_idx < len(df):
                                entry_price = df.iloc[breakout_idx]['close']
                                signals.append({
                                    'type': 'Falling Wedge',
                                    'entry_idx': breakout_idx,
                                    'entry_time': df.iloc[breakout_idx]['datetime'],
                                    'entry_price': entry_price,
                                    'pattern_points': highs + lows_seq,
                                    'direction': 'LONG',
                                    'slope_high': slope_high,
                                    'slope_low': slope_low
                                })
        
        return signals


class TripleStrategy:
    def __init__(self):
        self.LOOKBACK_PERIOD = 40
        self.PRICE_THRESHOLD = 0.05
        # Try to import candlestick detection functions
        self.has_candlestick = self._import_candlestick_functions()

    def _import_candlestick_functions(self):
        """Try to import candlestick detection functions"""
        try:
            # Try to load from triple-pattern directory
            spec = importlib.util.spec_from_file_location(
                "rsi14_candlestick_confluence", 
                "triple-pattern/rsi14_candlestick_confluence.py"
            )
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                self.detect_bullish_engulfing = module.detect_bullish_engulfing
                self.detect_hammer = module.detect_hammer
                self.detect_bullish_doji = module.detect_bullish_doji
                self.detect_bearish_engulfing = module.detect_bearish_engulfing
                self.detect_shooting_star = module.detect_shooting_star
                self.detect_bearish_doji = module.detect_bearish_doji
                return True
        except Exception as e:
            print(f"⚠️ Không thể import candlestick functions: {e}")
            return False
        return False

    def detect_triple_top(self, df, lookback_period=None, price_threshold=None):
        """Detect triple top pattern"""
        if lookback_period is None:
            lookback_period = self.LOOKBACK_PERIOD
        if price_threshold is None:
            price_threshold = self.PRICE_THRESHOLD
            
        if len(df) < lookback_period:
            return False, None, None
        
        window = df.tail(lookback_period)
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

    def detect_triple_bottom(self, df, lookback_period=None, price_threshold=None):
        """Detect triple bottom pattern"""
        if lookback_period is None:
            lookback_period = self.LOOKBACK_PERIOD
        if price_threshold is None:
            price_threshold = self.PRICE_THRESHOLD
            
        if len(df) < lookback_period:
            return False, None, None
        
        window = df.tail(lookback_period)
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

    def is_bullish_reversal_candle(self, df):
        """Kiểm tra nến đảo chiều tăng"""
        if not self.has_candlestick or len(df) < 2:
            return False
        
        try:
            return (
                self.detect_hammer(df).iloc[-1] or
                self.detect_bullish_engulfing(df).iloc[-1] or
                self.detect_bullish_doji(df).iloc[-1]
            )
        except:
            return False

    def is_bearish_reversal_candle(self, df):
        """Kiểm tra nến đảo chiều giảm"""
        if not self.has_candlestick or len(df) < 2:
            return False
        
        try:
            return (
                self.detect_shooting_star(df).iloc[-1] or
                self.detect_bearish_engulfing(df).iloc[-1] or
                self.detect_bearish_doji(df).iloc[-1]
            )
        except:
            return False

    def find_triple_signals(self, df):
        """Tìm tín hiệu triple pattern"""
        signals = []
        if len(df) < self.LOOKBACK_PERIOD + 1:
            return signals

        # Precompute candlestick flags if available
        flags = None
        if self.has_candlestick:
            try:
                flags = {
                    'is_hammer': self.detect_hammer(df).astype(bool).values,
                    'is_bullish_engulfing': self.detect_bullish_engulfing(df).astype(bool).values,
                    'is_bullish_doji': self.detect_bullish_doji(df).astype(bool).values,
                    'is_shooting_star': self.detect_shooting_star(df).astype(bool).values,
                    'is_bearish_engulfing': self.detect_bearish_engulfing(df).astype(bool).values,
                    'is_bearish_doji': self.detect_bearish_doji(df).astype(bool).values,
                }
            except:
                flags = None

        n = len(df)
        for i in range(self.LOOKBACK_PERIOD, n - 1):
            window = df.iloc[:i+1]
            
            try:
                # Triple Bottom breakout + bullish reversal
                has_bottom, _, resistance = self.detect_triple_bottom(window)
                if has_bottom:
                    current_close = df.iloc[i]['close']
                    is_bullish_reversal = False
                    if flags:
                        is_bullish_reversal = bool(
                            flags['is_hammer'][i] or flags['is_bullish_engulfing'][i] or flags['is_bullish_doji'][i]
                        )
                    else:
                        is_bullish_reversal = self.is_bullish_reversal_candle(window)
                    
                    if resistance is not None and current_close > resistance and is_bullish_reversal:
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
                # Triple Top breakdown + bearish reversal
                has_top, support, _ = self.detect_triple_top(window)
                if has_top:
                    current_close = df.iloc[i]['close']
                    is_bearish_reversal = False
                    if flags:
                        is_bearish_reversal = bool(
                            flags['is_shooting_star'][i] or flags['is_bearish_engulfing'][i] or flags['is_bearish_doji'][i]
                        )
                    else:
                        is_bearish_reversal = self.is_bearish_reversal_candle(window)
                    
                    if support is not None and current_close < support and is_bearish_reversal:
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


class ButterflyStrategy:
    def __init__(self):
        self.LOOKBACK_PERIOD = 40

    def detect_swing_points(self, df, window=3):
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

    def is_within_tolerance(self, actual, expected, tolerance=0.15):
        """Check if actual value is within tolerance of expected Fibonacci ratio"""
        return abs(actual - expected) / expected <= tolerance

    def find_butterfly_patterns(self, df, max_pattern_length=72):
        """Tìm Butterfly Pattern"""
        signals = []
        
        # Detect swing points
        df = self.detect_swing_points(df, window=3)
        
        # Tìm Bullish Butterfly Pattern
        for i in range(15, len(df)):
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

                # Check Fibonacci ratios
                AB_XA_ratio = AB / XA
                BC_AB_ratio = BC / AB
                CD_BC_ratio = CD / BC if BC > 0 else 0
                AD_XA_ratio = AD / XA
                
                # Butterfly pattern ratios với tolerance 15-25%
                valid_AB = self.is_within_tolerance(AB_XA_ratio, 0.786, 0.2)
                valid_BC = (self.is_within_tolerance(BC_AB_ratio, 0.382, 0.2) or 
                           self.is_within_tolerance(BC_AB_ratio, 0.886, 0.2))
                valid_CD = (self.is_within_tolerance(CD_BC_ratio, 1.27, 0.25) or
                           self.is_within_tolerance(CD_BC_ratio, 1.618, 0.25))
                valid_AD = self.is_within_tolerance(AD_XA_ratio, 0.786, 0.2)
                
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

                valid_AB = self.is_within_tolerance(AB_XA_ratio, 0.786, 0.2)
                valid_BC = (self.is_within_tolerance(BC_AB_ratio, 0.382, 0.2) or
                           self.is_within_tolerance(BC_AB_ratio, 0.886, 0.2))
                valid_CD = (self.is_within_tolerance(CD_BC_ratio, 1.27, 0.25) or
                           self.is_within_tolerance(CD_BC_ratio, 1.618, 0.25))
                valid_AD = self.is_within_tolerance(AD_XA_ratio, 0.786, 0.2)
                
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


class TriangleStrategy:
    def __init__(self):
        self.ATR_PERIOD = 14
        self.ATR_MULTIPLIER = 2.0
        self.MIN_SLOPE_THRESHOLD = 0.001
        self.MAX_PATTERN_LENGTH = 72
        self.TOLERANCE_MULTIPLIER = 1.5
        self.NUM_LOWS = 3
        self.NUM_HIGHS = 3

    def calculate_atr(self, data, period=14):
        """Calculate Average True Range"""
        high = data['high']
        low = data['low']
        close = data['close'].shift(1)
        
        tr1 = high - low
        tr2 = abs(high - close)
        tr3 = abs(low - close)
        
        true_range = np.maximum(tr1, np.maximum(tr2, tr3))
        atr = true_range.rolling(window=period).mean()
        
        return atr

    def find_adaptive_pivots(self, data, base_window=3):
        """Find pivot with adaptive window size based on ATR"""
        atr = self.calculate_atr(data)
        avg_price = (data['high'] + data['low'] + data['close']) / 3
        
        pivot_highs = []
        pivot_lows = []
        
        for i in range(len(data)):
            if i < self.ATR_PERIOD or i >= len(data) - base_window:
                continue
                
            # Calculate adaptive window size
            current_atr = atr.iloc[i]
            current_avg_price = avg_price.iloc[i]
            
            if pd.notna(current_atr) and current_avg_price > 0:
                adaptive_factor = (current_atr / current_avg_price) * self.ATR_MULTIPLIER
                window = max(base_window, min(10, int(base_window + adaptive_factor * 10)))
            else:
                window = base_window
            
            # Check if there is enough data for the window
            if i < window or i >= len(data) - window:
                continue
                
            # Find pivot high
            highs = data['high'].iloc[i-window:i+window+1]
            if data['high'].iloc[i] == highs.max() and highs.iloc[window] >= highs.iloc[window-1] and highs.iloc[window] >= highs.iloc[window+1]:
                pivot_highs.append((i, data['high'].iloc[i]))
            
            # Find pivot low
            lows = data['low'].iloc[i-window:i+window+1]
            if data['low'].iloc[i] == lows.min() and lows.iloc[window] <= lows.iloc[window-1] and lows.iloc[window] <= lows.iloc[window+1]:
                pivot_lows.append((i, data['low'].iloc[i]))
        
        return pivot_highs, pivot_lows

    def is_horizontal_line(self, pivots, atr_values, indices):
        """Kiểm tra các pivot có tạo thành đường ngang với tolerance dựa trên ATR"""
        if len(pivots) < 2:
            return False
        
        prices = [p[1] for p in pivots]
        pivot_indices = [p[0] for p in pivots]
        
        # Tính ATR trung bình tại các pivot points
        avg_atr = 0
        valid_atr_count = 0
        
        for idx in pivot_indices:
            if idx < len(atr_values) and pd.notna(atr_values[idx]):
                avg_atr += atr_values[idx]
                valid_atr_count += 1
        
        if valid_atr_count == 0:
            # Fallback to percentage if no ATR available
            return abs(max(prices) - min(prices)) / np.mean(prices) < 0.01
        
        avg_atr = avg_atr / valid_atr_count
        tolerance = avg_atr * self.TOLERANCE_MULTIPLIER
        
        return abs(max(prices) - min(prices)) < tolerance

    def calculate_simple_slope(self, points):
        """Calculate simple slope for trendline validation"""
        if len(points) < 2:
            return 0
        
        x = [p[0] for p in points]  # indices
        y = [p[1] for p in points]  # prices
        
        # Simple linear slope calculation
        slope = (y[-1] - y[0]) / (x[-1] - x[0]) if (x[-1] - x[0]) != 0 else 0
        
        return slope

    def find_triangle_patterns(self, df):
        """Tìm triangle pattern với các cải thiện"""
        signals = []
        
        pivot_highs, pivot_lows = self.find_adaptive_pivots(df)
        atr = self.calculate_atr(df)
        
        # Tam giác tăng: đáy cao dần + đỉnh ngang
        for i in range(len(pivot_lows) - (self.NUM_LOWS-1)):
            lows = pivot_lows[i:i+self.NUM_LOWS]
            
            # Kiểm tra pattern length
            pattern_length = lows[-1][0] - lows[0][0]
            if pattern_length > self.MAX_PATTERN_LENGTH:
                continue
            
            # Kiểm tra trendline slope của đáy
            slope = self.calculate_simple_slope(lows)
            if abs(slope) < self.MIN_SLOPE_THRESHOLD or slope <= 0:  # Đáy phải tăng dần
                continue
            
            # Tìm các đỉnh trong khoảng thời gian này
            highs_in_range = [h for h in pivot_highs if lows[0][0] <= h[0] <= lows[-1][0]]
            
            if len(highs_in_range) >= 2:
                # Kiểm tra đỉnh có tạo đường ngang không (với ATR tolerance)
                if self.is_horizontal_line(highs_in_range, atr, [h[0] for h in highs_in_range]):
                    # Xác định breakout point
                    last_high = max(highs_in_range, key=lambda x: x[0])
                    breakout_idx = min(last_high[0] + 1, len(df) - 1)
                    
                    if breakout_idx < len(df):
                        entry_price = df.iloc[breakout_idx]['close']
                        resistance_level = np.mean([h[1] for h in highs_in_range])
                        
                        # Chỉ tạo signal nếu có breakout thực sự
                        if entry_price > resistance_level:
                            signals.append({
                                'type': 'Ascending Triangle',
                                'entry_idx': breakout_idx,
                                'entry_time': df.iloc[breakout_idx]['datetime'],
                                'entry_price': entry_price,
                                'pattern_points': lows + highs_in_range,
                                'direction': 'LONG',
                                'slope': slope,
                                'pattern_length': pattern_length,
                                'resistance_level': resistance_level
                            })
        
        # Tam giác giảm: đỉnh thấp dần + đáy ngang
        for i in range(len(pivot_highs) - (self.NUM_HIGHS-1)):
            highs = pivot_highs[i:i+self.NUM_HIGHS]
            
            # Kiểm tra pattern length
            pattern_length = highs[-1][0] - highs[0][0]
            if pattern_length > self.MAX_PATTERN_LENGTH:
                continue
            
            # Kiểm tra trendline slope của đỉnh
            slope = self.calculate_simple_slope(highs)
            if abs(slope) < self.MIN_SLOPE_THRESHOLD or slope >= 0:  # Đỉnh phải giảm dần
                continue
            
            # Tìm các đáy trong khoảng thời gian này
            lows_in_range = [l for l in pivot_lows if highs[0][0] <= l[0] <= highs[-1][0]]
            
            if len(lows_in_range) >= 2:
                # Kiểm tra đáy có tạo đường ngang không
                if self.is_horizontal_line(lows_in_range, atr, [l[0] for l in lows_in_range]):
                    # Xác định breakout point
                    last_low = max(lows_in_range, key=lambda x: x[0])
                    breakout_idx = min(last_low[0] + 1, len(df) - 1)
                    
                    if breakout_idx < len(df):
                        entry_price = df.iloc[breakout_idx]['close']
                        support_level = np.mean([l[1] for l in lows_in_range])
                        
                        # Chỉ tạo signal nếu có breakout thực sự
                        if entry_price < support_level:
                            signals.append({
                                'type': 'Descending Triangle',
                                'entry_idx': breakout_idx,
                                'entry_time': df.iloc[breakout_idx]['datetime'],
                                'entry_price': entry_price,
                                'pattern_points': highs + lows_in_range,
                                'direction': 'SHORT',
                                'slope': slope,
                                'pattern_length': pattern_length,
                                'support_level': support_level
                            })
        
        return signals