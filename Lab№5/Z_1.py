# 1. Опишите состав представленных ниже датасетов.
# Какая структура данных лежит в основе.
# Что представляет собой целевая переменная и признаки.
# Для каких задач они могут использоваться.
# Реализуйте нижеприведенный код.

import matplotlib.pyplot as plt
import mglearn.datasets
import numpy as np
from sklearn.datasets import load_breast_cancer

X, y = mglearn.datasets.make_forge()

mglearn.discrete_scatter(X[:,0], X[:, 1], y)
plt.legend(['Класс 0', 'Класс 1'], loc=4)
plt.xlabel('Первый признак')
plt.ylabel('Второй признак')
print('Форма массива X: {}'.format(X.shape))
plt.show()


# make_forge()
# X - матрица признаков (26, 2), содержит 2 числовых признака - координаты точек
# y - массив меток классов 0 или 1, количество 26
# Для каких задач подходит: Классификация
# Визуализация работы алгоритма knn - демонстрация разделяющих границ

cancer = load_breast_cancer()
print('\nКлючи cancer(): \n{}'.format(cancer.keys()))
print('\nФорма массива data для набора cancer: {}'.format(cancer.data.shape))
print('\nКоличество примеров для каждого класса:\n{}'.format({n for n,v in zip(cancer.target_names, np.bincount(cancer.target))}))
print('\nИмена признаков:\n{}'.format(cancer.feature_names))

# load_breast_cancer()
# data - матрица признаков (569, 30), 30 числовых признаков - характеристики опухолей
# target - массив меток 0 - злокачественная, 1 - доброкачественная, количество 569
# диагностика рака груди
# Для каких задач подходит: Классификация, регрессия
# Отбор признаков - выявление значимых параметров опухоли
