import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
webVeggieList = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[text() = 'Veg/fruit name']").click()
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    webVeggieList.append(ele.text)

OrgSortedList = webVeggieList.copy()

webVeggieList.sort()

assert webVeggieList == OrgSortedList

time.sleep(3)
