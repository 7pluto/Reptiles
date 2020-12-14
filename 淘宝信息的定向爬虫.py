import requests
import re

def getHtmlText(url):
    try:
        r = requests.get(url,params=req_header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return " "

def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"reservePrice\"\:\".*?\"',html)
        tlt = re.findall(r'\"title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print(" ")

def printGoodList(ilt):
    tplt = "{:4}\t{:8}\t{:16}\t"
    count = 0
    for j in ilt:
        count += 1
        print(tplt.format(count,g[0],g[1]))


def main():
    start_url = 'https://s.taobao.com/search?q=手机'
    infolList = []
    html = getHtmlText(start_url)
    parsePage(infolList,html)
    printGoodList(infolList)

main()
