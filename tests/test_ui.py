import allure
import config
from utils import init_driver, click_element, wait_for_element
from selenium.webdriver.common.by import By


def accept_city(driver):
    click_element(driver, config.CITY_ACCEPT_BUTTON_SELECTOR)


@allure.suite("Тесты 'Читай-город'")
@allure.epic("UI_TEST")
@allure.feature("SEARCH")
@allure.title("Позитивный тест: Поиск существующей книги")
@allure.severity("critical")
def test_search_existing_book():
    driver = init_driver()
    try:
        driver.get("https://www.chitai-gorod.ru/")
        accept_city(driver)
        search_box = driver.find_element(By.NAME, "search")  # Замените на актуальный селектор
        search_box.send_keys("Существующая книга")  # Замените на название существующей книги
        search_box.submit()

        assert "Результаты поиска" in driver.page_source  # Замените на актуальное сообщение
    finally:
        driver.quit()


@allure.suite("Тесты 'Читай-город'")
@allure.epic("UI_TEST")
@allure.feature("SEARCH")
@allure.title("Негативный тест: Поиск несуществующей книги")
@allure.severity("critical")
def test_search_non_existent_book():
    driver = init_driver()
    try:
        driver.get("https://www.chitai-gorod.ru/")
        accept_city(driver)
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys("Несуществующая книга")
        search_box.submit()

        assert "Книги не найдены" in driver.page_source  # Замените на актуальное сообщение
    finally:
        driver.quit()


@allure.suite("Тесты 'Читай-город'")
@allure.epic("UI_TEST")
@allure.feature("SEARCH")
@allure.title("Негативный тест: Поиск с пустым названием")
@allure.severity("critical")
def test_search_empty_title():
    driver = init_driver()
    try:
        driver.get("https://www.chitai-gorod.ru/")
        accept_city(driver)
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys("")
        search_box.submit()

        assert "Пожалуйста, введите название книги" in driver.page_source  # Замените на актуальное сообщение
    finally:
        driver.quit()


@allure.suite("Тесты 'Читай-город'")
@allure.epic("UI_TEST")
@allure.feature("SEARCH")
@allure.title("Негативный тест: Поиск с недопустимыми символами")
@allure.severity("critical")
def test_search_invalid_characters():
    driver = init_driver()
    try:
        driver.get("https://www.chitai-gorod.ru/")
        accept_city(driver)
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys("@#$%^&*()")
        search_box.submit()

        assert "Книги не найдены" in driver.page_source  # Замените на актуальное сообщение
    finally:
        driver.quit()


@allure.suite("Тесты 'Читай-город'")
@allure.epic("UI_TEST")
@allure.feature("SEARCH")
@allure.title("Негативный тест: Поиск с очень длинным названием")
@allure.severity("critical")
def test_search_long_title():
    long_title = "A" * 256  # Пример очень длинного названия
    driver = init_driver()
    try:
        driver.get("https://www.chitai-gorod.ru/")
        accept_city(driver)
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys(long_title)
        search_box.submit()

        assert "Книги не найдены" in driver.page_source  # Замените на актуальное сообщение
    finally:
        driver.quit()
