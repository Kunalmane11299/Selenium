import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(3)

driver.find_element(By.LINK_TEXT, "Click Here").click()

windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.XPATH, "//h3").text)

driver.switch_to.window(windowsOpened[0])
print(driver.find_element(By.XPATH, "//h3").text)

time.sleep(3)
