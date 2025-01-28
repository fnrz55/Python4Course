from threading import Thread
from TrafficLightSimulator import TraficLightSimulator


tl = TraficLightSimulator(2)
tr = Thread(target=tl.run)
tr.start()

for i in range(0, 10):
    tl.wait_for_change()
tl.cancel()
