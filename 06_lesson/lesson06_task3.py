from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

last = WebDriverWait(driver, 20)
last.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#landscape"))
)
img_award = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#award"))
)
src_value = img_award.get_attribute("src")
print(src_value)
driver.close()

driver.quit()
