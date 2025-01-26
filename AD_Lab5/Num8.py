import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, sigma):
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-x**2 / (2 * sigma**2))

x = np.linspace(-5, 5, 1000)

sigmas = [1, 1.5, 2]

plt.figure(figsize=(10, 6))

for sigma in sigmas:
    y = gaussian(x, sigma)
    plt.plot(x, y, label=f"σ = {sigma}")

plt.xlabel('x')
plt.ylabel('g(x)')
plt.title('Нормализованная гауссова функция для различных значений σ')
plt.legend()
plt.grid(True)
plt.show()