from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService

service = EdgeService(
    executable_path='C:/Users/yan16/Downloads/edgedriver_win64/msedgedriver.exe')
driver = webdriver.Edge(service=service)


def test_data_types():
    service = EdgeService(
        executable_path='C:/Users/yan16/Downloads/edgedriver_win64/msedgedriver.exe')
    driver = webdriver.Edge(service=service)

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.implicitly_wait(10)

    first_name = driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.CSS_SELECTOR, "[name='last-name']")
    last_name.send_keys("Петров")

    address = driver.find_element(By.CSS_SELECTOR, "[name='address']")
    address.send_keys("Ленина, 55-3")

    city = driver.find_element(By.CSS_SELECTOR, "[name='city']")
    city.send_keys("Москва")

    country = driver.find_element(By.CSS_SELECTOR, "[name='country']")
    country.send_keys("Россия")

    email = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']")
    email.send_keys("test@skypro.com")

    phone_number = driver.find_element(By.CSS_SELECTOR, "[name='phone']")
    phone_number.send_keys("+7985899998787")

    job_position = driver.find_element(
        By.CSS_SELECTOR, "[name='job-position']")
    job_position.send_keys("QA")

    company = driver.find_element(By.CSS_SELECTOR, "[name='company']")
    company.send_keys("QA")

    last = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[name='company']"))
    )

    button = driver.find_element(
        By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3")

    WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3"))
    ).click()

    zip_code = driver.find_element(
        By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
    assert zip_code == 'rgba(248, 215, 218, 1)'

    fields = ["first-name", "last-name", "address", "city",
              "country", "e-mail", "phone", "job-position", "company"]

    for field in fields:
        color = driver.find_element(
            By.XPATH, "//div[contains(@class, 'alert py-2 alert-success')]").value_of_css_property("background-color")
    assert color == 'rgba(209, 231, 221, 1)'


driver.quit()
