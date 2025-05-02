from exchange_binance import get_binance_symbols, get_binance_klines
from exchange_coinex import get_coinex_symbols, get_coinex_klines
from exchange_lbank import get_lbank_symbols, get_lbank_klines
from technical_analysis import calculate_rsi, detect_divergence, analyze_order_block
from ai_model import SimpleAIPredictor
from onchain_data import get_mock_onchain_data
from pro_trader_analysis import ProTraderAnalyzer
from telegram_bot import send_telegram_message
from config import TIMEFRAMES, CHECK_INTERVAL_MINUTES
from backtesting import backtest_strategy
import time

ai_model = SimpleAIPredictor()
pro_analyzer = ProTraderAnalyzer()

while True:
    all_symbols = list(set(
        get_binance_symbols() +
        get_coinex_symbols() +
        get_lbank_symbols()
    ))

    for symbol in all_symbols:
        for timeframe in TIMEFRAMES:
            try:
                candles = get_binance_klines(symbol, timeframe)
                close_prices = [float(c[4]) for c in candles]

                rsi_value = calculate_rsi(close_prices)
                divergence = detect_divergence(close_prices, close_prices)
                order_block = analyze_order_block(candles)
                onchain = get_mock_onchain_data(symbol)

                data = {
                    'rsi': rsi_value,
                    'divergence': divergence,
                    'order_block': order_block,
                    'onchain': onchain
                }

                prediction = ai_model.predict_signal(data)

                if prediction in ['BUY', 'SELL']:
                    message = f"🔔 Signal: {prediction}\nSymbol: {symbol}\nRSI: {rsi_value:.2f}\nTimeframe: {timeframe}"
                    send_telegram_message(message)

                    win_rate = backtest_strategy(close_prices, ai_model)
                    send_telegram_message(f"🔍 Backtest Win Rate: {win_rate:.2f}%")

            except Exception as e:
                print(f"Error processing {symbol}: {e}")

    pro_analyzer.fetch_top_trader_data()
    pro_analyzer.cluster_patterns()
    new_strategy = pro_analyzer.suggest_strategy()
    print("Updated AI with strategy:", new_strategy)

    time.sleep(CHECK_INTERVAL_MINUTES * 60)
