import time
import requests

def retry_request(url, params=None, retries=3, delay=2):
    for i in range(retries):
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            time.sleep(delay)
            if i == retries - 1:
                raise e
