from TickTack_th import TickTackThread
from TickTack import TickTack

tt = TickTack()
flow1 = TickTackThread("tick", tt)
flow2 = TickTackThread("tack", tt)

try:
    flow1.join()
    flow2.join()
except KeyboardInterrupt:
    print("Прерывание основного потока")
