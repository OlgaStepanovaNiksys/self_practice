from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import math

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://suninjuly.github.io/redirect_accept.html")
button=driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
button.click()
new_window=driver.window_handles[1]
driver.switch_to.window(new_window)
expected_url = "http://suninjuly.github.io/redirect_page.html?"
current_url = driver.current_url
print(current_url)
assert current_url==expected_url
input=driver.find_element(By.CSS_SELECTOR, "input#answer")
x = int(driver.find_element(By.CSS_SELECTOR, "span#input_value").text)
print(x)
math_form = math.log(abs(12 * math.sin(x)))
print(math_form)
input.send_keys(math_form)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
alert= driver.switch_to.alert
print(alert.text)
driver.quit()
