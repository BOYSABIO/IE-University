import pandas as pd

df = pd.read_csv('CSV_FILES/cholesterol.csv')
print(df.rename(columns={'name':'first and last names'}, index={0:1000, 1:1001, 2:1002}))
