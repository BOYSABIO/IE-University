import math
import pandas as pd


income = int(input("Enter income: "))
expense = int(input("Enter expense: "))

net = income - expense
allowance = 600
check = input("Do you want to add allowance?: ")
if check == "yes":
    total = net + allowance
else:
    total = net

def food(total):
    grocery = (total * 0.075) * 4
    fast_food = (total * 0.075) * 4
    total_food = grocery + fast_food
    return grocery, fast_food, total_food

grocery, fast_food, total_food = food(total)

def finance(total):
    savings = total * 0.2
    remainder = round(((total - (grocery + fast_food + savings))), 2)

    stocks = round((remainder * 0.7), 2)
    bonds = round((remainder * 0.1), 2)
    Saving = (savings / 2)
    Roth_IRA = (savings / 2)
    schwab = Saving + Roth_IRA + stocks + bonds
    fun = round((remainder - (stocks + bonds)), 2)
    return remainder, stocks, bonds, Saving, Roth_IRA, schwab, fun

remainder, stocks, bonds, Saving, Roth_IRA, schwab, fun = finance(total)

# When you are in middle of the month (calculate how much left for grocery / fast food)
def money_check(grocery, fast_food):
    balance = int(input("Enter balance: "))
    print(balance)
    difference = (grocery + fast_food) - balance
    remainder_for_food = balance - grocery
    amount_per_week = round((grocery / 4),2)
    balance_per_week = round((balance / 4), 2)
    remainder_per_week = balance_per_week - amount_per_week

    return print(difference, remainder_for_food, amount_per_week, balance_per_week, remainder_per_week)





# Quick add for expenses (food / grocery / other)
# def quick_add():



dict = {
    "Income":total,
    "Grocery":grocery,
    "Fast_Food":fast_food,
    "Total Food":total_food,
    "Saving":Saving,
    "Roth_IRA":Roth_IRA,
    "Remainder":remainder,
    "Stocks":stocks,
    "Bonds":bonds,
    "Schwab Total":schwab,
    "Fun":fun
}

money_check(grocery, fast_food)
print(dict)
s = pd.Series(dict)
print(s)

print()
print("Grocery amount per week: ", round((grocery / 4),2))
print()

ff_days = fast_food / 20
print("Number of fast food deliveries under 20: ", round(ff_days))
print("Every ", round(((ff_days / 31) * 7),3) , "days, you can order 20€ fast food")

# print(grocery + fast_food + Saving + Roth_IRA + stocks + bonds + fun)
# print(grocery / 31)
# print(Saving + Roth_IRA + stocks + bonds)
# print(income * 0.075)
# print()



