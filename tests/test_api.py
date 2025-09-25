import allure
import requests
from config import BASE_URL_V1, BASE_URL_V2, CATEGORIES_1, PROD_1, SS_2, PROD_2, SP_2, TOKEN


@allure.suite("Тесты 'Читай-город'")
@allure.epic("API_TEST")
@allure.feature("POSITIVE_TEST")
@allure.title("Поиск существующего товара")
@allure.severity("critical")
def test_search_real():
    """
    Тест поиска существующего товара по API.
    Входные данные:
    - Заголовок с токеном авторизации: 'Authorization': f'Bearer {TOKEN}'
    - Путь для запроса: BASE_URL_V2 + SS_2
    Ожидаемые выходные данные:
    - Статус код ответа: 200
    """
    with allure.step("Авторизация"):
        headers = {
        'Authorization': f'Bearer {TOKEN}'  # Тип: строка (Bearer token)
    }
    with allure.step("Поиск товара через API"):
        resp = requests.get(BASE_URL_V2 + SS_2, headers=headers)  # Тип: GET запрос
    with allure.step("Получение статус-кода"):
        assert resp.status_code == 200  # Тип: int (HTTP статус код)

@allure.suite("Тесты 'Читай-город'")
@allure.epic("API_TEST")
@allure.feature("POSITIVE_TEST")
@allure.title("Поиск товара по категории")
@allure.severity("critical")
def test_search_categories():
    """
    Тест поиска товаров по категории.
    Входные данные:
    - Заголовок с токеном авторизации: 'Authorization': f'Bearer {TOKEN}'
    - Путь для запроса: BASE_URL_V1 + CATEGORIES_1
    Ожидаемые выходные данные:
    - Статус код ответа: 200
    """
    with allure.step("Авторизация"):
        headers = {
        'Authorization': f'Bearer {TOKEN}'  # Тип: строка (Bearer token)
    }
    with allure.step("Поиск товара по категории через API"):
        resp = requests.get(BASE_URL_V1 + CATEGORIES_1, headers=headers)  # Тип: GET запрос
    with allure.step("Получение статус-кода"):
        assert resp.status_code == 200  # Тип: int (HTTP статус код)

@allure.suite("Тесты 'Читай-город'")
@allure.epic("API_TEST")
@allure.feature("POSITIVE_TEST")
@allure.title("Поиск товаров с использованием фильтров")
@allure.severity("critical")
def test_search_filtred():
    """
    Тест поиска товаров с использованием фильтров.
    Входные данные:
    - Заголовок с токеном авторизации: 'Authorization': f'Bearer {TOKEN}'
    - Путь для запроса: BASE_URL_V2 + PROD_2
    Ожидаемые выходные данные:
    - Статус код ответа: 200
    """
    with allure.step("Авторизация"):
        headers = {
        'Authorization': f'Bearer {TOKEN}'  # Тип: строка (Bearer token)
    }
    with allure.step("Поиск товаров с использованием фильтров через API"):
        resp = requests.get(BASE_URL_V2 + PROD_2, headers=headers)  # Тип: GET запрос
    with allure.step("Получение статус-кода"):
        assert resp.status_code == 200  # Тип: int (HTTP статус код)

@allure.suite("Тесты 'Читай-город'")
@allure.epic("API_TEST")
@allure.feature("POSITIVE_TEST")
@allure.title("Поиск товаров с использованием поисковых параметров")
@allure.severity("critical")
def test_search_params():
    """
    Тест поиска товаров с использованием поисковых параметров.
    Входные данные:
    - Заголовок с токеном авторизации: 'Authorization': f'Bearer {TOKEN}'
    - Путь для запроса: BASE_URL_V2 + SP_2
    Ожидаемые выходные данные:
    - Статус код ответа: 200
    """
    with allure.step("Авторизация"):
        headers = {
        'Authorization': f'Bearer {TOKEN}'  # Тип: строка (Bearer token)
    }
    with allure.step("Поиск товаров с использованием поисковых параметров через API"):
        resp = requests.get(BASE_URL_V2 + SP_2, headers=headers)  # Тип: GET запрос
    with allure.step("Получение статус-кода"):
        assert resp.status_code == 200  # Тип: int (HTTP статус код)


@allure.suite("Тесты 'Читай-город'")
@allure.epic("API_TEST")
@allure.feature("NEGATIVE_TEST")
@allure.title("Получение информации о несуществующей книге")
@allure.severity("critical")
def test_search_notreal():
    """
    Тест получения информации о несуществующей книге.
    Входные данные:
    - Заголовок с токеном авторизации: 'Authorization': f'Bearer {TOKEN}'
    - Путь для запроса: BASE_URL_V1 + PROD_1
    Ожидаемые выходные данные:
    - Статус код ответа: 400 (Bad Request), так как товар не существует.
    """
    with allure.step("Авторизация"):
        headers = {
        'Authorization': f'Bearer {TOKEN}'  # Тип: строка (Bearer token)
    }
    with allure.step("Получение информации о несуществующей книге через API"):
        resp = requests.get(BASE_URL_V1 + PROD_1, headers=headers)  # Тип: GET запрос
    with allure.step("Получение статус-кода"):
        assert resp.status_code == 400  # Тип: int (HTTP статус код)
