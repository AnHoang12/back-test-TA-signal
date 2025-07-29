#!/usr/bin/env python3
"""
Candlestick Pattern Detection Functions
"""

import pandas as pd
import numpy as np

def detect_hammer(df):
    """Detect hammer pattern"""
    if len(df) < 1:
        return pd.Series([False] * len(df))
    
    results = []
    for i in range(len(df)):
        if i == 0:
            results.append(False)
            continue
            
        current = df.iloc[i]
        body = abs(current['close'] - current['open'])
        lower_shadow = min(current['open'], current['close']) - current['low']
        upper_shadow = current['high'] - max(current['open'], current['close'])
        
        # Hammer conditions
        is_hammer = (
            lower_shadow > 2 * body and  # Long lower shadow
            upper_shadow < body and      # Short upper shadow
            body > 0                     # Has body
        )
        
        results.append(is_hammer)
    
    return pd.Series(results)

def detect_bullish_engulfing(df):
    """Detect bullish engulfing pattern"""
    if len(df) < 2:
        return pd.Series([False] * len(df))
    
    results = []
    for i in range(len(df)):
        if i < 1:
            results.append(False)
            continue
            
        current = df.iloc[i]
        previous = df.iloc[i-1]
        
        # Bullish engulfing conditions
        is_bullish_engulfing = (
            previous['close'] < previous['open'] and  # Previous bearish
            current['close'] > current['open'] and    # Current bullish
            current['open'] < previous['close'] and   # Current opens below previous close
            current['close'] > previous['open']       # Current closes above previous open
        )
        
        results.append(is_bullish_engulfing)
    
    return pd.Series(results)

def detect_bullish_doji(df):
    """Detect bullish doji pattern"""
    if len(df) < 1:
        return pd.Series([False] * len(df))
    
    results = []
    for i in range(len(df)):
        current = df.iloc[i]
        body = abs(current['close'] - current['open'])
        total_range = current['high'] - current['low']
        
        # Doji conditions (small body relative to range)
        is_doji = (
            body <= total_range * 0.1 and  # Small body
            total_range > 0                 # Has some range
        )
        
        results.append(is_doji)
    
    return pd.Series(results)

def detect_shooting_star(df):
    """Detect shooting star pattern"""
    if len(df) < 1:
        return pd.Series([False] * len(df))
    
    results = []
    for i in range(len(df)):
        current = df.iloc[i]
        body = abs(current['close'] - current['open'])
        lower_shadow = min(current['open'], current['close']) - current['low']
        upper_shadow = current['high'] - max(current['open'], current['close'])
        
        # Shooting star conditions
        is_shooting_star = (
            upper_shadow > 2 * body and  # Long upper shadow
            lower_shadow < body and      # Short lower shadow
            body > 0                     # Has body
        )
        
        results.append(is_shooting_star)
    
    return pd.Series(results)

def detect_bearish_engulfing(df):
    """Detect bearish engulfing pattern"""
    if len(df) < 2:
        return pd.Series([False] * len(df))
    
    results = []
    for i in range(len(df)):
        if i < 1:
            results.append(False)
            continue
            
        current = df.iloc[i]
        previous = df.iloc[i-1]
        
        # Bearish engulfing conditions
        is_bearish_engulfing = (
            previous['close'] > previous['open'] and  # Previous bullish
            current['close'] < current['open'] and    # Current bearish
            current['open'] > previous['close'] and   # Current opens above previous close
            current['close'] < previous['open']       # Current closes below previous open
        )
        
        results.append(is_bearish_engulfing)
    
    return pd.Series(results)

def detect_bearish_doji(df):
    """Detect bearish doji pattern (same as bullish doji for simplicity)"""
    return detect_bullish_doji(df) 