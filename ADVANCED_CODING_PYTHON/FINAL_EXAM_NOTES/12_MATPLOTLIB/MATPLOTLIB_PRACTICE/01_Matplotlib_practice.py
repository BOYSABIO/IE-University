"""Write a program that asks the user for sales over a range of years and displays a line diagram showing the 
evolution of sales."""

import matplotlib.pyplot as plt

start = int(input("Enter start year: "))
end = int(input("Enter end year: "))
sales = {}

for i in range(start, end +1):
    sales[i] = float(input("Enter sales for year " + str(i) + ": "))

fig, ax = plt.subplots()
ax.plot(sales.keys(), sales.values())
plt.show()