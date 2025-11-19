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

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
   

def open_labirint():
    # перейти на сайт лабиринта
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)


def search(term):
    # найти все книги по слову
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()


def add_books():
    # добавить все книги в корзину и посчитать количество
    buy_bottons = browser.find_elements(By.CSS_SELECTOR, "[data-carttext]")
    counter = 0
    for btn in buy_bottons:
        btn.click()
        counter += 1

    return counter


def go_to_cart():
    # перейти в корзину
    browser.get("https://www.labirint.ru/cart/")


def get_cart_counter():
# проверить счетчик товаров, должен быть равен числу нажатий
    txt = browser.find_element(By.ID, 'basket-default-prod-count2').text
    return int(txt.split()[0])


def close_driver():
    #закрываем браузер
    browser.quit()


def test_cart_counter():
    open_labirint()
    search('python')
    added = add_books()
    go_to_cart()
    cart_counter = get_cart_counter()
    close_driver()
    assert added == cart_counter

def test_empty_search():
  open_labirint()
  search("12345678901234567890")
  txt = browser.find_element(
    By.CSS_SELECTOR, ".b-rfooter-info-e-text").text.strip()
  close_driver()

  assert txt.split("?")[0].strip() == \
    "Пока не нашли для себя ничего в Лабиринте"
