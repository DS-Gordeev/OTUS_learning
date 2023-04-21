import pytest
import requests
import json
from csv import DictReader
from jsonschema import validate
from test_API.api_files import ALL_USERS_CVS, PH_DATA, PH_HEADERS


with open(PH_DATA, 'r') as json_file, open(PH_HEADERS, 'r') as headers_file:
    json_data = json.loads(json_file.read())
    headers_data = json.loads(headers_file.read())


def test_json_ph_1(base_url):
    """Тест добавляет новую запись posts и проверяет, что добавление прошло корректно"""
    res = requests.post(base_url + 'posts', json=json_data, headers=headers_data)
    assert res.status_code == 201
    assert res.json()['title'] == 'foo'
    assert res.json()['body'] == 'bar'
    assert res.json()['userId'] == 1


def test_json_ph_2(base_url):
    """Тест удаляет запись и проверяет, что возвращается корректный пустой результат"""
    res = requests.request('delete', url=base_url + 'posts/1')
    assert res.status_code == 200
    assert not res.next


@pytest.mark.parametrize('end_point', ['posts', 'comments', 'albums', 'photos', 'todos', 'users'])
def test_json_ph_3(base_url, end_point):
    """Тест проверяет, что все ручки отвечают корректно"""
    res = requests.post(base_url + f'{end_point}', json=json_data, headers=headers_data)
    assert res.status_code == 201


def test_json_ph_4(base_url):
    """Тест проверяет, что API возвращает все комментарии и они соответствуют схеме"""
    res = requests.get(base_url + 'comments', json=json_data, headers=headers_data)

    schema = {
        "type": "object",
        "properties": {
            "postId": {"type": "number"},
            "id": {"type": "number"},
            "name": {"type": "string"},
            "email": {"type": "string"},
            "body": {"type": "string"},
        },
        "required": ["id", "name"]
    }

    all_comments = res.json()

    for comment in all_comments:
        validate(instance=comment, schema=schema)


def users_generator():
    with open(ALL_USERS_CVS, newline='') as users:
        reader = DictReader(users)
        for row in reader:
            yield row


users_from_csv = users_generator()
next(users_from_csv)


@pytest.mark.parametrize('user', users_from_csv)
def test_json_ph_5(base_url, user):
    """Тест проверяет, что API возвращает корректные поля пользователей: id, name, username, city, website
    согласно файлу users.csv"""
    res = requests.get(base_url + 'users', params={'id': user['id']}).json()[0]
    assert res['id'] == int(user['id'])
    assert res['name'] == user['name']
    assert res['username'] == user['username']
    assert res['address']['city'] == user['city']
    assert res['website'] == user['website']
