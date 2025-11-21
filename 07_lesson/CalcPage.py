from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def enter_delay(self, delay):
        text_delay = self.driver.find_element(
            By.CSS_SELECTOR, "#delay")
        text_delay.clear()
        text_delay.send_keys()

    def enter_numbers(self):
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()
        WebDriverWait(self.driver, 55).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, 'div.screen'), '15'))

    def get_result(self):
        WebDriverWait(self.driver, 55).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, 'div.screen'), '15'))

        result = self.driver.find_element(By.CSS_SELECTOR, 'div.screen').text
        return result
