from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Вывести заголовок страницы
driver.get("https://www.example.com")
print(f'Заголовок страницы: {driver.title}')
driver.quit()

#  Нажатие кнопки Донат на сайте питон
driver.get("https://www.python.org/")
driver.find_element(By.LINK_TEXT, "Donate").click()
driver.quit()

# поиск в Гугл
driver.get("https://www.google.com/")

search_box = driver.find_element(By.NAME, "q")

search_box.send_keys("Selenium", Keys.RETURN)
sleep(15)
driver.quit()
sleep(10)