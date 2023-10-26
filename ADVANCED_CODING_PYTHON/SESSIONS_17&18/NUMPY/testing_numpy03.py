import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a[(a % 2 == 0)])
print()
print(a[(a % 2 ==0) & (a > 2)])
