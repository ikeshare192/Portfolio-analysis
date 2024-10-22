import pandas as pd
import yfinance as yfinance
import ffn
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

open_on_date = "2021-01-04"
close_date = "2021-01-05"

def get_tickers():
    url = "https://raw.githubusercontent.com/timothewt/SP100AnalysisWithGNNs/master/data/SP100/raw/stocks.csv"
    data = pd.read_csv(url)
    tickers = data["Symbol"]
    return tickers

def get_data(tickers):
    data_set = []
    for item in tickers:
        data = yf.download(ticker, start="2020-06-01", end="2020-12-31")
'''      
def get_open_prices(start, end):

    data = pd.read_csv('top_20 2021-01-01_to_2021-06-30.csv')
    tickers = data.columns[1:]
    prices_open = ffn.get(tickers, start = open_on_date, end = close_date )
    transposed = prices_open.T
    transposed.columns = ['Price']
    transposed.index.name = 'Stock'
    print(transposed)
    return transposed

get_open_prices(open_on_date, close_date)
'''