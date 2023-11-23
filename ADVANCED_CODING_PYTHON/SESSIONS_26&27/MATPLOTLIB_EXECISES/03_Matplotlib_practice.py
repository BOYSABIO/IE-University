"""Write a function that receives a series of Pandas with the grades of the students of acourse 
and returns a box plot with the grades. The diagram should have the title"Distribution of grades"."""

import pandas as pd
import matplotlib.pyplot as plt

def plot_grades(grades):
    fig, ax = plt.subplots()
    grades.plot(kind = "box", ax = ax)
    plt.xticks([])
    plt.title("Distribution of Grades")
    return ax

grades = [4, 8, 7.5, 10, 5.5, 3, 6]
series = pd.Series(grades)

plot_grades(series)
plt.show()