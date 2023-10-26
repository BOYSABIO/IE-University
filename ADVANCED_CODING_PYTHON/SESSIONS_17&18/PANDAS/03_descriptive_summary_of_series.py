import pandas as pd

s = pd.Series([1, 1, 1, 1, 2, 2, 2, 3, 3, 4])

print(s.count())  # Sample size
print()

print(s.sum())  # Sum
print()

print(s.cumsum())  # Accumulated sum
print()

print(s.value_counts()) # Absolute frequencies
print()

print(s.value_counts(normalize=True))  # Relative frequencies
print()

print(s.min())  # Minimum
print()

print(s.max())  # Maximum
print()

print(s.mean())  # Mean
print()

print(s.var())  # Variance
print()

print(s.std())  # Standard deviation
print()

print(s.describe())  # Descriptive summary
