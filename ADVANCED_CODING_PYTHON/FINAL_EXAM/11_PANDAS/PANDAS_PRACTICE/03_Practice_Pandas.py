"""Write a function that receives a dictionary with the grades of the students of a course and 
returns a series with the grades of the passed students ordered from highest to lowest."""

import pandas as pd

def passed(grades):
    grades = pd.Series(grades)
    return grades[grades >= 5].sort_values(ascending = False)
    



grades = {
    'John':9, 
    'Mary':6.5, 
    'Peter':4, 
    'Alice': 8.5, 
    'Louis': 5
}

print(passed(grades))