import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.epic("UI Тестирование")
@allure.feature("Поиск книжной информации")
@allure.title("Поиск книги по полному названию на кириллице")
@allure.description("Тест проверяет возможность поиска книги по заголовку 'игрушки'.")
@pytest.mark.positive
@pytest.mark.ui
def test_search_by_full_name(driver):
    with allure.step("Открытие сайта"):
        driver.get("https://www.chitai-gorod.ru")

    with allure.step("Поиск книги"):
        search_field = driver.find_element(By.NAME, "search")
        search_field.clear()
        search_field.send_keys("игрушки")
        driver.find_element(By.XPATH, "//button[@aria-label='Найти']").click()

        WebDriverWait(driver, 20).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "search-title__head"), "игрушки"))

    with allure.step("Проверка результатов поиска"):
        result = driver.find_element(By.CLASS_NAME, "search-title__head").text
        assert "Результаты поиска «игрушки»" in result, f"Ожидалось 'Результаты поиска «игрушки»', но получено '{result}'"
