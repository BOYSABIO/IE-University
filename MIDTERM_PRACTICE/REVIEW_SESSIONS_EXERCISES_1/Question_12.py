"""Create a program that generates 1000 random integers between 1 and 100 (both included) and save them into a list.
    o Then, print the numbers in the list until it finds a number greater or equal to 90.
    o When it finds that number, it stops printing.
    o Then it prints the following 2 items:
        1. The count of how many numbers were printed
        2. The total sum of those numbers printed."""

from random import randint

numbers_list = []
total = 0
count = 0

for i in range(1000):
    new_number = randint(1, 100)
    total += new_number
    count += 1

    if new_number <= 90:
        numbers_list.append(new_number)
    else:
        numbers_list.append(new_number)
        break

print(numbers_list)
print(total)
print(count)