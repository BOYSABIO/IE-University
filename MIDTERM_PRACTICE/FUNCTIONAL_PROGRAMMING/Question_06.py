"""Write a function to receive a list of grades and return the list of grades corresponding to those grades."""

def get_grades():
    number_of_grades = int(input("How many grades do you need to give?: "))
    grades = []
    for i in range(number_of_grades):
        new_grade = int(input("Please enter grade: "))
        grades.append(new_grade)
    print(grades)
    return grades

    

def converter(list):
    final_list = []
    for item in list:
        if item < 5:
            final_list.append('pass')
        else:
            final_list.append('fail')
    return final_list


list = get_grades()
print(list)
print(converter(list))
