from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
from math import log, sin
import os

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://suninjuly.github.io/file_input.html")
name_field=driver.find_element(By.NAME, "firstname")
name_field.send_keys("Olga")
surname_field=driver.find_element(By.NAME, "lastname")
surname_field.send_keys("Step")
mail_field=driver.find_element(By.NAME, "email")
mail_field.send_keys("alz@gmail.com")

file_attach=driver.find_element(By.ID, "file")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'Olga Stepanova Cover letter, Paintgun.pdf')
#file_path = r"D:\Testing - learning\резюме\Olga Stepanova Cover letter, Paintgun.txt"
file_attach.send_keys(file_path)

driver.find_element(By.CSS_SELECTOR, "button.btn").click()
time.sleep(10)