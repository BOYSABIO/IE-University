import pandas as pd

df = pd.read_csv('CSV_FILES/cholesterol.csv')
print(df[(df['gender']=='M') & (df['cholesterol'] > 260)])
