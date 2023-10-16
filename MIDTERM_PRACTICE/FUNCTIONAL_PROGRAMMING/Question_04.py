"""Write a function that receives another boolean function and a list, and returns another list with the 
elements of the list that return True when the boolean function is applied to them."""

# Program that filters the even numbers of a list using a boolean function

def filter_list(function, list):
    l = []
    for i in list:
        if function(i): #In other words, if True
            l.append(i)
    return l

def even(n):
    return n % 2 == 0 #Return boolean

list = [1, 2, 3, 4, 5, 6]

print(filter_list(even, list))