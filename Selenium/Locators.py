import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

#ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME, "email").send_keys("kunalmane0987@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")

#Dropdown techniques
dropdown = Select(driver.find_element(By.XPATH, "//select[@class= 'form-control']"))
dropdown.select_by_index(0)

driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Kunal")

# Xpath - //tagname[@attribute='value']   e.g. //input[@type='submit']
driver.find_element(By.XPATH, "//input[@value='Submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert").text
print(message)
driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys("Kunal")
assert "Success" in message

time.sleep(10)
