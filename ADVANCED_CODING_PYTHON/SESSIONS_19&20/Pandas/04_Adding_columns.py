import pandas as pd

df = pd.read_csv('CSV_FILES/cholesterol.csv')
# df['diabetes'] = pd.Series([False, False, True, False, True])
print(df)

series = []

for i in range(len(df)):
    if df.loc[i, 'cholesterol'] >= 200:
        series.append(True)
    elif df.loc[i, 'cholesterol'] < 200:
        series.append(False)
    else:
        series.append("NaN")

print(series)

df['diabetes'] = pd.Series(series)
print(df)