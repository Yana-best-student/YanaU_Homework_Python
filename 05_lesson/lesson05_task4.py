from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")

username_input = driver.find_element(By.CSS_SELECTOR, "#username")
username_input.send_keys("tomsmith")
password_input = driver.find_element(By.CSS_SELECTOR, "#password")
password_input.send_keys("SuperSecretPassword!")
login_button = driver.find_element(
    By.XPATH, "//button[@class='radius']").click()
message = driver.find_element(By.ID, "flash").text
print(message.split("\n")[0].strip())
driver.quit()
