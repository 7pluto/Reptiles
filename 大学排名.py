#CrawUnivRankingA.py 
import requests 
from bs4 import BeautifulSoup 
import bs4 
def getHTMLText(url):     
    try:         
        r = requests.get(url, timeout=30)         
        r.raise_for_status()         
        r.encoding = r.apparent_encoding         
        return r.text     
    except:         
        return "" 
    
def fillUnivList(ulist, html):     
    soup = BeautifulSoup(html, "html.parser")     
    for tr in soup.find('tbody').children:
    #soup.find('tbody').children 是<tboy>里的<tr>和其它信息，<tr>中有大学的信息

        if isinstance(tr, bs4.element.Tag):
        #判断是否为<tr>             
            tds = tr('td')             
            ulist.append([tds[0].string, tds[1].string, tds[3].string]) 
                
def printUnivList(ulist, num):     
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校名称","总分"))     
    for i in range(num):         
        u=ulist[i]         
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))

def main():     
    uinfo = []     
    url = 'https://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'     
    html = getHTMLText(url)     
    fillUnivList(uinfo, html)     
    printUnivList(uinfo, 20) # 20 univs 

main()