import pandas as pd

s = pd.Series({'Mathematics': 6.0,  'Economics': 4.5, 'Programming': 8.5})
print(s[s>5])
