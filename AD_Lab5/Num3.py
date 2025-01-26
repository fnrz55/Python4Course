import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

# Линейная функция
x = np.linspace(-10, 10, 1000)
k_init, b_init = 1, 0
y1 = k_init * x + b_init

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.3)

line, = ax.plot(x, y1, label=f'$y = {k_init} * x + {b_init}$')
ax.legend(loc="upper right")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("График линейной функции")
ax.set_xlim(-10, 10)
ax.set_ylim(-20, 20)

# Поля ввода для линейной функции
axbox_k = plt.axes([0.15, 0.15, 0.2, 0.05])
axbox_b = plt.axes([0.65, 0.15, 0.2, 0.05])

text_box_k = TextBox(axbox_k, "k", initial=str(k_init))
text_box_b = TextBox(axbox_b, "b", initial=str(b_init))


def update(val):
    try:
        k = float(text_box_k.text)
        b = float(text_box_b.text)

        y1 = k * x + b
        line.set_ydata(y1)

        line.set_label(f'$y = {k:.2f} * x + {b:.2f}$')
        ax.legend(loc="upper right")
        fig.canvas.draw_idle()
    except ValueError:
        pass


text_box_k.on_submit(update)
text_box_b.on_submit(update)

# Второй график: квадратный корень
x_sqrt = np.linspace(0, 10, 1000)
y2 = np.sqrt(x_sqrt)

fig1, ax1 = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.3)
line1, = ax1.plot(x_sqrt, y2, label=f'y = √x')
ax1.legend(loc="upper right")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_title("График квадратного корня из x")
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 4)

# Поле ввода для x
axbox_x2 = plt.axes([0.4, 0.15, 0.2, 0.05])
text_box_x2 = TextBox(axbox_x2, "x", initial="1")


def update_sqrt(val):
    try:
        x1 = float(text_box_x2.text)
        if x1 < 0:
            raise ValueError("x должен быть >= 0")

        y2 = np.sqrt(x_sqrt + x1)
        line1.set_ydata(y2)

        line1.set_label(f'y = √{x1}')
        ax1.legend(loc="upper right")
        fig1.canvas.draw_idle()
    except ValueError:
        pass


text_box_x2.on_submit(update_sqrt)

#Третий график
x_power = np.linspace(-10, 10, 1000)
n_init = 2
y3 = x_power**n_init

fig2, ax2 = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.3)
line2, = ax2.plot(x_power, y3, label=f'$y = x^{n_init}$')
ax2.legend(loc="upper right")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_title(r"График $y = x^n$")
ax2.set_xlim(-10, 10)
ax2.set_ylim(-100, 100)


axbox_n = plt.axes([0.4, 0.15, 0.2, 0.05])
text_box_n = TextBox(axbox_n, "n", initial=str(n_init))

def update_power(val):
    try:
        n = int(text_box_n.text)

        y3 = x_power**n
        line2.set_ydata(y3)

        line2.set_label(f'$y = x^{n}$')
        ax2.legend(loc="upper right")
        fig2.canvas.draw_idle()
    except ValueError:
        pass

text_box_n.on_submit(update_power)



plt.show()