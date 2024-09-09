"""Write a function that receives another function and a list, and returns another list with the result of applying 
the given function to each of the elements in the list."""


def apply_function(f, list):
    l = []

    for i in list:
        l.append(f(i))
    return l


def square(n):
    return n * n

list = [1, 2, 3, 4, 5, 6]

print(apply_function(square, list))