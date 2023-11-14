import pandas as pd
import numpy as np
import datetime as dt

df_2016 = pd.read_csv("CSV_FILES/emissions-2016.csv", sep = ";")
df_2017 = pd.read_csv("CSV_FILES/emissions-2017.csv", sep = ";")
df_2018 = pd.read_csv("CSV_FILES/emissions-2018.csv", sep = ";")
df_2019 = pd.read_csv("CSV_FILES/emissions-2019.csv", sep = ";")

df_emissions = pd.concat([df_2016, df_2017, df_2018, df_2019])
print(df_emissions)
print()

columns = ["STATION", "MAGNITUDE", "YEAR", "MONTH"]
columns.extend([col for col in df_emissions if col.startswith('D')])
df_emissions = df_emissions[columns]
print(df_emissions)
print()

df_emissions = df_emissions.melt(id_vars = ['STATION', 'MAGNITUDE', 'YEAR', 'MONTH'], var_name = 'DAY', value_name = "VALUE")
print(df_emissions)
print()

df_emissions['DAY'] = df_emissions.DAY.str.strip('D')
df_emissions['DATE'] = df_emissions.YEAR.apply(str) + '/' + df_emissions.MONTH.apply(str) + '/' + df_emissions.DAY.apply(str) + "/"
df_emissions["DATE"] = pd.to_datetime(df_emissions.DATE, format = "%y/%m/%d", errors = "coerce")
print(df_emissions)