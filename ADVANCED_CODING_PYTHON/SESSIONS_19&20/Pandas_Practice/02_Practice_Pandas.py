"""Write a function that receives a dictionary with the grades of the students of a course and returns a 
series with the minimum grade, maximum grade, average and standard deviation."""

import pandas as pd

def statistics_grades(grades):
    grades = pd.Series(grades)
    statistics = pd.Series([grades.min(), grades.max(), grades.mean(), grades.std()], 
                           index = ["Min", "Max", "Mean", "STD"])
    return statistics

grades = {
    'John':9, 
    'Mary':6.5, 
    'Peter':4, 
    'Alice': 8.5, 
    'Louis': 5
}

print(statistics_grades(grades))