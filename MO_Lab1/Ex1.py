import numpy as np

vector_row = np.array([1,2,3])
vector_column = np.array([[1],
                         [2],
                         [3]])

print(vector_row)
print(vector_column)


vector = input('Введите вектор: ')
vector_row = np.array(list(map(int, vector.split())))
vector_column = vector_row.reshape(-1, 1)
print("Горизонтальный вектор: ")
print(vector_row)
print("Вертикальный вектор: ")
print(vector_column)
