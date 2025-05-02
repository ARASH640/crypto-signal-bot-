from utils import retry_request
from config import LBANK_API_URL

def get_lbank_symbols():
    url = f'{LBANK_API_URL}/v1/currencyPairs.do'
    data = retry_request(url)
    symbols = [s['symbol'] for s in data['data'] if 'usdt' in s['symbol']]
    return symbols

def get_lbank_klines(symbol, interval, size=100):
    url = f'{LBANK_API_URL}/v1/kline.do'
    params = {'symbol': symbol, 'type': interval, 'size': size}
    data = retry_request(url, params)
    return data['data']
