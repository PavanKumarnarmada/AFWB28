from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#driver = webdriver.Chrome("./../driver/chromedriver.exe")

driver = webdriver.Chrome (service=Service ("./../driver/chromedriver.exe"))
driver.get("http://www.google.com")
driver.close()