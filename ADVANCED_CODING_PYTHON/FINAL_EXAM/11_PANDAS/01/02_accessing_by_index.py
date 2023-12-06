import pandas as pd
s = pd.Series(['Mathematics', 'Statistics', 'Economics', 'Programming', 'Technology'], dtype='string')
print(s[1:3])

import pandas as pd
s = pd.Series({'Mathematics': 6.0,  'Economics': 4.5, 'Programming': 8.5})
print(s['Economics'])

import pandas as pd
s = pd.Series({'Mathematics': 6.0,  'Economics': 4.5, 'Programming': 8.5})
print(s[['Programming','Economics']])
