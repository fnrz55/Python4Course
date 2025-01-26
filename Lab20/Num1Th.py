from threading import Thread
from time import sleep


class MyThread(Thread):

    def __init__(self, name):
        super().__init__(name=name)
        self.start()

    def run(self):
        num = 0
        print(f'{self.name} начал исполнение')

        for i in range(0, 10):
            sleep(0.4)
            print(f'В потоке {self.name} счетчик {num}')
            num += 1

        print(f'Поток {self.name} прекратил исполнение')
