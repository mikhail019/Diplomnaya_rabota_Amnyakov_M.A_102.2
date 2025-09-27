#UI-TEST
# Путь к драйверу Chrome
CHROME_DRIVER_PATH = "path_to_chrome_driver"

# Селекторы для тестов
CITY_ACCEPT_BUTTON_SELECTOR = "div.button.change-city__button.change-city__button--accept.blue"
CATALOG_BUTTON_SELECTOR = ".catalog__button"
CATEGORY_MENU_ACTIVE_SELECTOR = "[class='categories-menu__item categories-menu__item--active']"
COMICS_CATEGORY_SELECTOR = "a[href='/catalog/books/komiksy-110063'].categories-menu__item"
CHECKBOX_SELECTOR = "div.checkbox-native__control.checkbox-native__control--search"
CHECKBOX_ICON_SELECTOR = "svg.checkbox-native__icon"
RADIO_BUTTON_SELECTOR = "span.chg-app-switch__control"
CERTIFICATE_BUTTON_SELECTOR = "a.header-bottom__link--certificate"
CERTIFICATE_CONFIRM_BUTTON_SELECTOR = "button.app-button.certificate-unauthorized-form__button.ultramarine"

# Настройки для адаптивного тестирования
SCREEN_SIZES = [(1920, 1080), (1366, 768), (375, 667), (768, 1024)]

# Таймауты и задержки
WAIT_TIMEOUT = 10  # Максимальное время ожидания элемента
WAIT_INTERVAL = 0.1  # Интервал ожидания


#API_TEST
# Основные URL API
BASE_URL_V1 = "https://web-gate.chitai-gorod.ru/api/v1/"
BASE_URL_V2 = "https://web-gate.chitai-gorod.ru/api/v2/"

# Параметры для API v1
CATEGORIES_1 = "categories/tree?slug=sovremennaya-proza-110002"
PROD_1 = "products/cycle/untitle-0000000"

# Параметры для API v2
SS_2 = "search/product?customerCityId=213&phrase=Дюна&products[page]=1&products[per-page]=48&sortPreset=relevance"
PROD_2 = "products/facet?filters[onlyNotOnSale]=1&forceFilters[categories]=110002&customerCityId=213"
SP_2 = "search/product?customerCityId=213&phrase=книги о любви&products[page]=1&products[per-page]=48&sortPreset=relevance"

# Токен авторизации
TOKEN = eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIyNTk2NTI3LCJpYXQiOjE3NTg5NTE4MDcsImV4cCI6MTc1ODk1NTQwNywidHlwZSI6MjAsImp0aSI6IjAxOTk4OWIyLTliNjUtNzNjYy04NGE0LTQwNjNmNGNkYmE5NiIsInJvbGVzIjoxMH0.Rnahb9dZUO3-jZesKzdlB0RY2gimQZmDBeqleq_f0bM