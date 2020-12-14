import requests
from bs4 import BeautifulSoup
import time
import re
import pymysql

#发出请求，并返回
def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        str1 = r.text.replace('\ufffd',' ')
        return str1
        return r.text
    except UnicodeEncodeError :
        return " "

#搜索 输入书名，得到搜索结果，再次选择书籍，返回地址和书名
def search_book():
    name = input("请输入书名：")
    find_url = 'https://www.biqugex.com/s.php?ie=gbk&s=9157106854577873494&q=' + name
    html = getHtmlText(find_url)
    soup = BeautifulSoup(html,'html.parser')
    a = soup.find_all('div',class_ = 'bookbox')
    print("搜索结果：")
    for i in range(len(a)):
        b = a[i].div.get_text()
        print(i , ":" ,a[i].h4.string)
        print("详细信息：")
        print(b)
    choice = int(input("请输入你要下载的小说(数字序号)："))
    print("准备下载中，请稍后...")
    url = a[choice].a.get('href')
    real_name = a[choice].h4.string
    return url,real_name

#接收小说的地址，返回小说各章节标题和地址列表
def search_catalogu(book_url):
    #接收小说的地址
    url  = 'https://www.biqugex.com/' + book_url
    html = requests.get(url)
    soup = BeautifulSoup(html.text,'html.parser')
    a = soup.select(' div dl dd a')
    #章节地址列表
    catalogu_link = []
    #章节标题列表
    catalogu = []
    #statr = input("开始下载章节：")
    #end = input("结束下载章节：")
    #删除重复的最新章节
    statr = 6
    end = len(a)
    for i in range(statr,end):
        catalogu_link.append(a[i].get('href'))
        catalogu.append(a[i].text)
    return catalogu_link,catalogu

#接收小说各章节的地址，返回小说内容列表
def novel_content(ilt,html,section_url):
    try:
        #正则表达式获取信息，得到列表
        title = re.findall(r'<h1>(.*?)</h1>',html)
        text = re.findall(r'<div id="content" class="showtxt">(.*?)</div>',html)
        #切割，得到想要的内容
        if text:
            text = text[0].split('<br />')
        #去除无用广告
        for i in text:
            if '&nbsp;'  in i:
                i = i.replace('&nbsp;'," ")
            if '天才一秒记住本站地址：www.biqugex.com。笔趣阁手机版阅读网址：m.biqugex.com'  in i:
                i = i.replace('天才一秒记住本站地址：www.biqugex.com。笔趣阁手机版阅读网址：m.biqugex.com'," ")
            if section_url in i:
                i = i.replace(section_url," ")
            #存入列表返回
            ilt.append(i)
        return title,ilt
    except:
        return " "

'''
#写入文件
def get_text(title,text,txt_name):
    with open (txt_name + '.txt','a',encoding = 'utf-8') as f:
        #写入文件格式为字符串
        title = ''.join(title)
        f.write(title)
        f.write('\n')
        f.write('\n')
        for i in text:
            f.write(i)
        f.write('\n')
        f.write('\n')
        print(title + " 下载成功!!")
'''

#写进数据库
class SqlOperate():
    def __init__(self,host,user,passwd,dbName):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbName = dbName

    def connect(self):
        self.db = pymysql.connect(self.host,self.user,self.passwd,self.dbName)
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def insert(self,sql):
        return self._edit(sql)
    def update(self,sql):
        return self._edit(sql)
    def delete(self,sql):
        return self._edit(sql)

    def _edit(self,sql):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
            print("提交成功")
        except:
            print("事物提交错误")
    

def main():
    book_url,book_name = search_book()
    catalogu_link,catalogu = search_catalogu(book_url)
    content = ""
    temp = ""
    l = " "
    for i in catalogu_link:
        url = 'https://www.biqugex.com' + i
        html = getHtmlText(url)
        ilt = []
        title,ilt = novel_content(ilt,html,url)

        content = ''.join(ilt)

        ##print(type(ilt))
        #print(type(content))

        s = SqlOperate("localhost","root","0710","chen")
        #res = s.insert("insert into novel value(%s,'%s')"%(0,book_name))
 
        #res1 = s.insert("insert into chapter value(%s,'%s','%s')"%(0,title[0],content))

        #延时，模拟人的行为
        time.sleep(1)
        break


main()