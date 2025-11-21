from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopLoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://www.saucedemo.com/")
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys("secret_sauce")

    def login_shop(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#login-button"))
        ).click()


class ShopMainPage:

    def __init__(self, driver):
        self.driver = driver

    def add_product(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    def cart_input(self):
        self.driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link").click()


class ShopCheckout:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        items = []
        cart_item_elements = self.driver.find_elements(
            By.CLASS_NAME, 'cart_item_label')
        for item in cart_item_elements:
            name = item.find_element(By.CLASS_NAME, 'inventory_item_name').text
            price = item.find_element(
                By.CLASS_NAME, 'inventory_item_price').text
            items.append({'name': name, 'price': price})
        return items

    def checkout_input(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()


class OrderPlacement:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def form_input(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys("Яна")
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys("Успенская")
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys("617400")

    def shop_continue(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#continue"))
        ).click()

    def get_total_price(self):
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[data-test="total-label"]'))
        )
        total_text = total_element.text
        total_str = total_text.split()[-1].replace('$', '')
        return float(total_str)
