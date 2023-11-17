import pandas as pd

df = pd.read_csv('CSV_FILES/cholesterol.csv')
print(df.groupby('gender').groups)
print()

print(df.groupby(['gender','age']).groups) # Returns dictionary of tuples
