import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(4)
driver.get("https://www.istqb.org/")
menu=driver.find_element(By.XPATH,"(//a[text()='About us '])[2]")