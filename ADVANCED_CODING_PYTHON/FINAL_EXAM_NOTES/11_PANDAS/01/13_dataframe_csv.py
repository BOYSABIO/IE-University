import pandas as pd

df = pd.read_csv('CSV_FILES/cholesterols.csv', sep = ';', decimal = ',') #In this case the csv is seperated by (;) and the decimals are (,)
print(df.head())
print()

print(df.shape)
print()

print(df.size)
print()

print(df.columns)
print()

print(df.index)
print()

print(df.dtypes)
print()