import pandas as pd

df = pd.read_csv('CSV_FILES/cholesterol.csv')
df = df._append(pd.Series(['Carlos Rivas', 28, 'M', 89.0, 1.78, 245.0], index=['name','age','gender','weight','height','cholesterol']), ignore_index=True)
print(df.tail())
