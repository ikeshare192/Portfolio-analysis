import pandas as pd
import yfinance as yfinance

def get_tickers():
    url = "https://raw.githubusercontent.com/timothewt/SP100AnalysisWithGNNs/master/data/SP100/raw/stocks.csv"
    data = pd.read_csv(url)
    tickers = data["Symbol"]
    return tickers

def get_data(tickers):
    data_set = []
    for item in tickers:
        data = yf.download(ticker, start="2020-06-01", end="2020-12-31")
        
