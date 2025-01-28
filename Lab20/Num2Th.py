import threading
from itertools import count
from threading import Thread


class Num2Thread(Thread):

    current_name = ''

    def __init__(self, name):
        super().__init__(name=name)
        self.count = 0
        self.stop = False
        Num2Thread.current_name = name

    def run(self):
        print(f"{self.name} запущен")
        while True:
            self.count += 1
            if Num2Thread.current_name != self.name:
                Num2Thread.current_name = self.name
                print(f"В потоке {self.current_name} \n")
            if self.stop or self.count >= 1e6:
                break
        self.stop = True
        print(f'Поток {self.name} прекратил исполнение')

