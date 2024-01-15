"""The files emissions-2016.csv, emissions-2017.csv, emissions-2018.csv and emissions-2019.csv, contain data on 
pollutant emissions in the city of Madrid in the years 2016, 2017,2018 and 2019 respectively. Write a program with 
the following requirements:
1. Generate a DataFrame with the data from the four files.
2. Filter the columns of the DataFrame to keep the columns STATION, MAGNITUDE,YEAR, MONTH and those corresponding to 
    the days D01, D02, etc.
3. Restructure the DataFrame so that the pollutant values of the day columns appear in a single column.
4. Add a column with the date from the concatenation of the year, month and day(use the datetime module).
5. Delete rows with invalid dates (use the isnat function of the numpy module) and sort the DataFrame by polluting 
    stations and date.
6. Display the available stations and pollutants in the DataFrame.
7. Create a function that receives a station, a pollutant and a date range and returns a series with the emissions of the 
    given pollutant at the given station and date range.
8. Display a descriptive summary (minimum, maximum, average, etc.) for each pollutant.
9. Display a descriptive summary for each pollutant by district."""

import pandas as pd
import datetime as dt
import numpy as np

# Generate a DataFrame with the data from the four files
emissions_2016 = pd.read_csv("CSV_FILES/emissions-2016.csv", sep = ';')
emissions_2017 = pd.read_csv("CSV_FILES/emissions-2017.csv", sep = ';')
emissions_2018 = pd.read_csv("CSV_FILES/emissions-2018.csv", sep = ';')
emissions_2019 = pd.read_csv("CSV_FILES/emissions-2019.csv", sep = ';')
df = pd.concat([emissions_2016, emissions_2017, emissions_2018, emissions_2019])
print(df)

# Filter the columns of the DataFrame to keep the columns STATION, MAGNITUDE,YEAR, MONTH and those corresponding to the days D01, D02, etc
columns = ['STATION', 'MAGNITUDE', 'YEAR', 'MONTH']
columns.extend([col for col in df if col.startswith('D')])
df = df[columns]
print(df)

# Restructure the DataFrame so that the pollutant values of the day columns appear in a single column
df = df.melt(id_vars = ["STATION", "MAGNITUDE", "YEAR", "MONTH"], var_name = "DAY", value_name = "VALUE")
print(df)

# Add a column with the date from the concatenation of the year, month and day(use the datetime module)
df["DAY"] = df.DAY.str.strip('D')
df["DATE"] = df.YEAR.apply(str) + "/" + df.MONTH.apply(str) + "/" + df.DAY.apply(str)
print(df)

df["DATE"] = pd.to_datetime(df.DATE, format = "%Y/%m/%d", errors = "coerce")
print(df)

# Delete rows with invalid dates (use the isnat function of the numpy module) and sort the DataFrame by polluting stations and date
df = df.drop(df[np.isnat(df.DATE)].index)

df.sort_values(['STATION', 'MAGNITUDE', 'DATE'])
print(df)

# Display the available stations and pollutants in the DataFrame
print(df.STATION.unique())
print(df.MAGNITUDE.unique())

# Create a function that receives a station, a pollutant and a date range and returns a series with the emissions of the given pollutant at the given station and date range
def summary(station, pollutant):
    return df[(df.MAGNITUDE == pollutant) & (df.STATION == station)].VALUE.describe()

print("Nitrogen Dioxide Summary at Plaza Eliptica: \n", summary(56, 8), '\n', sep = '')
print("Nitrogen Dioxide Summary at Plaza Del Carmen: \n", summary(35, 8), '\n', sep = '')

def monthly_average(pollutant, year):
    return df[(df.MAGNITUDE == pollutant) & (df.YEAR == year)].groupby(["STATION", "MONTH"]).VALUE.mean().unstack('MONTH')

print("Nitrogen Dioxide evolution in 2019: \n", monthly_average(8, 2019))

# Display a descriptive summary (minimum, maximum, average, etc.) for each pollutant
print(df.groupby("MAGNITUDE").describe())

# Display a descriptive summary for each pollutant by district
print(df.groupby("STATION")["MAGNITUDE"].describe())
