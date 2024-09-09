import pandas as pd
import numpy as np

df = pd.read_csv('CSV_FILES/cholesterol.csv')
print(df.groupby('gender').agg(np.max))
