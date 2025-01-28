import threading
import time

class TickTack():
    def __init__(self):
        self.synchronize = threading.Lock()
        self.condition = threading.Condition()
        self.state = ''

    def tick(self, run1):
        with self.synchronize:
            if not run1:
                self.state = 'tick'
                with self.condition:
                    self.condition.notify()
                return
            print('tick')
            self.state = 'tick'
            with self.condition:
                self.condition.notify()
            try:
                time.sleep(0.5)
                while not self.state == 'tack':
                    with self.condition:
                        self.condition.wait()
            except InterruptedError:
                print('Прерывание потока')

    def tack(self, run1):
        with self.synchronize:
            if not run1:
                self.state = 'tack'
                with self.condition:
                    self.condition.notify()
                return
            print('tack')
            self.state = 'tack'
            with self.condition:
                self.condition.notify()
            try:
                time.sleep(0.5)
                while not self.state == 'tick':
                    with self.condition:
                        self.condition.wait()
            except InterruptedError:
                print('Прерывание потока')


