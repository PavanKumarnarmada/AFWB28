import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#open the chrome browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#enter the URL & wait till the page is loaded
driver.get("file:///C:/Users/pavan.srinivasa/Desktop/element.html")
time.sleep(1)
status=driver.find_element(By.ID,"A6").is_selected()
print(status) #False- check box is not selected
driver.find_element(By.ID,"A6").click()
status=driver.find_element(By.ID,"A6").is_selected()
print(status)#True- check box is selected
time.sleep(1)