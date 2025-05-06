import numpy as np

matrix_a = np.array([[1, 1, 1],
                     [1, 1, 1],
                     [1, 1, 2]])

matrix_b = np.array([[1, 3, 1],
                     [1, 3, 1],
                     [1, 3, 8]])

print("add: ")
print(np.add(matrix_a, matrix_b))
print("subtract: ")
print(np.subtract(matrix_a, matrix_b))

print("add: ")
print(np.add(matrix_b, matrix_a))
print("subtract: ")
print(np.subtract(matrix_b, matrix_a))
