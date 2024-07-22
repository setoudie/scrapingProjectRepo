import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import requests
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://www.indeed.com/?from=jobsearch-empty-whatwhere'

SEARCH_THEME = 'Technology'
LOCALITY = 'Senegal'

driver = webdriver.Chrome()
driver.get(url)

search_box_input = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "text-input-what"))
)
search_box_input.send_keys(SEARCH_THEME + Keys.ENTER)
locality_box_input = driver.find_element(By.ID, "text-input-where")
locality_box_input.send_keys(LOCALITY + Keys.ENTER)

job_search_page = driver.page_source
soupe = BeautifulSoup(job_search_page, 'html.parser')

print(soupe)
time.sleep(5)
