import yfinance as yf
import pandas as pd

# Must be within the past 60 days
dataF = yf.download("EURUSD=X", start = "2023-10-1", end = "2023-10-30", interval = "15m")
dataF.iloc[-1:,:]
dataF.Open.iloc


# This can be modified depending on the strategy
def signal_generator(df):
    # Opening / closing price of candle
    open = df.Open.iloc[-1]
    close = df.Close.iloc[-1]
    # Opening / closing price of previous candle
    previous_open = df.Open.iloc[-2]
    previous_close = df.Close.iloc[-2]

    # Bearish Pattern
    if (open > close and previous_open < previous_close and close < previous_open and open >= previous_close):
        return 1
    
    # Bullish Pattern
    elif (open < close and previous_open > previous_close and close > previous_open and open <= previous_close):
        return 2
    
    # No clear pattern
    else:
        return 0
    
signal = []
signal.append(0)
for i in range(1, len(dataF)):
    df = dataF[i-1:i+1]
    signal.append(signal_generator(df))

# signal_generator(data)
dataF["signal"] = signal
print(dataF)
print(dataF.signal.value_counts())