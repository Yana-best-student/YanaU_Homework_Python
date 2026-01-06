import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from CalcPage import CalcPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера
    """
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("CALCULYATOR")
@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет корректную работу калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
def test__submission_flow(driver):
    """
    Проверка работы калькулятора.
    :param driver: webdriver - объект драйвера, переданый фикстурой.
    :param //span[text()='8': str - первое число для операции.
    :param //span[text()='+': str - операция сложения (+).
    :param //span[text()='7': str - второе число для операции,
    :param //span[text()='=': str - знак равенства.
    :param 'div.screen': str строка с текстом элемента 'div.screen.
    """
    calc_page = CalcPage(driver)

    with allure.step(f"Установка задержки {45} секунд"):
        calc_page.enter_delay("45")

    with allure.step("Нажатие кнопок: [8 '+' 7 '=']"):
        calc_page.enter_numbers()

    with allure.step("Проверка результата"):
        result = calc_page.get_result()
        print(result)
        assert result == '15'
