from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'https://www.linkedin.com/jobs/search/?keywords=technology'
db_name = 'IT_Jobs.db'
csv_path = '/home/setoudie/PycharmProjects/scrapingProject/job_scraping_project/data/raw/Linkedin_IT_jobs.csv'


