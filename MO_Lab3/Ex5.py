import numpy as np

n = int(input('Введите N размер матрицы:'))
m = int(input('Введите M размер матрицы:'))

matrix = np.random.randint(-100, 100, size = (n,m))

print('Исходная матрица:\n', matrix)

first_n = np.mean(matrix[0])
last_n = np.mean(matrix[-1])

print(f'Среднее первой строки: {first_n}')
print(f'Среднее второй строки: {last_n}')

max_value = np.max(matrix)
print('max = ', max_value)
if first_n < last_n:
    print('Ср.арифметическое первой строки больше последней')
    matrix[0] += max_value
else:
    print('Ср.арифметическое второй строки больше последней')
    matrix[-1] += max_value

print('Измененная матрица:\n', matrix)

