# 1.Сгенерируйте псевдослучайные числа, для алгоритма линейной регрессии.
# Представьте полученные данные графически.
# По примеру приведенного ниже кода:
# - Создайте и обучите модель на полученных случайных данных. Выведите на экран матрицу признаков и вектор целей обучающего и тестового наборов. Представьте данные графически.
# - Сформируйте прогноз.
# Определите правильность и обобщающую способность модели.
# Определите оптимальные значения параметров модели


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

features, target, coefficients = make_regression(n_samples=100,
                                                 n_features=3,
                                                 n_informative=3,
                                                 n_targets=1,
                                                 noise=0.0,
                                                 coef=True,
                                                 random_state=1)

print("Матрица признаков (первые 3 строки):\n", np.round(features[:3], 2))
print("Вектор целей (первые 3 значения):\n", np.round(target[:3], 2))

plt.figure(figsize=(15, 5))
for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.scatter(features[:, i], target, alpha=0.7)
    plt.xlabel(f'Признак {i+1}')
    plt.ylabel('Целевая переменная')
    plt.title(f'Распределение данных (Признак {i+1})')
plt.tight_layout()
plt.show()


X_train, X_test, y_train, y_test = train_test_split(features, target,random_state=0)

reg = KNeighborsRegressor(n_neighbors=3)
reg.fit(X_train, y_train)

print("\nОбучающий набор")
print("Матрица признаков (первые 3 строки):\n", np.round(X_train[:3], 2))
print("Вектор целей (первые 3 значения):", np.round(y_train[:3], 2))

print("\nТестовый набор")
print("Матрица признаков (первые 3 строки):\n", np.round(X_test[:3], 2))
print("Вектор целей (первые 3 значения):", np.round(y_test[:3], 2))

y_pred = reg.predict(X_test)
print("\nПрогнозы для тестового набора (первые 5 значений):\n", np.round(y_pred[:5], 2))

print("\nR² на обучающем наборе:", round(reg.score(X_train, y_train), 2))
print("R² на тестовом наборе:", round(reg.score(X_test, y_test), 2))

test_scores = []
train_scores = []
neighbors = range(1, 15)

for n in neighbors:
    model = KNeighborsRegressor(n_neighbors=n)
    model.fit(X_train, y_train)
    test_scores.append(model.score(X_test, y_test))
    train_scores.append(model.score(X_train, y_train))

n = neighbors[np.argmax(test_scores)]
print(f"\nОптимальное n_neighbors: {n} (R² тест: {max(test_scores):.2f})")


plt.figure(figsize=(10, 6))
plt.plot(neighbors, train_scores, label="Обучающая выборка")
plt.plot(neighbors, test_scores, label="Тестовая выборка")
plt.axvline(n, color='red', linestyle='--')
plt.xlabel("Количество соседей")
plt.ylabel("R² оценка")
plt.title("Зависимость качества от количества соседей")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([min(y_test), max(y_test)],[min(y_test), max(y_test)],color='red',linestyle='--')
plt.xlabel('Истинные значения')
plt.ylabel('Предсказания')
plt.title('Сравнение истинных и предсказанных значений')
plt.grid(True)
plt.show()


# Графики распределения показывают нелинейные зависимости
# Оптимальное количество соседей найдено = 6
# R² показывает:
# 0.85 на обучающих данных
# 0.71 на тестовых данных
# График сравнения прогнозов показывает хорошее, но не идеальное соответствие
