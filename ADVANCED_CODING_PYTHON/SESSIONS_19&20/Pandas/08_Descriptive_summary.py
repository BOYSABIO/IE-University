import pandas as pd
import numpy as np

df = pd.read_csv('CSV_FILES/cholesterol.csv')

print(df.age.count())  # Sample size
print()

print(df.age.mean())  # Mean
print()

print(df.age.var())  # Variance
print()

print(df.age.std())  # Standard deviation
print()

print(df.describe())  # Descriptive summary
print()

print(df.describe(include='object'))
