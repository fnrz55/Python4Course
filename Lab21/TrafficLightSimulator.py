import threading
from TrafficLightColor import TrafficLightColor


class TraficLightSimulator:
    def __init__(self, init):
        self.color_idx = init
        self.colors = list(TrafficLightColor)
        self.trafic_light_off = False
        self.stop = False
        self.counter = 11
        self.changed = False
        self.synchronize = threading.Lock()
        self.condition = threading.Condition(self.synchronize)

    def run(self):
        while not self.stop:
            try:
                self.timer(self.colors[self.color_idx])
            except InterruptedError:
                print('Поток прерван')
            self.change_color()

    def change_color(self):
        with self.condition:
            if self.color_idx == len(self.colors) - 1:
                self.color_idx = 0
                self.changed = True
                return
            if self.trafic_light_off:
                self.color_idx = 1
                self.condition.notify()
            else:
                self.color_idx += 1
                self.condition.notify()
            self.changed = True

    def wait_for_change(self):
        with self.condition:
            try:
                while not self.changed:
                    self.condition.wait()
                self.changed = False
            except InterruptedError:
                print('Поток прерван')

    def timer(self, color):
        with self.condition:
            print(color.get_name())
            sec = color.get_time()
            while sec != 0:
                print(sec)
                sec -= 1
                self.condition.wait(1)
                self.counter += 1
                if self.counter == 60:
                    print('13:00 Светофор выключается')
                    self.trafic_light_off = True
                    self.condition.wait(1)
                    self.counter = 0
                    self.changed = True
                    break

    def cancel(self):
        self.stop = True