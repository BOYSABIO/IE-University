"""Write a Python program that takes 10 numbers using a loop and puts them in a list.
Then multiply all the items in the list and print the result in the output."""

number_list = []
final_value = 1

for i in range(10):
    new_number = int(input("Please enter a number to add to the list: "))
    number_list.append(new_number)
    final_value *= new_number

print("Here is your list: \n", number_list)
print('All the numbers multiplied together:', final_value)