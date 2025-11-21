import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from ShopPage import ShopLoginPage
from ShopPage import ShopMainPage
from ShopPage import ShopCheckout
from ShopPage import OrderPlacement


@pytest.fixture
def driver():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_submission_flow(driver):
    shop_login = ShopLoginPage(driver)
    shop_login.fill_form()
    shop_login.login_shop()

    shop_main = ShopMainPage(driver)
    shop_main.add_product()
    shop_main.cart_input()

    shop_checkout = ShopCheckout(driver)
    cart_items = shop_checkout.get_cart_items()
    expected_items = [
        {'name': 'Sauce Labs Backpack', 'price': '$29.99'},
        {'name': 'Sauce Labs Bolt T-Shirt', 'price': '$15.99'},
        {'name': 'Sauce Labs Onesie', 'price': '$7.99'}
    ]
    assert cart_items == expected_items, "Items in cart do not match expected items"
    shop_checkout.checkout_input()

    shop_order = OrderPlacement(driver)
    shop_order.form_input()
    shop_order.shop_continue()

    total = shop_order.get_total_price()
    expected_total = 58.29
    print(total)
    assert total == expected_total, f"Expected total ${expected_total}, but got ${total}"
