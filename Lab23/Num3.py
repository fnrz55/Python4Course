isIn = lambda a, b: b in a

str_value = "Это тест"
print("Тестируемая строка:", str_value)

if isIn(str_value, "Это"):
    print("'Это' найдено")
else:
    print("'Это' не найдено")

if isIn(str_value, "xyz"):
    print("'xyz' найдено")
else:
    print("'xyz' не найдено")
