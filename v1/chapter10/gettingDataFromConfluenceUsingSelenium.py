from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import base64
import random

chrome_options = Options()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(
    service=Service("/Users/nkamat/.wdm/drivers/chromedriver/mac64/121.0.6167.184/chromedriver-mac-arm64/chromedriver"),
    options=chrome_options
)
# driver.get('https://pp.seismic.com/app#/doccenter/1f0a02a2-5310-4f1b-9158-63c37ab99370/doc/%252Flfc3b4fc0c-8209-40e5-ac8b-dec6e56f4666//?mode=view&parentPath=sessionStorage')

# driver.get("https://auth.seismic.com/tenants/pp/connect/authorize?client_id=0188a34d-cdbd-4208-8ebc-d0567984915e&response_type=id_token token&scope=openid id library download reporting engagement_read engagement_write upload external_authorization buyer_experience_service_read buyer_experience_service_write feature_read collection_read collection_write contentdiscovery doccenter_backend_read doccenter_backend_write contenttemplate livedoc livedoc_express wms_readwrite feature_tier_read guided_assembly ums_bulk_management ums_bff_read ums_bff_readwrite das_schema_ro das_data_rw email profile contentmanager_bff pnsbff_readwrite ext_meetings_read ext_meetings_write seismic.custom_schema.view seismic.custom_schema.manage entitlement_read entitlement_readwrite meeting_analytics_read aiml_llm learning&state=c75312b3f860c8058a552bccde1d7826&redirect_uri=https%3a%2f%2fpp.seismic.com%2fapp&response_mode=form_post&nonce=d685b8c826a6b804b4b8fc318e83e318")

#driver.get("https://paypal.atlassian.net/wiki/spaces/Crawler/pages/346130752/Getting+Started")
driver.get("https://paypal.atlassian.net/wiki/spaces/PSIntheKnow/pages/458919817/GPS+In+the+Know+20220803+-+Removal+of+0+Item+Validation")
# This ensures the page opened is a full screen window

time.sleep(60)
try:

    #element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "css-rplcu4 e5xcnr80")))
    element = WebDriverWait(driver, 30)
finally:
    # print("The credentials are ", driver.get_credentials())

    # print("The downloadable files are ", driver.get_downloadable_files())

    random_prefix = random.random().__str__()

    driver.fullscreen_window()
    pageSource = driver.page_source
    fileScraped = open("Confluence_"+random_prefix+".html", "w")
    fileScraped.write(pageSource)
    fileScraped.close()

    # base64Page = driver.get_screenshot_as_base64()
    #
    # fileScraped = open("MyFileConfluence.png", "wb")
    # fileScraped.write(base64.b64decode(base64Page))
    # fileScraped.close()
    #
    # driver.get_screenshot_as_file('Trial1Confluence.png')
    #
    # fileInBytes = driver.get_screenshot_as_png()
    # fileScraped = open("MyFile1Confluence.png", "wb")
    # fileScraped.write(fileInBytes)
    # fileScraped.close()
    # print(driver.find_element(By.ID, 'PSPDFKit-2z5hjphww7fvh1z69wxptsw1b9').text)

    # print("The important thing from driver.get_log('performance')", driver.get_log('performance'))
    driver.close()
