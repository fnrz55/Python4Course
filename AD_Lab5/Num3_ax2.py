import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

x = np.linspace(-10, 10, 1000)
a_init, b_init, c_init = 1, 0, 0
y = a_init * x ** 2 + b_init * x + c_init

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.3)
line, = ax.plot(x, y, label=f'$y = {a_init}x^2 + {b_init}x + {c_init}$')
ax.legend(loc="upper right")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("График квадратичной функции")
ax.set_xlim(-10, 10)
ax.set_ylim(-100, 100)

axbox_a = plt.axes([0.15, 0.15, 0.2, 0.05])
axbox_b = plt.axes([0.4, 0.15, 0.2, 0.05])
axbox_c = plt.axes([0.65, 0.15, 0.2, 0.05])

text_box_a = TextBox(axbox_a, "a", initial=str(a_init))
text_box_b = TextBox(axbox_b, "b", initial=str(b_init))
text_box_c = TextBox(axbox_c, "c", initial=str(c_init))

def update(val):
    try:
        a = float(text_box_a.text)
        b = float(text_box_b.text)
        c = float(text_box_c.text)

        y = a * x ** 2 + b * x + c
        line.set_ydata(y)

        line.set_label(f'$y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}$')
        ax.legend(loc="upper right")
        fig.canvas.draw_idle()
    except ValueError:
        pass

text_box_a.on_submit(update)
text_box_b.on_submit(update)
text_box_c.on_submit(update)


x_abs = np.linspace(-10, 10, 1000)
y2 = np.abs(x_abs)

fig1, ax1 = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.3)
line1, = ax1.plot(x_abs, y2, label='$y = |x|$')
ax1.legend(loc="upper right")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_title("График модуля x")
ax1.set_xlim(-10, 10)
ax1.set_ylim(-3, 10)


axbox_n = plt.axes([0.4, 0.1, 0.2, 0.05])
text_box_n = TextBox(axbox_n, "n", initial="0")

def update_abs(val):
    try:
        n = float(text_box_n.text)
        y2 = np.abs(x_abs + n)
        line1.set_ydata(y2)

        line1.set_label(f'$y = |x + {n:.2f}|$')
        ax1.legend(loc="upper right")
        fig1.canvas.draw_idle()
    except ValueError:
        pass

text_box_n.on_submit(update_abs)

plt.show()