import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from FormObject import PageObject


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


@allure.feature("FORM")
@allure.title("Тестирование формы регистрации на ошибку")
@allure.description("Тест проверяет возникновение "
                    "ошибки при не корректном заполнении формы,"
                    " не заполненое поле подсвечивается красным цветом")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission_flow(driver):
    """
    Проверка работы формы регистрации.
    :param driver: webdriver - объект драйвера, переданый фикстурой.
    :param fields: dict - словарь с данными для заполнения формы,
    где ключи — названия полей, а значения — данные для ввода.

    """
    with allure.step("Открытие страницы с формой для заполнения данными"):
        page_object = PageObject(driver)

    with allure.step("Открытие страницы с формой для заполнения"):
        page_object.open()

    with allure.step("Заполнение формы данными"):
        page_object.fill_form()

    with allure.step("Нажатие на кнопку 'Submit'"):
        page_object.submit_form()

    with allure.step("Проверка результата: возвращает ошибку"
                     " при незаполненом поле, поле подсвечено красным"):
        page_object.check_form_submission()
