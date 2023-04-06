import requests
import pytest
from random import randint
from jsonschema import validate


@pytest.mark.parametrize('brewery_id', ['d6317b33-57b6-4509-b4f8-d96094716eef',
                                        'add42f7c-059e-4ecc-81dd-2f7d3eabb800',
                                        '5fdcc498-f9df-4fa5-b35d-487a59f0fecc'],
                         ids=['BottleHouse Brewery', 'Pedestrian Brewing', '2Kids Brewing Company'])
def test_brewery_api_1(base_url, brewery_id):
    """Тест проверяет, что API возвращает пивоварню с тем id который был указан в запросе"""
    res = requests.get(base_url + f'{brewery_id}')
    assert res.status_code == 200
    assert res.json()['id'] == brewery_id


def test_brewery_api_2(base_url):
    """Тест проверяет, что API возвращает запрашиваемое кол-во пивоварен"""
    per_page_random = randint(1, 200)
    res = requests.get(base_url, params={'per_page': per_page_random})
    assert res.status_code == 200
    assert len(res.json()) == per_page_random


@pytest.mark.parametrize('brewery_type', ['micro', 'nano', 'regional', 'brewpub', 'large', 'planning', 'bar',
                                          'contract', 'proprietor', 'closed'])
def test_brewery_api_3(base_url, brewery_type):
    """Тест проверяет, что API возвращает пивоварни только запрашиваемого типа"""
    res = requests.get(base_url, params={'by_type': brewery_type, 'per_page': 200})
    assert res.status_code == 200
    for brewery in res.json():
        assert brewery['brewery_type'] == brewery_type


@pytest.mark.parametrize('query', ['cat', 'dog', 'beer', 'pig', 'horse'])
def test_brewery_api_4(base_url, query):
    """Тест проверяет, что API возвращает пивоварни с указанной подстрокой в наименовании и ответ соответствует схеме"""
    res = requests.get(base_url + 'autocomplete', params={'query': query})
    print(res.json())

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"}
        },
        "required": ["id", "name"]
    }

    for brewery_data in res.json():
        validate(instance=brewery_data, schema=schema)

@pytest.mark.parametrize('country', ['Austria', 'England', 'France', 'Isle of Man', 'Ireland', 'Poland', 'Portugal',
                                          'Scotland', 'South Korea', 'United States'])
@pytest.mark.parametrize('brewery_type', ['micro', 'nano', 'regional', 'brewpub', 'large', 'planning', 'bar',
                                          'contract', 'proprietor', 'closed'])
def test_brewery_api_5(base_url, country, brewery_type):
    """Тест проверяет, что API возвращает пивоварни в каждой стране каждого типа и ответ соответствует схеме"""
    res = requests.get(base_url + 'meta', params={'by_country': country, 'by_type': brewery_type})

    schema = {
        "type": "object",
        "properties": {
            "total": {"type": "string"},
            "page": {"type": "string"},
            "per_page": {"type": "string"}
        },
        "required": ["total", "page", "per_page"]
    }

    validate(instance=res.json(), schema=schema)
