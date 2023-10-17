"""Create a program that uses a loop to ask what items a visitor to the IE canteen wants. They are first presented 
with the following menu:
    What would you like from the IE canteen today?
    Toast with tomato [type "toast"]
    Coffee [type "coffee"]
    Croissant [type "croissant"]
    Tuna Baguette [type "baguette"]
        • Then, the program will ask them to enter as many items as they want, one at a time. When a user types the 
        item, it should be added to a list of items.
        • To stop adding items, the user should type "finished"
        • Finally, loop through the list and count how many of each item the user typed. The program will then 
        create a simple receipt (list of the products and the number ordered), e.g.You asked for:
            2 Toast(s)4 Coffee(s)
            1 Croissant(s)
            0 Tuna Baguette(s)"""


print("What would you like from the IE Canteen today?")
print("Toast with tomato [type 'toast']")
print("Coffee [type 'coffee']")
print("Croissant [type 'croissant]")
print("Tuna Baguette [type 'baguette']")

menu_list = []

while True:
    item = input('Enter here: ')
    if item == 'finished':
        break
    menu_list.append(item)

print(menu_list)

a = menu_list.count('toast')
b = menu_list.count('coffee')
c = menu_list.count('croissant')
d = menu_list.count('baguette')

print("Your Final Order:")
print(a, 'Toasts with tomato')
print(b, 'Coffees')
print(c, 'Criossants')
print(d, 'Baguettes')

