"""Create a program that allows the user to enter 5 first names: 
The program should:
    • Add these names to a list.
    • Create a new list with the number of letters of each first name as elements.
    • Calculate the square root of each number in the list in a new list.
    • Calculate the average number of letters of the names entered.
    
    Finally, the program will display the four things:
        • A list with the first names
        • A list with the number of letters of each first name
        • A list of the square root of each number
        • A sentence indicating the average number of letters of the names added by the user"""

from math import sqrt

names_list = []
count_names_list = []
square_root_list = []

for i in range(5):
    new_name = input("Please enter a name: ")
    new_name_count = len(new_name)
    names_list.append(new_name)

    names_list.append(new_name)
    count_names_list.append(new_name_count)
    square_root_list.append(sqrt(new_name_count))

print('The list of names:\n', names_list)
print('The length of each word in the list of names:\n', count_names_list)
print('The square root of the length of each word in the list:\n', square_root_list)