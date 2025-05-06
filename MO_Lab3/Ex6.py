import numpy as np

n = int(input('Введите N размер матрицы:'))
m = int(input('Введите M размер матрицы:'))

matrix = np.random.randint(-100, 100, size = (n,m))
print(matrix)

max_value = np.max(matrix)
min_value = np.min(matrix)

print(f'max = {max_value}')
print(f'min = {min_value}')

max_index = np.where(matrix == max_value)
min_index = np.where(matrix == min_value)

if max_value % 2 == 0 and min_value % 2 == 0:
    print('max и min являются четными. Делим на два.')
    matrix[max_index] = max_value // 2
    matrix[min_index] = min_value // 2
    print('Измененная матрица:\n', matrix)
else:
    print('max и min не являются четными одновременно.')
    print('Измененная матрица:\n', matrix.T)