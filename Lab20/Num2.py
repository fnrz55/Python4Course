import time

from Num2Th import Num2Thread

print("Основной поток запущен")

mt1 = Num2Thread("Высокий приоритет")
mt2 = Num2Thread("Низкий приоритет")

mt1.start()
mt2.start()

try:
    mt1.join()
    mt2.join()
except InterruptedError:
    print("Главный поток приостановлен")

print(f"Поток с высоким приоритетом считается {mt1.count}")
print(f"Поток с низким приоритетом считается {mt2.count}")
