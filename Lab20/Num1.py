from time import sleep

from Lab20.Num1Th import MyThread

th1 = MyThread('#child1')
th2 = MyThread('#child2')
th3 = MyThread('#child3')

for i in range(0,50):
    print('.')
    sleep(0.5)