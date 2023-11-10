"""Write a program that asks the user for sales over a range of years and displays a series of sales data 
indexed by years, before and after applying a 10% discount."""

import pandas as pd

start = int(input("Please enter the starting year: "))
end = int(input("Please enter the ending year: "))
sales = {}

for i in range(start, end + 1):
    sales[i] = float(input("Enter the sales for year " + str(i) + ": "))

sales = pd.Series(sales)
print("Sales:\n", sales)
print()

print("Discount Sales:\n", sales * 0.9)