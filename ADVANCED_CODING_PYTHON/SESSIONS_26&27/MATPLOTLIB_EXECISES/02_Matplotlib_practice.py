"""Write a function that receives a dictionary with the grades of the subjects of a course and a string 
with the name of a color and returns a bar chart of the grades in the given color."""

import matplotlib.pyplot as plt

def bar_diagrams_grades(grades, color):
    fig, ax = plt.subplots()
    ax.bar(grades.keys(), grades.values(), color = color)
    return ax

grades = {
    "Programming":9,
    "Math":7,
    "Economics":6,
    "Statistics":8
}

bar_diagrams_grades(grades, color = "orange")
plt.show()