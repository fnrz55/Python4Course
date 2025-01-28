from threading import Thread


class TickTackThread(Thread):

    def __init__(self, name, tt):
        super().__init__(name=name)
        self.ttob = tt
        self.start()

    def run(self):
        if self.name == 'tick':
            while True:
                self.ttob.tick(True)
        else:
            while True:
                self.ttob.tack(True)

