import random

def get_mock_onchain_data(symbol):
    return {
        'funding_rate': random.uniform(-0.01, 0.01),
        'open_interest': random.randint(10000, 1000000),
        'active_addresses': random.randint(1000, 100000),
    }
