import matplotlib.pyplot as plt

text_file = 'Kerroll_Alisa_1_Alisa-v-Strane-Chudes.VjvULw.293178.txt'
letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

lcount = dict([(letter, 0) for letter in letters])

for letter in open(text_file, encoding='utf-8').read():
    try:
        lcount[letter.upper()] += 1
    except KeyError:
        pass


norm = sum(lcount.values())
freq = {letter: (count / norm) * 100 for letter, count in lcount.items()}

sorted_letters = sorted(freq, key=freq.get, reverse=False)
sorted_freq = [freq[letter] for letter in sorted_letters]

fig, ax = plt.subplots()
ax.barh(sorted_letters, sorted_freq, color='g', alpha=0.5)
ax.set_yticks(sorted_letters)
ax.set_yticklabels(sorted_letters)
ax.tick_params(axis='y', direction='out')
ax.set_ylim(-0.5, 33)
ax.xaxis.grid(True)
ax.set_xlabel('Частота букв, %')
ax.set_title("Частота появления букв в повести 'Алиса в Стране Чудес'")

top_n = 10
letter_scatter = sorted_letters[-top_n:]
freq_scatter = sorted_freq[-top_n:]

fig1, ax1 = plt.subplots()
ax1.scatter(letter_scatter, freq_scatter)
ax1.set_xlabel('Буква')
ax1.set_ylabel('Частота букв, %')
ax1.set_title(f"{top_n} букв, встречающихся чаще всего в повести 'Алиса в Стране Чудес'")
ax1.grid(True, alpha=0.3)

plt.show()