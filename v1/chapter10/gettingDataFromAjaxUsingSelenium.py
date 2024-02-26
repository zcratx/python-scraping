from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(
    service=Service("/Users/nkamat/.wdm/drivers/chromedriver/mac64/121.0.6167.184/chromedriver-mac-arm64/chromedriver"),
    options=chrome_options
)
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3)
print(driver.find_element(By.ID, 'content').text)
driver.close()