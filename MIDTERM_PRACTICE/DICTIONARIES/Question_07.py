"""Write a program that creates a dictionary simulating a shopping cart. The program should ask for the item and 
its price and add the pair to the dictionary, until the user decides to finish. Then the shopping list and the 
total cost should be displayed on the screen, with the following format 
Shopping list
Item 1 Price
Item 2 Price
Item 3 Price
... ...
Total Cost"""

shopping_cart = {}
check = ''
total = 0

while check != 'quit':
    item = input("Please enter item name: ")
    price = int(input("Please enter item price: "))
    total += price
    shopping_cart.update({item.capitalize():price})
    print('Shopping Cart View:')
    print(shopping_cart)
    check = input("Type <quit> to get final shopping cart or enter to add another item: ")

print()
print("Your Final Shopping Cart:")
print(shopping_cart)
print("Total:", total)