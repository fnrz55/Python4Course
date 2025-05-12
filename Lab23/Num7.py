import math

a = int(input('Введите катет а: '))
b = int(input('Введите катет b: '))

hip = lambda a, b: math.sqrt(a ** 2 + b ** 2)
c = hip(a, b)

check = lambda a, b, c: a > 0 and b > 0 and math.isclose(a ** 2 + b ** 2, c ** 2)

if check(a, b, c):
    print(f'Треугольник существует. Гипотенуза = {c:0.2f}')
else:
    print(f'Треугольник не существует')