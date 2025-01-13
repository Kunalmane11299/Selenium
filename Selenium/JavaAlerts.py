import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Kunal")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
time.sleep(5)
assert "Kunal" in alertText
alert.accept()


time.sleep(5)
