"""
Необходимо реализовать скрипт, который будет получать с русскоязычной википедии список всех животных
(https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту) и записывать в файл в формате beasts.csv
количество животных на каждую букву алфавита.
Содержимое результирующего файла:

А,642
Б,412
В,....

Примечание:
анализ текста производить не нужно, считается любая запись из категории
(в ней может быть не только название, но и, например, род)
"""
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "beautifulsoup4"])
    import requests
    from bs4 import BeautifulSoup

import csv
from collections import defaultdict
import time

BASE_URL = "https://ru.wikipedia.org"
START_URL = BASE_URL + "/wiki/Категория:Животные_по_алфавиту"

def get_counts():
    counts = defaultdict(int)
    next_page = START_URL

    while next_page:
        print(f"Парсинг страницы: {next_page}")
        response = requests.get(next_page)
        soup = BeautifulSoup(response.content, 'html.parser')

        items = soup.select('#mw-pages .mw-category-group ul li a')
        for item in items:
            title = item.text.strip()
            if title:
                first_letter = title[0].upper()
                if 'А' <= first_letter <= 'Я':
                    counts[first_letter] += 1

        next_page = None
        for a in soup.select('#mw-pages a'):
            if 'Следующая страница' in a.text:
                next_page = BASE_URL + a['href']
                break

        time.sleep(0.5)

    return counts

def save_to_csv(counts, filename='beasts.csv'):
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for letter in sorted(counts.keys()):
            writer.writerow([letter, counts[letter]])

if __name__ == "__main__":
    counts = get_counts()
    save_to_csv(counts)
    print("Готово! Данные записаны в beasts.csv")
