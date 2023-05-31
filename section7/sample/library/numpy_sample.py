import numpy as np

A = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

B = np.matrix([[1, 1, 1], [0, 1, 1], [0, 0, 1]])

print(A)
print(B)

AB = np.dot(A, B)
print(AB)
