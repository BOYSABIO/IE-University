"""Write a function that receives a series of Pandas with the number of sales of a product during the 
months of a quarter and a title and creates a pie chart with the sales in png format with the given title. 
The diagram should be saved in a file with png format and thegiven title."""

import matplotlib.pyplot as plt
import pandas as pd

def pie_chart(sales, title):
    fig, ax = plt.subplots()
    sales.plot(kind = "pie", ax = ax)
    plt.ylabel("")
    plt.title(title)
    plt.savefig("PNG_FILES/" + title + ".png")
    return 

sales = {
    "Jan":200,
    "Feb":240,
    "Mar":310
}

series = pd.Series(sales)

pie_chart(series, title = "Sales_Pie_Chart")
plt.show()