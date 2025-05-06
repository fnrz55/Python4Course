import numpy as np
from scipy import sparse

matrix = np.array([[0, 0],
                   [0, 1],
                   [3, 0]])

matrix_sparse = sparse.csr_matrix(matrix)
print(matrix_sparse)
print()
matrix_large = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                         [3, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

matrix_large_sparse = sparse.csr_matrix(matrix_large)
print(matrix_sparse)
print()
print(matrix_large_sparse)