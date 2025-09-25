from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Вспомогательная функция для инициализации WebDriver
def init_driver() -> webdriver.Chrome:
    """
    Функция инициализирует драйвер для браузера Chrome с использованием ChromeDriverManager.
    Входные данные:
    - Нет входных параметров.
    Выходные данные:
    - Возвращает объект WebDriver (тип: webdriver.Chrome).
    """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # Тип: webdriver.Chrome
    driver.maximize_window()  # Тип: webdriver.Chrome
    return driver  # Тип: webdriver.Chrome


# Вспомогательная функция для клика по элементу
def click_element(driver: webdriver.Chrome, css_selector: str) -> None:
    """
    Функция выполняет клик по элементу на странице.
    Входные данные:
    - driver: Объект Selenium WebDriver (тип: webdriver.Chrome), который управляет браузером.
    - css_selector: Строка, представляющая CSS-селектор элемента (тип: str).
    Выходные данные:
    - Ничего не возвращает (тип: None).
    """
    element = driver.find_element(By.CSS_SELECTOR, css_selector)  # Тип: WebElement
    element.click()  # Тип: None


# Вспомогательная функция для ожидания элемента
def wait_for_element(driver: webdriver.Chrome, css_selector: str,
                     timeout: int = 10, interval: float = 0.1) -> webdriver.remote.webelement.WebElement:
    """
    Функция ожидает появления элемента на странице с использованием явного ожидания.
    Входные данные:
    - driver: Объект Selenium WebDriver (тип: webdriver.Chrome), который управляет браузером.
    - css_selector: Строка, представляющая CSS-селектор элемента (тип: str).
    - timeout: Время ожидания в секундах (тип: int, по умолчанию 10 секунд).
    - interval: Интервал между проверками наличия элемента в секундах (тип: float, по умолчанию 0.1 секунд).
    Выходные данные:
    - Возвращает объект WebElement, представляющий найденный элемент (тип: webdriver.remote.webelement.WebElement).
    """
    waiter = WebDriverWait(driver, timeout, interval)  # Тип: WebDriverWait
    return waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, css_selector)))  # Тип: webdriver.remote.webelement.WebElement
