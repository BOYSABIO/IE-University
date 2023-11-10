"""Write a program that generates and displays a DataFrame with the data from the following table:
Month 		Sales	Expenses
January 	30500 	22000
February 	35600 	23400
March 		28300 	18100
April 		33900 	20700
"""

import pandas as pd

table = {
    "Month" : ["January", "February", "March", "April"],
    "Sales": [30500, 35600, 28300, 33900],
    "Expenses" : [22000, 23400, 18100, 20700]
}

df = pd.DataFrame(table)
print(df)

print(df.set_index("Month"))


# Alternative Solution

data = [["January", 30500, 22000], ["February", 35600, 23400], ["March", 28300, 18100], ["April", 33900, 20700]]

accounting = pd.DataFrame(data, columns = ["Month", "Sales", "Expenses"])
print(accounting.set_index("Month"))