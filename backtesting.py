from technical_analysis import calculate_rsi

def backtest_strategy(prices, ai_model):
    signals = []
    for i in range(15, len(prices)):
        subset = prices[i-15:i]
        rsi_value = calculate_rsi(subset)
        prediction = ai_model.predict_signal({'rsi': rsi_value, 'divergence': False, 'order_block': False, 'onchain': {}})
        signals.append((i, prediction))

    wins = 0
    losses = 0

    for i, signal in signals:
        if signal == 'BUY':
            entry_price = prices[i]
            future_price = prices[i+5] if i+5 < len(prices) else prices[-1]
            if future_price > entry_price:
                wins += 1
            else:
                losses += 1
        elif signal == 'SELL':
            entry_price = prices[i]
            future_price = prices[i+5] if i+5 < len(prices) else prices[-1]
            if future_price < entry_price:
                wins += 1
            else:
                losses += 1

    win_rate = (wins / (wins + losses)) * 100 if wins + losses > 0 else 0
    return win_rate
