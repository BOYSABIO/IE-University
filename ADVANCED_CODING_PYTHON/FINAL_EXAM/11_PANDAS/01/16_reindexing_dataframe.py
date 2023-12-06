import pandas as pd

df = pd.read_csv('CSV_FILES/cholesterol.csv')
print(df.reindex(index=[4, 3, 1], columns=['name', 'pressure', 'cholesterol']))
