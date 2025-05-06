import numpy as np

n = int(input("Введите размерность матрицы: "))

matrix = np.array([[(i + j - 1) ** (n - 1) for j in range(1, n + 1)] for i in range(1, n + 1)])

x = np.random.rand(n)
s = np.array([np.sum(x**k) for k in range(2 * n - 1)])
matrix2 = np.array([[s[i + j] for j in range(n)] for i in range(n)])

print(matrix)
print(matrix2)

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
print()
print("Результат сложения Матрицы 3 и Матрицы 4:\n", np.add(matrix, matrix2))
print("Результат вычитания Матрицы 3 и Матрицы 4:\n", np.subtract(matrix, matrix2))
print("Результат умножения Матрицы 3 и Матрицы 4:\n", np.dot(matrix, matrix2))