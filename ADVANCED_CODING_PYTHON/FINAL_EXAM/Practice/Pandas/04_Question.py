"""Write a program that generates and displays a DataFrame with the data from the followingtable:"""

import pandas as pd

data = {
    "Month":["Jan", "Feb", "Mar", "Apr"],
    "Sales":[30500, 35600, 28300, 33900],
    "Expenses":[2200, 23400, 18100, 20700]
}

df = pd.DataFrame(data)
print(df)