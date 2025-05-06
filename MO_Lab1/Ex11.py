import numpy as np

matrix = np.array([[1, 1, 1],
                   [1, 1, 10],
                   [1, 1, 15]])

print(np.linalg.matrix_rank(matrix))
