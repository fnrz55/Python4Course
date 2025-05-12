get_constant_value = lambda: 98.6
print("Постоянное значение:", get_constant_value())

get_value = lambda n: 1.0 / n
print("Обратная величина 4 равна:", get_value(4.0))
print("Обратная величина 8 равна:", get_value(8.0))

try:
    myVal = lambda: "three"
    print("Новое значение:", myVal())
except Exception as e:
    print("Ошибка:", e)

try:
    get_value = lambda: 1
    print("Новое значение:", get_value())
except Exception as e:
    print("Ошибка:", e)
