import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.actitime.com/login.do")
driver.find_element(By.ID,'username').send_keys("admin")
driver.find_element()
time.sleep(2)