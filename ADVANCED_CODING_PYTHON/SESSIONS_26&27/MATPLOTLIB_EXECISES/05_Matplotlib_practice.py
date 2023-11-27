"""Write a function that receives a series of Pandas with the number of sales of a product by years and a 
string with the type of graph to generate (lines, bars, sectors, areas) and returns a diagram of the 
indicated type with the evolution of sales by years and with thetitle "Evolution of the number of sales"""

import matplotlib.pyplot as plt
import pandas as pd

def diagram(series, diagram_type):
    fig, ax = plt.subplots()
    series.plot(kind = diagram_type, ax = ax)
    plt.title("Evolution of the number of sales")
    return ax

# Alternative
#df_sales = pd.Series([100, 200, 300, 400, 500], index = [2000, 2001, 2003, 2004, 2005])

start = int(input("Enter start year: "))
end = int(input("Enter end year: "))
sales = {}

for i in range(start, end +1):
    sales[i] = float(input("Enter sales for year " + str(i) + ": "))

diagram_type = input("Enter diagram type (line/bar/pie/area): ")

series = pd.Series(sales)

diagram(series, diagram_type)
plt.show()
