import json
import pandas
from csv import DictReader
from files import CSV_BOOKS_FILE_PATH
from files import JSON_USERS_PATH

# При помощи библиотеки Pandas изменяем порядок полей в файле books.csv
open_csv = pandas.read_csv(CSV_BOOKS_FILE_PATH)
reorder_csv_fields = open_csv[['Title', 'Author', 'Pages', 'Genre', 'Publisher']]
reorder_csv_fields.to_csv(CSV_BOOKS_FILE_PATH, index=False)

# Создаем пустой список и словарь для формирования итогового списка словарей с данными пользователей
user_list = []
user_dict = {}

# Создаем генератор с книгами без лишнего поля publisher, ключи в нижнем регистре
def books_generator():
    with open(CSV_BOOKS_FILE_PATH, newline='') as books:
        reader = DictReader(books)
        for row in reader:
            row = {key.lower(): value for key, value in row.items()}
            yield dict(filter(lambda item: item[0] != "publisher", row.items()))


# Из файла users.json формируем список словарей с полями name, gender, address, age
with open(JSON_USERS_PATH, "r") as all_users_data:
    users = json.loads(all_users_data.read())
    for index in range(len(users)):
        user_dict["name"] = users[index]["name"]
        user_dict["gender"] = users[index]["gender"]
        user_dict["address"] = users[index]["address"]
        user_dict["age"] = users[index]["age"]
        user_list.append(user_dict.copy())

# Инициализируем генератор книг
books_generator = books_generator()

# Служебные переменные-счетчики для работы алгоритма по распределению книг между пользователями
n = 0
j = 0

# Алгоритм распределения книг
for new_book in books_generator:
    # Сперва выдадим всем по одной книге
    if n != len(user_list):
        user_list[n]["books"] = [new_book]
        n += 1
    else:
        # Потом будем выдавать еще по одной по-кругу пока книги не закончатся (генератор опустеет)
        if j == len(user_list):
            j = 0
        else:
            user_list[j]["books"].append(new_book)
            j += 1

# Записываем в файл result.json итоговый результат user_list
with open("result.json", "w") as result_json:
    data = json.dumps(user_list, indent=4)
    result_json.write(data)
