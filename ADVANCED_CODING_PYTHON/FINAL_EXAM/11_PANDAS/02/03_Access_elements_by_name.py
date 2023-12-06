import pandas as pd

df = pd.read_csv('CSV_FILES/cholesterol.csv')
print(df.loc[2, 'cholesterol'])
print()
print(df.loc[:3, ('cholesterol','weight')])
print()
print(df['cholesterol'])
