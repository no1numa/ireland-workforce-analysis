# Libraries used
import requests
import time
import datetime as dt
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

# Changing Quarter attribute to datetime format
def quarter_to_dt(df):
    df['period'] = pd.PeriodIndex(df['Quarter'], freq='Q')
    df['date'] = df['period'].dt.start_time
    df.drop(columns=['period', 'Quarter'], inplace=True)

# Putting columns in lower case and without spaces between words
def col_renaming(df):
    df.columns = df.columns.map(lambda x: x.lower().replace(' ', '_'))

# Dropping aggregations and null values
def clean_data(df):
    df.dropna(subset=['value'], inplace=True)
    
    agg_values = ['All NACE economic sectors',
                 'Both sexes',
                 'All ILO economic status',
                 'All employment status',
                 'State',
                 'Ireland',
                 'All nationalities',
                 'All countries',
                 'All persons in employment	',
                 'All marital status',
                 'All occupational groups']

    #df.drop(agg_values)
                         
                         
    