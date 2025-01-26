import numpy as np
import matplotlib.pyplot as plt

Km = 0.04  # М
Vmax = 0.1  # М/с

S = np.linspace(0, 1, 100)  # М

v = Vmax * S / (Km + S)

plt.plot(S, v)
plt.xlabel('Концентрация субстрата [S], М')
plt.ylabel('Скорость реакции v, М/с')
plt.title('Зависимость скорости реакции от концентрации субстрата по уравнению Михаэлиса-Ментен')
plt.grid(True)
plt.show()