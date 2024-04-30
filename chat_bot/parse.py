import requests
from bs4 import BeautifulSoup
import os
import random

# Чтобы избежать блокировки сохраним сайт в отдельный файл
if not os.path.exists('index.html'):
    url = 'https://www.kp.ru/russia/tyumen/dostoprimechatelnosti/'
    response = requests.get(url)
    response.encoding = 'utf-8'
    source = response.text
    with open('index.html', 'w', encoding="utf-8") as file:
        file.write(source)

squares = []
squares_words = ['Мост', 'Площадь', 'Сквер']
museums = []
museums_words = ['Школьникам,', 'Музей']
parks = []
parks_words = ['Экопарк','Гагарина', 'Японский', 'Аптекарский', 'зоопарк']
monuments = []
monuments_words = ['Кремль', 'Церковь', 'Знаменский', 'Башня']
places = []
places_words = ['Александровский', 'Аквапарк', 'Тюменская', 'Комплекс', 'правительства', 'Бульвар', 'Аллея', 'Театр', 'Памятник', 'Экспозиция']

def add_list(places, words, new_list):
    indices_to_remove = []
    for index, place in enumerate(places):
        for word in words:
            if word.lower() in place.lower():
                place = place.replace('\xa0', ' ')
                new_list.append(f"{len(new_list) + 1}. {place.split(' ', 1)[1]}")
                indices_to_remove.append(index)

    for index in sorted(indices_to_remove, reverse=True):
        del places[index]

    return new_list

with open('index.html', encoding="utf-8") as file:
    result = file.read()

soup = BeautifulSoup(result, 'lxml')
first_elements = soup.find('div', class_='content-column').find_all('h3')
two_elements = soup.select('.text-block > ul > li')
all_elements = []
for first in first_elements:
    name = first.text.strip()
    if name[0].isdigit():
        all_elements.append(name)
for two in two_elements:
    name = two.text.strip()
    if name[0].isdigit():
        all_elements.append(name)


squares_list = add_list(all_elements, squares_words, squares)
museums_list = add_list(all_elements, museums_words, museums)
parks_list = add_list(all_elements, parks_words, parks)
monuments_list = add_list(all_elements, monuments_words, monuments)
places_list = add_list(all_elements, places_words, places)


