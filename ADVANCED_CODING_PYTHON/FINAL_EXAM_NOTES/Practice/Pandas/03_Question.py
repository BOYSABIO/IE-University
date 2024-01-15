"""Write a function that receives a dictionary with the grades of the students of a course and returns a series 
with the grades of the passed students ordered from highest to lowest"""

import pandas as pd

def grade_sort(grades):
    series = pd.Series(grades)
    return series[series >= 5].sort_values(ascending = False)

grades = {
    "Jeff":10,
    "Steve":5,
    "Mary":8,
    "Malinda":3
}

print(grade_sort(grades))