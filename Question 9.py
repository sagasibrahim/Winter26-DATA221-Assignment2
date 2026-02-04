#QUESTION 9
import requests
from bs4 import BeautifulSoup
import csv
url = 'https://en.wikipedia.org/wiki/Machine_learning'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

content_area = soup.find('div', id='mw-content-text')
target_table = None

if content_area:
    tables = content_area.find_all('table')

    for table in tables:
        rows = table.find_all('tr')
        if len(rows) >= 4:
            target_table = table
            break
if target_table:
    all_data = []
    rows = target_table.find_all('tr')
    header_row = rows[0]
    th_tags = header_row.find_all('th')
    if th_tags:
        headers = [th.get_text().strip() for th in th_tags]
    else:
        first_data_row = rows[1].find_all(['td', 'th'])
        headers = [f"col{i + 1}" for i in range(len(first_data_row))]

    num_columns = len(headers)
    for row in rows[1:]:
        cols = row.find_all(['td', 'th'])
        data = [col.get_text().strip() for col in cols]
        while len(data) < num_columns:
            data.append("")
        data = data[:num_columns]

        if data:
            all_data.append(data)
    with open('wiki_table.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(all_data)
    print("Success! wiki_table.csv has been created.")
else:
    print("Could not find a table with at least 3 data rows.")