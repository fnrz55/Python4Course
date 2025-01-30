def is_factor(n, d):
    return n % d == 0

def is_in(a, b):
    return b in a

def main():
    if is_factor(10, 2):
        print("2 является делителем 10")
    print()

    if is_factor(212.0, 4.0):
        print("4.0 является делителем 212.0")
    print()

    str_test = "Обобщенный функциональный интерфейс."
    print(f"Тестируемая строка: {str_test}")
    if is_in(str_test, "face"):
        print("'face' найдено")
    else:
        print("'face' не найдено")
    print()

if __name__ == "__main__":
    main()