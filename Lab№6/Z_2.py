# 2. Сгенерируйте псевдослучайные числа, для алгоритма классификации.
# Представьте полученные данные графически.
# По примеру приведенного ниже кода:
# - Создайте и обучите модель на полученных случайных данных. Выведите на экран матрицу признаков и вектор целей обучающего и тестового наборов. Представьте данные графически.
# - Сформируйте прогноз.
# -Определите правильность и обобщающую способность модели.
# Определите оптимальные значения параметров модели.
# Импорт необходимых библиотек
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import mglearn

features, target = make_classification(n_samples=100,
                                       n_features=3,
                                       n_informative=3,
                                       n_redundant=0,
                                       n_classes=2,
                                       weights=[.25,.75],
                                       random_state=1)

print("Исходные данные")
print("Матрица признаков первые 10 строки:\n", np.round(features[:10], 2))
print("Вектор целей первые 3 значения:", target[:10])

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(features[:,0], features[:,1], features[:,2], c=target, cmap='coolwarm')
ax.set_xlabel('Признак 1')
ax.set_ylabel('Признак 2')
ax.set_zlabel('Признак 3')
plt.title('Данные классификации')
plt.legend(*scatter.legend_elements(), title="Классы")
plt.show()

X_train, X_test, y_train, y_test = train_test_split(features, target,test_size=0.25,random_state=0,stratify=target)

clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)

print("\nОбучающий набор")
print("Размер матрицы признаков:", X_train.shape)
print("Примеры признаков первые 10 строки:\n", np.round(X_train[:10], 2))
print("Примеры целей первые 10 значения:", y_train[:10])

print("\nТестовый набор")
print("Размер матрицы признаков:", X_test.shape)
print("Примеры признаков первые 10 строки:\n", np.round(X_test[:10], 2))
print("Примеры целей первые 10 значения:", y_test[:10])

y_pred = clf.predict(X_test)
print("\nПрогнозы для тестового набора первые 10 значений:", y_pred[:10])
print("Фактические значения первые 10:        ", y_test[:10])

print("\nПравильность на обучающем наборе: {:.2f}".format(clf.score(X_train, y_train)))
print("Правильность на тестовом наборе: {:.2f}".format(clf.score(X_test, y_test)))

test_accuracy = []
train_accuracy = []
neighbors_range = range(1, 15)

for n in neighbors_range:
    model = KNeighborsClassifier(n_neighbors=n)
    model.fit(X_train, y_train)
    test_accuracy.append(model.score(X_test, y_test))
    train_accuracy.append(model.score(X_train, y_train))

n = neighbors_range[np.argmax(test_accuracy)]
print(f"\nОптимальное количество соседей: {n} (Точность: {max(test_accuracy):.2f})")

plt.figure(figsize=(10, 5))
plt.plot(neighbors_range, train_accuracy, label="Обучающая выборка")
plt.plot(neighbors_range, test_accuracy, label="Тестовая выборка")
plt.axvline(n, color='red', linestyle='--')
plt.xlabel("Количество соседей")
plt.ylabel("Точность")
plt.title("Зависимость точности от количества соседей")
plt.legend()
plt.grid(True)
plt.show()



feature_par = [(0, 1), (1, 2), (0, 2)]
titles = ['Признаки 1 и 2', 'Признаки 2 и 3', 'Признаки 1 и 3']

plt.figure(figsize=(15, 5))
for i, (f1, f2) in enumerate(feature_par):
    plt.subplot(1, 3, i + 1)
    X_pair = features[:, [f1, f2]]
    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(X_pair, target)

    mglearn.plots.plot_2d_separator(clf, X_pair, fill=True, alpha=0.4)
    mglearn.discrete_scatter(X_pair[:, 0], X_pair[:, 1], target)
    plt.xlabel(f'Признак {f1 + 1}')
    plt.ylabel(f'Признак {f2 + 1}')
    plt.title(titles[i])

plt.tight_layout()
plt.show()

# график показывает хорошую разделимость классов
# Оптимальное количество соседей 7
# Точность 92% на тестовых данных показывает хорошую обобщающую способность
# График разделяющей поверхности демонстрирует нелинейную границу решения
# Небольшая разница между точностью на обучающих и тестовых данных 93% и 92%