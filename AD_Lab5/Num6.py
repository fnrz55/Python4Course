import matplotlib.pyplot as plt
from ruts import ReadabilityStats

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def calculate_readability_stats(text):
    rs = ReadabilityStats(text)
    stats = rs.get_stats()
    return stats

def main():
    filenames = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']
    texts = [read_file(filename) for filename in filenames]
    stats_list = [calculate_readability_stats(text) for text in texts]

    metric_name = 'flesch_reading_easy'
    metrics = [stats[metric_name] for stats in stats_list]

    plt.bar(filenames, metrics)
    plt.xlabel('Файл')
    plt.ylabel('Индекс удобочитаемости Флеша')
    plt.title('Уровень удобочитаемости текстов')
    plt.show()

if __name__ == "__main__":
    main()