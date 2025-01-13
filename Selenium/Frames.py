import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.switch_to.frame("(//div[@class ='clearfix'])[3]")
time.sleep(2)
# action = ActionChains(driver)
# action.move_to_element(driver.find_element(By.XPATH, "(//li/a[@class ='dropdown-toggle'])[2]")).perform()

driver.find_element(By.LINK_TEXT, "About us").click()

