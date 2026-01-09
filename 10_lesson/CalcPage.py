import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    def __init__(self, driver):
        """
        Конструктор класса CalcPage.

        :param driver: Webdriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        """
        Открывает страницу "slow-calculator.html" в браузере,
        использует driver.get для открытия страницы
        """

    @allure.step("Установка задержки {delay} секунд")
    def enter_delay(self, delay: int) -> None:
        """
        Устанавливает задержку перед выполнением операций на калькуляторе.

        :param delay: количество секунд задержки
        :type delay: int
        :return: None
        """
        text_delay = self.driver.find_element(
            By.CSS_SELECTOR, "#delay")
        text_delay.clear()
        text_delay.send_keys()

    @allure.step("Нажатие кнопок: 8 + 7 =")
    def enter_numbers(self):
        """
        Находит и кликает по кнопке с указанным текстом
        :param span[text(): int текст на кнопке, которую нужно нажать.
        """
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()
        WebDriverWait(self.driver, 55).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, 'div.screen'), '15'))
        """
        Ожидает появления текста '15' в элементе с селектором 'div.screen'.
        """
    @allure.step("Проверка, результат сложения равен 15")
    def get_result(self):
        """
        Устанавливает задержку 55 секунд перед
        появления текста '15' в элементе с селектором 'div.screen'.
        :param 55: количество секунд задержки
        """
        WebDriverWait(self.driver, 55).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, 'div.screen'), '15'))
        """
        :return: str метод возвращает строку с текстом элемента 'div.screen'.
        """

        result = self.driver.find_element(By.CSS_SELECTOR, 'div.screen').text
        return result
