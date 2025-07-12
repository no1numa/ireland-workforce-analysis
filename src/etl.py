# For extracting and handling data
import requests
import time
import pandas as pd
from pyjstat import pyjstat


#
def fetch_data(url, retries=5, wait=15):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=15)
            response.raise_for_status()
            return pyjstat.Dataset.read(response.text)
        except Exception as e:
            #print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(wait)
    raise Exception("All attempts failed!")