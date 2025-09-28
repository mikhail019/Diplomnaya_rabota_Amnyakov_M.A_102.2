import allure
import requests
from config import BASE_URL_V1, BASE_URL_V2, CATEGORIES_1, PROD_1, SS_2, PROD_2, SP_2, TOKEN

# Заголовки для API запросов
headers = {
    'Authorization': f'Bearer {TOKEN}',
    "User-Agent": "PostmanRuntime/7.45.0"
}

@allure.suite("Тесты 'Читай-город'")
@allure.epic("API_TEST")
@allure.feature("POSITIVE_TEST")
@allure.title("Поиск существующего товара")
@allure.severity("critical")
def test_search_existing_product():
    with allure.step("Поиск товара через API"):
        resp = requests.get(BASE_URL_V2 + SS_2, headers=headers)
    with allure.step("Получение статус-кода"):
        assert resp.status_code == 200
        assert len(resp.json().get('products', [])) > 0  # Проверка, что есть результаты

@allure.suite("Тесты 'Читай-город'")
@allure.epic("API_TEST")
@allure.feature("NEGATIVE_TEST")
@allure.title("Получение информации о несуществующей книге")
@allure.severity("critical")
def test_search_non_existent_product():
    with allure.step("Получение информации о несуществующей книге через API"):
        resp = requests.get(BASE_URL_V1 + PROD_1, headers=headers)
    with allure.step("Получение статус-кода"):
        assert resp.status_code == 404  # Проверка статус-кода для несуществующего продукта

@allure.suite("Тесты 'Читай-город'")
@allure.epic("API_TEST")
@allure.feature("NEGATIVE_TEST")
@allure.title("Поиск товара с пустым названием")
@allure.severity("critical")
def test_search_empty_title():
    with allure.step("Поиск товара с пустым названием через API"):
        resp = requests.get(BASE_URL_V2 + "search/product?customerCityId=213&phrase=&products["
                                          "page]=1&products[per-page]=48", headers=headers)
    with allure.step("Получение статус-кода"):
        assert resp.status_code == 400  # Проверка статус-кода для пустого запроса

@allure.suite("Тесты 'Читай-город'")
@allure.epic("API_TEST")
@allure.feature("NEGATIVE_TEST")
@allure.title("Поиск товара с недопустимыми символами")
@allure.severity("critical")
def test_search_invalid_characters():
    with allure.step("Поиск товара с недопустимыми символами через API"):
        resp = requests.get(BASE_URL_V2 + "search/product?customerCityId=213&phrase=@#$%^&*()&products["
                                          "page]=1&products[per-page]=48", headers=headers)
    with allure.step("Получение статус-кода"):
        assert resp.status_code == 400  # Проверка статус-кода для недопустимых символов

@allure.suite("Тесты 'Читай-город'")
@allure.epic("API_TEST")
@allure.feature("NEGATIVE_TEST")
@allure.title("Поиск товара с очень длинным названием")
@allure.severity("critical")
def test_search_long_title():
    long_title = "A" * 256  # Пример очень длинного названия
    with allure.step("Поиск товара с очень длинным названием через API"):
        resp = requests.get(BASE_URL_V2 + f"search/product?customerCityId=213&phrase={
        long_title}&products[page]=1&products[per-page]=48", headers=headers)
    with allure.step("Получение статус-кода"):
        assert resp.status_code == 400  # Проверка статус-кода для слишком длинного названия
