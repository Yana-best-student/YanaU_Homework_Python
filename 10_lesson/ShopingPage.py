import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopLoginPage:

    def __init__(self, driver):
        """
        Конструктор класса ShopLoginPage.

        :param driver: Webdriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.driver.get(
            "https://www.saucedemo.com/")

        """Открывает страницу "www.saucedemo.com" в браузере,
        использует driver.get для открытия страницы
        """
        self.wait = WebDriverWait(driver, 10)
        """
        Настраивается ожидание WebDriverWait на
        10 секунд для работы с элементами.
        """

    @allure.step("Авторизация в интернет магазине")
    def fill_form(self):
        """
        Находит поле с ID user-name и вводит в него текст "standard_user".
        Находит поле с ID password и вводит в него текст "secret_sauce".
        """

        self.driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys("secret_sauce")

    @allure.step("Выполняется вход в интернет-магазин")
    def login_shop(self):
        """
        Ожидание, пока кнопка с ID login-button станет кликабельной.
        Кликает по кнопке для выполнения входа.
        """
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#login-button"))
        ).click()


class ShopMainPage:

    def __init__(self, driver):
        """
        Конструктор класса ShopMainPage.

        :param driver: Webdriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Добавление товаров в корзину")
    def add_product(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        """
        Находит элемент с CSS селектором #add-to-cart-sauce-labs-backpack
        и кликает по нему, добавляя товар в корзину.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        """
        Находит элемент с CSS селектором #dd-to-cart-sauce-labs-onesie
        и кликает по нему, добавляя товар в корзину.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        """
        Находит элемент с CSS селектором #add-to-cart-sauce-labs-onesi
        и кликает по нему, добавляя товар в корзину.
        """
    @allure.step("Переход в корзину")
    def cart_input(self):
        """
        Находит элемент с CSS селектором .shopping_cart_link
        и кликает по нему, переходя в корзину.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link").click()


class ShopCheckout:

    def __init__(self, driver):
        """
        Конструктор класса ShopCheckout.

        :param driver: Webdriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Получение списка товаров в корзине")
    def get_cart_items(self):
        """
        Ищет элементы корзины по классу cart_item_label.
        Для каждого элемента получает имя (inventory_item_name)
        и цену (inventory_item_price).
        Возвращает список словарей с именем и ценой каждого товара.
        """
        items = []
        cart_item_elements = self.driver.find_elements(
            By.CLASS_NAME, 'cart_item_label')
        for item in cart_item_elements:
            name = item.find_element(By.CLASS_NAME, 'inventory_item_name').text
            price = item.find_element(
                By.CLASS_NAME, 'inventory_item_price').text
            items.append({'name': name, 'price': price})
        return items

    @allure.step("Переход на страницу оформления заказа")
    def checkout_input(self):
        """
        Находит элемент с CSS-селектором #checkout и
        кликает на него, инициируя процесс оформления заказа.
        """
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()


class OrderPlacement:
    def __init__(self, driver):
        """
        Конструктор класса OrderPlacement.

        :param driver: Webdriver — объект драйвера Selenium.
        """
        self.driver = driver
        """
        создаёт объект ожидания, который будет ждать элементы до 5 секунд.
        """
        self.wait = WebDriverWait(driver, 5)

    @allure.step("заполнение формы личными данными для оформления заказа")
    def form_input(self):
        """
        находит элемент по CSS-селектору с id first-name и вводит текст "Lana".
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys("Lana")
        """
        находит элемент по CSS-селектору с id last-name
        и вводит текст "Banana".
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys("Banana")
        """
        находит элемент по CSS-селектору
        с id postal-code и вводит текст "617777"
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys("617777")

    @allure.step("Продолжение оформления заказа")
    def shop_continue(self):
        """
        Создаётся ожидание до 10 секунд для элемента,
        который можно кликнуть, используя CSS-селектор #continue.
        Кликает на найденный элемент.
        """
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#continue"))
        ).click()

    @allure.step("Получение и обработка итоговой цены")
    def get_total_price(self):
        """
        Ожидает, пока элемент с CSS-селектором [data-test="total-label"]
        станет видимым, и сохраняет его в total_element.
        """
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[data-test="total-label"]'))
        )
        total_text = total_element.text
        """
        Делит текст на части, берёт последний элемент
        (цену), и удаляет символ $
        """
        total_str = total_text.split()[-1].replace('$', '')
        """
        Преобразует строку в число с плавающей точкой и возвращает его.
        :return: Итоговая цена в формате с плавающей точкой.
        :rtype: float
        """
        return float(total_str)
