import pandas as pd

df = pd.read_csv('CSV_FILES/cholesterol.csv')
print(df.groupby('gender').get_group('F'))
