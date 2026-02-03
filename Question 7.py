# QUESTION 7
import requests
from bs4 import BeautifulSoup

# 1. Fetch the wiki page
url = "https://en.wikipedia.org/wiki/Data_science"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

# 2. Parse the html content
soup = BeautifulSoup(response.text, 'html.parser')

# 3. Extract and print page title
page_title = soup.title.string
print(f"Page Title: {soup.title.string}")
print("-" * 30)

# 4. Find the main content div
content_div = soup.find('div', id='mw-content-text')

# 5. Extract the first valid paragraph (at leat 50 characters)
paragraphs = content_div.find_all('p')

for p in paragraphs:
    text = p.get_text().strip()
    if len(text) >= 50:
        print("First Main Paragraph:")
        print(text)
        break # Stop after finding the first one