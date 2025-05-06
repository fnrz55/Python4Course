import numpy as np

n = int(input('Введите размер массива: '))
arr = np.random.randint(-15, 15, size=n)

print(arr)

maximum = np.max(arr)
minimum = np.min(arr)

for i in range(n):
    if arr[i] == maximum:
        print(f'max = {arr[i]}. Увеличим в два раза и заменим значение на {maximum * 2}')
        arr[i] = maximum * 2
        print(f'Отнимем от остальных значений элементов {minimum}')
    else:
        arr[i] = arr[i] - minimum

print(arr)
