import numpy as np

def stats_report(list_of_numbers):
    """
    This function takes a list of numbers and returns a dictionary of statistics.
    """
    stats_dict = {}
    stats_dict['mean'] = np.mean(list_of_numbers)
    stats_dict['median'] = np.median(list_of_numbers)
    stats_dict['std'] = np.std(list_of_numbers)
    return stats_dict

def divide(number_1, number_2):
    number_1 / number_2

def factorial(n):
    if not isinstance(n, int): 
        raise TypeError()
    if n < 0:
        raise ValueError() 
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    print(stats_report(data))
    print(divide(data[0], data[1]))
    print(factorial(5))