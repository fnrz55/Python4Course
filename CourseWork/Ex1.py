import csv
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

filename = "Тюрморезов.csv"
filename_ru = "Данные РФ ноябрь24г.csv"
industries = {}
industries_values = {}
industries_ru = {}

with open(filename, encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        code, industry, count = row
        count = int(count)
        category = code[0]

        if category not in industries:
            industries[category] = {}
        industries[category][industry] = count

        if category not in industries_values:
            industries_values[category] = 0
        industries_values[category] += count

with open(filename_ru, encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    header = next(reader)
    for row in reader:
        industry = row[0].strip()
        count = row[1].replace(" ", "").strip()
        count = int(count) if count.isdigit() else 0

        if industry not in industries_ru:
            industries_ru[industry] = 0
        industries_ru[industry] += count

print("Словарь отраслей:")
print(industries)

print("\nКоличество работников по видам экономической деятельности:")
print(industries_values)

print("\nДанные по численности работников в РФ:")
print(industries_ru)

categories_ru = list(industries.keys())
totals_ru = list(industries_ru.values())

categories = list(industries_values.keys())
totals = [value / 1000 for value in industries_values.values()]



plt.figure(figsize=(10, 6))
str1 = plt.plot(categories, totals, color='blue', marker='o', label='Общее количество работников')
plt.title("Общее количество работников старше 15 лет по видам экономической деятельности в первом регионе")
plt.xlabel("Раздел вида экономической деятельности")
plt.ylabel("Количество работников, тыс.")
plt.grid(linewidth=0.3)
plt.legend()
plt.show()


plt.figure(figsize=(10, 6))
markers = []
sizes = []
colors = []
max_value = max(totals)
min_value = min(totals)
max_index = totals.index(max_value)
min_index = totals.index(min_value)

for i in range(len(totals)):
    if i == 0:
        markers.append('o')
        sizes.append(100)
        colors.append('red')
    else:
        if totals[i] > totals[i - 1]:
            markers.append('^')
        else:
            markers.append('v')

        if i == max_index or i == min_index:
            sizes.append(150)
            colors.append('black')
        else:
            sizes.append(100)
            colors.append('red')


for i, category in enumerate(categories):
    plt.scatter(category, totals[i], color=colors[i], marker=markers[i], s=sizes[i], label='_nolegend_')

plt.scatter([], [], color='black', marker='^', s=150, label=f'Максимальное значение {max_value:.1f}')
plt.scatter([], [], color='black', marker='v', s=150, label=f'Минимальное значение {min_value:.1f}')
plt.plot(categories, totals, color='blue')
plt.title("График динамики изменения показателей численности работников по видам экономической деятельности")
plt.xlabel("Раздел вида экономической деятельности")
plt.ylabel("Количество работников, тыс.")
plt.grid(linewidth=0.3)
plt.legend()
plt.show()

fig, axs = plt.subplots(1, 2, figsize=(15, 6))
axs[0].plot(categories, totals, color='red', marker='o')
axs[0].set_title("Общее количество работников в первом регионе")
axs[0].set_xlabel("Раздел вида экономической деятельности")
axs[0].set_ylabel("Количество работников, тыс.")
axs[0].grid(linewidth=0.3)
axs[1].plot(categories_ru, totals_ru, color='blue', marker='o')
axs[1].set_title("Общее количество работников в Росси")
axs[1].set_xlabel("Раздел вида экономической деятельности")
axs[1].set_ylabel("Количество работников, тыс.")
axs[1].grid(linewidth=0.3)

fig.suptitle("Сравнение численности работников по категориям отраслей")
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(categories_ru, totals_ru, color='blue', marker='o', label='Общее количество работников в РФ')
plt.plot(categories, totals, color='red', marker='o', label='Общее количество работников в первом регионе')
plt.title("Общее количество работников старше 15 лет по категориям отраслей в Российской Федерации")
plt.xlabel("Раздел вида экономической деятельности")
plt.ylabel("Количество работников, тыс.")
plt.grid(linewidth=0.3)
plt.legend()
plt.show()


fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
x = np.arange(len(categories))
z = np.zeros(len(categories))
dz = totals
ax.bar3d(x, z, z, 1, 1, dz, color='skyblue', edgecolor='black')
ax.set_title("Общее количество работников по категориям отраслей в первом регионе")
ax.set_xlabel("Раздел вида экономической деятельности")
ax.set_zlabel("Количество работников, тыс.")
ax.set_xticks(range(len(categories)))
ax.set_xticklabels(categories)
plt.show()