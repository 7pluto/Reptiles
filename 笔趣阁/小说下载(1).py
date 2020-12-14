import requests
import re
from bs4 import BeautifulSoup
import time

def getHtmlText(url,req_header):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        str1 = r.text.replace('\ufffd',' ')
        return str1
        return r.text
    except UnicodeEncodeError :
        return " "
    
def parsePage(ilt,html,section_url):
    try:
        title = re.findall(r'<h1>(.*?)</h1>',html)
        text = re.findall(r'<div id="content" class="showtxt">(.*?)</div>',html)
        if text:
            text = text[0].split('<br />')
        
        for i in text:
            if '&nbsp;'  in i:
                i = i.replace('&nbsp;'," ")
            if '天才一秒记住本站地址：www.biqugex.com。笔趣阁手机版阅读网址：m.biqugex.com'  in i:
                i = i.replace('天才一秒记住本站地址：www.biqugex.com。笔趣阁手机版阅读网址：m.biqugex.com'," ")
            if section_url in i:
                i = i.replace(section_url," ")
            ilt.append(i)
        return title,ilt
    except:
        return " "

def searchUrl():
    name = input("请输入书名：")
    find_url = 'https://www.biqugex.com/s.php?ie=gbk&s=9157106854577873494&q=' + name
    html = requests.get(find_url)
    soup = BeautifulSoup(html.text,'html.parser')
    a = soup.find_all('div',class_ = 'bookbox')
    l = len(a)
    for i in range(l):
        b = a[i].div.get_text()
        print(i , ":" ,a[i].h4.string)
        print(b)
    choice = int(input("请输入你的选择："))
    url = a[choice].a.get('href')
    return url

def get_text(title,ilt,fiction):
    print("准备下载中，请稍后...")
    with open (fiction[0] + '.txt','a',encoding = 'utf-8') as f:
        title = ''.join(title)
        f.write(title)
        f.write('\n')
        f.write('\n')
        for i in ilt:
            f.write(i)
        f.write('\n')
        f.write('\n')



def main():
    # 请求字典
    req_header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'__guid=229476762.1831687419270337500.1559012567789.3096; UM_distinctid=16afc63f33631-0496da063cc752-3c604504-1fa400-16afc63f337430; bcolor=; font=; size=; fontcolor=; width=; CNZZDATA1260821856=1968022043-1559010775-%7C1559091853; monitor_count=49',
    'Host':'www.biqugex.com',
    'If-Modified-Since':'Sat, 13 Apr 2019 16:32:25 GMT',
    'If-None-Match':'"1555173145"',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }

    book = searchUrl()
    start_url = 'https://www.biqugex.com' + book
    print(start_url)
    dome = getHtmlText(start_url,req_header)
    url = re.findall(r'<dd><a href \=\"\/(.*?)</a></dd>',dome)
    fiction = re.findall(r'<h2>(.*?)</h2>',dome)
    for i in url:
        time.sleep(1)
        section = i.split('>')[1]
        section_url = 'https://www.biqugex.com/' + i.split('">')[0]
        html = getHtmlText(section_url,req_header)
        
        ilt = []
        title,ilt = parsePage(ilt,html,section_url)
        print(html)

        get_text(title,ilt,fiction)
        print(section + "下载成功") 
        break

main()
