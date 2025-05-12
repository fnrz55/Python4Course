# 4.Реализуйте графическую интерпретацию алгоритма k-ближайших соседей в двумерном виде,
# через формирование границы принятия решений.

import matplotlib.pyplot as plt
import mglearn.datasets
from sklearn.neighbors import KNeighborsClassifier

X, y = mglearn.datasets.make_forge()

fig, axes = plt.subplots(1, 3, figsize=(10,3))

for n_neighbors, ax in zip([1,3,9], axes):
    # создаем объект-классификатор и подгоняем в одной строке
    clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X,y)
    mglearn.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax=ax, alpha=.4)
    mglearn.discrete_scatter(X[:,0], X[:,1], y, ax=ax)
    ax.set_title('количество соседей: {}'.format(n_neighbors))
    ax.set_xlabel('признак 0')
    ax.set_ylabel('признак 1')
axes[0].legend(loc=3)
plt.show()