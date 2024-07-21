import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'https://www.linkedin.com/login'

E_MAIL = 'tdseny@gmail.com'
PASSWORD = 'd58b470c030cb8d4eb0a0f608bc4f8c0c3af7719'
SEARCH_THEME = 'Technology'

db_name = 'IT_Jobs.db'
csv_path = '/home/setoudie/PycharmProjects/scrapingProject/job_scraping_project/data/raw/Linkedin_IT_jobs.csv'

driver_path = '/usr/local/bin/chromedriver'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

# driver.get('https://google.com')
driver.get(url)

# Enter the login informations
# Get the username input and write here the E_MAIL
username_input = driver.find_element(By.ID, "username")
username_input.send_keys(E_MAIL)

# Get the password input and write here the PASSWORD
password_input = driver.find_element(By.ID, 'password')
password_input.send_keys(PASSWORD + Keys.ENTER)

time.sleep(10)

driver.quit()



