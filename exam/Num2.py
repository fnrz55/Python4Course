import matplotlib.pyplot as plt

x = [10,20,30,40,50,60,80,90,100]
y = [1,2,3,4,5,6,3,3,7]

selected_x = 40
selected_y = 4
arrowprops = {
    'arrowstyle': '->',
}
plt.plot(x,y)
plt.scatter(x,y)
plt.annotate('Значение (40;4)',
                 xy=(selected_x, selected_y),
                 xytext=(selected_x - 4, selected_y + 0.5),
                 arrowprops=arrowprops)
plt.show()