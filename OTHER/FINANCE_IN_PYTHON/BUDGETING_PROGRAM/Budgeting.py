import math
import pandas as pd
import calendar
import datetime

while True:
    print("1 ---- General")
    print("2 ---- Money Check")
    print("3 ---- Exit")
    program = int(input("Please indicate: "))
    if program == 1:
        print("Starting General Program...")
        print("---------------------------")
        income = int(input("Enter income: "))
        expense = int(input("Enter expense: "))
        net = income - expense

        # Add allowance
        allowance = 600
        check = input("Do you want to add allowance?: ")
        if check == "yes":
            total = net + allowance
        else:
            total = net
    
        # Initialize Basic Needs
        grocery = (total * 0.075) * 4
        fast_food = (total * 0.075) * 4
        total_food = grocery + fast_food
        ff_days = fast_food / 20

        # Initialize Finance Variables
        savings = total * 0.2
        remainder = round(((total - (grocery + fast_food + savings))), 2)

        stocks = round((remainder * 0.7), 2)
        bonds = round((remainder * 0.1), 2)
        Saving = (savings / 2)
        Roth_IRA = (savings / 2)
        schwab = Saving + Roth_IRA + stocks + bonds
        fun = round((remainder - (stocks + bonds)), 2)

        # Create & Print Dictionary
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

        print(dict)
        s = pd.Series(dict)
        print(s)

        print()
        print("Extra Points:")
        print("Grocery amount per week: ", round((grocery / 4),2))
        print()
        print("Number of fast food deliveries under 20: ", round(ff_days))
        print("Every ", round((31 / ff_days),3) , "days, you can order 20€ fast food")

    elif program == 2:
        print("test")

    elif program == 3:
        print("Ending Program...")
        break
     





def food(total):
    grocery = (total * 0.075) * 4
    fast_food = (total * 0.075) * 4
    total_food = grocery + fast_food
    return grocery, fast_food, total_food

#grocery, fast_food, total_food = food(total)

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

#remainder, stocks, bonds, Saving, Roth_IRA, schwab, fun = finance(total)

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



# Create a per week converter
def per_week(value):
    now = datetime.datetime.now()
    month_days = calendar.monthrange(now.year, now.month)[1]
    per_week = value / month_days
    return per_week


# Quick add for expenses (food / grocery / other)
# def quick_add():

3
#money_check(grocery, fast_food)



