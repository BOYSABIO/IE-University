# Input = name, age, address, telephone number 
# Data type = Dictionary
# Output = NAME is AGE years old, lives at ADDRESS and his phone number is TELEPHONE

def main():
    name = input("Please enter name: ")
    age = int(input("Please enter age: "))
    address = input("Please enter your address: ")
    phone = input("Please enter phone number: ")

    person = {
        "Name":name,
        "Age":age,
        "address":address,
        "Phone Number":phone
    }

    print(name, "is", age, "years old, lives at", address, "and his phone number is", phone)

main()