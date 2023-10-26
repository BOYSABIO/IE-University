"""Write a function to receive a dictionary with the subjects and grades of a student and return another dictionary 
with the subjects in capital letters and the grades corresponding to the grades."""

def converter(dictionary):
    new_dictionary = {}
    for subject, grade in dictionary.items():
        new_dictionary.update({subject.capitalize():grade.capitalize()})
    return new_dictionary

dictionary = {
    "math":'a',
    "science":'b',
    'fitness':'c'
}

print(converter(dictionary))