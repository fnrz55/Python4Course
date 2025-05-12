# 6.Представьте графически работу модели изменяя количество соседей от 1 до 9.

import mglearn
import matplotlib.pyplot as plt

for i in range(1, 10):
    mglearn.plots.plot_knn_regression(n_neighbors=i)
    plt.title(f"Соседей = {i}")
    plt.legend(loc=4)
    plt.show()

