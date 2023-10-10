# Multi Side Die
# Class definition for an n-sided die

from random import randrange

class MSDIE:

    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides + 1)

    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value


# Die with 6 sides
die1 = MSDIE(6) #Consructor
die1.roll()
print("The result between 1 and 6 is:", die1.getValue())
print()

# Die with 100 sides
die2 = MSDIE(100) #Consructor
die2.roll()
print("The result between 1 and 6 is:", die2.getValue())
print()

die1.setValue(3)
print(die1.getValue())