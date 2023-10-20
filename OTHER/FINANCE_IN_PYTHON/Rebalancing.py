# Simple Rebalancing Program

import yfinance as yf
import pandas as pd
import datetime

test_data = yf.Ticker('META')

print(test_data.info)

for key, value in test_data.info.items():
    print(key, ':', value)

pd.set_option('display.max_rows', None)

#df = test_data.history(period = 'max')
df = test_data.history(period = '6mo')



print(df)

print(df.info())


start_date = datetime.datetime(2020, 5, 30)
end_date = datetime.datetime(2023, 1, 1)
print(test_data.history(start = start_date, end = end_date))