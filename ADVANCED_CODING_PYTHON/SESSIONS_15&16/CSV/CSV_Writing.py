import csv

mycsvfile = input("Please enter the name of your csv file: ")
csv_rowlist = [["SN", "Movie", "Main Protagonist"],
               [1, "The Lord of the rings", "Frodo Baggings"],
               [2, "Harry Potter", "Hary Potter"]]

with open(mycsvfile, 'w', newline ="") as csvfile:
    file = csv.writer(csvfile)
    file.writerows(csv_rowlist)

