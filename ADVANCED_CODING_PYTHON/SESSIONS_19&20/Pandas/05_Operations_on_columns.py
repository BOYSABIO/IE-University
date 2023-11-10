import pandas as pd

df = pd.read_csv('CSV_FILES/cholesterol.csv')

print(df['height']*100)
print()

print(df['gender']=='F')
