import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from CalcPage import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test__submission_flow(driver):
    calc_page = CalcPage(driver)
    calc_page.enter_delay("45")
    calc_page.enter_numbers()
    result = calc_page.get_result()
    print(result)
    assert result == '15'
