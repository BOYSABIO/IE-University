"""Create a program that asks the user for a string. Then ask them for a search term and write a function that 
searches the string for a search term and returns true if the term is present in the string or false if it is not. 
For example: 
What is the text: This is some text to search 
What do you want to search for: some 
True. The search term “some” is present in text you entered."""

text = input("Type some text: ")

split_text = text.split()
print("Your text has been created: ")
print(split_text)
print()

search = input("Search for a word in text: ")
if search in split_text:
    print(True)
else:
    print(False)