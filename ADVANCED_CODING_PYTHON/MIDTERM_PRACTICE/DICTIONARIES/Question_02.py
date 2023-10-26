"""Write a program that asks the user for his name, age, address and telephone number andstores it in a dictionary. 
It should then display the message <name> is <age> years old,lives at <address> and his phone number is <phone>."""

name = input("Please enter name: ")
age = int(input("Please enter age: "))
address = input("Please enter address: ")
phone_number = int(input("Please enter phone number: "))
print("Items stored to a dictionary")


person = {
    'Name':name,
    'Age':age,
    'Address':address,
    'Phone':phone_number
}

print(person.get('Name'), "is", person.get('Age'), "years old, lives at", person.get('Address'), "and his phone number is", person.get('Phone'))