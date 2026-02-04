#QUESTION 8
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Data_science'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

content_area = soup.find('div', id='mw-content-text')

exclude_list = ["References", "External links", "See also", "Notes"]
headings = []

if content_area:
    for h2 in content_area.find_all('h2'):
        text = h2.get_text().replace('[edit]', '').strip()

        if not any(exclude in text for exclude in exclude_list) and text:
            headings.append(text)

    with open('headings.txt', 'w', encoding='utf-8') as file:
        for heading in headings:
            file.write(heading + '\n')

    print("Success! headings.txt has been created.")
