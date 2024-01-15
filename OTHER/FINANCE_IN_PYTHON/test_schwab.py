import schwab_api as api
import yfinance as yf


stock_data = yf.Ticker(input("Enter symbol: "))
info = stock_data.info
summary = info.get('longBusinessSummary')
print(summary)