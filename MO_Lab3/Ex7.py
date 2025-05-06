import numpy as np

rows = int(input("Введите количество строк массива: "))
cols = int(input("Введите количество столбцов массива: "))
array = np.random.randint(0, 101, size=(rows, cols))

print("Исходный массив:")
print(array)

max_value = np.max(array)
max_index = np.unravel_index(np.argmax(array), array.shape)
print("Максимальный элемент:", max_value)
print("Индексы максимального элемента:", max_index)

diagonal1 = max_index[0] == max_index[1]
diagonal2 = max_index[0] + max_index[1] == cols - 1

if diagonal1 or diagonal2:
    max_value1 = 2 * max_value

    if diagonal1:
        for i in range(rows):
            if i < cols:
                array[i, cols - 1 - i] += max_value1

    if diagonal2:
        for i in range(cols):
            if i < rows:
                array[i, i] += max_value1

    print("Элементы противоположной диагонали увеличены на", max_value1)
else:
    print("Максимум не лежит на диагоналях.")

print("Измененный массив:")
print(array)