import requests
import re
from bs4 import BeautifulSoup


name = input("请输入书名：")
find_url = 'https://www.biqugex.com/s.php?ie=gbk&s=9157106854577873494&q=' + name
html = requests.get(find_url)
soup = BeautifulSoup(html.text,'html.parser')
a = soup.find_all('div',class_ = 'bookbox')
b = a[0].a.text


l = len(a)
print(l)
for i in range(l):
    b = a[i].div.get_text()
    print(i , ":" ,a[i].h4.string)
    print(b)
choice = int(input("请输入你的选择："))
url = a[choice].a.get('href')
print(url)

