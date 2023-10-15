"""Write a program that stores in a variable the dictionary {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},asks the user for a 
currency and displays its symbol or a warning message if the currency isnot in the dictionary."""

dictionary = {
    'euro':'€',
    'dollar':'$',
    'yen':'¥'
}

user_input = input("Please enter a currency (euro/dollar/yen): ")

print(dictionary.get(user_input))