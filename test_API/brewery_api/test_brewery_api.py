import requests
import pytest


@pytest.mark.parametrize('brewery_id', ['b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0',
                                        '4a09f017-db8f-42e1-a8ec-a0cd81c28761',
                                        'ee6d39c6-092f-4623-8099-5b8643f70dbe'])
def test_brewery_api_1(base_url, brewery_id):
    """Тест проверяет, что API возвращает пивоварню с тем id который был указан в запросе"""
    req = requests.get(base_url + '/' + f'{brewery_id}')
    assert req.status_code == 200
    assert req.json()['id'] == brewery_id


