import numpy as np

n = int(input('Введите размер массива: '))

arr1 = np.random.randint(0, 20, size = n)
arr2 = np.random.randint(0, 20, size = n)

mean_arr1 = np.mean(arr1)
mean_arr2 = np.mean(arr2)

print('Первый массив:\n', arr1)
print('Второй массив:\n', arr2)

if mean_arr1 == mean_arr2:
    print('Ср. арифметическое первого и второго массива равны')

if mean_arr1 > mean_arr2:
    print(f'Ср. арифметическое первого массива больше второго и равно {mean_arr1}')
else:
    print(f'Ср. арифметическое второго массива больше первого и равно {mean_arr2}')




