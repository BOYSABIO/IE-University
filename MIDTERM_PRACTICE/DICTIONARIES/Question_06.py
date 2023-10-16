"""Write a program that creates an empty dictionary and fills it with information about aperson 
(e.g. name, age, gender, telephone, e-mail, etc.) that is requested from the user. Each time a new piece of 
information is added, the contents of the dictionary must be printed."""

dictionary = {}

# dictionary.update({input("Please enter item to add: "):input("Please enter information for added item: ")})

"""name = input("Please enter name: ")
dictionary.update({'Name':name.capitalize()})
print(dictionary)
print()

age = int(input("Please enter age: "))
dictionary.update({'Age':age})
print(dictionary)
print()

gender = input("Please enter gender: ")
dictionary.update({'Gender':gender.capitalize()})
print(dictionary)
print()

telephone = input("Please enter telephone number: ")
dictionary.update({'Phone':telephone})
print(dictionary)
print()

test = input("Please enter what information you want to add: ")
test_2 = input("Please fill information for above: ")
dictionary.update({test.capitalize():test_2.capitalize()})
print(dictionary)"""

check = 'yes'

while check != 'no':
    dictionary.update({input("Please enter item to add: ").capitalize():input("Please enter information for added item: ").capitalize()})
    print(dictionary)
    
    check = input("Type 'no' to quit: ")