class SimpleAIPredictor:
    def __init__(self):
        pass

    def predict_signal(self, data):
        if data['rsi'] < 30:
            return 'BUY'
        elif data['rsi'] > 70:
            return 'SELL'
        return 'HOLD'
