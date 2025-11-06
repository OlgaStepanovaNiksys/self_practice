from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://suninjuly.github.io/selects1.html")

# Get numbers and compute sum
num_1 = driver.find_element(By.CSS_SELECTOR, "span#num1").text
num_2 = driver.find_element(By.CSS_SELECTOR, "span#num2").text
res = str(int(num_1) + int(num_2))

# Select the option
select = Select(driver.find_element(By.CSS_SELECTOR, "select#dropdown"))
select.select_by_visible_text(res)

# Click submit
submit_b = driver.find_element(By.CSS_SELECTOR, "button")
submit_b.click()

time.sleep(25)
