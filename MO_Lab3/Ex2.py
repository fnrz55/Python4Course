import numpy as np

n = int(input('Введите размер n матрицы: '))
arr = np.array(np.random.randint(-10, 10, (n, n)))
print("Исходная матрица:\n",arr)

sum_main_diag = np.trace(arr)
sum_p_diag = np.trace(np.fliplr(arr))

if sum_main_diag > sum_p_diag:
    print('Сумма главной диагонали больше суммы побочной диагонали.')
    d = sum_main_diag - sum_p_diag
    d_sq = d**2
    print(f'Меняем отрицательные значения над главной диагонали на квадрат разности сумм диагоналей, равную {d_sq}')
    for i in range(n):
        for j in range(n):
            if j > i and arr[i, j] < 0:
                arr[i,j] = d_sq

    print("Измененная матрица:\n", arr)
else:
    print('Сумма главной диагонали меньше суммы побочной диагонали. Изменения не требуются.')

