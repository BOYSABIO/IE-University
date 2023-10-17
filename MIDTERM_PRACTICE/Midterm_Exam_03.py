apartments = [{'year': 2000, 
               'meters': 100, 
               'rooms': 3, 
               'garage': True, 
               'zone': 'A'}, 
               {'year': 2012, 
                'meters': 60, 
                'rooms': 2, 
                'garage': True, 
                'zone': 'B'}, {'year': 1980, 'meters': 120, 'rooms': 4, 'garage': False, 'zone': 'A'}, {'year': 2005, 'meters': 75, 'rooms': 3, 'garage': True, 'zone': 'B'}, {'year': 2015, 'meters': 90, 'rooms': 2, 'garage': False, 'zone': 'A'}]

print(apartments[1])
print(int(True))


# input = list of properties and a price
# Output = another list wiht properties price <= input

input = int(input("Please enter price: "))
list = []
less_than_price = []

for property in apartments:
    if property.get('zone') == 'A':
        price = (property.get('meters') * 1000 + property.get('rooms') * 5000 + int(property.get('garage')) * 15000) * ((1-property.get('year'))/100)
        list.append(price)
        property.update({'Price':price})
    else:
        price = (property.get('meters') * 1000 + property.get('rooms') * 5000 + int(property.get('garage')) * 15000) * (1-property.get('year')/100) *1.5
        list.append(price)
        property.update({'Price':price})

for property in apartments:
    if property.get('Price') <= input:
        less_than_price.append(property)

print(less_than_price)


# There must be an error in the formula as it only outputs negative numbers 
print("Property price list: \n", list)
print(apartments)
