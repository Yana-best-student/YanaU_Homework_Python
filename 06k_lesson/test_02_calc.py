from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc_types():

    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    text_delay = driver.find_element(By.CSS_SELECTOR, "#delay")
    text_delay.clear()
    text_delay.send_keys("45")

    text_delay = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
    )

    driver.find_element(By.XPATH, "//span[text()='8']").click()

    driver.find_element(By.XPATH, "//span[text()='+']").click()

    driver.find_element(By.XPATH, "//span[text()='7']").click()

    driver.find_element(By.XPATH, "//span[text()='=']").click()

    WebDriverWait(driver, 55).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, 'div.screen'), '15'))
    result = driver.find_element(By.CSS_SELECTOR, 'div.screen').text
    print(result)
    assert result == '15'

    driver.quit()
