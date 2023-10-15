"""Metric system to imperial system converter:
    o Create a program that allows a user to input a distance in meters and convertsit to feet, yards or chains.
    o The user should type or decide if meters should be converted to feet, yards orchains. 
    Then print the distance in the selected unit to screen.
        • 1 meter = 3.28084 feet
        • 1 meter = 1.09361 yards
        • 1 meter = 0.0497097 chains
    • The user must not be able to enter a negative number.
    • A loop must be used to prompt the user again if the input is invalid"""


meters = float(input("Please enter distance in meters: "))
choice = input("Would you like to convert to feet, yards, or chains?: ")

if choice == 'feet':
    result = meters * 3.28084
    print(result)
elif choice == 'yards':
    result = meters * 1.09361
    print(result)
elif choice == 'chains':
    result = meters * 0.0497097
    print(result)

print("Done")