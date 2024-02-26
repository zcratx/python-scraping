from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
print("Driver is installed at : ",driver.service.path)
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(5)
print(driver.page_source)
driver.close()