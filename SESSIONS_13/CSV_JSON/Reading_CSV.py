import csv

mycsvfile = input("Please enter the csv file you would like to read: ")

with open(mycsvfile) as csvfile:
    file = csv.reader(csvfile)
    print(file)
    
    # Iterating over the file to show all through the output
    for row in file:
        print(row)