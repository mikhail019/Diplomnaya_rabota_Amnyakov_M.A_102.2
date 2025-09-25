import allure
import config
from utils import init_driver, click_element, wait_for_element


def accept_city(driver):
    """
    Функция для принятия условий по выбору города.
    Входные данные:
    - driver: WebDriver (объект Selenium WebDriver, управляющий браузером)
    Выходные данные:
    - Никаких данных не возвращается, функция выполняет клик по кнопке.
    """
    click_element(driver, config.CITY_ACCEPT_BUTTON_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)


@allure.suite("Тесты 'Читай-город'")
@allure.epic("UI_TEST")
@allure.feature("SELECTORS")
@allure.title("Тестирование работы выпадающего списка (селектора)")
@allure.severity("critical")
def test_selector():
    """
    Тестирование работы выпадающего списка (селектора) на странице.
    Входные данные:
    - driver: WebDriver (объект Selenium WebDriver, управляющий браузером)
    Ожидаемые выходные данные:
    - Никаких данных не возвращается, тест проверяет взаимодействие с элементами UI.
    """
    driver = init_driver()  # Тип: WebDriver (инициализация WebDriver)
    try:
        driver.get("https://www.chitai-gorod.ru/")  # Тип: string (URL)
        accept_city(driver)  # Входные данные: WebDriver
        click_element(driver, config.CATALOG_BUTTON_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        wait_for_element(driver, config.CATEGORY_MENU_ACTIVE_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        click_element(driver, config.CATEGORY_MENU_ACTIVE_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        wait_for_element(driver, config.COMICS_CATEGORY_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        click_element(driver, config.COMICS_CATEGORY_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
    finally:
        driver.quit()  # Тип: WebDriver (закрытие браузера)


@allure.suite("Тесты 'Читай-город'")
@allure.epic("UI_TEST")
@allure.feature("BUTTON")
@allure.title("Тестирование работы активных кнопок")
@allure.severity("critical")
def test_activ_but():
    """
    Тестирование работы кнопок на странице.
    Входные данные:
    - driver: WebDriver (объект Selenium WebDriver)
    Ожидаемые выходные данные:
    - Никаких данных не возвращается, тест проверяет взаимодействие с кнопками.
    """
    driver = init_driver()  # Тип: WebDriver (инициализация WebDriver)
    try:
        driver.get("https://www.chitai-gorod.ru/")  # Тип: string (URL)
        accept_city(driver)  # Входные данные: WebDriver
        click_element(driver, config.CERTIFICATE_BUTTON_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        wait_for_element(driver, config.CERTIFICATE_CONFIRM_BUTTON_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        click_element(driver, config.CERTIFICATE_CONFIRM_BUTTON_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
    finally:
        driver.quit()  # Тип: WebDriver


@allure.suite("Тесты 'Читай-город'")
@allure.epic("UI_TEST")
@allure.feature("CHECK_BOX")
@allure.title("Тестирование работы чекбоксов")
@allure.severity("critical")
def test_check_box():
    """
    Тестирование работы чекбоксов на странице.
    Входные данные:
    - driver: WebDriver (объект Selenium WebDriver)
    Ожидаемые выходные данные:
    - Никаких данных не возвращается, тест проверяет взаимодействие с чекбоксами.
    """
    driver = init_driver()  # Тип: WebDriver (инициализация WebDriver)
    try:
        driver.get("https://www.chitai-gorod.ru/")  # Тип: string (URL)
        accept_city(driver)  # Входные данные: WebDriver
        click_element(driver, config.CATALOG_BUTTON_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        wait_for_element(driver, config.CATEGORY_MENU_ACTIVE_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        click_element(driver, config.CATEGORY_MENU_ACTIVE_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        wait_for_element(driver, config.COMICS_CATEGORY_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        click_element(driver, config.COMICS_CATEGORY_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        wait_for_element(driver, config.CHECKBOX_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        click_element(driver, config.CHECKBOX_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        wait_for_element(driver, config.CHECKBOX_ICON_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        click_element(driver, config.CHECKBOX_ICON_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
    finally:
        driver.quit()  # Тип: WebDriver


@allure.suite("Тесты 'Читай-город'")
@allure.epic("UI_TEST")
@allure.feature("RADIO_BUTTON")
@allure.title("Тестирование работы радиокнопок")
@allure.severity("critical")
def test_radio_button():
    """
    Тестирование работы радиокнопок на странице.
    Входные данные:
    - driver: WebDriver (объект Selenium WebDriver)
    Ожидаемые выходные данные:
    - Никаких данных не возвращается, тест проверяет взаимодействие с радиокнопками.
    """
    driver = init_driver()  # Тип: WebDriver (инициализация WebDriver)
    try:
        driver.get("https://www.chitai-gorod.ru/")  # Тип: string (URL)
        accept_city(driver)  # Входные данные: WebDriver
        click_element(driver, config.CATALOG_BUTTON_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        wait_for_element(driver, config.CATEGORY_MENU_ACTIVE_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        click_element(driver, config.CATEGORY_MENU_ACTIVE_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        wait_for_element(driver, config.COMICS_CATEGORY_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        click_element(driver, config.COMICS_CATEGORY_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        wait_for_element(driver, config.RADIO_BUTTON_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        click_element(driver, config.RADIO_BUTTON_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        wait_for_element(driver, config.RADIO_BUTTON_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
        click_element(driver, config.RADIO_BUTTON_SELECTOR)  # Тип: WebDriver, string (CSS-селектор)
    finally:
        driver.quit()  # Тип: WebDriver


@allure.suite("Тесты 'Читай-город'")
@allure.epic("UI_TEST")
@allure.feature("ADAPTABILITY")
@allure.title("Тестирование адаптивности интерфейса")
@allure.severity("critical")
def test_interface():
    """
    Тестирование адаптивности интерфейса на различных разрешениях экрана.
    Входные данные:
    - driver: WebDriver (объект Selenium WebDriver)
    - config.SCREEN_SIZES: список кортежей с размерами экрана (ширина, высота)
    Ожидаемые выходные данные:
    - Никаких данных не возвращается, тест проверяет отображение интерфейса на различных разрешениях.
    """
    driver = init_driver()  # Тип: WebDriver (инициализация WebDriver)
    try:
        driver.get("https://www.chitai-gorod.ru/")  # Тип: string (URL)
        accept_city(driver)  # Входные данные: WebDriver
        for width, height in config.SCREEN_SIZES:  # Входные данные: список кортежей (int, int)
            driver.set_window_size(width, height)  # Тип: int, int (размеры окна)
        driver.maximize_window()  # Тип: WebDriver
    finally:
        driver.quit()  # Тип: WebDriver
