import json



# Open and change balances

# Open previous balances to allocate

# Create initial dictionary
balances = {}

while True:
    new_item = input("Enter asset: ")
    if new_item == "":
        break
    balances.update({new_item.capitalize():0})

print(balances)
    
print()
print("Initial Allocaton: ")

for asset, percentage in balances.items():
    percentage = int(input("Enter amount for {}:".format(asset)))
    balances.update({asset:percentage})
    print("Updated: \n", asset + ': ', percentage)
    

print()
print('Allocated')
for asset, percentage in balances.items():
    print(asset + ': ', str(percentage) + '%')

with open(input("Enter file name: ") + '.json', 'w') as file:
    json.dump(balances, file)

print("File Saved")