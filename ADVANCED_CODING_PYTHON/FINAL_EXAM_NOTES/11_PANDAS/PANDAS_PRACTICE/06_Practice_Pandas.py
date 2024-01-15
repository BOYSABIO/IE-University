"""The file prices.csv contains the prices of the IBEX35 companies with the following columns: name 
(name of the company), End (price of the share at the close of the stock exchange), Maximum (maximum 
price of the share during the day), Minimum (minimum price of theshare during the day), volume (Volume at the 
close of the stock exchange), Cash(capitalization at the close in thousands of euros). Build a function that 
builds a DataFrame from a file with the above format and returns another DataFrame with the minimum,maximum and 
average of each column."""

import pandas as pd

def prices_summary(file):
    df = pd.read_csv(file, sep = ";", decimal = ",", thousands = ".", index_col = 0) #Adapt CSV File
    return pd.DataFrame([df.min(), df.max(), df.mean()], index = ["Minimum", "Maximum", "Mean"])


file = "CSV_FILES/prices.csv"
print(prices_summary(file))

