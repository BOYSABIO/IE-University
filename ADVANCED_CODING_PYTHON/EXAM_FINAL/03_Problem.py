import csv

def read_create(file, column, percentage):
    with open(file) as csvfile:
        new_file = csv.reader(csvfile)
        print(new_file)
    
    # Iterating over the file to show all through the output
    for row in file:
        print(row)

file = "CSV_FILES/bank-loans.csv"
column = 'education'
print(read_create(file, column, percentage = True))