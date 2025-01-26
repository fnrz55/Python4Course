import matplotlib.pyplot as plt

years = list(range(2000, 2010))  # Годы от 2000 до 2010
divorce_rate = [5.0, 4.7, 4.6, 4.4, 4.3, 4.1, 4.2, 4.2, 4.2, 4.1]
margarine_consumption = [8.2, 7, 6.5, 5.3, 5.2, 4, 4.6, 4.5, 4.2, 3.7]

if len(years) != len(divorce_rate) or len(years) != len(margarine_consumption):
    raise ValueError("Массивы должны иметь одинаковую длину")

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(years, divorce_rate, marker='o')
plt.title('Количество разводов в штате Мэн (США) с 2000 по 2010 гг.')
plt.xlabel('Год')
plt.ylabel('Количество разводов')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(years, margarine_consumption, marker='o')
plt.title('Потребление маргарина на душу населения в США с 2000 по 2010 гг.')
plt.xlabel('Год')
plt.ylabel('Потребление маргарина (кг/чел.)')
plt.grid(True)

plt.tight_layout()
plt.show()