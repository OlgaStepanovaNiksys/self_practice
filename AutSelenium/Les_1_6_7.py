import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/find_xpath_form"
browser = None
try:
    browser = webdriver.Chrome()
    time.sleep(20)
    browser.get(link)

   # link1 = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e) * 10000)))
  #  link1.click()
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    #WebDriverWait.until(EC.element_to_be_clickable(button)).click().
    button = browser.find_element(By.XPATH, "//form//button[text()='Submit']")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций

    browser.quit()