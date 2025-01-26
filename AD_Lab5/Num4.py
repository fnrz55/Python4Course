import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from collections import Counter


def scarpy(url):
  wordlist = []
  response = requests.get(url, verify=False)

  if response.status_code == 200:
    sour_text = response.text
    print(f"Данные получены успешно с {url}")
  else:
    print(f"Ошибка доступа к странице {url}: {response.status_code}")
    exit()

  t_soup = BeautifulSoup(sour_text, 'html.parser')
  paragraphs = t_soup.find_all(['p', 'li', 'span'])

  if not paragraphs:
    print(f"Не найден текст для анализа на сайте {url}.")
    exit()

  for each_text in paragraphs:
    content = each_text.text
    words = content.lower().split()
    wordlist.extend(words)

  return wordlist

def filter_wlist(wordlist):
    clean_list = []
    symbols = "!@#$%^&*()_-+={[}]|\\;:\"<>?/.,"

    for word in wordlist:
        for symbol in symbols:
            word = word.replace(symbol, '')
        if len(word) > 0:
            clean_list.append(word)

    return clean_list


def create_plot(clean_list, title):
    word_count = Counter(clean_list)
    most_common = word_count.most_common(20)

    if not most_common:
        print(f"Нет данных для построения графика: {title}")
        return

    words, counts = zip(*most_common)

    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color='skyblue')
    plt.title(title, fontsize=16)
    plt.xlabel("Слова", fontsize=12)
    plt.ylabel("Количество слов, шт", fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # Первый сайт
    url1 = "http://www.kremlin.ru/"
    wordlist = scarpy(url1)
    clean_list = filter_wlist(wordlist)
    create_plot(clean_list, "20 наиболее часто встречаемых слов на сайте kremlin.ru")

    # Второй сайт
    url2 = "https://www.volgograd.ru/"
    wordlist = scarpy(url2)
    clean_list = filter_wlist(wordlist)
    create_plot(clean_list, "20 наиболее часто встречаемых слов на сайте volgograd.ru")

    # Третий сайт
    url3 = "http://volgadmin.ru/"
    wordlist = scarpy(url3)
    clean_list = filter_wlist(wordlist)
    create_plot(clean_list, "20 наиболее часто встречаемых слов на сайте volgadmin.ru")

    # Четвертый сайт
    url4 = "https://www.vstu.ru/"
    wordlist = scarpy(url4)
    clean_list = filter_wlist(wordlist)
    create_plot(clean_list, "20 наиболее часто встречаемых слов на сайте vstu.ru")
