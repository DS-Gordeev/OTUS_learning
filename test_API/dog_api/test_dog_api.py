import requests
import json
import pytest
from test_API.api_files import ALL_BREEDS_JSON


def all_breeds_from_json():
    with open(ALL_BREEDS_JSON, 'r') as f:
        reader = json.loads(f.read())
        breads_list = [k for k, v in reader['message'].items()]
        for breads in breads_list:
            yield breads


all_breeds_gen_test_1 = all_breeds_from_json()


@pytest.mark.parametrize('bread', all_breeds_gen_test_1)
def test_dog_api_1(bread, all_breeds_from_api):
    """Тест проверяет, что API возвращает все породы собак согласно нашему списку из файла"""
    assert bread in all_breeds_from_api


@pytest.mark.parametrize('quantity, response', [(0, 1), (1, 1), (25, 25), (49, 49), (50, 50), (51, 50), (75, 50), (-1, 1)])
def test_dog_api_2(base_url, quantity, response):
    """Тест проверяет, что API возвращает указанное кол-во случайных фото собак разных пород"""
    res = requests.get(base_url + f'breeds/image/random/{quantity}]')
    assert res.status_code == 200
    assert len(res.json()['message']) == response


all_breeds_gen_test_3 = all_breeds_from_json()


@pytest.mark.parametrize('bread_name', all_breeds_gen_test_3)
def test_dog_api_3(base_url, bread_name):
    """Тест проверяет, что API возвращает фотографии только указанной породы собак (включая разновидности)"""
    res = requests.get(base_url + f'breed/{bread_name}/images')
    assert res.status_code == 200
    for bread_url in res.json()['message']:
        assert bread_name in bread_url


@pytest.mark.parametrize('bread_name', ['boxer', 'poodle', 'rottweiler', 'spitz'])
def test_dog_api_4(base_url, bread_name):
    """Тест проверяет, что API возвращает случайное фото указанной породы собаки"""
    res = requests.get(base_url + f'breed/{bread_name}/images/random')
    assert res.status_code == 200
    assert bread_name in res.json()['message']


@pytest.mark.parametrize('bread_name, sub_bread', [('mastiff', ['bull', 'english', 'tibetan']),
                                                   ('retriever', ['chesapeake', 'curly', 'flatcoated', 'golden']),
                                                   ('husky', [])
                                                   ])
def test_dog_api_5(base_url, bread_name, sub_bread):
    """Тест проверяет, что API возвращает разновидности породы указанной породы собак"""
    res = requests.get(base_url + f'breed/{bread_name}/list')
    assert res.status_code == 200
    assert res.json()['message'] == sub_bread
