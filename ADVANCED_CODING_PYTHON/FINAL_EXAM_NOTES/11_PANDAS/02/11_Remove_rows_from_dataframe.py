import pandas as pd

df = pd.read_csv('CSV_FILES/cholesterol.csv')
print(df.drop([1, 3]))
