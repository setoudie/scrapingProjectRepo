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

# Website to scrap
glassdoor_link = 'https://www.glassdoor.com/index.htm'
monster_link = "https://identity.monster.com"
linkedin_url = "https://www.linkedin.com/checkpoint/lg/sign-in-another-account"

# Login information
E_MAIL = 'tdseny@gmail.com'
PASSWORD = 'd58b470c030cb8d4eb0a0f608bc4f8c0c3af7719'  # only monster website password has '#'
SEARCH_THEME = 'Technology'
LOCALITY = "Senegal"

db_name = 'IT_Jobs.db'
csv_path = '/home/setoudie/PycharmProjects/scrapingProject/job_scraping_project/data/raw/Linkedin_IT_jobs.csv'

driver_path = '/usr/local/bin/chromedriver'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

# driver.get('https://google.com')
driver.maximize_window()
driver.get(linkedin_url)


def get_number_of_jobs_in_page(ul_xpath, web_driver):
    WebDriverWait(web_driver, 5).until(
        EC.presence_of_element_located((By.XPATH, ul_xpath))
    )

    ul_page = driver.page_source
    soupe = BeautifulSoup(ul_page, 'html.parser')
    ul_jobs_soup = soupe.find_all('div', class_="flex-grow-1 artdeco-entity-lockup__content ember-view")
    print(ul_jobs_soup)
    print(len(ul_jobs_soup))


# Put the username value : the e-mail
"""
    1. Get the mail input 
    2. wait 3 sec and put it the correct username value
"""
username_input = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, "username"))
)
username_input.send_keys(E_MAIL)
time.sleep(3)

# Put the password value : PASSWORD
"""
    1. Get the password input 
    2. wait 3 sec and put it the correct password value
"""
password_input = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, "password"))
)
password_input.send_keys(PASSWORD)
time.sleep(3)
password_input.send_keys(Keys.ENTER)

# Detect the search box input
"""
    1. After successfully login in wait 10 sec
    2. Get the input search box by XPATH
    3. Put in the SEARCH_THEME and Enter
"""
search_box_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id=\"global-nav-typeahead\"]/input"))
)
search_box_input.send_keys(SEARCH_THEME, Keys.ENTER)

# Click on employs results search
employs_btn = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id=\"search-reusables__filters-bar\"]/ul/li[1]/button"))
)
employs_btn.click()
time.sleep(12)
get_number_of_jobs_in_page("//*[@id=\"main\"]/div/div[2]/div[1]/div/ul", driver)
time.sleep(190)
