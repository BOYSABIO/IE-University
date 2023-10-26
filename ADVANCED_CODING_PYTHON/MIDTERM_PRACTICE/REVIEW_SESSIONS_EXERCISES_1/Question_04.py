"""Create a program that collects three lists of information about a user’s likes:
    • A list of their three favorite films
    • A list of their three favorite countries
    • A list of their three favorite numbers
        • The program will first ask the user for the three films, 
        the three numbers, and the three countries. 
        
        It will print the three lists in the following way:
            i.The list of films should be printed in alphabetical order (from A to Z)
            ii.The list of countries should be printed in REVERSE alphabetical order(from Z to A)
            iii. The list of numbers can be printed in any order. 
            
        In addition, after printing the list, the average of the three numbers in the list should 
        be printed. Note: focus on a proper use of loops in the program"""

films_list = []
countries_list = []
numbers_list = []
count = 0

for i in range(3):
    new_film = input("Please enter a film: ")
    new_country = input("Please enter a country: ")
    new_number = int(input("Please enter a number: "))

    count += new_number

    films_list.append(new_film)
    countries_list.append(new_country)
    numbers_list.append(new_number)

films_list.reverse()
print('Films in reverse alphabetical order:', films_list)

countries_list.sort()
print('Countries in alphabetical order:', countries_list)

print('List of numbers:', numbers_list)
print('Average of numbers in list:', count/3)