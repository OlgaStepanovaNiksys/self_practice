from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
from math import log, sin

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://suninjuly.github.io/execute_script.html")
num=driver.find_element(By.CSS_SELECTOR, "span#input_value").text
f = str(log(abs(12 * sin(int(num)))))
answ_field=driver.find_element(By.CSS_SELECTOR,"input#answer")
driver.execute_script("arguments[0].scrollIntoView();",answ_field)
answ_field.send_keys(f)
checkbox=driver.find_element(By.CSS_SELECTOR,"input#robotCheckbox")
checkbox.click()
radio_b=driver.find_element(By.CSS_SELECTOR, "input#robotsRule")
radio_b.click()
driver.find_element(By.CSS_SELECTOR, "button").click()
time.sleep(10)

