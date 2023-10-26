def get_phone(file, client):
    try:
        f = open(file, "r")
    except FileNotFoundError:
        return("The file " + file + " does not exist!")
    else:
        directory = f.readlines()
        f.close()
        directory = dict([tuple(line.split(",")) for line in directory]) #Compressing
        if client in directory:
            return directory[client]
        else:
            return ("The client " + client + " does not exist!")
 
def add_phone(file, client, telf):
    try:
        f = open(file, "a")
    except FileNotFoundError:
        return ("The file " + file + " does not exist!")
    else:
        f.write(client + "," + telf + "\n")
        f.close()
        return("The telephone has been added.")
 
def remove_phone(file, client):
    try:
        f = open(file, "r")
    except FileNotFoundError:
        return ("The file " + file + " does not exist!")
    else:
        directory = f.readlines()
        f.close()
        directory = dict([tuple(line.split(",")) for line in directory]) #Compressing
        if client in directory:
            del directory[client]
            f = open(file, "w")
            for name, telf in directory.items():
                f.write(name + "," + telf)
            f.close()
            return("Client has been deleted!")
        else:
            return("The client " + client + " does not exist!")
        
def create_directory(file):
    import os
    if os.path.isfile(file):
        answer = input("The file" + file + "already exists. Do you want to empty it?: ")
        if answer == "No":
            return "The file was not created (already exists)"
    f = open(file, "w")
    f.close()
    return "The file has been created"

def menu():
    print("Phone book management")
    print("==============================")
    print("1 = Consult a phone")
    print("2 = Add a number")
    print("3 = Delete a number")
    print("4 = Create a phonebook")
    print("0 = End")

    option = input("Please enter the number here: ")
    return option
    
def directory():
    file = "phone_book.txt"
    while True:
        option = menu()
        if option == "1":
            name = input("Enter the customers name: ")
            print(get_phone(file, name))
        elif option == "2":
            name = input("Enter the customers name: ")
            telf = input("Enter customers telephone number: ")
            print(add_phone(file, name, telf))
        elif option == "3":
            name = input("Enter the customers name: ")
            print(remove_phone(file, name))
        elif option == "4":
            print(create_directory(file))
        else:
            break
    return

directory()