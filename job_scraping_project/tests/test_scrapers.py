import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = '/home/setoudie/PycharmProjects/scrapingProject/job_scraping_project/data/raw/Top_50_movies.csv'
datas = []

html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

tables = data.find_all('tbody')

rows = tables[0].find_all('tr')
# print(len(rows))
# print(rows[0])

# Recuperation de l'entete
header = rows[0].find_all('th')
header_cols = [header[i].contents[0] for i in range(len(header))]
# print(header_cols)

for row in rows[1:]:
    col = row.find_all('td')
    # print(col)
    row_content = [col[i].contents[0] for i in range(len(col))]
    datas.append(row_content)
    # print(data)

# Create the dataFrame
df = pd.DataFrame(data=datas, columns=header_cols)
# Supprimer les caractères de nouvelle ligne dans les colonnes
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

df.to_csv(csv_path)
print(df)
