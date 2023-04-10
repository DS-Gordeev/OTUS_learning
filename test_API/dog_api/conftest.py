import pytest
import requests


def pytest_addoption(parser):
    parser.addoption("--url", default="https://dog.ceo/api/", help="Base URL for dog API")


@pytest.fixture(scope='session')
def base_url(request):
    """Фикстура для передачи базового URL в каждый тест"""
    return request.config.getoption("--url")


@pytest.fixture(scope='session')
def all_breeds_from_api(base_url):
    """Фикстура для теста test_dog_api_1. Делает один запрос к API и возвращает список всех пород собак"""
    req = requests.get(base_url + 'breeds/list/all')
    assert req.status_code == 200
    return [k for k, v in req.json()['message'].items()]
