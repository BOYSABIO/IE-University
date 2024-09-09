import pandas as pd

df = pd.read_csv('CSV_FILES/cholesterol.csv')
age = df.pop('age')

print(df)
print()

print(age)
