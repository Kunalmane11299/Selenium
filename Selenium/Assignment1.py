import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(3)

driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()

openedWindows = driver.window_handles
driver.switch_to.window(openedWindows[1])
# message = driver.find_element(By.CSS_SELECTOR, ".red").text
# var = message.split("at")[1].strip().split(" ")[0] or
mail = (driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com")).text

driver.switch_to.window(openedWindows[0])
driver.find_element(By.ID, "username").send_keys(mail)
driver.find_element(By.ID, "password").send_keys("Kunal2123")
buttons = driver.find_elements(By.XPATH, "(//span[@class= 'checkmark'])[1]")

dropdown = Select(driver.find_element(By.XPATH, "//select[@class= 'form-control']"))
dropdown.select_by_index(1)

driver.find_element(By.XPATH, "//input[@id= 'terms']").click()
driver.find_element(By.XPATH, "//input[@id= 'signInBtn']").click()

wait = (WebDriverWait(driver, 5))
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class= 'alert alert-danger col-md-12']")))
print(driver.find_element(By.XPATH, "//div[@class= 'alert alert-danger col-md-12']").text)

time.sleep(3)