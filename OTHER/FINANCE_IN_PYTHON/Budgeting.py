import math
import pandas as pd

expense = int(input("Enter expense: "))

income = 723 - expense
allowance = 600
total = income + allowance

grocery = (total * 0.075) * 4
fast_food = (total * 0.075) * 4

savings = total * 0.2
remainder = round(((total - (grocery + fast_food + savings))), 2)

stocks = round((remainder * 0.7), 2)
bonds = round((remainder * 0.1), 2)
fun = round((remainder - (stocks + bonds)), 2)


dict = {
    "Income":total,
    "Grocery":grocery,
    "Fast_Food":fast_food,
    "Saving":(savings / 2),
    "Roth_IRA":(savings / 2),
    "Remainder":remainder,
    "Stocks":stocks,
    "Bonds":bonds,
    "Fun":fun
}

print(dict)
print(pd.Series(dict))

print()
print(grocery / 4)