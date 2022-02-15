from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options,service=Service(ChromeDriverManager().install()))
driver.get("http://www.google.com")