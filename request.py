import requests
url = "http://item.jd.com/2967929.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding
except:
    print("爬取失败")
r.text[0:1000]