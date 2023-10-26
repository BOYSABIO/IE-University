import pandas as pd
import numpy as np

s = pd.Series(['a', 'b', None, 'c', np.NaN,  'd'])
print(s)
print()

print(s.dropna())
