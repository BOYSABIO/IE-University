from random import *

def maxMin(list):
    maxList = max(list)
    minList = min(list)
    return maxList, minList

def main():
    numbers = []
    for i in range(3):
        number = randint(0,50)
        numbers.append(number)

    print()
    print(numbers)

    maximum, minimum = maxMin(numbers)
    print()
    print("The maximum number is: ", maximum)
    print("The minimum number is: ", minimum)

main()