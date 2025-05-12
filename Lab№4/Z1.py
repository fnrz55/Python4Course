# 1. Загрузка данных и вывод на экран структуры данных.
# 2. Определите и опишите, какие данные и какие структуры содержаться в датасете (по ключу).
# 3. Задайте обучающие данные, обучающие метки, тестовые данные, тестовые метки с помощью функции train_test_split.
# 4. Выведите получившиеся обучающие и тестовые наборы данных, а также количество элементов в каждом наборе.
# 5. Визуализируйте данные с помощью диаграммы рассеяния.
# 6. Построение модели (k-ближайших соседей).
# 7. Получение прогноза.
# 8. Оценка качества модели
# 9. Определите возможно ли решение задачи классификации с использованием исходных данных из файлов: Mall_Customers.csv, winequality-red
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.plotting import scatter_matrix
import mglearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris_dataset = load_iris()

print('Ключи iris_dataset:\n{}'.format(iris_dataset.keys()))

ik = list(iris_dataset.keys())

print(iris_dataset['data'].size)
print(iris_dataset['target'].size)

print(iris_dataset[ik[1]])
for i in ik:
    try:
        print(f'{i}:\n{iris_dataset[i][:5]}')
    except:
        print(f'{i}:\n Ошибка получения данных')

X = iris_dataset['data']
y = iris_dataset['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Вывод обучающего набора признаков (X_train) и меток (y_train)
print("\nОбучающий набор признаков (X_train):\n", X_train[:10])
print("\nМетки обучающего набора (y_train):\n", y_train[:10])
print("\nКоличество элементов в обучающем наборе:", X_train.shape)
print("\nКоличество меток в обучающем наборе:", y_train.shape)

# Вывод тестового набора признаков (X_test) и меток (y_test)
print("\nТестовый набор признаков (X_test):\n", X_test[:10])
print("\nМетки тестового набора (y_test):\n", y_test[:10])
print("\nКоличество элементов в тестовом наборе:", X_test.shape)
print("\nКоличество меток в тестовом наборе:", y_test.shape)

iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)

grr = scatter_matrix(iris_dataframe, c=y_train, figsize=(15,15),
                        marker='o', hist_kwds={'bins':20}, s=60, alpha=.8,
                        cmap=mglearn.cm3)
plt.show()

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

X_new = np.array([[5,2.9,1,0.2]])
print('ФОРМА МАССИВА x_new: {}'.format(X_new.shape))

prediction = knn.predict(X_new)
print('Прогноз: {}'.format(prediction))
print('Спрогнозированная метка: {}'.format(iris_dataset['target_names'][prediction]))

y_pred = knn.predict(X_test)

print('Прогнозы для тестового набора:\n {}')
for item in y_pred:
    if item == 0:
        print(iris_dataset['target_names'][0])
    elif item == 1:
            print(iris_dataset['target_names'][1])
    elif item == 2:
            print(iris_dataset['target_names'][2])

# 1 способ
print('Правильность на тестовом наборе: {:.2f}'.format(np.mean(y_pred == y_test)))

# 2 способ
print('Правильность на тестовом наборе: {:.2f}'.format(knn.score(X_test, y_test)))