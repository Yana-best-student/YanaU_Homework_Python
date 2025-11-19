from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES


cookie = {
    "name": "cookie_policy",
    "value": "1"
}


def test_cart_counter():
    browser = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))

    # перейти на сайт лабиринта
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window
    browser.add_cookie(cookie)


# найти все книги по слову Python
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys("Python")
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()


# добавить все книги в корзину и посчитать количество
    buy_bottons = browser.find_elements(By.CSS_SELECTOR, "[data-carttext]")
    counter = 0
    for btn in buy_bottons:
        btn.click()
        counter += 1

# перейти в корзину
    browser.get("https://www.labirint.ru/cart/")

    # проверить счетчик товаров, должен быть равен числу нажатий
    # получить текущее значение
    txt = browser.find_element(By.ID, 'basket-default-prod-count2').text

    # сравнить с counter
    assert counter == int(txt.split()[0])

    browser.quit()
