import numpy as np

n = int(input("Введите размерность матрицы: "))
a = np.random.rand(n)
b = np.random.rand(n)

matrix = np.array([
    [((1-a[i]**n * b[j]**n) / (1-a[i]*b[j])) for j in range(n)]
    for i in range(n)
])

matrix2 = np.array([
    [(a[i] + b[i]) for j in range(n)]
    for i in range(n)
])

print(matrix)
print("Матрица 2:\n",matrix2)

print("Размерность матрицы: ", matrix.shape)
print("Размер матрицы: ", matrix.size)
print("Число осей матрицы: ", matrix.ndim)
print("Минимальное значение: ", np.min(matrix))
print("Максимальное значение: ", np.max(matrix))
print("Среднее значение: ", np.mean(matrix))
print("Дисперсия: ", np.var(matrix))
print("Стандартное отклонение: ", np.std(matrix))
print("Транспонирование матрицы:\n", matrix.T, "\n")
print("Reshape: ", matrix.reshape(n, n))
print("Сглаживание матрицы:\n", matrix.flatten(), "\n")
print("Ранг матрицы: ", np.linalg.matrix_rank(matrix))
print("Определитель матрицы: ", np.linalg.det(matrix))
print("Диагональ матрицы: ", matrix.diagonal())
print("След матрицы: ", matrix.trace())
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Собственное значение матрицы: ", eigenvalues)
print("Собственный вектор матрицы:\n", eigenvectors)
print("Результат сложения Матрицы 1 и Матрицы 2:\n", np.add(matrix, matrix2))
print("Результат вычитания Матрицы 1 и Матрицы 2:\n", np.subtract(matrix, matrix2))
print("Результат умножения Матрицы 1 и Матрицы 2:\n", np.dot(matrix, matrix2))
