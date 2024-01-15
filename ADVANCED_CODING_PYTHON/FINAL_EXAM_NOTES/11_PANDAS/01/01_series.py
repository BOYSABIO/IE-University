import pandas as pd

s = pd.Series(['Mathematics', 'Statistics', 'Economics', 'Programming', 'Technology'], dtype='string')
print(s)

s_dictionary = s = pd.Series({'Mathematics' : 6.0, 'Statistics' : 5.0, 'Economics' : 4.0, 'Programming' : 8.0, 'Technology' : 6.0})
print(s_dictionary)

s_sequence = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print(s_sequence.size)
print(s_sequence.index)
print(s_sequence.dtype)