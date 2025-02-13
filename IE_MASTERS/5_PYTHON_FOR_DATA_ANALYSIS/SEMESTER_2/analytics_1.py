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

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    print(stats_report(data))
    print(divide(data[0], data[1]))
