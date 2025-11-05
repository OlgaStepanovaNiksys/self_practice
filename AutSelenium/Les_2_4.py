from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import math

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("http://suninjuly.github.io/explicit_wait2.html")
wait = WebDriverWait(driver, 12)
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), "100"))
book_button=driver.find_element(By.ID, "book")
book_button.click()

input=driver.find_element(By.CSS_SELECTOR, "input#answer")
x = int(driver.find_element(By.ID, "input_value").text)
print(x)
math_form = math.log(abs(12 * math.sin(x)))
print(math_form)
input.send_keys(math_form)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

alert= driver.switch_to.alert
print(alert.text)
driver.quit()