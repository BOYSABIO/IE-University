# Simple Rebalancing Program

import yfinance as yf
import pandas as pd
import datetime

for i in range(10):
    stock = yf.Ticker('META')
    info = stock.info
    if len(stock.history()) > 0:
        break

print(stock.info)

for key, value in stock.info.items():
    print(key, ':', value)

pd.set_option('display.max_rows', None)

#df = test_data.history(period = 'max')
df = stock.history(period = '6mo')



print(df)

print(df.info())


start_date = datetime.datetime(2020, 5, 30)
end_date = datetime.datetime(2023, 1, 1)
print(stock.history(start = start_date, end = end_date))