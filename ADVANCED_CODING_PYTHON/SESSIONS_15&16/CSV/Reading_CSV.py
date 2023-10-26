import csv

mycsvfile = input("Please enter csv file: ")
with open(mycsvfile) as csvfile:
    file = csv.reader(csvfile)
    print(file)

    for i in file:
        print(i)