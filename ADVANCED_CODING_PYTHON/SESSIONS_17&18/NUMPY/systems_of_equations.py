import numpy as np

# System of two equations and two unknowns
# x + 2y = 1
# 3x + 5y = 2
a = np.array([[1, 2], [3, 5]])
b = np.array([1, 2])
print(np.linalg.solve(a, b))
