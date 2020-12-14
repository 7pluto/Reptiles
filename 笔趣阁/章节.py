import requests
from bs4 import BeautifulSoup

url = 'https://www.biqugex.com/book_139/'
html = requests.get(url)
soup = BeautifulSoup(html.text,'html.parser')
#print(type(soup))
a = soup.select(' div dl dd a')
#print(type(a))
l = len(a)
list1 = []
list2 = []
for i in range(l):
    if i <6:
        continue
    list1.append(a[i].get('href'))
    list2.append(a[i].text)
print(list1)
print(list2)
