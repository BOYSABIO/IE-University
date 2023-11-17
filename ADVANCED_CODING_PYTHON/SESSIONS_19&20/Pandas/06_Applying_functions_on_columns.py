import pandas as pd
from math import log

df = pd.read_csv('CSV_FILES/cholesterol.csv')
print(df['height'].apply(log))
