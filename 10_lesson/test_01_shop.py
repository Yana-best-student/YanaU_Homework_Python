import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from ShopingPage import ShopLoginPage
from ShopingPage import ShopMainPage
from ShopingPage import ShopCheckout
from ShopingPage import OrderPlacement


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера
    """
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("SHOPING")
@allure.title("Тестирование интернет магазина")
@allure.description(
    "Проверка авторизации, добавление товара в корзину, "
    "оформление заказа"
)
@allure.severity(allure.severity_level.BLOCKER)
def test_shop_submission_flow(driver):
    with allure.step("Открытие страницы авторизации в интернет-магазине"):
        shop_login = ShopLoginPage(driver)
    with allure.step("Авторизация на сайте магазина по логину и паролю"):
        shop_login.fill_form()
    with allure.step("Нажатие на кнопку 'Login'"):
        shop_login.login_shop()

    with allure.step("Открытие страницы с товарами"):
        shop_main = ShopMainPage(driver)
    with allure.step("Добавление товаров в корзину"):
        shop_main.add_product()
    with allure.step("Нажатие на иконку корзины"):
        shop_main.cart_input()

    with allure.step("открытие страницы с добавлеными в корзину товарами"):
        shop_checkout = ShopCheckout(driver)
    with allure.step("Получение элементов корзины"):
        cart_items = shop_checkout.get_cart_items()
        allure.attach(str(cart_items), name="Список товаров в корзине",
                      attachment_type=allure.attachment_type.TEXT)
        expected_items = [
            {'name': 'Sauce Labs Backpack', 'price': '$29.99'},
            {'name': 'Sauce Labs Bolt T-Shirt', 'price': '$15.99'},
            {'name': 'Sauce Labs Onesie', 'price': '$7.99'}
        ]
    with allure.step("Проверка соответствия корзины ожидаемым товарам"):
        assert cart_items == expected_items, "Items in cart do not match expected items"

    with allure.step("Нажатие кнопки 'Checkout'"):
        shop_checkout.checkout_input()

    with allure.step("открытие страницы для оформления заказа"):
        shop_order = OrderPlacement(driver)

    with allure.step("Заполнение полей данными для оформления заказа"):
        shop_order.form_input()
    with allure.step("Нажатие кнопки 'Continue'"):
        shop_order.shop_continue()

    with allure.step("Получает и обрабатывает итоговую цену с веб-страницы."):
        """
        Получает и обрабатывает итоговую цену с веб-страницы.
        :return: Итоговая цена.
        :rtype: float
        """
        total = shop_order.get_total_price()
        expected_total = 58.29
        print(total)
        assert total == expected_total, f"Expected total ${expected_total}, but got ${total}"
