import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y=x**3
fig, ax = plt.subplots(1, 3)

ax[0].set_title('Логарфмическая шкала только для оси х')
ax[0].plot(x, y)
ax[0].set_xscale('log')
ax[0].set_xlabel('x(log)')
ax[0].set_ylabel('y')

ax[1].set_title('Логарифмическая шкала только для оси у')
ax[1].plot(x, y)
ax[1].set_yscale('log')
ax[1].set_xlabel('x')
ax[1].set_ylabel('y(log)')

ax[2].set_title('Логарифмическая шкала для осей х и у')
ax[2].plot(x, y)
ax[2].set_xscale('log')
ax[2].set_yscale('log')
ax[2].set_xlabel('x(log)')
ax[2].set_ylabel('y(log)')
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(1, 3)

ax[0].set_title('Логарфмическая шкала только для оси х')
ax[0].plot(x, y)
ax[0].set_xscale('symlog')
ax[0].set_xlabel('x(log)')
ax[0].set_ylabel('y')

ax[1].set_title('Логарифмическая шкала только для оси у')
ax[1].plot(x, y)
ax[1].set_yscale('symlog')
ax[1].set_xlabel('x')
ax[1].set_ylabel('y(log)')

ax[2].set_title('Логарифмическая шкала для осей х и у')
ax[2].plot(x, y)
ax[2].set_xscale('symlog')
ax[2].set_yscale('symlog')
ax[2].set_xlabel('x(log)')
ax[2].set_ylabel('y(log)')
plt.tight_layout()
plt.show()
