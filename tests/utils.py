from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Вспомогательная функция для инициализации WebDriver
def init_driver() -> webdriver.Chrome:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver

# Вспомогательная функция для клика по элементу
def click_element(driver: webdriver.Chrome, css_selector: str) -> None:
    element = wait_for_element(driver, css_selector)  # Ожидаем элемент перед кликом
    assert element is not None, "Элемент не найден для клика"
    assert element.is_displayed(), "Элемент не отображается для клика"
    element.click()

# Вспомогательная функция для ожидания элемента
def wait_for_element(driver: webdriver.Chrome, css_selector: str,
                     timeout: int = 10, interval: float = 0.1) -> webdriver.remote.webelement.WebElement:
    waiter = WebDriverWait(driver, timeout, interval)
    element = waiter.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
    assert element is not None, "Элемент не найден после ожидания"
    return element
