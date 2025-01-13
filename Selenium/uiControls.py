import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
#
# for checkbox in checkboxes:
#     if checkbox.get_attribute("value") == "option2":
#         checkbox.click()
#         break


#Radio button code -
radios = driver.find_elements(By.XPATH, "//input[@name='radioButton']")
for radio in radios:
    if radio.get_attribute("value") == "radio2":
        radio.click()
        break

assert driver.find_element(By.ID, "displayed-text").is_displayed()
time.sleep(20)

driver.find_element(By.ID, "hide-textbox").click()

assert not driver.find_element(By.ID, "displayed-text").is_displayed()

time.sleep(5)
