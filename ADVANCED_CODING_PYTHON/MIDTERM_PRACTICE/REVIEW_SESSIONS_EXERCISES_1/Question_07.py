"""Create a baby name generatoro Ask the user to input one list with boy names.
    o Create another list with girl names, again asking the user for the names.
    o Each list should have four names.
    o Ask the user the gender of the baby. There should be THREE choices BOY, GIRL, and UNKNOWN
    o Based on the answer, randomly choose a name from the correct list and provideit as output to 
    user: 
        If the baby is a BOY from the boy list, if the baby is a GIRL from the girl list and if the 
        baby is UNKNOWN print a random name from eachlist."""

from random import *

boy_names = []
girl_names = []
unknown = []

for i in range(4):
    boy = input("Please enter a boy name: ")
    girl = input("Please enter a girl name: ")

    boy_names.append(boy)
    girl_names.append(girl)
    unknown.append(boy)
    unknown.append(girl)

print('Boys:\n', boy_names)
print('Girls:\n', girl_names)
print('Unknown:\n', unknown)

choice = input("Please enter (boy/girl/unknown): ")
if choice == 'boy':
    print(boy_names[randrange(len(boy_names) + 1)])
elif choice == 'girl':
    print(girl_names[randrange(len(girl_names))])
else:
    print(unknown[randrange(len(unknown))])

