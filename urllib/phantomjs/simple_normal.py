#!/usr/bin/env python3.6
import urllib.request
from bs4 import BeautifulSoup
'''
直接读取js渲染的html页面
'''
def getPage(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    page = response.read().decode('UTF-8')
    return page

page = getPage('http://localhost/testjs.html')
soup = BeautifulSoup(page,'lxml')

print(soup.prettify())
