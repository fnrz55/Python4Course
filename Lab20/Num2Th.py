from itertools import count
from threading import Thread

class Num7Cl(Thread):
    def __init__(self, name):
        super().__init__(name=name)
        self.count = 0
        self.stop = False
        self.current_name = name



    def run(self):
        print(f"{self.name} запущен")
        while not self.stop and self.count < 1e6:
            self.count += 1
            if self.current_name != self.name:
                self.current_name = self.name
                print(f"В потоке {self.current_name}")

    def stop(self):
        self.stop = False