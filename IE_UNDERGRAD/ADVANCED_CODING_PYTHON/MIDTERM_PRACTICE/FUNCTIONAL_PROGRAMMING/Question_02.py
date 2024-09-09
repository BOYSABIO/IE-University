"""Write a function that simulates a scientific calculator to calculate the sine, cosine, tangent, exponential and 
neperian logarithm. The function will ask the user for the value and the function to apply, and will display a table 
with the integers from 1 to the value entered and the result of applying the function to those integers."""

from math import *

def apply_function(x, n):
    functions = {
        'sine':sin,
        'cos':cos,
        'tan':tan,
        'exp':exp,
        'log':log
    }

    result = {}

    for i in range(1, n+1):
        result[i] = functions[x](i)
    return result

def calculator():
    x = input("Enter the funtion you would like to apply: ")
    n = int(input("Enter a positive Integer: "))

    for i, j in apply_function(x, n).items():
        print(i, '\t', j)
    return

calculator()