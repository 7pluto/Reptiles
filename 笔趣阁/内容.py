import requests
from bs4 import BeautifulSoup

url = 'https://www.biqugex.com/book_139/24806185.html'
html = requests.get(url)
soup = BeautifulSoup(html.text,'html.parser')
txt = soup.find_all('div',class_ = 'showtxt')[0].text
title = soup.select('div h1')[0].text
print(title)
