from utils import retry_request
from config import BINANCE_API_URL

def get_binance_symbols():
    url = f'{BINANCE_API_URL}/api/v3/exchangeInfo'
    data = retry_request(url)
    symbols = [s['symbol'] for s in data['symbols'] if s['quoteAsset'] == 'USDT' and s['status'] == 'TRADING']
    return symbols

def get_binance_klines(symbol, interval, limit=100):
    url = f'{BINANCE_API_URL}/api/v3/klines'
    params = {'symbol': symbol, 'interval': interval, 'limit': limit}
    data = retry_request(url, params)
    return data
