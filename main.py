import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

page = requests.get(url, allow_redirects=True)

print(page.title)