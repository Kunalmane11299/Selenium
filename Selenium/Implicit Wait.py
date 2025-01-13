import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
#adding implicit wait so it will wait max of 5 sec and if page is loaded it will not wait and will proceed
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
driver.find_element(By.XPATH, "//button[@class = 'search-button']").click()
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
assert len(results) > 0
#chaining for Add to Cart button
for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

print(driver.find_element(By.XPATH, "//span[@class='promoInfo']").text)


time.sleep(5)
