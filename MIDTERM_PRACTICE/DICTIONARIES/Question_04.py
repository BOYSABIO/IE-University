"""Write a program that asks for a date in dd/mm/yyyy format and displays the same date in the format: <month> dd, 
yyyy where <month> is the name of the month."""

months = {
    1:'january',
    2:'february',
    3:'march',
    4:'april'
}

date = input("Please enter date (dd/mm/yyy): ")
list = date.split('/')
print(list)
print(months.get(int(list[1])).capitalize(), list[0], list[2])