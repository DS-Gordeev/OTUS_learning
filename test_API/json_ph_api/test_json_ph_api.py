import pytest
import requests
from jsonschema import validate

json = {'title': 'foo',
        'body': 'bar',
        'userId': 1}

headers = {'Content-type': 'application/json; charset=UTF-8'}

def test_json_ph_1(base_url):
    """Тест добавляет новую запись posts и проверяет, что добавление прошло корректно"""
    res = requests.post(base_url + 'posts', json=json, headers=headers)
    assert res.status_code == 201
    assert res.json()['title'] == 'foo'
    assert res.json()['body'] == 'bar'
    assert res.json()['userId'] == 1


def test_json_ph_2(base_url):
    """Тест удаляет запись и проверяет, что возвращается корректный пустой результат"""
    res = requests.request('delete', url=base_url + 'posts/1')
    assert res.status_code == 200
    assert not res.next

@pytest.mark.parametrize('end_point, code', [('posts', 201), ('comments', 201), ('albums', 201),
                                               ('photos', 201), ('todos', 201), ('users', 201)])
def test_json_ph_3(base_url, end_point, code):
    """Тест проверяет, что все ручки отвечают корректно"""
    res = requests.post(base_url + f'{end_point}', json=json, headers=headers)
    assert res.status_code == code


def test_json_ph_4(base_url):
    """Тест проверяет, что API возвращает все комментарии и они соответствуют схеме"""
    res = requests.get(base_url + 'comments', json=json, headers=headers)

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



# https://jsonplaceholder.typicode.com/comments?postId=1&id=5