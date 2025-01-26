from Levenshtein import ratio
from difflib import SequenceMatcher
import matplotlib.pyplot as plt


def read_file(filename):
    with open(filename, 'r') as file:
        print("1")
        return file.read()


def compare_strings(str1, str2):
    print("2")
    levenshtein_ratio = ratio(str1, str2)
    print("3")
    sequence_matcher_ratio = SequenceMatcher(None, str1, str2).ratio()
    print("4")
    return levenshtein_ratio, sequence_matcher_ratio


text1 = read_file('file1.txt')
text2 = read_file('file2.txt')

levenshtein_ratio, sequence_matcher_ratio = compare_strings(text1, text2)

print(f"Коэффициент Левенштейна: {levenshtein_ratio}")
print(f"SequenceMatcher ratio: {sequence_matcher_ratio}")

labels = ['Коэффициент Левенштейна', 'SequenceMatcher']
values = [levenshtein_ratio, sequence_matcher_ratio]

plt.bar(labels, values)
plt.xlabel('Метод сравнения')
plt.ylabel('Уровень сходства')
plt.title('Сходство текстов')
plt.show()