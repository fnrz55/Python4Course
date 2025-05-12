# 3.Реализуйте алгоритм k-ближайших соседей на представленных выше наборах данных.
# Результаты представьте графически.
# ---Проведите сравнение правильности на обучающем и на тестовом наборах.
# Как изменяться показатели правильности и обобщающая способность модели при изменении параметра random_state и количества соседей.
# Определите оптимальную величину этих параметров.

import matplotlib.pyplot as plt
import mglearn.datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

mglearn.plots.plot_knn_classification(n_neighbors=1)
plt.title("knn с 1 соседом")
plt.show()

X,y = mglearn.datasets.make_forge()
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=0)

clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)
print('\nПрогнозы на тестовом наборе: {}'.format(clf.predict(X_test)))
print('\nПравильность на тестовом наборе: {:.2f}'.format(clf.score(X_test, y_test)))

# График для n_neighbors=1 показывает зубчатую границу решения - модель переобучается, реагируя на шумы
# При n_neighbors=3 точность на тестовых данных составит 0.86. Значение меняется на 1 при изменении random_state


for i in range(100):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=i)
    clf = KNeighborsClassifier(n_neighbors=3).fit(X_train, y_train)
    print('random_state={}: test score={:.2f}'.format(i, clf.score(X_test, y_test)))

# Влияет только на разбиение данных не на сам алгоритм knn.
# Изменение random_state может немного менять точность из-за вариативности выборок.

# Поиск наилучшего количества соседей с использованием кроссвалидации
neighbors = range(1, 20)
best_k = 0
best_score = 0
for k in neighbors:
    scores = cross_val_score(KNeighborsClassifier(n_neighbors=k), X, y, cv=5)
    if scores.mean() > best_score:
        best_score = scores.mean()
        best_k = k
print('Лучшее k: {}, точность: {:.2f}'.format(best_k, best_score))


# Визуализация точности выборок в зависимости от количества соседей
plt.figure(figsize=(10, 6))
train = []
test = []
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=643)
for k in neighbors:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train, y_train)
    train.append(clf.score(X_train, y_train))
    test.append(clf.score(X_test, y_test))

plt.plot(neighbors, train, label='Обучающая выборка')
plt.plot(neighbors, test, label='Тестовая выборка')
plt.xlabel('Количество соседей (k)')
plt.xticks(neighbors)
plt.ylabel('Правильность')
plt.legend()
plt.grid()
plt.show()