"""Write a function that receives a Pandas dataframe with the income and expenses of a company by months and 
returns a line diagram with two lines, one for income and one for expenses. The diagram must have a legend 
identifying the income line and the expense line, a title with the name "Evolution of income and expenses" 
and the y-axis must start at 0."""

import pandas as pd
import matplotlib.pyplot as plt

def line_diagram_income_expense(dataframe):
    fig, ax = plt.subplots()
    dataframe.plot(ax = ax)
    ax.set_ylim([0, max(dataframe.Income.max(), dataframe.Expenses.max()) + 500])
    plt.title("Income and Expenses Evolution")
    return ax

data = {
    "Month":["Jan", "Feb", "Mar", "Apr"],
    "Income":[100, 200, 300, 400],
    "Expenses":[50, 100, 150, 200]
}

dataframe = pd.DataFrame(data).set_index("Month")

line_diagram_income_expense(dataframe)
plt.legend(loc = "lower left")
plt.show()