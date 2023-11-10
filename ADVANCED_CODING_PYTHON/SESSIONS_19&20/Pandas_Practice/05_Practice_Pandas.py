"""Write a function that receives a DataFrame with the format of the previous exercise, a list of 
months, and returns the total balance (sales - expenses) in the indicated months."""

import pandas as pd

table = {
    "Month" : ["January", "February", "March", "April"],
    "Sales": [30500, 35600, 28300, 33900],
    "Expenses" : [22000, 23400, 18100, 20700]
}

df = pd.DataFrame(table)

# print("The total balance is:", df["Sales"].sum() - df["Expenses"].sum())

def balance(df, months):
    df["Balance"] = df.Sales - df.Expenses
    return df.set_index("Month").loc[months, "Balance"].sum()

print(balance(df, months = ["January", "April"]))
print()


def balance2(df, months):
    df["Balance"] = df.Sales - df.Expenses
    return df[df.Month.isin(months)].Balance.sum()

print(balance2(df, months = ["January"]))
