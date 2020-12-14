import urllib2,re
import MySQLdb

class Sql(object):
    conn = MySQLdb.connect(host='192.168.19.213',port=3306,user='root',passwd='Admin123',db='novel',charset='utf8')
    def addnovels(self,sort,novelname):
        cur = self.conn.cursor()
        cur.execute("insert into novel(sort,novelname) values(%s , '%s')" %(sort,novelname))
        lastrowid = cur.lastrowid
        cur.close()
        self.conn.commit()
        return lastrowid
    def addchapters(self,novelid,chaptername,content):
        cur = self.conn.cursor()
        cur.execute("insert into chapter(novelid,chaptername,content) values(%s , '%s' ,'%s')" %(novelid,chaptername,content))
        cur.close()
        self.conn.commit()


domain = 'http://www.quanshu.net'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

def getTypeList(pn=1): #获取分类列表的函数
    req = urllib2.Request('http://www.quanshu.net/map/%s.html' % pn) #实例将要请求的对象
    req.headers = headers  #替换所有头信息
    #req.add_header() #添加单个头信息
    res = urllib2.urlopen(req)   #开始请求
    html = res.read().decode('gbk')  #decode解码，解码成Unicode
    reg = r'<a href="(/book/.*?)" target="_blank">(.*?)</a>'
    reg = re.compile(reg) #增加匹配效率  正则匹配返回的类型为List

    return re.findall(reg,html)

def getNovelList(url):  #获取章节列表函数
    req = urllib2.Request(domain + url)
    req.headers = headers
    res = urllib2.urlopen(req)
    html = res.read().decode('gbk')
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    reg = re.compile(reg)
    return re.findall(reg,html)

def getNovelContent(url):  #获取章节内容
    req = urllib2.Request(domain + url)
    req.headers = headers
    res = urllib2.urlopen(req)
    html = res.read().decode('gbk')
    reg = r'style5\(\);</script>(.*?)<script type="text/javascript">style6\(\)'
    return re.findall(reg,html)[0]

mysql = Sql()
if __name__ == '__main__':
    for sort in range(1,10):
        for url,title in getTypeList(sort):
            lastrowid = mysql.addnovels(sort, title)
            for zurl,ztitle in getNovelList(url):
                print u'正则爬取----%s' %ztitle
                content = getNovelContent(url.replace('index.html',zurl))
                print u'正在存储----%s' %ztitle
                mysql.addchapters(lastrowid,ztitle,content)
