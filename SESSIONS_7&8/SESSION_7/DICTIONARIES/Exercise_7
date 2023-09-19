basket = {}

more = True
while more:
    item = input("Please enter an item: ")
    price = float(input("Enter the price of", item, ":"))
    basket[item] = price
    more = input("Do you want to add another item?: ") == "Yes"

cost = 0
print("Shopping list")
for item, price in basket.items():
    print(item, "\t", price) # \t is indentation
    cost += price
print("Total Cost: ", cost)
