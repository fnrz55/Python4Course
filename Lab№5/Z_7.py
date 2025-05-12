# 7.Сравните результаты работы модели на обучающей и на тестовой выборке.
# ---Проанализируйте как изменяется правильность и обобщающая способность модели
# в процессе увеличения количества соседей и изменения параметра random_state.
# Найдите оптимальное значение параметра и соседей.

import mglearn.datasets
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

X,y = mglearn.datasets.make_wave(n_samples=40)

# разбиваем набор данных wave на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# создаем экземпляр модели и устанавливаем количество соседей = 3
reg = KNeighborsRegressor(n_neighbors=3)

# подгоняем модель с использованием обучающих данных и обучающих ответов
reg.fit(X_train, y_train)
print('Прогнозы для тестового набора:\n{}'.format(reg.predict(X_test)))
print('R^2 на тестовом наборе: {:.2f}'.format(reg.score(X_test, y_test)))
print('R^2 на обучающем наборе: {:.2f}'.format(reg.score(X_train, y_train)))

fig, axes = plt.subplots(1,3, figsize=(15,7))

# создаем 1000 точек данных, равномерно распределенных между -3 и 3
line = np.linspace(-3,3,1000).reshape(-1,1)
for n_neighbors, ax in zip([1,3,7], axes):
    # получаем прогнозы, используя 1, 3 и 9 соседей
    reg = KNeighborsRegressor(n_neighbors=n_neighbors)
    reg.fit(X_train, y_train)
    ax.plot(line, reg.predict(line))
    ax.plot(X_train, y_train, '^', c=mglearn.cm2(0), markersize=8)
    ax.plot(X_test, y_test, 'v', c=mglearn.cm2(1), markersize=8)

    ax.set_title('{} neighbor(s)\ntrain score: {:.2f} test score: {:.2f}'.format(n_neighbors,
                                                                                 reg.score(X_train, y_train),
                                                                                 reg.score(X_test, y_test)))
    ax.set_xlabel('Признак')
    ax.set_ylabel('Целевая переменная')
    axes[0].legend(['Прогнозы модели', 'Обучающие данные/ответы', 'Тестовые данные/ответы'], loc='best')

plt.show()