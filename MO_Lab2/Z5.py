import numpy as np

n = int(input("Введите размерность матрицы: "))

x_vals = np.random.rand(n)
s = np.array([np.sum(x_vals**k) for k in range(2 * n)])

x = float(input("Введите значение x: "))

matrix = np.array([[s[i + j] if j < n else x**i for j in range(n + 1)] for i in range(n + 1)])

print("Матрица:")
print(matrix)

print("Размерность матрицы: ", matrix.shape)
print("Размер матрицы: ", matrix.size)
print("Число осей матрицы: ", matrix.ndim)
print("Минимальное значение: ", np.min(matrix))
print("Максимальное значение: ", np.max(matrix))
print("Среднее значение: ", np.mean(matrix))
print("Дисперсия: ", np.var(matrix))
print("Стандартное отклонение: ", np.std(matrix))
print("Транспонирование матрицы:\n", matrix.T, "\n")
print("Сглаживание матрицы:\n", matrix.flatten(), "\n")
print("Ранг матрицы: ", np.linalg.matrix_rank(matrix))
print("Определитель матрицы: ", np.linalg.det(matrix))
print("Диагональ матрицы: ", matrix.diagonal())
print("След матрицы: ", matrix.trace())
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Собственное значение матрицы: ", eigenvalues)
print("Собственный вектор матрицы:\n", eigenvectors)
print("reshape:\n", matrix.reshape((n + 1, n + 1)))