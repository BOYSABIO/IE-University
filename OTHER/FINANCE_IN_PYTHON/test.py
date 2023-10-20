import yfinance as yf
import pandas as pd

getstockdata = yf.Ticker(input("Enter symbol: "))
print(getstockdata.info)