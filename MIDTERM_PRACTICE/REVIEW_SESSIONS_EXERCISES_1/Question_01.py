"""Suppose we have eight different colors. Make a program that chooses one of these colors at random 
and writes out the color. Use a list of color names and use either arandom number generator or the 
choice function in the random module to pick a list element."""

from random import *

color_list = ['red', 'blue', 'green', 'yellow', 'black', 'white', 'grey', 'orange']

print('Your random color is:', choice(color_list))