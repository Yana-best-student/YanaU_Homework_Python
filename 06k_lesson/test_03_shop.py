from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))


def test_shop_types():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://www.saucedemo.com/")

    username_input = driver.find_element(By.CSS_SELECTOR, "#user-name")
    username_input.send_keys("standard_user")
    password_input = driver.find_element(By.CSS_SELECTOR, "#password")
    password_input.send_keys("secret_sauce")
    login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#login-button"))
    ).click()
    backpack = driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"))
    ).click()

    bolt_shirt = driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"))
    ).click()

    labs_onesie = driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"))
    ).click()

    cart = driver.find_element(
        By.CSS_SELECTOR, ".shopping_cart_link")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".shopping_cart_link"))
    ).click()

    checkout = driver.find_element(
        By.CSS_SELECTOR, "#checkout")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#checkout"))
    ).click()

    first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
    first_name.send_keys("Яна")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#first-name")))

    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    last_name.send_keys("Успенская")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#last-name")))

    postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    postal_code.send_keys("617400")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#postal-code")))

    continue_price = driver.find_element(
        By.CSS_SELECTOR, "#continue")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#continue"))
    ).click()

    total_price = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="total-label"]')))

    sum = driver.find_element(
        By.CSS_SELECTOR, '[data-test="total-label"]')
    total_price = sum.text
    assert total_price == 'Total: $58.29'
    
    driver.close()
    
driver.quit()
