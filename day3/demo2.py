from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("http://www.google.com")
driver.close()