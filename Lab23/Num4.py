smallestF = lambda n: next((i for i in range(2, abs(n) + 1) if n % i == 0), abs(n))


print("Наименьшим делителем 12 является", smallestF(12))
print("Наименьшим делителем 11 является", smallestF(11))