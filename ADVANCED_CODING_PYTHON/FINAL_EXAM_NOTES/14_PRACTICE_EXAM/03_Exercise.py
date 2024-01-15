"""The file trains.csv contains information about Madrid commuter train lines: id (train identifier),
line (line name), stations (origin and destination stations separated by a hyphen). You are requested to:
    1. Build a function that reads the file trains.csv and creates a dictionary where the key of each 
        pair is the line identifier and the associated value a list of two elements with the origin 
        station and the destination station as shown below as an example:
        {'10T0001C1': ['Principe Pio', 'Aeropuerto'], '10T0002C1':['Aeropuerto', 'Principe Pio'], ...}
        The function must receive the file name as parameter.
    2. Construct another function that saves the information of the dictionary obtained in the previous 
        section in a csv file separated by semicolon with 3 columns with the headers id, origin and 
        destination. The function must receive as parameters the dictionary with the trains and the 
        name of the resulting file."""

import pandas as pd
import csv

# Converting a Dataframe to a dictionary based off of a set index
def read_create(file):
    df = pd.read_csv(file)
    print(df)
    train_dict = df.set_index('id')['estaciones'].str.split('-').to_dict()
    return train_dict

# This part didnt work
def save_csv(dictionary):
    mycsvfile = "CSV_FILES/" + input("Please enter the name of your csv file: ") + ".csv"
    

    with open(mycsvfile, 'w', newline ="") as csvfile:
        file = csv.writer(csvfile)
        file.writerows(dictionary)
    
    return print("File Saved")
    

file = "CSV_FILES/trains.csv"
new_dictionary = read_create(file)
print(save_csv(new_dictionary))