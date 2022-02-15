from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#downloading driver executable and opening the chrome browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#enter the url ,send request and 'get; the response - home page
driver.get("http://www.fb.com")
#get the current title of the page
print(driver.title)
#get the current url of the page
print(driver.current_url)
#get the html code of the webpage
print(driver.page_source)