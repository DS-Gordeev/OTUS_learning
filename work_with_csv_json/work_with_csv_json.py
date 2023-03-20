import json
import pandas
from csv import DictReader
from files import CSV_BOOKS_FILE_PATH
from files import JSON_USERS_PATH

# При помощи библиотеки Pandas изменяем порядок полей в файле books.csv
open_csv = pandas.read_csv(CSV_BOOKS_FILE_PATH)
reorder_csv_fields = open_csv[['Title', 'Author', 'Pages', 'Genre', 'Publisher']]
reorder_csv_fields.to_csv(CSV_BOOKS_FILE_PATH, index=False)

# Создаем пустой список для формирования итогового списка словарей с данными пользователей
user_list = []

# Создаем генератор с книгами без лишнего поля publisher, ключи в нижнем регистре
def books_generator():
    with open(CSV_BOOKS_FILE_PATH, newline='') as books:
        reader = DictReader(books)
        for row in reader:
            row = {key.lower(): value for key, value in row.items()}
            yield dict(filter(lambda item: item[0] != "publisher", row.items()))


# Из файла users.json формируем список словарей с полями name, gender, address, age и books
with open(JSON_USERS_PATH, "r") as all_users_data:
    users = json.loads(all_users_data.read())
    for index in range(len(users)):
        user_list.append(
            {
                "name": users[index]["name"],
                "gender": users[index]["gender"],
                "address": users[index]["address"],
                "age": users[index]["age"],
                "books": []
            }
        )

# Инициализируем генератор книг
books_generator = books_generator()

# Служебная переменная-счетчики для работы алгоритма по распределению книг между пользователями
n = 0

# Алгоритм распределения книг (обратить внимание на использование оператора %)
for new_book in books_generator:
    idx = n % len(user_list)
    user_list[idx]["books"].append(new_book)
    n += 1

# Записываем в файл result.json итоговый результат user_list
with open("result.json", "w") as result_json:
    data = json.dumps(user_list, indent=4)
    result_json.write(data)
