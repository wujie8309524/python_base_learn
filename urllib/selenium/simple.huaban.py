#!/usr/bin/env python3.6
import urllib.request
from bs4 import BeautifulSoup

def getPage(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    page = response.read().decode('UTF-8')
    return page

page = getPage('http://huaban.com/')
soup = BeautifulSoup(page,'lxml')
# 输出格式化内容

with open('test.huaban.html','w') as f:
    f.write(soup.prettify())
