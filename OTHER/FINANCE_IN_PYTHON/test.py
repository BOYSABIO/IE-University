import yfinance as yf
import pandas as pd

getstockdata = yf.Ticker(input("Enter symbol: "))
print(getstockdata.history())
print(getstockdata.fast_info)
print(getstockdata.major_holders)
print()

df = pd.DataFrame(getstockdata.history("10y"))
print(df.info())
print(df.describe())