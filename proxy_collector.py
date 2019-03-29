from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup


url="https://www.proxyrotator.com/free-proxy-list/1/#free-proxy-list"
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
response=urlopen(req, timeout=15)
bsObj=BeautifulSoup(response,"html.parser")
table=bsObj.find('table',{'data-mode':'stack'})
print(table.get_text())
