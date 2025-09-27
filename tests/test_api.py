import allure
import requests
from config import BASE_URL_V1, BASE_URL_V2, CATEGORIES_1, PROD_1, SS_2, PROD_2, SP_2, TOKEN

# Заголовки для API запросов
headers = {
    'Authorization': f'Bearer {TOKEN}',
    "User-Agent": "PostmanRuntime/7.45.0"  # Добавлен User-Agent
}

@allure.suite("Тесты 'Читай-город'")
@allure.epic("API_TEST")
@allure.feature("POSITIVE_TEST")
@allure.title("Поиск существующего товара")
@allure.severity("critical")
def test_search_real():
    with allure.step("Поиск товара через API"):
        resp = requests.get(BASE_URL_V2 + SS_2, headers=headers)  # Используем обновленные заголовки
    with allure.step("Получение статус-кода"):
        assert resp.status_code == 200  # Проверка статус-кода

@allure.suite("Тесты 'Читай-город'")
@allure.epic("API_TEST")
@allure.feature("POSITIVE_TEST")
@allure.title("Поиск товара по категории")
@allure.severity("critical")
def test_search_categories():
    with allure.step("Поиск товара по категории через API"):
        resp = requests.get(BASE_URL_V1 + CATEGORIES_1, headers=headers)  # Используем обновленные заголовки
    with allure.step("Получение статус-кода"):
        assert resp.status_code == 200  # Проверка статус-кода

@allure.suite("Тесты 'Читай-город'")
@allure.epic("API_TEST")
@allure.feature("POSITIVE_TEST")
@allure.title("Поиск товаров с использованием фильтров")
@allure.severity("critical")
def test_search_filtred():
    with allure.step("Поиск товаров с использованием фильтров через API"):
        resp = requests.get(BASE_URL_V2 + PROD_2, headers=headers)  # Используем обновленные заголовки
    with allure.step("Получение статус-кода"):
        assert resp.status_code == 200  # Проверка статус-кода

@allure.suite("Тесты 'Читай-город'")
@allure.epic("API_TEST")
@allure.feature("POSITIVE_TEST")
@allure.title("Поиск товаров с использованием поисковых параметров")
@allure.severity("critical")
def test_search_params():
    with allure.step("Поиск товаров с использованием поисковых параметров через API"):
        resp = requests.get(BASE_URL_V2 + SP_2, headers=headers)  # Используем обновленные заголовки
    with allure.step("Получение статус-кода"):
        assert resp.status_code == 200  # Проверка статус-кода

@allure.suite("Тесты 'Читай-город'")
@allure.epic("API_TEST")
@allure.feature("NEGATIVE_TEST")
@allure.title("Получение информации о несуществующей книге")
@allure.severity("critical")
def test_search_notreal():
    with allure.step("Получение информации о несуществующей книге через API"):
        resp = requests.get(BASE_URL_V1 + PROD_1, headers=headers)  # Используем обновленные заголовки
    with allure.step("Получение статус-кода"):
        assert resp.status_code == 400  # Проверка статус-кода
