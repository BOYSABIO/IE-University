import pandas as pd

df = pd.read_csv('CSV_FILES/cholesterol.csv')
print(df.sort_values('cholesterol'))
