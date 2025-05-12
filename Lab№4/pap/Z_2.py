# 1. Загрузка данных и вывод на экран структуры данных.
# 2. Определите и опишите, какие данные и какие структуры содержаться в датасете(по ключу).
# 3. Задайте обучающие данные, обучающие метки, тестовые данные, тестовые метки с помощью функции train_test_split.
# 4. Выведите получившиеся обучающие и тестовые наборы данных, а также количество элементов в каждом наборе.
# 5. Визуализируйте данные с помощью диаграммы рассеяния.
# 6. Построение модели (k-ближайших соседей).
# 7. Получение прогноза.
# 8. Оценка качества модели.
import numpy as np
import pandas as pd
import mglearn
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

url = 'mall_customers.csv'

customers_dataset = pd.read_csv(url)

print("Ключи customers_dataset: \n {}".format(customers_dataset.keys()))

# 'customer_id' - 'идентификатор клиента'
# 'gender' - 'пол'
# 'age' - 'возраст'
# 'annual_income' - 'годовой доход'
# 'spending_score' - 'расходы'
# dtype='object' - 'объект'


x_train, x_test, y_train, y_test = train_test_split(
    customers_dataset['data'], customers_dataset['target'], random_state=0
)
print('Обучающие данные  - x_train \n{}'.format(x_train))
print('Количество элементов: {}'.format(x_train.shape))
print('Обучающие метки - x_test \n{}'.format(x_test))
print('Количество элементов: {}'.format(x_test.shape))
print('Тестовые данные - y_train \n{}'.format(y_train))
print('Количество элементов: {}'.format(y_train.shape))
print('Тестовые метки - y_test \n{}'.format(y_test))
print('Количество элементов: {}'.format(y_test.shape))

# Создаём dataframe из данных в масиве x_train
# Маркируем столбцы, используя строки в iris_dataset.feature_names
customers_dataframe = pd.DataFrame(x_train, columns=customers_dataset.feature_names)
# Создаём матрицу рассеяния из dataframe, цвет точек задаём с помощью y_train
grr = pd.plotting.scatter_matrix(customers_dataframe,
                        c = y_train,
                        figsize = (15, 15),
                        marker = 'o',
                        hist_kwds = {'bins': 20},
                        s = 60,
                        alpha = .8,
                        cmap = mglearn.cm3)
plt.show()

knn = KNeighborsClassifier(n_neighbors=1)
print('Построение модели (k-ближайших соседей) \n{}'.format(knn.fit(x_train, y_train)))

x_new = np.array([[5, 2.9, 1, 0.2]])
print('Форма массива x_new: \n{}'.format(x_new.shape))
prediction = knn.predict(x_new)
print('Прогноз: \n{}'.format(prediction))
print('Спрогнозированная метка: \n{}'.format(customers_dataset['target_names'][prediction]))

y_pred = knn.predict(x_test)
print('Прогнозы для тестового набора: \n{}'.format(y_pred))

print('Правильность на тестовом наборе: \n{:.2f}'.format(np.mean(y_pred == y_test)))
print('Правильность на тестовом наборе: \n{:.2f}'.format(knn.score(x_test, y_test)))