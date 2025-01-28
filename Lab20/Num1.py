from time import sleep
from Num1Th import MyThread


th1 = MyThread('#child1')
th2 = MyThread('#child2')
th3 = MyThread('#child3')

try:
    for i in range(0, 50):
        print('.')
        sleep(0.1)
except InterruptedError:
    print('Главный поток приостановлен')

print('Главный поток завершил исполнение')