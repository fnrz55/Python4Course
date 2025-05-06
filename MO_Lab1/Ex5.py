import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

add_100 = lambda i: i + 100
vectorized_add_100 = np.vectorize(add_100)
vectorized_add_100(matrix)

print(vectorized_add_100(matrix))

# np.array([[101, 102, 103],
#        [104, 105, 106],
#        [107, 108, 109]])
