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
# "Cookie": "_T_WM=4b986f6a3305d803766741144291bbdf; M_WEIBOCN_PARAMS=rl%3D1; SUB=_2A255_uNFDeTxGeNP7FER9C7EwziIHXVbAI0NrDV6PUJbrdANLVnbkW0oal4JVpNrA0k6w_cTUz4ysS8m0Q..; gsid_CTandWM=4ufme93c1hJ1dUZnfPCzxlHK8eg"
    "Cookie": "_T_WM=4b986f6a3305d803766741144291bbdf; SUB=_2A255-gnBDeTxGeNP7FER9C7EwziIHXVbBJeJrDV6PUJbvNBeLUTQkW0JVor8kVOlboZ709f3gCi4fFwcBA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5PuzaHsVOSciAkxQSZYYyr5JpX5K-t; SUHB=00xpZeQMLg1DCX; M_WEIBOCN_PARAMS=rl%3D1"
}

def get(url):
    request = urllib.request.Request(url, headers = HEADERS)
    response = urllib.request.urlopen(request)
    html = response.read()
    page = html.decode("utf-8")
    return BeautifulSoup(page, "html.parser")
