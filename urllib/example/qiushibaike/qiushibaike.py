#!/usr/bin/evn python3.6
import urllib.request
import re

URL = "https://www.qiushibaike.com/8hr/page/2/"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0"
TEXT = "./qiushibaike.data"
try:
    headers = {
        'User-Agent': UA
    }
    request = urllib.request.Request(URL,headers=headers)

    response = urllib.request.urlopen(request)
    page = response.read().decode('UTF-8')

    compile = r'<div.*?class="author.*?</a>.*?<a.*?<h2>(.*?)</h2>'
    pattern = re.compile(compile, re.S)

    items = re.findall(pattern, page)

    for item in items:
        print(item)


except urllib.request.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)