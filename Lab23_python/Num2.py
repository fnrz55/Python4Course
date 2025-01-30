isF = lambda n, d: (n % d) == 0
lessThan = lambda n, m: n < m
absEqual = lambda n, m: abs(n) == abs(m)

if __name__ == "__main__":
    if isF(10, 2):
        print("2 является делителем 10")
    if not isF(10, 3):
        print("3 НЕ является делителем 10")
    print()

    if lessThan(2, 10):
        print("2 меньше 10")
    if not lessThan(10, 2):
        print("10 не меньше 2")
    print()

    if absEqual(4, -4):
        print("Абсолютные величины 4 и -4 равны")
    if not absEqual(4, -5):
        print("Абсолютные величины 4 и -5 не равны")