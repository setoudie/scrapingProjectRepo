import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.emploisenegal.com/recherche-jobs-senegal/it?f%5B0%5D=im_field_offre_metiers%3A31&f%5B1%5D=im_field_offre_metiers%3A35&f%5B2%5D=im_field_offre_metiers%3A39'
db_name = 'IT_Jobs.db'
table_name = 'EmploisSenegal_IT_jobs'
csv_path = '/home/setoudie/PycharmProjects/scrapingProject/job_scraping_project/data/raw/EmploisSenegal_IT_jobs.csv'

rows = []  # This is all dataFrame row
# row = [job_title_name, company_name, job_description, job_contract_type, job_skils]

cols_name = ['Title', 'Company', 'Description', 'ContractType', 'Skills']
# Ajouter un User-Agent à la requête HTTP

response = requests.get(url)

# Vérifier si la requête HTTP a réussi
if response.status_code == 200:
    html_page = response.text
    soupe = BeautifulSoup(html_page, 'html.parser')

    # Detail du poste
    job_card_detail = soupe.find_all('div', class_="card-job-detail")

    for i in range(len(job_card_detail)):
        # Recupoeration du titre du job
        job_title_detail = job_card_detail[i].find_all('h3')  # cptr i
        job_title = job_title_detail[0].find_all('a')
        job_title_name = job_title[0].contents[0]

        # Recuperation du nom de la compagnie
        company_detail = job_card_detail[i].find_all('a', class_="card-job-company company-name")  # cptr i
        company_name = company_detail[0].contents[0]

        # Recuperation de la description du poste
        job_desc_detail = job_card_detail[i].find_all('p')  # cptr i
        job_description = job_desc_detail[0].contents[0]

        # Recuperation du type de contrat
        job_contract_detail = job_card_detail[i].find_all('li')[2]  # le type est dans le <li> 3
        job_contract_type = job_contract_detail.find_all('strong')[0].contents[0]

        # Recuperation des skils
        job_skils_detail = job_card_detail[i].find_all('li')[-1]  # the last li tag contient les skils
        job_skils = job_skils_detail.find_all('strong')[0].contents[0]

        # contenu de la ligne i
        row = [job_title_name, company_name, job_description, job_contract_type, job_skils]
        rows.append(row)
        # print(row)
        row = []  # init row content

else:
    print(f"Erreur lors de la requête HTTP : {response.status_code}")

df = pd.DataFrame(data=rows, columns=cols_name)
csv_file = df.to_csv(csv_path)

print(df[['Title', 'Skills']].head(6))