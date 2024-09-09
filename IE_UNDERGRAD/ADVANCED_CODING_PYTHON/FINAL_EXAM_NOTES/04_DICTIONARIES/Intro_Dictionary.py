# Dictionary is a way to store values in pairs
# Curly braces are used to create dictionaries {}
# Dictionaries can contain any datatype including lists and even dictionaries
# You can add and remove information (same as lists)
# The key's are unique and cannot be repeated in the same dictionary

dictionary = {
    "name":"Paul",
    "office":218,
    "email":"pjohn@gmail.com"
}

print(dictionary["name"]) # You get the corresponing value
print(dictionary)

print(dictionary.get("company", "google"))
print(dictionary)

dictionary["company"] = "google" # Add
print(dictionary)

dictionary.pop("office") # Remove
print(dictionary)

print(dictionary.popitem()) # Take it use it and then remove it (If no item is indicated it takes the last one)

del dictionary["email"]
print(dictionary)

dictionary.clear()
print(dictionary)


# Copying dictionaries by reference
a = {
    1:"A",
    2:"B",
    3:"C"
}

print(a)
b = a 

b.pop(2)

# They will be the same as they are coppied by reference
print(b)
print(a)

#Copy by values
a = {
    1:"A",
    2:"B",
    3:"C"
}

b = dict(a)

b.pop(2)

print(a)
print(b)
