"""Write a function to receive a dictionary with the subjects and grades of a student and return another dictionary 
with the subjects in capital letters and the grades corresponding to the grades passed."""

def grades(dictionary):
    final_report = {}
    for subject, grade in dictionary.items():
        if grade < 5:
            final_report.update({subject.capitalize():'Fail'})
        else:
            final_report.update({subject.capitalize():'Pass'})
    return final_report


dictionary = {
    "math":5,
    'science':10,
    'fitness':3
}

print(grades(dictionary))