"""Write a program that stores in a dictionary the prices of the fruits in the table, asks the user for a fruit, 
a number of kilos and displays the price of that number of kilos of fruit. If the fruit is not in the dictionary 
it should display a message informing about it."""

fruits = {}
prices = {}
n = int(input("How many items would you like to add to the cart?: "))

for i in range(n):
    fruit = input("Enter a food: ")
    kilo = int(input("Enter the weight: "))
    fruits.update({fruit.capitalize():kilo})

print(fruits)

for fruit, kilo in fruits.items():
    if kilo < 10:
        prices.update({fruit.capitalize():kilo * 2})
    else:
        prices.update({fruit.capitalize():kilo * 1.5})

print(prices)