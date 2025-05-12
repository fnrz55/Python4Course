# 5.Реализуйте код. () Определите оптимальные значения параметра random_state и количества соседей.
# ---Как измениться правильность и обобщающая способность модели при изменении количества соседей?

import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data,
                                                    cancer.target,
                                                    stratify=cancer.target,
                                                    random_state=66)

training_accuracy = []
test_accuracy = []
# пробуем n_neighbors от 1 до 10
neighbors_settings = range(1,11)

for n_neighbors in neighbors_settings:
    # строим модель
    clf = KNeighborsClassifier(n_neighbors=n_neighbors)
    clf.fit(X_train, y_train)

    # записываем правильность на обучающем наборе
    training_accuracy.append(clf.score(X_train, y_train))
    # записываем правильность на тестовом наборе
    test_accuracy.append(clf.score(X_test, y_test))

plt.plot(neighbors_settings, training_accuracy, label='правильность на обучающем наборе')
plt.plot(neighbors_settings, test_accuracy, label='правильность на тестовом наборе')
plt.ylabel('Правильность')
plt.xlabel('количество соседей')
plt.legend()
plt.show()

# При k=1:
# Обучающая точность = 1.0 модель подстраивается под данные
# Тестовая точность = 0.91
# При k=6:
# Максимальная тестовая точность = 0.94
# При k>6:
# Точность падает. Модель становится слишком простой
# Влияние random_state: Параметр влияет только на разбиение данных.
# При изменении возможны колебания точности
# Выводы
# Обобщающая способность максимальна при k=6.
# k<3 — переобучение
# k>8 — недообучение