# 1. Загрузка данных и вывод на экран структуры данных.
# 2. Определите и опишите, какие данные и какие структуры содержаться в датасете (по ключу).
# 3. Задайте обучающие данные, обучающие метки, тестовые данные, тестовые метки с помощью функции train_test_split.
# 4. Выведите получившиеся обучающие и тестовые наборы данных, а также количество элементов в каждом наборе.
# 5. Визуализируйте данные с помощью диаграммы рассеяния.
# 6. Построение модели (k-ближайших соседей).
# 7. Получение прогноза.
# 8. Оценка качества модели
# 9. Определите возможно ли решение задачи классификации с использованием исходных данных из файлов: Mall_Customers.csv, winequality-red

import pandas as pd
from pandas.plotting import scatter_matrix
import mglearn
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error

mall_customers_dataset = pd.read_csv('mall_customers.csv')
mall_customers_dataset['gender'] = mall_customers_dataset['gender'].map({'Male': 0, 'Female': 1})


X = mall_customers_dataset[['age','annual_income', 'spending_score']]
y = mall_customers_dataset['gender']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=32)

print("\nОбучающий набор признаков (X_train):\n", X_train.head(10))
print("\nМетки обучающего набора (y_train):\n", y_train.head(10))
print("\nКоличество элементов в обучающем наборе:", X_train.shape[0])
print("\nКоличество меток в обучающем наборе:", y_train.shape[0])

print("\nТестовый набор признаков (X_test):\n", X_test.head(10))
print("\nМетки тестового набора (y_test):\n", y_test.head(10))
print("\nКоличество элементов в тестовом наборе:", X_test.shape[0])
print("\nКоличество меток в тестовом наборе:", y_test.shape[0])

customer_features = ['age','annual_income', 'spending_score']

mall_customers_dataframe = pd.DataFrame(X_train, columns=customer_features)

grr = scatter_matrix(mall_customers_dataframe, c=y_train, figsize=(15, 15),
               marker='o', hist_kwds={'bins': 20}, s=60, alpha=0.8,
               cmap=mglearn.cm3)
plt.show()

knn = KNeighborsClassifier(n_neighbors=5) #При 5 0,56 при 12 0,58
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

y_pred_str = pd.DataFrame({'gender': y_pred})
y_pred_str['gender'] = y_pred_str['gender'].map({0: 'Male', 1: 'Female'})

print('Прогнозы для тестового набора:\n{}'.format(y_pred_str))

mse = mean_squared_error(y_test, y_pred)
print('Среднеквадратическая ошибка: {:.2f}'.format(mse))

r2 = knn.score(X_test, y_test)
print('Коэффициент детерминации: {:.2f}'.format(r2))



###############################################

# 1. Загрузка данных и вывод на экран структуры данных.
# 2. Определите и опишите, какие данные и какие структуры содержаться в датасете (по ключу).
# 3. Задайте обучающие данные, обучающие метки, тестовые данные, тестовые метки с помощью функции train_test_split.
# 4. Выведите получившиеся обучающие и тестовые наборы данных, а также количество элементов в каждом наборе.
# 5. Визуализируйте данные с помощью диаграммы рассеяния.
# 6. Построение модели (k-ближайших соседей).
# 7. Получение прогноза.
# 8. Оценка качества модели
# 9. Определите возможно ли решение задачи классификации с использованием исходных данных из файлов: Mall_Customers.csv, winequality-red

import pandas as pd
from pandas.plotting import scatter_matrix
import mglearn
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error

mall_customers_dataset = pd.read_csv('mall_customers.csv')
mall_customers_dataset['gender'] = mall_customers_dataset['gender'].map({'Male': 0, 'Female': 1})

def categorize(score):
    if score < 40:
        return 0
    elif score < 70:
        return 1
    else:
        return 2

mall_customers_dataset['segment'] = mall_customers_dataset['spending_score'].apply(categorize)
X = mall_customers_dataset[['gender','age','spending_score']]
y = mall_customers_dataset['segment']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

print("\nОбучающий набор признаков (X_train):\n", X_train.head(10))
print("\nМетки обучающего набора (y_train):\n", y_train.head(10))
print("\nКоличество элементов в обучающем наборе:", X_train.shape[0])
print("\nКоличество меток в обучающем наборе:", y_train.shape[0])

print("\nТестовый набор признаков (X_test):\n", X_test.head(10))
print("\nМетки тестового набора (y_test):\n", y_test.head(10))
print("\nКоличество элементов в тестовом наборе:", X_test.shape[0])
print("\nКоличество меток в тестовом наборе:", y_test.shape[0])

customer_features = ['gender','age', 'spending_score']

mall_customers_dataframe = pd.DataFrame(X_train, columns=customer_features)

grr = scatter_matrix(mall_customers_dataframe, c=y_train, figsize=(15, 15),
               marker='o', hist_kwds={'bins': 20}, s=60, alpha=0.8,
               cmap=mglearn.cm3)
plt.show()

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print('Прогнозы для тестового набора:\n{}'.format(y_pred))

mse = mean_squared_error(y_test, y_pred)
print('Среднеквадратическая ошибка: {:.2f}'.format(mse))

r2 = knn.score(X_test, y_test)
print('Коэффициент детерминации: {:.2f}'.format(r2))
plt.plot(range(y_test.size),y_test,  label='Тестовые значения', color='blue',linestyle='-')
plt.plot( range(y_pred.size), y_pred, label='Предсказаные значения', color='red',linestyle='--')

plt.xticks(range(y_test.size))
plt.legend()
plt.show()

print('Правильность на обучающем наборе = ', knn.score(X_train, y_train))
print('Правильность на тестовом наборе = ',knn.score(X_test, y_test))