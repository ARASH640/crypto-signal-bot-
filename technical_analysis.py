import numpy as np

def calculate_rsi(prices, period=14):
    deltas = np.diff(prices)
    seed = deltas[:period]
    up = seed[seed >= 0].sum()/period
    down = -seed[seed < 0].sum()/period
    rs = up/down
    rsi = 100. - 100./(1.+rs)
    return rsi

def detect_divergence(prices, indicator_values):
    return np.random.choice([True, False])

def analyze_order_block(candles):
    return np.random.choice([True, False])
