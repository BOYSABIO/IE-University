import pandas as pd

df = pd.DataFrame({'Name': ['María', 'Carlos', 'Carmen'], 'Birth_date':['05-03-2000', '20-05-2001', '10-12-1999']})
print(pd.to_datetime(df.Birth_date, format = '%d-%m-%Y'))

