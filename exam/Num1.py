import numpy as np
import matplotlib.pyplot as plt


def debt_per_person(vals1, vals2):
    debts = []

    for i in range(len(vals1)):
        try:
            debt = vals1[i] / vals2[i] * 1e6
        except ZeroDivisionError:
            debt = 0

        debts.append(debt)
    return debts

def sum_total(values):
    sum = 0
    for val in values:
        sum += val

    return sum

def percents_of_total(val, total_val):
    one_percent = total_val / 100
    percent = val / one_percent
    return percent



categories =  [
    {'name':"Сельское хозяйство", 'info':{"Всего": 44.7, "Бюджет": 0, "Собственные": 44.7, "Численность": 0.9}},
    {'name':"Рыбоводство", 'info':{"Всего": 2.7, "Бюджет": 0, "Собственные": 2.7, "Численность": 0.0}},
    {'name':"Добыча ископаемых", 'info': {"Всего": 25.0, "Бюджет": 0, "Собственные": 25.0, "Численность": 0.4}},
    {'name':"Обрабатывающие производства", 'info': {"Всего": 353.5, "Бюджет": 0, "Собственные": 353.5, "Численность": 4.2}},
    {'name':"Обеспечение электроэнергией", 'info': {"Всего": 7.7, "Бюджет": 0, "Собственные": 7.7, "Численность": 0.3}},
    {'name':"Водоснабжение", 'info':{"Всего": 25.7, "Бюджет": 0, "Собственные": 25.7, "Численность": 0.4}},
    {'name':"Строительство", 'info':{"Всего": 94.2, "Бюджет": 0, "Собственные": 94.2, "Численность": 1.1}},
    {'name':"Транспорт", 'info':{"Всего": 63.9, "Бюджет": 0, "Собственные": 63.9, "Численность": 0.4}},
    {'name':"Управление недвижимым имещуством", 'info':{"Всего": 10.9, "Бюджет": 0, "Собственные": 10.9, "Численность": 0.1}},
    {'name':"Научные исследования", 'info':{"Всего": 0.5, "Бюджет": 0, "Собственные": 0.5, "Численность": 0.0}},
    {'name':"Образование", 'info':{"Всего": 13.4, "Бюджет": 10.2, "Собственные": 3.2, "Численность": 0.5}},
    {'name':"Здравоохранение", 'info':{"Всего": 0.5, "Бюджет": 0, "Собственные": 0.5, "Численность": 0.0}},
    {'name':"Культура и телевещание", 'info':{"Всего": 0, "Бюджет": 0, "Собственные": 0, "Численность": 0}}
]

names, totals, budgets, owns, numbers_of_employees = [], [], [], [], []

for category in categories:
    name = category['name']
    info = category['info']
    total = info['Всего']
    budget = info['Бюджет']
    own = info['Собственные']
    number_of_employees = info['Численность'] * 1e3

    names.append(name)
    totals.append(total)
    budgets.append(budget)
    owns.append(own)
    numbers_of_employees.append(number_of_employees)


title = 'Просроченная задолженность по заработной плате\n работникам организаций по видам экономической деятельности в 2022г.'
bars = plt.bar(names, totals, color='red')
plt.bar_label(bars)
plt.title(title, fontsize=16)
plt.xlabel("Вид экономической деятельности", fontsize=12)
plt.ylabel("Задолженность, млн руб.", fontsize=10)
plt.xticks(rotation=75, fontsize=10)
plt.tight_layout()
plt.show()

total = sum_total(totals)

percents = []
for val in totals:
    percent = percents_of_total(val, total)
    percents.append(percent)

title = 'Доля задолженности по видам экономической деятельности\n к общей задолженности в 2022г.'
plt.pie(percents, autopct='%.2f')
plt.title(title)
plt.legend(names)
plt.show()

debt_to_employees = debt_per_person(totals, numbers_of_employees)

title = 'Задолженность организаций на 1 сотрудника \nв среднем по видам экономической деятельности'
bars = plt.bar(names, debt_to_employees, color='blue')
plt.bar_label(bars)
plt.title(title, fontsize=16)
plt.xlabel("Вид экономической деятельности", fontsize=12)
plt.ylabel("Задолженность, руб.", fontsize=10)
plt.xticks(rotation=75, fontsize=10)
plt.tight_layout()
plt.show()

max_total = max(totals)
max_debt = max(debt_to_employees)
max_budget = max(budgets)
min_total = min(totals)

print('Выводы:\n')
print(f'Всего за 2022г. просрочная задолженность по заработной плате составила {total*1e6} руб.')
print(f'Самая большая просрочная задолженность по заработной плате составила {max_total * 1e6} руб.')
print(f'Самая маленькая просрочная задолженность по заработной плате составила {min_total * 1e6} руб.')
print(f'Самая большая просрочная задолженность  по заработной плате  из за несвоевременного получения средств из бюджета составила {max_budget * 1e6} руб.')
print(f'Самая большая средняя задолженность на 1 человека по заработной плате составила {max_debt} руб.')

