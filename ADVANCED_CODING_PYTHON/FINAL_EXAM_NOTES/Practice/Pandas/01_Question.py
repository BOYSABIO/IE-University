"""Write a program that asks the user for sales over a range of years and displays a series of sales data 
indexed by years, before and after applying a 10% discount."""

import pandas as pd

start_date = int(input("Please enter start year: "))
end_date = int(input("Please enter end year: "))
sales = {}

for i in range(start_date, end_date + 1):
    sales[i] = float(input(f"Please enter sales for {i}:"))

sales_series = pd.Series(sales)
print("Sales \n", sales_series)
print("Discounted Sales \n", sales_series * 0.9)