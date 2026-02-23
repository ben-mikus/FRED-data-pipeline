
import os
import pandas as pd
from fredapi import Fred
from dotenv import load_dotenv

# Establishes a connection to the FRED API using a custom key
# NOTE: To reproduce this code, one must store their API key in a .env file within the project's folder
load_dotenv()
connection = Fred(api_key=os.getenv('API_KEY'))

series_IDs = {
    "cpi headline": "CPIAUCSL",
    "cpi core": "CPILFESL",
    "unemployment rate": "UNRATE",
    "avg hourly earnings": "CES0500000003",
    "ppi": "PPIACO"
}

def fetch_data(series):
    data = {}
    for name, ID in series.items():
        data[name] = connection.get_series(ID, frequency='m')
    return data

df = pd.DataFrame(fetch_data(series_IDs))

df.to_csv("data.csv")
