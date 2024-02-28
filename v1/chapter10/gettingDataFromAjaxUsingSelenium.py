from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

chrome_options = Options()
#chrome_options.add_argument("--headless")

driver = webdriver.Chrome(
    service=Service("/Users/nkamat/.wdm/drivers/chromedriver/mac64/121.0.6167.184/chromedriver-mac-arm64/chromedriver"),
    options=chrome_options
)
driver.get('https://pp.seismic.com/app#/doccenter/1f0a02a2-5310-4f1b-9158-63c37ab99370/doc/%252Fdd13fccb49-338b-6351-5930-35ff01be09bc%252Flfdb61b6f0-1c36-445d-8453-0e16a7e39b6b//?mode=view&parentPath=sessionStorage')
time.sleep(60)
try:

    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located(By.CLASS_NAME, 'seismic-next-ui ng-scope'))

finally:
    print(driver.find_element(By.CLASS_NAME, 'seismic-next-ui ng-scope').text)

    #print("The important thing from driver.get_log('performance')", driver.get_log('performance'))

    driver.close()