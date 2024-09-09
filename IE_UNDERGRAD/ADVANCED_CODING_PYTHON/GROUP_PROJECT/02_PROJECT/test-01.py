"""The aim of this work is to check whether the traffic restrictions established in Madrid Central 
have served to significantly reduce pollutant gas emissions."""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

# Dataset (Open data from madrid city council: Air Quality, Daily Data years 2001 to 2009)
df = pd.read_csv("CSV_FILES/emissions-madrid.csv")
print(df)
print(df.describe())

# Restructure the DataFrame so that the pollutant values of the day columns appear in a single column
df = df.melt(id_vars = ["STATION", "MAGNITUDE", "YEAR", "MONTH"], var_name = "DAY", value_name = "Air_Quality")
print(df)

# Add a column with the date from the concatenation of the year, month and day(use the datetime module)
df["DAY"] = df.DAY.str.strip('D')
df["DATE"] = df.YEAR.apply(str) + "/" + df.MONTH.apply(str) + "/" + df.DAY.apply(str)
print(df)

df["DATE"] = pd.to_datetime(df.DATE, format = "%Y/%m/%d", errors = "coerce")
print(df)

# Delete rows with invalid dates (use the isnat function of the numpy module) and sort the DataFrame by polluting stations and date
df = df.drop(df[np.isnat(df.DATE)].index)
print(df)


#1
def magnitude_station(station, magnitude):
    df1 = df[(df.MAGNITUDE == magnitude) & (df.STATION == station)]
    return df1['Air_Quality'].values.tolist()

station = int(input("Please enter station: "))
magnitude = int(input("Please enter magnitude: "))
print(f"The air quality measurements for station: {station}, and magnitude: {magnitude} are:\n", magnitude_station(station, magnitude))

#2
def month_station(station, month):
    df2 = df[(df.MONTH == month) & (df.STATION == station)]
    return df2.groupby(['MAGNITUDE'])['Air_Quality'].mean().to_dict()
print(month_station(4, 1))

#3
def month_magnitude(month, magnitude):
    df3 = df[(df.MONTH == month) & (df.MAGNITUDE == magnitude)]
    return df3.groupby(['STATION'])['Air_Quality'].mean().to_dict()
print(month_magnitude(1, 1))

#4
def graph_station(station, start_date, end_date):
    df4 = df[(df.STATION == station) & (df.DATE >= start_date) & (df.DATE <= end_date)]
    df4.plot(x = "DATE", y = "Air_Quality")
    plt.show()
graph_station(4,"2018-08-01" ,"2019-08-01" )

#5
def graph_magnitude(magnitude, start_date, end_date):
    df5 = df[(df.MAGNITUDE == magnitude) & (df.DATE >= start_date) & (df.DATE <= end_date)]
    df5.plot(x = "DATE", y = "Air_Quality")
    plt.show()
graph_magnitude(1,"2018-08-01" ,"2019-08-01" )

#6