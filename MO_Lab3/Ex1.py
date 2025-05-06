import numpy as np

arr = np.arange(-10, 11, 1)
print('Исходный массив:\n', arr)

for i in range(len(arr)):
    if i % 2 == 1:
        arr[i] = 0

print('Замена нечетных элементов на 0:\n', arr)

for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = -1

print("Замена отрицательных значений на -1:\n", arr)