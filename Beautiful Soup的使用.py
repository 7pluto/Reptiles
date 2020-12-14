import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.python123.io./ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
print(soup.prettify())

'''
print(tag)
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>
print(tag.string)
Basic Python
'''

#遍历
'''
#下行
.contents       子节点的列表
.chidren        子节点的迭代
.descendants    子孙节点迭代
#平行
.previous_sibling    文本顺序上一个
.next_sibling        文本顺序下一个
.previous_siblings   文本顺序上一个，迭代
.next_siblings       文本顺序下一个，迭代
#上行
.parent
.parents
soup.title.parent
'''
tag = soup.a
print(tag.contents)
for child in soup.body.children:
    print(child)