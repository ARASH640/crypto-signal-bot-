from utils import retry_request
from config import COINEX_API_URL

def get_coinex_symbols():
    url = f'{COINEX_API_URL}/v1/market/list'
    data = retry_request(url)
    symbols = [item for item in data['data'] if 'USDT' in item]
    return symbols

def get_coinex_klines(symbol, interval, limit=100):
    url = f'{COINEX_API_URL}/v1/market/kline'
    params = {'market': symbol, 'type': interval, 'limit': limit}
    data = retry_request(url, params)
    return data['data']
