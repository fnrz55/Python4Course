from Lab20.TickTack import TickTack
from Lab20.TickTack_th import TickTackThread

ttob = TickTack()
thrd1 = TickTackThread('tick', ttob)
thrd2 = TickTackThread('tack', ttob)

try:
    thrd1.join()
    thrd2.join()
except InterruptedError:
    print('Прерывание основного потока')