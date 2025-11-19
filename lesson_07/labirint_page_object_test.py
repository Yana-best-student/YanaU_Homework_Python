from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage


def test_cart_counter():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser);
    main_page.set_cookie_policy()
    main_page.search("12345678901234567890")

    result_page = ResultPage(browser)
    msg = result_page.get_empty_result_message()
    print(msg)
    assert "Все, что мы нашли в Лабиринте по запросу" in msg
    # to_be = result_page.add_books()

    # cart_page = CartPage(browser)
    # cart_page.get()
    # as_is = cart_page.get_cart_counter()
    # assert as_is == to_be

    browser.quit()
   

