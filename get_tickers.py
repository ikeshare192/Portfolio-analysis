import pandas as pd
import yfinance as yfinance
import ffn
import warnings
import numpy as np

warnings.simplefilter(action="ignore", category=FutureWarning)

start_date = "2021-01-01"
close_date = "2021-01-31"


# Step #1 get the tickers
def get_tickers():
    url = "https://raw.githubusercontent.com/timothewt/SP100AnalysisWithGNNs/master/data/SP100/raw/stocks.csv"
    data = pd.read_csv(url)
    tickers = data["Symbol"]
    return tickers


# Step #2 get the data from ffn
def get_data(tickers):
    for item in tickers:
        data = ffn.get(tickers, start=start_date, end=close_date)
        print(data)
        return data


# Step #3 build a df sorted and ranked by top 20 monthly returns.
def get_monthly_data(data):  # calculate the monthly returns, sort and return top 20
    # determine the daily returns
    daily_returns = data.pct_change()
    # calculate a monthly return
    monthly_retun = (daily_returns + 1).prod() - 1
    # sort based on the highest return in the month
    sorted_mnthly_returns = pd.DataFrame(monthly_retun.sort_values(ascending=False))
    # select the top 20
    sorted_top_20 = sorted_mnthly_returns[0:20].index
    # create one df with the top 20 and their daily closing values.
    top_20df = data[[column for column in sorted_top_20]]
    return top_20df  # returns the top 20 data frame with daily closing values


# Step #4 get the month returns per stock in the top 20
def get_monthly_returns(df):
    # determine the daily returns
    daily_returns = df.pct_change()
    # calculate a monthly return
    monthly_retun = (daily_returns + 1).prod() - 1
    return monthly_retun


# Step #5 determine the variance
def get_montly_cov(monthly_data):
    trading_days = len(monthly_data)
    top_20_cov_daily = monthly_data.cov()
    top_20_cov_monthly = top_20_cov_daily * trading_days
    return top_20_cov_monthly


# 1
symbols = get_tickers()
# 2
data = get_data(symbols)
# 3
sorted_monthly_closing_values = get_monthly_data(data)
# 4
mon_returns = get_monthly_returns(sorted_monthly_closing_values)
# 5
covariance_monthly = get_montly_cov(mon_returns)  # calculates the volatility

port_returns = []
port_volatility = []
sharpe_ratio = []
stock_weights = []
num_assets = len(covariance_monthly)
num_portfolios = 50000
np.random.seed(42)

# populate the empty lists with each portfolios returns,risk and weights
for single_portfolio in range(num_portfolios):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    returns = np.dot(weights, top_20_ret_ann)
    volatility = np.sqrt(np.dot(weights.T, np.dot(covariance_monthly, weights)))
    sharpe = returns / volatility
    sharpe_ratio.append(sharpe)
    port_returns.append(returns)
    port_volatility.append(volatility)
    stock_weights.append(weights)

# a dictionary for Returns and Risk values of each portfolio
portfolio = {
    "Returns": port_returns,
    "Volatility": port_volatility,
    "Sharpe Ratio": sharpe_ratio,
}

for counter, symbol in enumerate(top_20):
    portfolio[symbol + " Weight"] = [Weight[counter] for Weight in stock_weights]

SP100_top_20_monthly = pd.DataFrame(portfolio)

print(SP100_top_20_monthly)

# print(monthly_ret_data)
