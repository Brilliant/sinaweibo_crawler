from bs4 import BeautifulSoup
import urllib.parse
import urllib.request

HOST = "http://weibo.cn/"
HEADERS = \
{
    "Host": "weibo.cn", 
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
#    "Accept-Encoding": "gzip, deflate",
    "Cookie": "_T_WM=364045e714b87cd4810745d56710b39a; SUB=_2A254AVxIDeTxGeNP7FER9C7EwziIHXVbCmQArDV6PUNbvtBeLRnQkW1w7MBWmYa7usvRifGaBhPyQGwdfg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5PuzaHsVOSciAkxQSZYYyr5JpX5KMt; SUHB=079jfA46Izzwd7;" 
}

def get(url):
    request = urllib.request.Request(url, headers = HEADERS)
    response = urllib.request.urlopen(request)
    html = response.read()
    page = html.decode("utf-8")
    return BeautifulSoup(page, "html.parser")
