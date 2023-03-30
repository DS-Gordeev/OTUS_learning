import requests
import json
import pytest
from api_files import ALL_BREEDS_JSON

def get_all_breeds():
    with open(ALL_BREEDS_JSON, 'r') as f:
        reader = json.loads(f.read())
        breads_list = [k for k, v in reader['message'].items()]
        for breads in breads_list:
            yield breads

all_breeds_gen = get_all_breeds()

@pytest.fixture(scope='session')
def all_breads_list():
    req = requests.get('https://dog.ceo/api/breeds/list/all')
    assert req.status_code == 200
    return [k for k, v in req.json()['message'].items()]


@pytest.mark.parametrize('bread', all_breeds_gen)
def test_dog_api_1(bread, all_breads_list):
    """Тест проверяет, что API возвращает все породы собак согласно нашему списку из файла"""
    assert bread in all_breads_list


@pytest.mark.parametrize('quantity, resp', [(0, 1), (1, 1), (25, 25), (49, 49), (50, 50), (51, 50), (75, 50), (-1, 1)])
def test_dog_api_2(quantity, resp):
    """Тест проверяет, что API возвращает указанное кол-во случайных фото собак разных пород"""
    req = requests.get(f'https://dog.ceo/api/breeds/image/random/{quantity}]')
    assert req.status_code == 200
    assert len(req.json()['message']) == resp

all_breeds_gen = get_all_breeds()

@pytest.mark.parametrize('bread_name', all_breeds_gen)
def test_dog_api_3(bread_name):
    """Тест проверяет, что API возвращает фото только указанной породы собак (включая разновидности)"""
    req = requests.get(f'https://dog.ceo/api/breed/{bread_name}/images')
    assert req.status_code == 200
    for bread_url in req.json()['message']:
        assert bread_name in bread_url
