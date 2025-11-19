from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultPage:

    def __init__(self, browser):
        self.driver = browser

    def add_books(self):
        buy_bottons = self.driver.find_elements(
            By.CSS_SELECTOR, "[data-carttext]")

        counter = 0
        for btn in buy_bottons:
            btn.click()
            counter += 1
        return counter

    def get_empty_result_message(self):
        element = self.driver.find_element(By.CSS_SELECTOR, ".index-top-title")
        full_text = element.text.strip()
        return full_text
