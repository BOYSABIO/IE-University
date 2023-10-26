import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print()
print(a[1, 0])  # Access to the element in row 1 column 0
print()
print(a[1][0])  # Another way to access the same element
print()
print(a[:, 0:2])
print()

