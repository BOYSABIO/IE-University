"""Write a function that receives a DataFrame with the format of the previous exercise, a list of months, and 
returns the total balance (sales - expenses) in the indicated months."""

import pandas as pd

def total_balance(data, months):
    df = pd.DataFrame(data)
    df["Profit"] = df["Sales"] - df["Expenses"]
    return df[df.Month.isin(months)].Profit.sum()

data = {
    "Month":["Jan", "Feb", "Mar", "Apr"],
    "Sales":[30500, 35600, 28300, 33900],
    "Expenses":[2200, 23400, 18100, 20700]
}

print(total_balance(data, ["Jan", "Feb"]))