import pandas as pd

df = pd.read_csv('CSV_FILES/cholesterol.csv')
print(df.iloc[1, 3])
print()
print(df.iloc[1, :2])
