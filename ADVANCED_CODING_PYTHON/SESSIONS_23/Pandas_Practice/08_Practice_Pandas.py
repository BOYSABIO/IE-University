import pandas as pd
import numpy as np
import datetime as dt
 
# Generate a DataFrame with the data of the four files
import pandas as pd
 
emissions_2016 = pd.read_csv('CSV_FILES/emissions-2016.csv', sep = ';')
emissions_2017 = pd.read_csv('CSV_FILES/emissions-2017.csv', sep = ';')
emissions_2018 = pd.read_csv('CSV_FILES/emissions-2018.csv', sep = ';')
emissions_2019 = pd.read_csv('CSV_FILES/emissions-2019.csv', sep = ';')
emissions = pd.concat([emissions_2016, emissions_2017, emissions_2018, emissions_2019])
#print(emissions)
 
 
columns = ['STATION', 'MAGNITUDE', 'YEAR', 'MONTH']
columns.extend([col for col in emissions if col.startswith('D')])
emissions = emissions[columns]
#print(emissions)
 
#03
emissions = emissions.melt(id_vars=['STATION', 'MAGNITUDE', 'YEAR', 'MONTH'], var_name='DAY', value_name='VALUE')
# print(emissions)
 
# Create a new column with the dates starting with the year, month and day.
# First we remove the character D from the beginning of the column of days
emissions['DAY'] = emissions.DAY.str.strip('D')
# Concatenate the year, month and day columns
emissions['DATE'] = emissions.YEAR.apply(str) + '/' + emissions.MONTH.apply(str) + '/' + emissions.DAY.apply(str)
# We convert the new column to date type
emissions['DATE'] = pd.to_datetime(emissions.DATE, format='%Y/%m/%d',  errors='coerce')
#print(emissions)
print()
 
#05 Remove rows with invalid dates
emissions = emissions.drop(emissions[np.isnat(emissions.DATE)].index)
# Sort the dataframe by station, magnitude and date
emissions.sort_values(['STATION', 'MAGNITUDE', 'DATE'])
print(emissions)
print()

print('Stations:', emissions.STATION.unique())
print('Pollutants: ', emissions.MAGNITUDE.unique())
print()

def evolution(station, pollutant, start_date, end_date):
    return emissions[(emissions.STATION == station) & (emissions.MAGNITUDE == pollutant) & (emissions.DATE >= start_date) & (emissions.DATE <= end_date)].sort_values('DATE').VALUE

print(evolution(56, 8, dt.datetime.strptime("2018/10/25", "%Y/%m/%d"), dt.datetime.strptime("2020/2/12", "%Y/%m/%d")))
print()

#emissions = emissions.groupby("MAGNITUDE").VALUE.describe()
#print(emissions)
print()

#emissions = emissions.groupby(["STATION", "MAGNITUDE"]).VALUE.describe()
#print(emissions)
print()

def summary(station, pollutant):
    return emissions[(emissions.MAGNITUDE == pollutant) & (emissions.STATION == station)].VALUE.describe()

print("Nitrogen Dioxide Summary at Plaza Eliptica: \n", summary(56, 8), '\n', sep = '')
print("Nitrogen Dioxide Summary at Plaza Del Carmen: \n", summary(35, 8), '\n', sep = '')

def monthly_average(pollutant, year):
    return emissions[(emissions.MAGNITUDE == pollutant) & (emissions.YEAR == year)].groupby(["STATION", "MONTH"]).VALUE.mean().unstack('MONTH')

print("Nitrogen Dioxide evolution in 2019: \n", monthly_average(8, 2019))
