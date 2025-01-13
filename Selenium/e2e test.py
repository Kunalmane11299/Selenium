from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//a[contains(@href, 'shop')]").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products :
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry" :
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, " //a[contains(@class, 'nav-link btn btn-primary')]").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()
