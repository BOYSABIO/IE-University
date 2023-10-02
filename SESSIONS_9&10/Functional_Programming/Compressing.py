subjects = ["math", "physics", "Chemistry", "Economics"]
grades = [6.0, 3.5, 7.5, 8.0]

compressedList = list(zip(subjects, grades))
print(compressedList)

dictionary = dict(zip(subjects, grades[0:3]))
print(dictionary)

from functools import reduce

def product(n, a):
    return n * a

def main():
    print(reduce(product, range(1,3)))
    
main()


print([x ** 2 for x in range(10)]) #Gives a list (merging two operations in one) list and squaring
print([x for x in range(10) if x%2 == 0])
print([x ** 2 for x in range(10) if x%2 == 0])


grades = {
    "Louis":5,
    "Alice":4,
    "John":3,
    "Fred":5,
    "Mary":3
}

print([name for (name, grade) in grades.items() if grade >= 5])

print({word:len(word) for word in ["I", "Love", "Programming"]})

print({name:grade + 1 for (name, grade) in grades.items() if grade >= 5})
