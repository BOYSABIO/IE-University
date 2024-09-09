"""Guess the number game: create a game where the user will have to guess an integerbetween 1 and 100. 
The program will pick a number between 1 and 100 randomly and prompt the user to guess it.
    o After each attempt the program will display
        • "higher" if the number to guess is greater than the user input,
        • "lower" if the number is lower than the user input or
        • "correct" if the user guessed the number.
    • The user will use that information to keep trying to guess the number. Once theuser guesses the number, the 
    program will display the number and the amount of attempts the user needed to guess it"."""

from random import *

count = 0
random_number = randint(1,100)
print("A random number has been selected\n")

while True:
    user_input = int(input("Please enter a number between 1 and 100:"))

    if user_input == random_number:
        print("Correct")
        break
    elif user_input >= random_number:
        print("Lower")
        count += 1
    elif user_input <= random_number:
        print("Higher")
        count += 1
    else:
        print("Is your input even a number?")

print("It took you", count, "tries!")