"""Write a program that places 6 countries inputted by the user into two lists corresponding to the 
two hemispheres, Northern and Southern. 
The guidelines would be as follows:
    • The user enters a country and its corresponding hemisphere: for example, Spain and Northern.
    • The program adds the country to the corresponding hemispheres list (in this case Spain would be 
    placed in the Northern list.)
    • The program will continue 6 TIMES asking for a country and its associated hemisphere. Each time 
    the country will be placed into the appropriate hemisphere list.
    • The program will print the 2 lists. 

The final output would be something similar to:
Northern: [Spain, Egypt, Japan]
Southern: [Peru, Chile, South Africa]"""

northern = []
southern = []

while len(northern) + len(southern) != 6:
    country = input("Please enter a country: ")
    hemisphere = input("Is the country northern or southern? ")

    if hemisphere == 'northern':
        northern.append(country)
    elif hemisphere == 'southern':
        southern.append(country)
    else:
        print("Wrong input")

print('Northern List:\n', northern)
print('Southern List:\n', southern)