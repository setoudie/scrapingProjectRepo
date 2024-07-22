import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'https://www.glassdoor.com/index.htm'
monster_link = "https://identity.monster.com"
E_MAIL = 'tdseny@gmail.com'
PASSWORD = 'd58b470c030cb8d4eb0a0f608bc4f8c0c3af7719#' # only monster website password has '#'
SEARCH_THEME = 'Technology'

db_name = 'IT_Jobs.db'
csv_path = '/home/setoudie/PycharmProjects/scrapingProject/job_scraping_project/data/raw/Linkedin_IT_jobs.csv'

driver_path = '/usr/local/bin/chromedriver'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

# driver.get('https://google.com')
driver.maximize_window()
driver.get(monster_link)
time.sleep(5)
# Get the "Log In" btn and click it
log_in_btn = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Log in"))
)
log_in_btn.click()

# Enter the login informations
# Get the username input and write here the E_MAIL
username_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "email"))
)
username_input.send_keys(E_MAIL)
time.sleep(3)
username_input.send_keys(Keys.ENTER)
# time.sleep(5)

# Get the password input and write here the PASSWORD
password_input = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "password"))
)
password_input.send_keys(PASSWORD)
time.sleep(5)
password_input.send_keys(Keys.ENTER)

time.sleep(60)

driver.quit()