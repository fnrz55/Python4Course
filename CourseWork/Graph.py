import csv
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def compare_codes(code):
    codes = {
        '1': '05',
        '2': '07',
        '3': '06',
        '4': '03',
        '5': '10',
    }
    return codes[code]

filename = "Попов.csv.csv"
filename_ru = "Данные_по_РФ.csv"
means = {}
means_values = {}
means_ru = {}
means_ru_compared = {}
means_values_ru = {}
means_values_ru_compared = {}
codes = []

with open(filename, encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        code, mean, count = row
        count = int(count)
        try:
            int(code)
        except ValueError:
            continue
        codes.append(code)

        if code not in means:
            means[code] = {}
        means[code][mean] = count

        if code not in means_values:
            means_values[code] = 0
        means_values[code] = count


for code in codes:
    means_values_ru_compared[code] = 0

for key, val in means.items():
    print(f'{key}:{val}')

with open(filename_ru,encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        code, mean, count = row[0].split(';')
        # print(row[0].split(';'))
        count = int(count)
        code = compare_codes(code)

        if code not in means_ru:
            means_ru[code] = {}
        means_ru[code][mean] = count

        if code not in means_values_ru:
            means_values_ru[code] = 0
        means_values_ru[code] = count


for key, value in means_values_ru.items():
    means_values_ru_compared[key] = value

print(codes)

print("Словарь способов:")
print(means)

print("\nКоличество учащихся по способам передвижения к учебным заведениям:")
print(means_values)

print("\nДанные по способам передвижения в РФ:")
print(means_ru)

categories_ru = list(means_values_ru_compared.keys())
totals_ru = list(means_values_ru_compared.values())

categories = list(means_values.keys())
totals = [value for value in means_values.values()]

plt.figure(figsize=(10, 6))
str1 = plt.plot(categories, totals, color='blue', marker='o', label='Общее количество учащихся')
plt.title("Распределение способов передвижения учащихся к учебным заведениям")
plt.xlabel("Код способа передвижения")
plt.ylabel("Количество учащихся, чел.")
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
    plt.scatter(category, totals[i], color='green' if markers[i] == '^' and sizes[i] == 100 else colors[i], marker=markers[i], s=sizes[i], label='_nolegend_')

plt.scatter([], [], color='black', marker='^', s=150, label=f'Максимальное значение {max_value:.1f}')
plt.scatter([], [], color='black', marker='v', s=150, label=f'Минимальное значение {min_value:.1f}')
plt.plot(categories, totals, color='blue')
plt.title("Динамика способов передвижения учащихся к учебным заведениям")
plt.xlabel("Код способа передвижения")
plt.ylabel("Количество учащихся, чел.")
plt.grid(linewidth=0.3)
plt.legend()
plt.show()

fig, axs = plt.subplots(1, 2, figsize=(15, 6))
axs[0].plot(categories, totals, color='red', marker='o')
axs[0].set_title("Количество учащихся в первом регионе")
axs[0].set_xlabel("Код способа передвижения")
axs[0].set_ylabel("Количество учащихся, чел.")
axs[0].grid(linewidth=0.3)
axs[1].plot(categories_ru, totals_ru, color='blue', marker='o')
axs[1].set_title("Количество учащихся в Российской Федерации")
axs[1].set_xlabel("Код способа передвижения")
axs[1].set_ylabel("Количество учащихся, чел.")
axs[1].grid(linewidth=0.3)

fig.suptitle("Сравнение количества учащихся по способам передвижения")
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(categories_ru, totals_ru, color='blue', marker='o', label='Общее количество учащихся в РФ')
plt.plot(categories, totals, color='red', marker='o', label='Общее количество учащихся в первом регионе')
plt.title("Общее количество учащихся по способам передвижения в Российской Федерации")
plt.xlabel("Код способа передвижения")
plt.ylabel("Количество учащихся, чел.")
plt.grid(linewidth=0.3)
plt.legend()
plt.show()


fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
x = np.arange(len(categories))
z = np.zeros(len(categories))
dz = totals
ax.bar3d(x, z, z, 1, 1, dz, color='blue', edgecolor='red')
ax.set_title("Общее количество учащихся по способам передвижения в первом регионе")
ax.set_xlabel("Код способа передвижения")
ax.set_zlabel("Количество учащихся, чел.")
ax.set_xticks(range(len(categories)))
ax.set_xticklabels(categories)
plt.show()

