from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import math

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://suninjuly.github.io/alert_accept.html")
button=driver.find_element(By.CSS_SELECTOR, "form button")
#wait.until(EC_element_to_be_visible(button))
button.click()
confirm=driver.switch_to.alert
confirm.accept()
input=driver.find_element(By.CSS_SELECTOR, "input#answer")
x = int(driver.find_element(By.CSS_SELECTOR, "span#input_value").text)
print(x)
math_form = math.log(abs(12 * math.sin(x)))
print(math_form)
input.send_keys(math_form)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(10)
driver.quit()


# Копируем результат. Спасибо за данный фрагмент кода Vitaliy Ya! =)
#    alert = browser.switch_to.alert
#    alert_text = alert.text
#    addToClipBoard = alert_text.split(': ')[-1]
#    pyperclip.copy(addToClipBoard)

#    textarea.send_keys(addToClipBoard)