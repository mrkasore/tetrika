import requests
from bs4 import BeautifulSoup
import csv
from collections import defaultdict


def get_animals_count():
    base_url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    letter_counts = defaultdict(int)

    while True:
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        category_groups = soup.find_all('div', class_='mw-category-group')

        for group in category_groups:
            letter = group.find('h3').text.strip()

            if len(letter) == 1 and letter.isalpha() and letter.isupper() and letter >= 'А' and letter <= 'Я':
                items = group.find_all('li')
                letter_counts[letter] += len(items)
            else:
                break

        next_page = soup.find('a', string='Следующая страница')
        if not next_page:
            break

        base_url = "https://ru.wikipedia.org" + next_page['href']

    return letter_counts


def write_to_csv(counts):
    sorted_letters = sorted(counts.keys(), key=lambda x: ord(x))
    with open('beasts.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for letter in sorted_letters:
            writer.writerow([letter, counts[letter]])


if __name__ == "__main__":
    counts = get_animals_count()
    write_to_csv(counts)
    print("Данные успешно записаны в beasts.csv")