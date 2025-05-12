import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt


wine_dataset = pd.read_csv('winequality-red.csv', sep=';')

print('Ключи wine_dataset:\n{}'.format(wine_dataset.keys()))
keys = list(wine_dataset.keys())
print(keys)

for i in keys:
    try:
        print(f'{i}:\n{wine_dataset[i][:5]}')
    except:
        print(f'{i}:\n{None}')

X = wine_dataset.drop(columns=['quality'])
y = wine_dataset['quality']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=34)

print("\nОбучающий набор признаков (X_train):\n", X_train.head(10))
print("\nМетки обучающего набора (y_train):\n", y_train.head(10))
print("\nКоличество элементов в обучающем наборе:", X_train.shape[0])
print("\nКоличество меток в обучающем наборе:", y_train.shape[0])

print("\nТестовый набор признаков (X_test):\n", X_test.head(10))
print("\nМетки тестового набора (y_test):\n", y_test.head(10))
print("\nКоличество элементов в тестовом наборе:", X_test.shape[0])
print("\nКоличество меток в тестовом наборе:", y_test.shape[0])




wine_features = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol']
wine_dataframe = pd.DataFrame(X_train, columns=wine_dataset.columns[:-1])

scatter_matrix(wine_dataframe[wine_features], c=y_train, figsize=(15, 15),
               marker='o', hist_kwds={'bins': 20}, s=60, alpha=0.8,
               cmap='viridis')
plt.show()

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
print('\nПрогнозы для тестового набора:\n{}'.format(y_pred[:10]))
print('Правильность на тестовом наборе 1 способ: {:.2f}'.format(np.mean(y_pred == y_test)))
print('Правильность на тестовом наборе 2 способ: {:.2f}'.format(knn.score(X_test, y_test)))