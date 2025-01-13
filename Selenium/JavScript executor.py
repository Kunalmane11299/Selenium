import time

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(3)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

time.sleep(3)