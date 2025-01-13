import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys("Demo@gmail.com")
driver.find_element(By.XPATH, "//input[@formcontrolname= 'userPassword']").send_keys("12345")
driver.find_element(By.XPATH, "//input[@formcontrolname= 'confirmPassword']").send_keys("12345")
driver.find_element(By.XPATH, "//button[@type= 'submit']").click()



time.sleep(20)
