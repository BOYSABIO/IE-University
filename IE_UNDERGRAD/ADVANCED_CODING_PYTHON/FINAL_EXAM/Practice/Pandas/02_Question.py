"""Write a function that receives a dictionary with the grades of the students of a course and returns a series with 
the minimum grade, maximum grade, average and standard deviation."""
import pandas as pd

def grade_stats(grades):
    series = pd.Series(grades)
    statistics = pd.Series([series.min(), series.max(), series.mean(), series.std()], index = ['Min', 'Max', "Mean", "Standard Deviation"])
    return statistics

grades = {
    "Jeff":10,
    "Steve":5,
    "Mary":8,
    "Malinda":3
}

print(grade_stats(grades))