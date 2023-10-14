"""Create a program that simulates a lottery where the user chooses the number of results
from 1 to 100. Use a loop to produce the correct number of results. 
Example: How many numbers should the program produce: 5 The results: 56 43 65 45 77"""

from random import *

spins = int(input("Please enter how many times you want to play: "))

for i in range(spins):
    print(randint(1,100))

