import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# opening the chrome browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#goto google.com
driver.get("http://www.google.com")
time.sleep(2)
#goto fb.com
driver.get("http://www.fb.com")
time.sleep(2)
#click back: from fb.com -> google.com
driver.back()
time.sleep(2)
#click forward : from google.com -> fb.com
driver.forward()
time.sleep(2)
#refresh the page: reload fb.com
driver.refresh()
time.sleep(2)