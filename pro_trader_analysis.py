import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

class ProTraderAnalyzer:
    def __init__(self):
        self.data = pd.DataFrame()

    def fetch_top_trader_data(self):
        sample_data = {
            'entry_price': np.random.uniform(100, 50000, 100),
            'exit_price': np.random.uniform(100, 50000, 100),
            'timeframe': np.random.choice(['5m', '15m', '1h', '4h'], 100),
            'volume': np.random.uniform(1000, 100000, 100),
            'profit_percent': np.random.uniform(0, 10, 100)
        }
        self.data = pd.DataFrame(sample_data)
        self.data['win'] = self.data['profit_percent'] > 0
        return self.data

    def cluster_patterns(self):
        X = self.data[['entry_price', 'exit_price', 'volume']]
        kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
        self.data['pattern_cluster'] = kmeans.labels_
        return self.data

    def find_best_patterns(self):
        grouped = self.data.groupby('pattern_cluster').mean()
        best_cluster = grouped['profit_percent'].idxmax()
        best_patterns = self.data[self.data['pattern_cluster'] == best_cluster]
        return best_patterns

    def suggest_strategy(self):
        best_patterns = self.find_best_patterns()
        avg_entry = best_patterns['entry_price'].mean()
        avg_volume = best_patterns['volume'].mean()
        avg_profit = best_patterns['profit_percent'].mean()
        best_timeframes = best_patterns['timeframe'].mode()

        suggestion = {
            'average_entry_price': avg_entry,
            'average_volume': avg_volume,
            'expected_profit': avg_profit,
            'preferred_timeframes': list(best_timeframes)
        }
        return suggestion
