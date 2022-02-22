# -*- coding: utf-8 -*-

# В очередной спешке, проверив приложение с прогнозом погоды, вы выбежали
# навстречу ревью вашего кода, которое ожидало вас в офисе.
# И тут же день стал хуже - вместо обещанной облачности вас встретил ливень.

# Вы промокли, настроение было испорчено и на ревью вы уже пришли не в духе.
# В итоге такого сокрушительного дня вы решили написать свою программу для прогноза погода
# Из источника, которому вы доверяете.

# Для этого вам нужно:

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database
import itertools
from pprint import pprint

import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

url = 'https://weather.com/ru-RU/weather/tenday/l/c811fe9cc55daf06ea556004a0e9d096035e4627903ea902da1650bc856a3b79#detailIndex5'
page = requests.get(url)
# print(page)
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.prettify())
forecast_14d_temp = soup.find_all('span', class_='DetailsSummary--highTempValue--3Oteu')
actual_temp = soup.find('span', class_='DailyContent--temp--3d4dn')
k = 0
list_temp = []
for temp in forecast_14d_temp:
    if k == 0:
        k += 1
        continue
    else:
        list_temp.append(temp.text)

forecast_14d_days = soup.find_all('h2', class_='DetailsSummary--daypartName--2FBp2')
actual_data = soup.find('span', class_='DailyContent--daypartDate--2A3Wi')
k = 0
list_days = []
for days in forecast_14d_days:
    if k == 0:
        k += 1
        continue
    else:
        list_days.append(days.text)

dict_forecast = {}
dict_forecast.setdefault(actual_data.text, actual_temp.text)
list_forecast = zip(list_days, list_temp)
for days, temp in list_forecast:
    dict_forecast.setdefault(days, temp)
pprint(dict_forecast)