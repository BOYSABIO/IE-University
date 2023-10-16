"""Write a program that stores the dictionary with the credits of the subjects of a course 
{'Mathematics': 6, 'Physics': 4, 'Chemistry': 5} and then displays the credits of each subject in the format 
<subject> has <credits> credits, where <subject> is each of the subjects of the course, and <credits> are its 
credits. At the end it should also show the total number of credits for the course."""

dictionary = {
    'Mathematics': 6, 
    'Physics': 4, 
    'Chemistry': 5
}

total = 0

for subject, credits in dictionary.items():
    total += credits
    print(subject.capitalize(), 'has', credits, 'credits')

print()
print('The total credits is:', total)
