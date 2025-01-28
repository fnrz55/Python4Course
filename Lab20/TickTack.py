import threading
import time


class TickTack:

    def __init__(self):
        self.state = ''
        self.synchronize = threading.Lock()
        self.condition = threading.Condition(self.synchronize)
    def tick(self, run1):
        with self.condition:
            if not run1:
                self.state = 'tick'
                self.condition.notify()
                return
            print('tick')
            self.state = 'tick'
            self.condition.notify()
            try:
                time.sleep(0.5)
                while self.state != 'tack':
                    self.condition.wait()
            except InterruptedError:
                print('Прерывание потока')

    def tack(self, run1):
        with self.condition:
            if not run1:
                self.state = 'tack'
                self.condition.notify()
                return
            print('tack')
            self.state = 'tack'
            self.condition.notify()
            try:
                time.sleep(0.5)
                while not self.state == 'tick':
                    self.condition.wait()
            except InterruptedError:
                print('Прерывание потока')


