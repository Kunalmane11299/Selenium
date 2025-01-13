import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
#adding implicit wait so it will wait max of 5 sec and if page is loaded it will not wait and will proceed
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
driver.find_element(By.XPATH, "//button[@class = 'search-button']").click()
time.sleep(2)
listofveg = driver.find_elements(By.XPATH, "//div[@class='products']/div/h4")
print("Searched Veg :")
printedList = []
for veg in listofveg:
    printedList.append(veg.text)
    print(veg.text)

OrgList = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
assert printedList == OrgList


results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
assert len(results) > 0
#chaining for Add to Cart button
for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

values = driver.find_elements(By.XPATH, "//td[5]/p")
sum = 0
for value in values:
    sum = sum + int(value.text)
print(sum)

value2 = int(driver.find_element(By.XPATH, "//span[@class='totAmt']").text)
assert sum == value2

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

wait = (WebDriverWait(driver,10))
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))
print(driver.find_element(By.XPATH, "//span[@class='promoInfo']").text)

Discount = float(driver.find_element(By.XPATH, "//span[@class='discountAmt']").text)
assert Discount < value2

time.sleep(5)
